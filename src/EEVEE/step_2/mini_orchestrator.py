"""
Step 2 Mini Orchestrator: Automatically detect visual priors and prepare hints.

Uses single Claude 4.5 call (temperature=0.0) with explicit iteration through all patterns.
Returns hints to guide the solver (max 3 hints).

This runs FIRST for every question before any islands start solving.
"""
import importlib
from typing import Dict, Any, List, Tuple

# Use importlib for modules with numeric prefixes
_classifier_module = importlib.import_module('EEVEE.step_2.children.classifier')
_llm_module = importlib.import_module('EEVEE.step_3.children.llm.llm_wrappers')

get_llm_classified_hints = _classifier_module.get_llm_classified_hints
_call_claude_opus = _llm_module.call_claude_opus

# Classifier uses temperature 0.0 for fully deterministic pattern detection
CLASSIFIER_TEMPERATURE = 0.0


async def _call_claude_classifier(prompt: str, context: str = "") -> str:
    """Claude call with temperature 0.0 for deterministic classifier."""
    return await _call_claude_opus(prompt, context, temperature=CLASSIFIER_TEMPERATURE)


async def execute_step_2(question_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute Step 2: Automatically detect visual priors and prepare hints.
    
    Uses single Claude 4.5 call with explicit YES/NO iteration through all patterns.
    This runs FIRST for every question before islands start solving.
    
    Args:
        question_data: Contains question_id, training_examples, etc.
    
    Returns:
        question_data with pattern_detector_hints_python field containing detected hints
    """
    question_id = question_data.get("question_id", "unknown")
    training_examples = question_data.get("train_examples", question_data.get("training_examples", []))
    
    # Run LLM-based classification with single Claude 4.5 call
    combined_hints, detected_prior_names = await _run_llm_classification(
        training_examples, question_id
    )
    
    # Always print Step 2 status
    print(f"\n{'='*70}")
    print(f"🔍 STEP 2: Visual Prior Detection (Claude 4.5)")
    print(f"{'='*70}")
    if detected_prior_names:
        print(f"   🎯 {len(detected_prior_names)} pattern(s) detected: {', '.join(detected_prior_names)}")
        print(f"   📤 Hints will be passed to all 5 islands")
    else:
        print(f"   ℹ️  No patterns detected")
        print(f"   📤 No hints to pass (all islands will solve without pattern hints)")
    
    return {
        **question_data,
        "pattern_detector_hints_python": combined_hints,
        "detected_priors": detected_prior_names,
    }


async def _run_llm_classification(
    training_examples: List[Dict],
    question_id: str,
) -> Tuple[str, List[str]]:
    """
    Run LLM-based pattern classification using Claude 4.5 (temperature=0.0).
    
    Returns:
        Tuple of (combined_hints, detected_pattern_names)
    """
    try:
        hints, detected_names = await get_llm_classified_hints(
            examples=training_examples,
            llm_call_func=_call_claude_classifier,
        )
        return hints, detected_names
        
    except Exception as e:
        print(f"   ⚠️ LLM classification failed: {e}")
        return "", []
