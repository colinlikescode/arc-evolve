"""
LLM-based visual prior classifier using a single Claude 4.5 call.

Classifies ALL patterns and returns up to 3 hints.
"""
import json
import re
import random
from typing import List, Dict, Tuple, Set

from EEVEE.prompts.classifier_prompt import (
    build_classifier_prompt,
    get_hints_for_patterns,
    get_pattern_names_list,
)

# Maximum number of hints to return
MAX_HINTS = 3


def _parse_explicit_response(response: str, pattern_names: List[str]) -> Dict[str, bool]:
    """
    Parse response with explicit YES/NO format for each pattern.
    """
    results = {name: False for name in pattern_names}
    
    # Look for explicit YES/NO patterns
    for name in pattern_names:
        pattern = rf'{re.escape(name)}[:\s]*(YES|NO)'
        match = re.search(pattern, response, re.IGNORECASE)
        if match:
            results[name] = match.group(1).upper() == "YES"
    
    # Also check JSON summary (detected_patterns array)
    json_match = re.search(r'\{[^{}]*"detected_patterns"[^{}]*\}', response, re.DOTALL)
    if json_match:
        try:
            json_data = json.loads(json_match.group())
            detected = json_data.get("detected_patterns", [])
            for name in detected:
                if name in results:
                    results[name] = True
        except json.JSONDecodeError:
            pass
    
    return results


async def get_llm_classified_hints(
    examples: List[Dict],
    llm_call_func,
    patterns_to_check=None,  # Ignored - we always check all patterns
) -> Tuple[str, List[str]]:
    """
    Main entry point: classify with single Claude call, return up to 3 hints.
    """
    all_patterns = get_pattern_names_list()
    total = len(all_patterns)
    
    print(f"   📡 Classifying {total} patterns with Claude 4.5...")
    
    prompt = build_classifier_prompt(examples)
    
    try:
        response = await llm_call_func(prompt, context="Pattern Classification")
        results = _parse_explicit_response(response, all_patterns)
        detected = {name for name, is_detected in results.items() if is_detected}
        print(f"   ✅ Found {len(detected)} pattern(s)")
    except Exception as e:
        print(f"   ⚠️ Classification failed: {e}")
        return "", []
    
    # Print detected patterns
    if detected:
        print(f"   🎯 Detected patterns ({len(detected)}):")
        for name in sorted(detected):
            print(f"      ✓ {name}")
    else:
        print(f"   ℹ️ No patterns detected")
        return "", []
    
    # Select final patterns (max 3)
    detected_list = list(detected)
    if len(detected_list) > MAX_HINTS:
        detected_list = random.sample(detected_list, MAX_HINTS)
    
    # Build results dict
    final_results = {name: (name in detected_list) for name in all_patterns}
    
    # Get combined hints
    hints = get_hints_for_patterns(final_results)
    
    print(f"   ✅ Final selection ({len(detected_list)}): {', '.join(detected_list)}")
    
    return hints, detected_list
