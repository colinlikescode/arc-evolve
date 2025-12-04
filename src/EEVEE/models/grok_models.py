"""Grok 4.1 Fast Reasoning Model Configuration."""
import os
import threading
from dotenv import load_dotenv

load_dotenv()

# Thread-safe rotating Grok API key counter
_grok_key_counter = 0
_grok_lock = threading.Lock()

# Grok Configuration
GROK_BASE_URL = "https://api.x.ai/v1"
GROK_MODEL = "grok-4-1-fast-reasoning"
GROK_TEMPERATURE = 1.0


def get_grok_credentials() -> tuple[str, int]:
    """
    Get the next Grok API key (rotates between keys 1, 2, and 3).
    Thread-safe rotation on every call.
    
    Returns:
        Tuple of (api_key, key_num)
    """
    global _grok_key_counter
    with _grok_lock:
        _grok_key_counter += 1
        key_num = (_grok_key_counter % 3) + 1
    
    api_key = os.getenv(f"GROK_API_KEY_{key_num}", "")
    return api_key, key_num


def get_grok_endpoint() -> str:
    """Get Grok API endpoint."""
    return f"{GROK_BASE_URL}/chat/completions"
