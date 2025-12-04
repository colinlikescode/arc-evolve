"""Simple summary generation for test results."""
from typing import List, Dict


def print_final_summary(results: List[Dict]):
    """
    Print final summary from a list of question results.
    
    Args:
        results: List of dicts with keys: question_id, correct, attempt_1_correct, 
                attempt_2_correct, attempt_1_source, attempt_2_source
    """
    if not results:
        print("\n⚠️  No results to summarize.")
        return
    
    print(f"\n{'='*80}")
    print(f"{'='*80}")
    print(f"{'🎯 FINAL COMPREHENSIVE SUMMARY':^80}")
    print(f"{'='*80}")
    print(f"{'='*80}\n")
    
    # Per-question breakdown
    print(f"{'─'*80}")
    print(f"📊 PER-QUESTION BREAKDOWN:")
    print(f"{'─'*80}\n")
    
    correct_count = 0
    incorrect_count = 0
    correct_questions = []
    incorrect_questions = []
    
    for result in sorted(results, key=lambda r: r.get('question_id', 0)):
        qid = result.get('question_id', 0)
        correct = result.get('correct', False)  # Default to False if key missing
        
        # Get attempt correctness and sources
        attempt_1_correct = result.get('attempt_1_correct')
        attempt_2_correct = result.get('attempt_2_correct')
        attempt_1_source = result.get('attempt_1_source', 'Unknown')
        attempt_2_source = result.get('attempt_2_source', 'Unknown')
        chosen_island_id = result.get('chosen_island_id', -1)
        
        # Track both attempts separately
        attempt_1_status = "⚪" if attempt_1_correct is None else ("✅" if attempt_1_correct else "❌")                                                         
        attempt_2_status = "⚪" if attempt_2_correct is None else ("✅" if attempt_2_correct else "❌")                                                         
        
        status_icon = "✅" if correct else "❌"
        status_text = "CORRECT" if correct else "INCORRECT"
        
        if correct:
            correct_count += 1
            correct_questions.append(qid)
        else:
            incorrect_count += 1
            incorrect_questions.append(qid)
        
        # Format chosen island
        island_label = f"Island {chosen_island_id + 1}" if chosen_island_id >= 0 else "Unknown"
        
        # Format attempt statuses (both attempts are from same island, so just show island)
        attempt_1_label = f"{attempt_1_status} {island_label}"
        attempt_2_label = f"{attempt_2_status} {island_label}"
        
        print(f"  {status_icon} Question {qid:3d} | {status_text:10s} | {attempt_1_label:20s} | {attempt_2_label:20s}")
    
    # Summary statistics
    print(f"\n{'─'*80}")
    print(f"📈 SUMMARY STATISTICS:")
    print(f"{'─'*80}\n")
    
    total_questions = len(results)
    accuracy = (correct_count / total_questions * 100) if total_questions > 0 else 0
    
    print(f"  📝 Total Questions Processed:  {total_questions}")
    print(f"  ✅ Correct Answers:            {correct_count}")
    print(f"  ❌ Incorrect Answers:          {incorrect_count}")
    print(f"  🎯 Overall Accuracy:           {accuracy:.1f}%")
    
    # Question number lists
    print(f"\n{'─'*80}")
    print(f"📋 QUESTION DETAILS:")
    print(f"{'─'*80}\n")
    
    if correct_questions:
        print(f"  ✅ CORRECT Questions: {', '.join(map(str, sorted(correct_questions)))}")
    else:
        print(f"  ✅ CORRECT Questions: None")
    
    if incorrect_questions:
        print(f"  ❌ INCORRECT Questions: {', '.join(map(str, sorted(incorrect_questions)))}")
    else:
        print(f"  ❌ INCORRECT Questions: None")
    
    print(f"{'='*80}")
    print(f"{'='*80}\n")

