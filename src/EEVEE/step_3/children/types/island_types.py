"""Type definitions for the solver."""
from typing import TypedDict, Optional, Literal


class TrainResult(TypedDict):
    """Result of running code on a single training example."""
    success: bool
    output: str
    soft_score: float
    error: Optional[str]
    code: str


class TestResult(TypedDict):
    """Result of running code on a single test input."""
    success: bool
    output: str
    soft_score: float
    error: Optional[str]
    code: str


class IslandResult(TypedDict):
    """Result from a single island's full evolution."""
    train_results: list[TrainResult]
    results: list[TestResult]  # test results
    iteration: int
    island_id: int  # Which island (0-4) produced this result
    attempts: list  # Previous solution attempts (for mass mutation context)


class Solution(TypedDict):
    """A solution attempt with feedback and score."""
    code: str
    explanation: str  # Step-by-step English instructions
    feedback: str
    score: float


class IslandConfig(TypedDict, total=False):
    """Configuration for a single island."""
    llm_id: Literal["claude", "gemini"]
    temperature: float
    max_iterations: int
    max_feedback_examples: int
    feedback_selection_rate: float
    seed: int
    randomize_training_order: bool
    ascending_score_order: bool
    return_best_result: bool
    timeout_s: float
    per_iteration_retries: int
    # Optional hybrid island fields
    switch_llm_after: int  # Switch to different LLM after this iteration
    switch_to_llm_id: Literal["claude", "gemini"]  # LLM to switch to
    # Optional round-based model switching (for complex schedules)
    # Note: Grok is ONLY used in the 4-round mass mutation phase AFTER all islands complete
    claude_rounds: list[int]  # Iteration numbers (0-indexed) where Claude should run
    # Visual prior hints control
    receives_hints: bool  # Whether this island receives visual prior hints (default True)

