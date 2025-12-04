CLASSIFIER_PROMPT = """Does this puzzle exhibit FRAME WITH SCALED PATTERN FILL?

This pattern type involves:
- A rectangular FRAME or border made of one color (forming a hollow rectangle)
- A separate small PATTERN/SHAPE made of a different color elsewhere in the input
- The output is the frame extracted and filled with the small pattern SCALED UP to fit the interior

Look at the training examples:
- Is there a hollow rectangular frame/border in the input?
- Is there a separate small shape or pattern (different color) elsewhere in the input?
- Does the output show the frame with its interior filled by a scaled-up version of the small pattern?
- Is the scaling factor determined by how many times the small pattern fits into the frame's interior?

The key insight: The small pattern acts as a "stamp" that gets enlarged to fill the frame's interior space.

Answer ONLY with: YES or NO"""
