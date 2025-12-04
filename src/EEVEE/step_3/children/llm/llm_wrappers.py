"""
LLM wrapper functions for Claude, Gemini, and Grok.

Provides async functions with automatic retry logic and load balancing.
"""
import time
import asyncio
import aiohttp
from typing import Callable, Dict, Any, Optional, Tuple


# ============================================================================
# SHARED RETRY LOGIC
# ============================================================================

async def _call_with_retry(
    model_name: str,
    endpoint: str,
    headers: Dict[str, str],
    payload: Dict[str, Any],
    extract_response: Callable[[dict], str],
    context: str = "",
    max_retries: int = 3,
    timeout_seconds: int = 600,
    backoff_strategy: str = "exponential",  # "exponential" or "fixed"
    fixed_backoff: int = 10,
    endpoint_info: str = "",
) -> str:
    """
    Shared retry logic for all LLM calls.
    
    Args:
        model_name: Name for logging (e.g., "Claude Opus 4.5")
        endpoint: API endpoint URL
        headers: HTTP headers
        payload: Request payload
        extract_response: Function to extract text from response JSON
        context: Context for logging
        max_retries: Maximum retry attempts
        timeout_seconds: Request timeout
        backoff_strategy: "exponential" (2^attempt) or "fixed"
        fixed_backoff: Seconds for fixed backoff
        endpoint_info: Additional info for logging (e.g., endpoint number)
    
    Returns:
        LLM response string
    """
    start_time = time.time()
    print(f"   🔵 Calling {model_name}... {context}", flush=True)
    
    for attempt in range(1, max_retries + 1):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    endpoint, 
                    headers=headers, 
                    json=payload, 
                    timeout=aiohttp.ClientTimeout(total=timeout_seconds)
                ) as response:
                    elapsed = time.time() - start_time
                    
                    if response.status == 200:
                        data = await response.json()
                        result = extract_response(data)
                        if result:
                            print(f"   ✅ {model_name} returned ({len(result)} chars) after {elapsed:.1f}s{endpoint_info}", flush=True)
                            return result
                        print(f"   ⚠️ {model_name} returned empty response after {elapsed:.1f}s", flush=True)
                        return ""
                    
                    # Calculate backoff
                    backoff = fixed_backoff if backoff_strategy == "fixed" else (2 ** attempt)
                    
                    if response.status == 429:
                        error_text = await response.text()
                        if attempt < max_retries:
                            print(f"   ⚠️ {model_name} rate limit 429{endpoint_info}, retry {attempt}/{max_retries} after {backoff}s...", flush=True)
                            await asyncio.sleep(backoff)
                            continue
                        print(f"   ❌ {model_name} error 429{endpoint_info} after {max_retries} retries: {error_text[:200]}", flush=True)
                        raise RuntimeError(f"{model_name} error 429 after {max_retries} retries: {error_text}")
                    
                    # Other HTTP errors
                    error_text = await response.text()
                    if backoff_strategy == "fixed" and attempt < max_retries:
                        # Grok retries all errors
                        print(f"   ⚠️ {model_name} error {response.status}{endpoint_info}, retry {attempt}/{max_retries} after {backoff}s...", flush=True)
                        await asyncio.sleep(backoff)
                        continue
                    print(f"   ❌ {model_name} error {response.status}{endpoint_info} after {elapsed:.1f}s: {error_text[:200]}", flush=True)
                    raise RuntimeError(f"{model_name} error {response.status}: {error_text}")
                    
        except RuntimeError:
            raise
        except Exception as e:
            backoff = fixed_backoff if backoff_strategy == "fixed" else (2 ** attempt)
            if attempt < max_retries:
                print(f"   ⚠️ {model_name} error, retry {attempt}/{max_retries} after {backoff}s: {str(e)[:80]}", flush=True)
                await asyncio.sleep(backoff)
            else:
                elapsed = time.time() - start_time
                print(f"   ❌ {model_name} failed after {max_retries} retries ({elapsed:.1f}s): {e}", flush=True)
                raise
    
    raise RuntimeError(f"{model_name} failed after all retries")


# ============================================================================
# RESPONSE EXTRACTORS
# ============================================================================

def _extract_claude_response(data: dict) -> str:
    """Extract text from Claude API response."""
    content = data.get("content", [])
    if content and len(content) > 0:
        return content[0].get("text", "")
    return ""


def _extract_openai_response(data: dict) -> str:
    """Extract text from OpenAI-compatible API response (Gemini, Grok)."""
    choices = data.get("choices", [])
    if choices and len(choices) > 0:
        message = choices[0].get("message", {})
        return message.get("content", "")
    return ""


# ============================================================================
# PUBLIC API
# ============================================================================

async def call_claude_opus(prompt: str, context: str = "", temperature: float = 1.0) -> str:
    """
    Call Claude Opus 4.5 with automatic retry and load balancing.
    Rotates between Azure endpoints on every call.
    
    Args:
        prompt: The prompt to send
        context: Context string for logging
        temperature: Sampling temperature (default 1.0, use 0.2 for classifier)
    """
    from EEVEE.models.claude_models import (
        get_azure_credentials,
        get_claude_opus_endpoint,
        CLAUDE_OPUS_MODEL,
        CLAUDE_OPUS_VERSION,
        CLAUDE_OPUS_MAX_TOKENS,
    )
    
    api_key, base_url, endpoint_num = get_azure_credentials()
    
    return await _call_with_retry(
        model_name="Claude Opus 4.5",
        endpoint=get_claude_opus_endpoint(base_url),
        headers={
            "x-api-key": api_key,
            "anthropic-version": CLAUDE_OPUS_VERSION,
            "Content-Type": "application/json",
        },
        payload={
            "model": CLAUDE_OPUS_MODEL,
            "max_tokens": CLAUDE_OPUS_MAX_TOKENS,
            "temperature": temperature,
            "messages": [{"role": "user", "content": prompt}],
        },
        extract_response=_extract_claude_response,
        context=context,
        endpoint_info=f" (endpoint {endpoint_num})",
    )


async def call_gemini_pro(prompt: str, context: str = "") -> str:
    """
    Call Gemini 3 Pro with automatic retry and load balancing.
    Rotates between GCP service accounts on every call.
    """
    from gcp import get_gemini_credentials
    from EEVEE.models.gemini_models import get_gemini_pro_url, GEMINI_PRO_MODEL
    
    project_id, access_token = get_gemini_credentials()
    
    return await _call_with_retry(
        model_name="Gemini 3 Pro",
        endpoint=get_gemini_pro_url(project_id),
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        payload={
            "model": GEMINI_PRO_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 1.0,
        },
        extract_response=_extract_openai_response,
        context=context,
    )


async def call_grok(prompt: str, context: str = "") -> str:
    """
    Call Grok 4.1 Fast Reasoning with automatic retry.
    Rotates between API keys on every call.
    Uses fixed 10s backoff and retries all errors.
    """
    from EEVEE.models.grok_models import (
        get_grok_credentials,
        get_grok_endpoint,
        GROK_MODEL,
        GROK_TEMPERATURE,
    )
    
    api_key, key_num = get_grok_credentials()
    
    return await _call_with_retry(
        model_name="Grok 4.1",
        endpoint=get_grok_endpoint(),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        payload={
            "model": GROK_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": GROK_TEMPERATURE,
        },
        extract_response=_extract_openai_response,
        context=context,
        timeout_seconds=900,  # 15 min for Grok
        backoff_strategy="fixed",
        fixed_backoff=10,
        endpoint_info=f" (key {key_num})",
    )
