"""
EEVEE Main Orchestrator - Parallel Python island pipeline.

Flow:
- Step 1: Detect 1, 2, or 3 test inputs
- Step 2: Determine visual priors and prepare hints
- Step 3: Run 5 parallel Python islands (3 Gemini, 2 Claude hybrid) with voting
- Step 4: Format answers for submission + SUDDEN DEATH if all islands agree
"""
import importlib
from typing import Dict, Any

# Import step modules
_step1_module = importlib.import_module('EEVEE.step_1.mini_orchestrator')
_step2_module = importlib.import_module('EEVEE.step_2.mini_orchestrator')
_step3_module = importlib.import_module('EEVEE.step_3.mini_orchestrator')
_step4_module = importlib.import_module('EEVEE.step_4.mini_orchestrator')

execute_step_1 = _step1_module.execute_step_1
execute_step_2 = _step2_module.execute_step_2
execute_step_3 = _step3_module.execute_step_3
execute_step_4 = _step4_module.execute_step_4


async def process_question(question_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process question through parallel Python islands with voting.
    
    Steps:
    1. Detect multiple test inputs
    2. Determine visual priors and prepare hints
    3. Run 5 parallel Python islands with voting
    4. Format answers for submission (+ sudden death if all islands agree)
    """
    print(f"\n{'='*70}")
    print(f"🚀 EEVEE: Parallel Python Islands")
    print(f"{'='*70}")
    
    step1_result = await execute_step_1(question_data)
    step2_result = await execute_step_2(step1_result)
    step3_result = await execute_step_3(step2_result)
    step4_result = await execute_step_4(step3_result)
    
    formatted_answer = step4_result.get("formatted_answer", [])
    has_answer = step4_result.get("has_answer", False)
    
    print(f"\n{'='*70}")
    print(f"🏁 PIPELINE COMPLETE")
    print(f"{'='*70}")
    
    if has_answer:
        print(f"✅ Final answer(s) ready for submission")
        print(f"   {len(formatted_answer)} answer(s) formatted")
    else:
        print(f"❌ No answer to submit")
    
    print(f"{'='*70}\n")
    
    return {
        "formatted_answer": formatted_answer,
        "has_answer": has_answer,
        "num_test_inputs": step2_result.get("num_test_inputs", 1),
        "winning_code": step3_result.get("top_result", {}).get("train_results", [{}])[0].get("code", "") if step3_result.get("top_result") else "",
        "question_id": question_data.get("question_id"),
        "dataset": question_data.get("dataset"),
        "attempt_1_source": step4_result.get("attempt_1_source", "Python"),
        "attempt_2_source": step4_result.get("attempt_2_source", "Python"),
        "ordered_results": step3_result.get("ordered_results", []),
        "chosen_island_id": step3_result.get("chosen_island_id", -1),
    }
