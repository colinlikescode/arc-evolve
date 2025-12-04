"""Feedback prompt for iteration rounds."""


FEEDBACK_TEMPLATE = """
╔══════════════════════════════════════════════════════════════╗
║             STEP 2: INSTRUCTIONS TO IMPROVE                 ║
╚══════════════════════════════════════════════════════════════╝

You already attempted this question earlier. It was tested on training examples. Here's how you did:

$$feedback$$

Use this feedback to improve your solution. Focus on fixing the errors identified above.

Do not move onto step 3, until step 2 is fully complete."""


def build_feedback_prompt(feedback_str: str) -> str:
    """
    Build feedback prompt for iteration rounds.
    
    Args:
        feedback_str: Formatted feedback from previous attempts
    
    Returns:
        Complete feedback prompt
    """
    return FEEDBACK_TEMPLATE.replace("$$feedback$$", feedback_str)

