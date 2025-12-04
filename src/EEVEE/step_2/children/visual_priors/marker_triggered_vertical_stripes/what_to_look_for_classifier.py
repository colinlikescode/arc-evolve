CLASSIFIER_PROMPT = """Does this puzzle exhibit a MARKER-TRIGGERED VERTICAL STRIPE FILL pattern?

This pattern means:
- The input contains a single non-background colored cell (a "marker")
- The output fills ALL rows ABOVE the marker's row with a repeating vertical stripe pattern
- The stripe pattern alternates between a fill color and the background color
- The stripe columns are determined by the marker's column position (same parity columns get filled)
- The marker cell remains in its original position
- Rows at or below the marker remain unchanged (all background)

Look at the training examples:
- Is there exactly one non-background cell in the input?
- In the output, are the rows above that cell filled with alternating vertical stripes?
- Does the marker stay in place while stripes appear above it?
- Do the stripes follow a consistent column parity pattern based on the marker's position?

Answer ONLY with: YES or NO"""
