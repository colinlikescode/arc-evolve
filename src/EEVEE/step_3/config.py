"""
Configuration for Python Path (Step 3).

Defines island configurations with flexible model selection.
Configure the number of islands and which models they use below.
"""
from .children.types.island_types import IslandConfig

# Evolution Rounds
MAX_EVOLUTION_ROUNDS = 10  # Maximum number of evolution rounds per island

# State Management (for legacy compatibility if needed)
FEEDBACK_SELECTION_RATE = 1.0  # Rate of selecting each solution for feedback (1.0 = all)
MAX_FEEDBACK_EXAMPLES = 5  # Maximum number of previous solutions to show
ASCENDING_SCORE_ORDER = True  # If True, show worst→best (for showing improvement)

# API Configuration
MAX_RETRIES = 3
REQUEST_TIMEOUT = 600  # 10 minutes
GROK_TIMEOUT = 900  # 15 minutes (for Grok if used)
TEMPERATURE = 1.0


# ============================================================================
# EXPERT CONFIGURATION
# ============================================================================
# Configure the number of islands and which models they use.
# Each island configuration specifies:
#   - llm_id: "claude" or "gemini" (determines which model to use)
#   - seed: Unique seed for this island (should be different for each)
#   - Other parameters as needed
#
# Example configurations:
#   - 2 Claude islands: [{"llm_id": "claude", "seed": 0}, {"llm_id": "claude", "seed": 10}]
#   - 2 Gemini islands: [{"llm_id": "gemini", "seed": 0}, {"llm_id": "gemini", "seed": 10}]
#   - Mixed: [{"llm_id": "claude", "seed": 0}, {"llm_id": "gemini", "seed": 0}]
# ============================================================================

EXPERT_CONFIGS: list[IslandConfig] = [
    # Island 1: Gemini 3 Pro (all rounds)
    {
        "llm_id": "gemini",
        "temperature": 1.0,
        "max_iterations": 12,
        "max_feedback_examples": 5,
        "feedback_selection_rate": 1.0,
        "seed": 0,
        "randomize_training_order": True,
        "ascending_score_order": True,
        "return_best_result": True,
        "timeout_s": 5.0,
        "per_iteration_retries": 2,
        "receives_hints": True,
    },
    # Island 2: Gemini 3 Pro (all rounds)
    {
        "llm_id": "gemini",
        "temperature": 1.0,
        "max_iterations": 12,
        "max_feedback_examples": 5,
        "feedback_selection_rate": 1.0,
        "seed": 10,
        "randomize_training_order": True,
        "ascending_score_order": True,
        "return_best_result": True,
        "timeout_s": 5.0,
        "per_iteration_retries": 2,
        "receives_hints": True,
    },
    # Island 3: Gemini 3 Pro (all rounds)
    {
        "llm_id": "gemini",
        "temperature": 1.0,
        "max_iterations": 12,
        "max_feedback_examples": 5,
        "feedback_selection_rate": 1.0,
        "seed": 20,
        "randomize_training_order": True,
        "ascending_score_order": True,
        "return_best_result": True,
        "timeout_s": 5.0,
        "per_iteration_retries": 2,
        "receives_hints": True,
    },
    # Island 4: Claude 4.5 for rounds 1-4, Gemini 3 Pro for rounds 5-12
    {
        "llm_id": "gemini",
        "temperature": 1.0,
        "max_iterations": 12,
        "max_feedback_examples": 5,
        "feedback_selection_rate": 1.0,
        "seed": 30,
        "randomize_training_order": True,
        "ascending_score_order": True,
        "return_best_result": True,
        "timeout_s": 5.0,
        "per_iteration_retries": 2,
        "claude_rounds": [0, 1, 2, 3],
        "receives_hints": True,
    },
    # Island 5: Claude 4.5 for rounds 1-4, Gemini 3 Pro for rounds 5-12
    {
        "llm_id": "gemini",
        "temperature": 1.0,
        "max_iterations": 12,
        "max_feedback_examples": 5,
        "feedback_selection_rate": 1.0,
        "seed": 40,
        "randomize_training_order": True,
        "ascending_score_order": True,
        "return_best_result": True,
        "timeout_s": 5.0,
        "per_iteration_retries": 2,
        "claude_rounds": [0, 1, 2, 3],
        "receives_hints": True,
    },
]

# Mass Mutation Configuration (runs AFTER all islands complete, only if no 100%)
# Uses context from the TOP scoring island
# Round 1: Grok 4.1 Fast Reasoning (100 parallel calls) - mass mutation hints set 1 (0-99)
# Round 2: Gemini 3 Pro (1 call) - regular prompt
# Round 3: Grok 4.1 Fast Reasoning (100 parallel calls) - mass mutation hints set 2 (100-199)
# Round 4: Claude 4.5 Opus (1 call) - regular prompt
# Round 5: Grok 4.1 Fast Reasoning (100 parallel calls) - mass mutation hints set 3 (200-299)
MASS_MUTATION_ROUNDS = 5  # Total mass mutation rounds
MASS_MUTATION_PATTERN = ["grok", "gemini", "grok", "claude", "grok"]
GROK_PARALLEL_CALLS = 100  # Number of parallel Grok calls per round
GEMINI_CALLS = 1  # Number of Gemini calls per round
CLAUDE_CALLS = 1  # Number of Claude calls per round
