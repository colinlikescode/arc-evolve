CLASSIFIER_PROMPT = """Does this puzzle exhibit PATTERN CONTINUATION/EXTRAPOLATION?

Pattern continuation means:
- The input contains a pattern of non-zero cells that has a clear directional movement or periodic structure
- The output grid is taller than the input (extended vertically)
- The pattern from the input is continued/extrapolated downward following the same trajectory or period
- The continuation preserves the same "motion" or "rhythm" of the original pattern

Look at the training examples:
- Is the output taller than the input while keeping the same width?
- Does the non-zero pattern in the input have a clear direction or periodicity?
- Does the output show the same pattern extended further in that direction?
- Is the pattern "continued" as if drawing the next logical steps?

Answer ONLY with: YES or NO"""
