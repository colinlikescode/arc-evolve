"""
Builds the single classifier prompt for all patterns.
Uses explicit iteration format where LLM outputs YES/NO for each pattern.
"""
import importlib
from typing import List, Dict, Optional

# Use importlib to handle numeric module name (step_2)
_visual_priors = importlib.import_module('EEVEE.step_2.children.visual_priors')
PATTERN_REGISTRY = _visual_priors.PATTERN_REGISTRY


def _format_grid(grid: List[List[int]]) -> str:
    """Format a grid for display in the prompt."""
    return "\n".join(" ".join(str(cell) for cell in row) for row in grid)


def _format_examples(examples: List[Dict]) -> str:
    """Format training examples for the classification prompt."""
    parts = []
    for i, ex in enumerate(examples, 1):
        inp = ex.get("input", [])
        out = ex.get("output", [])
        parts.append(f"=== Example {i} ===")
        parts.append(f"Input ({len(inp)}x{len(inp[0]) if inp else 0}):")
        parts.append(_format_grid(inp))
        parts.append(f"\nOutput ({len(out)}x{len(out[0]) if out else 0}):")
        parts.append(_format_grid(out))
        parts.append("")
    return "\n".join(parts)


def get_pattern_names_list() -> List[str]:
    """Get list of all pattern names."""
    return sorted(list(PATTERN_REGISTRY.keys()))


def build_classifier_prompt(examples: List[Dict], pattern_subset: Optional[List[str]] = None) -> str:
    """
    Build a prompt that forces explicit iteration through each pattern.
    The LLM must output "Pattern #X [name]: YES" or "Pattern #X [name]: NO" for each.
    
    Args:
        examples: Training examples with input/output grids
        pattern_subset: Optional list of pattern names to classify (default: all patterns)
    
    Returns:
        Complete prompt string
    """
    examples_text = _format_examples(examples)
    pattern_names = pattern_subset if pattern_subset else get_pattern_names_list()
    pattern_count = len(pattern_names)
    
    # Build pattern descriptions with explicit numbering
    pattern_descriptions = []
    for idx, pattern_name in enumerate(pattern_names, 1):
        if pattern_name in PATTERN_REGISTRY:
            classifier_prompt = PATTERN_REGISTRY[pattern_name]["classifier_prompt"]
            # Strip the "Answer ONLY with: YES or NO" line
            lines = classifier_prompt.strip().split('\n')
            if lines and "YES or NO" in lines[-1]:
                lines = lines[:-1]
            clean_prompt = '\n'.join(lines)
            pattern_descriptions.append(f"{'='*60}\nPATTERN #{idx}: {pattern_name}\n{'='*60}\n{clean_prompt}")
    
    all_descriptions = "\n\n".join(pattern_descriptions)
    
    prompt = f"""You are a careful, methodical pattern classifier for ARC-AGI puzzles.

╔══════════════════════════════════════════════════════════════════════════════╗
║  CRITICAL INSTRUCTIONS - READ CAREFULLY                                      ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  1. You will analyze {pattern_count} patterns ONE BY ONE                     ║
║  2. For EACH pattern, you MUST output: "Pattern #X [name]: YES" or "NO"      ║
║  3. Go SLOWLY and METHODICALLY through each pattern                          ║
║  4. Do NOT skip any patterns - you must evaluate ALL {pattern_count}         ║
║  5. Avoid selecting OVERLAPPING patterns (pick the MOST specific one)        ║
║  6. After all patterns, output a JSON summary                                ║
╚══════════════════════════════════════════════════════════════════════════════╝

═══════════════════════════════════════════════════════════════════════
THE PUZZLE TO CLASSIFY (study these training examples):
═══════════════════════════════════════════════════════════════════════

{examples_text}

═══════════════════════════════════════════════════════════════════════
PATTERNS TO EVALUATE ({pattern_count} total):
═══════════════════════════════════════════════════════════════════════

{all_descriptions}

═══════════════════════════════════════════════════════════════════════
INSTRUCTIONS FOR YOUR RESPONSE:
═══════════════════════════════════════════════════════════════════════

Step 1: For EACH pattern from #1 to #{pattern_count}, write:
   "Pattern #[number] [pattern_name]: YES" or "Pattern #[number] [pattern_name]: NO"
   
   Think about whether this specific pattern matches the puzzle.
   Be conservative - only say YES if you're confident.
   
Step 2: After evaluating ALL patterns, provide a JSON summary:
   {{"detected_patterns": ["pattern_name_1", "pattern_name_2"]}}
   
   Only include patterns you marked as YES.
   If you marked multiple similar/overlapping patterns as YES, 
   only include the MOST SPECIFIC one in the JSON.

BEGIN YOUR EVALUATION NOW - Start with Pattern #1:
"""
    
    return prompt


def get_hints_for_patterns(detected_patterns: Dict[str, bool]) -> str:
    """
    Get combined hint text for all detected patterns.
    
    Args:
        detected_patterns: Dict mapping pattern names to detection results
    
    Returns:
        Combined hint string for all detected patterns
    """
    hints = []
    
    for pattern_name, detected in detected_patterns.items():
        if detected and pattern_name in PATTERN_REGISTRY:
            hints.append(PATTERN_REGISTRY[pattern_name]["hint"])
    
    return "\n".join(hints)

