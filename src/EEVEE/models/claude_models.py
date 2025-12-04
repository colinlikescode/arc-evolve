"""Claude Opus 4.5 Model Configuration."""
import os
import threading
from dotenv import load_dotenv

load_dotenv()

# Thread-safe rotating Azure endpoint counter
_azure_key_counter = 0
_azure_lock = threading.Lock()


def get_azure_credentials() -> tuple[str, str, int]:
    """
    Get the next Azure API key and base URL (rotates between endpoints 1 and 2).
    Thread-safe rotation on every call.
    
    Returns:
        Tuple of (api_key, base_url, endpoint_num)
    """
    global _azure_key_counter
    with _azure_lock:
        _azure_key_counter += 1
        key_num = (_azure_key_counter % 2) + 1
    
    api_key = os.getenv(f"AZURE_API_KEY_{key_num}", "")
    base_url = os.getenv(f"AZURE_API_URL_BASE_{key_num}", "")
    
    if base_url and not base_url.startswith("http"):
        base_url = f"https://{base_url}"
    
    return api_key, base_url, key_num


# Claude Opus 4.5 Configuration
CLAUDE_OPUS_MODEL = os.getenv("CLAUDE_OPUS_MODEL", "claude-opus-4-5")
CLAUDE_OPUS_VERSION = "2023-06-01"
CLAUDE_OPUS_MAX_TOKENS = 64000


def get_claude_opus_endpoint(base_url: str = None) -> str:
    """Get Claude Opus endpoint with load-balanced base URL."""
    if base_url is None:
        _, base_url, _ = get_azure_credentials()
    return f"{base_url}/anthropic/v1/messages"
