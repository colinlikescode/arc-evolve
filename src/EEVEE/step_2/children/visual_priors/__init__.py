"""
Visual pattern registry - automatically discovers all pattern modules.

To add a new pattern:
1. Create a new folder with the pattern name (e.g., "new_pattern")
2. Add what_to_look_for_classifier.py with CLASSIFIER_PROMPT = "..."
3. Add hint_for_llm.py with HINT = "..."
4. The pattern will be automatically discovered!
"""
import os
import re
from typing import Dict

_current_dir = os.path.dirname(os.path.abspath(__file__))


def _extract_string_constant(file_path: str, var_name: str) -> str:
    """Extract a string constant from a Python file without importing."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Match triple-quoted strings
        pattern = rf'{var_name}\s*=\s*"""(.*?)"""'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        # Try single-quoted triple strings
        pattern = rf"{var_name}\s*=\s*'''(.*?)'''"
        match = re.search(pattern, content, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        return ""
    except Exception:
        return ""


def _discover_patterns() -> Dict[str, Dict[str, str]]:
    """
    Discover all pattern modules by reading files directly (no imports needed).
    """
    patterns = {}
    failed = []
    
    for item in os.listdir(_current_dir):
        item_path = os.path.join(_current_dir, item)
        
        if not os.path.isdir(item_path):
            continue
        if item.startswith("__") or item.startswith(".") or item == "old":
            continue
        
        classifier_file = os.path.join(item_path, "what_to_look_for_classifier.py")
        hint_file = os.path.join(item_path, "hint_for_llm.py")
        
        if os.path.exists(classifier_file) and os.path.exists(hint_file):
            classifier_prompt = _extract_string_constant(classifier_file, "CLASSIFIER_PROMPT")
            hint = _extract_string_constant(hint_file, "HINT")
            
            if classifier_prompt and hint:
                patterns[item] = {
                    "classifier_prompt": classifier_prompt,
                    "hint": hint,
                }
            else:
                failed.append(item)
    
    if failed:
        print(f"   ⚠️ Failed to load {len(failed)} patterns: {', '.join(failed[:5])}{'...' if len(failed) > 5 else ''}")
    
    return patterns


PATTERN_REGISTRY = _discover_patterns()

__all__ = ["PATTERN_REGISTRY"]
