"""
Step 1 Mini Orchestrator: Detect multiple test inputs.
"""
import importlib
from typing import Dict, Any

# Use importlib for numeric module name
_detector_module = importlib.import_module('EEVEE.step_1.children.detector')
detect_test_inputs = _detector_module.detect_test_inputs


async def execute_step_1(question_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Detect if question has multiple test inputs.
    
    Args:
        question_data: Contains test_inputs and other question data
    
    Returns:
        question_data with num_test_inputs added
    """
    print(f"\n{'='*70}")
    print(f"📋 STEP 1: Detect Multiple Test Inputs")
    print(f"{'='*70}")
    
    num_test_inputs = detect_test_inputs(question_data)
    
    print(f"   Test inputs found: {num_test_inputs}")
    
    if num_test_inputs > 1:
        print(f"   ⚠️  SPECIAL CASE: Question has {num_test_inputs} test inputs")
    else:
        print(f"   ✅ Standard case: 1 test input")
    
    return {
        **question_data,
        "num_test_inputs": num_test_inputs
    }

