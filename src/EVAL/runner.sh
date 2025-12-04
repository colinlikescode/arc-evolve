#!/bin/bash
#
# ARC-AGI Solver Runner
# Production-ready runner script for processing ARC-AGI questions
#

set -e  # Exit on error

# Get the directory of this script (EVAL folder)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Get project root (two levels up from EVAL)
PROJECT_ROOT="$( cd "${SCRIPT_DIR}/../.." && pwd )"

cd "$SCRIPT_DIR"

# Set up Python path
export PYTHONPATH="${PROJECT_ROOT}/src:${PYTHONPATH}"

# Log file path (save to project root)
LOG_FILE="${PROJECT_ROOT}/logs.txt"

# Clear previous logs if they exist
> "$LOG_FILE"

echo "=========================================="
echo "🚀 ARC-AGI Solver Runner"
echo "=========================================="
echo "Project root: $PROJECT_ROOT"
echo "Working directory: $SCRIPT_DIR"
echo "Python path: $PYTHONPATH"
echo "Logs will be saved to: $LOG_FILE"
echo ""

# Check if .env file exists
if [ ! -f "${PROJECT_ROOT}/.env" ]; then
    echo "⚠️  WARNING: .env file not found at ${PROJECT_ROOT}/.env"
    echo "Make sure your API keys are configured"
fi

# Check if service account files exist (in gcp folder in project root)
if [ ! -f "${PROJECT_ROOT}/gcp/gcp_service_account_1.json" ]; then
    echo "❌ ERROR: gcp_service_account_1.json not found at ${PROJECT_ROOT}/gcp/gcp_service_account_1.json"
    echo "Please add your GCP service account JSON file to the gcp/ folder"
    exit 1
fi
if [ ! -f "${PROJECT_ROOT}/gcp/gcp_service_account_2.json" ]; then
    echo "❌ ERROR: gcp_service_account_2.json not found at ${PROJECT_ROOT}/gcp/gcp_service_account_2.json"
    echo "Please add your GCP service account JSON file to the gcp/ folder"
    exit 1
fi

echo "✅ Environment checks passed"
echo ""

# Run the orchestrator
echo "🏃 Starting ARC-AGI processing..."
echo ""

# Run with uv (handles venv automatically)
uv run python -c "
import asyncio
import sys
import os
# Ensure we're importing from EVAL directory
sys.path.insert(0, os.path.dirname(os.path.abspath('${SCRIPT_DIR}/orchestrator.py')))
from orchestrator import run_orchestrator
from helpers.summary import print_final_summary
from EVAL.config import NUM_QUESTIONS, STARTING_QUESTION_NUMBER, MAX_IN_PARALLEL, DATASET, QUESTION_NUMBERS

class Tee:
    '''Write to both stdout and a file.'''
    def __init__(self, file_path):
        self.file = open(file_path, 'a', encoding='utf-8')
        self.stdout = sys.stdout
    
    def write(self, text):
        self.stdout.write(text)
        self.file.write(text)
        self.file.flush()
    
    def flush(self):
        self.stdout.flush()
        self.file.flush()
    
    def close(self):
        self.file.close()

async def main():
    # Set up tee to logs.txt
    log_file = '${LOG_FILE}'
    tee = Tee(log_file)
    original_stdout = sys.stdout
    sys.stdout = tee
    
    try:
        # Print Eevee ASCII art (goes to both terminal and logs)
        from helpers.ascii import print_eevee
        print_eevee()
        print()
        # Validate configuration: if QUESTION_NUMBERS is set, NUM_QUESTIONS and STARTING_QUESTION_NUMBER must be None
        if QUESTION_NUMBERS is not None and len(QUESTION_NUMBERS) > 0:
            if NUM_QUESTIONS is not None or STARTING_QUESTION_NUMBER is not None:
                error_msg = ('Configuration error: If QUESTION_NUMBERS is set, NUM_QUESTIONS and STARTING_QUESTION_NUMBER must be None. '
                            f'Current values: QUESTION_NUMBERS={QUESTION_NUMBERS}, NUM_QUESTIONS={NUM_QUESTIONS}, STARTING_QUESTION_NUMBER={STARTING_QUESTION_NUMBER}')
                raise ValueError(error_msg)
            print(f'🧪 Running ARC-AGI processing - {len(QUESTION_NUMBERS)} specific questions: {QUESTION_NUMBERS}...')
            print(f'   Dataset: {DATASET}')
        else:
            if NUM_QUESTIONS is None or STARTING_QUESTION_NUMBER is None:
                error_msg = ('Configuration error: If QUESTION_NUMBERS is None, both NUM_QUESTIONS and STARTING_QUESTION_NUMBER must be set. '
                            f'Current values: QUESTION_NUMBERS={QUESTION_NUMBERS}, NUM_QUESTIONS={NUM_QUESTIONS}, STARTING_QUESTION_NUMBER={STARTING_QUESTION_NUMBER}')
                raise ValueError(error_msg)
            print(f'🧪 Running ARC-AGI processing - {NUM_QUESTIONS} questions starting at question {STARTING_QUESTION_NUMBER}...')
            print(f'   Dataset: {DATASET}')
        print(f'   Max {MAX_IN_PARALLEL} running at once')
        
        result = await run_orchestrator(
            num_questions=NUM_QUESTIONS, 
            starting_question_number=STARTING_QUESTION_NUMBER,
            dataset=DATASET,
            actually_submit=True,
            question_numbers=QUESTION_NUMBERS
        )
        
        # Print comprehensive final summary
        print_final_summary(result)
        
        print(f'\\n✅ Processed {len(result)} questions successfully')
        
        return result
    finally:
        sys.stdout = original_stdout
        tee.close()

asyncio.run(main())
"

RESULT=$?

echo ""
echo "=========================================="
if [ $RESULT -eq 0 ]; then
    echo "✅ Run completed successfully"
else
    echo "❌ Run failed with exit code $RESULT"
fi
echo "=========================================="
echo "📄 Full logs saved to: $LOG_FILE"
echo ""

exit $RESULT

