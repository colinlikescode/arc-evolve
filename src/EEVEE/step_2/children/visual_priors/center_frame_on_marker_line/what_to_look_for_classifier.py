CLASSIFIER_PROMPT = """Does this puzzle involve CENTERING A SHAPE ALONG A LINE OF MARKERS?

Look for these indicators:
- There is a small rectangular frame/border shape made of one color surrounding a center cell of another color
- There is a line of single marker cells (same color as the center) extending outward from the frame in one or two opposite directions
- The markers form a line (horizontal or vertical) that passes through the frame's center
- The transformation repositions the frame to be CENTERED along the full extent of the marker line
- The markers themselves remain in their positions, only the frame shape moves

Check if:
- Input has a bordered rectangular shape with markers extending in a line from its center
- Output shows the same elements but with the frame shifted to balance the markers on both sides

Answer ONLY with: YES or NO"""
