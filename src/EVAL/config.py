"""Configuration for EVAL pipeline"""

# ============================================================================
# QUESTION SELECTION: Choose ONE of the following two options:
# ============================================================================
# 
# OPTION 1: Process a range of questions (use NUM_QUESTIONS + STARTING_QUESTION_NUMBER)
# OPTION 2: Process specific questions (use QUESTION_NUMBERS)
#
# If QUESTION_NUMBERS is set to a list, it will override NUM_QUESTIONS and STARTING_QUESTION_NUMBER
# ============================================================================

# OPTION 1: Range-based selection
# Number of questions to process in sequence (must be None if using OPTION 2)
NUM_QUESTIONS = 400
# Starting question number (1-indexed) (must be None if using OPTION 2)
STARTING_QUESTION_NUMBER = 1

# OPTION 2: Specific question selection (overrides OPTION 1 if set)
# Set to None to use OPTION 1 (NUM_QUESTIONS + STARTING_QUESTION_NUMBER)
QUESTION_NUMBERS = None


# ============================================================================
# EVAL SETTINGS
# ============================================================================

# Max questions running at once. As one finishes, next one starts immediately.
MAX_IN_PARALLEL = 50

# Dataset to use ("arc-agi-1" or "arc-agi-2")
DATASET = "arc-agi-1"

# Orchestrator to use ("system")
ORCHESTRATOR = "system"

