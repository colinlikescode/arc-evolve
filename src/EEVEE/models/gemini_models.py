"""Gemini 3 Pro Model Configuration."""
import os
from dotenv import load_dotenv

load_dotenv()

# Gemini 3 Pro Configuration
GEMINI_PRO_MODEL = "google/gemini-3-pro-preview"
GEMINI_PRO_REGION = "global"
GEMINI_PRO_ENDPOINT = "aiplatform.googleapis.com"


def get_gemini_pro_url(project_id: str) -> str:
    """Get the Gemini Pro API URL."""
    return f"https://{GEMINI_PRO_ENDPOINT}/v1/projects/{project_id}/locations/{GEMINI_PRO_REGION}/endpoints/openapi/chat/completions"


def get_gemini_api_key() -> str:
    """Get Gemini API key from environment."""
    return os.getenv("GEMINI_API_KEY", "")
