CLASSIFIER_PROMPT = """Does this puzzle exhibit L-SHAPED LINE EXTENSION FROM MARKER PAIRS?

Look for these indicators:
- There are exactly TWO distinct non-background, non-noise marker colors in the grid
- Each marker color appears as a small cluster (typically 2 adjacent cells forming a short line segment)
- The two marker clusters are positioned at different locations, not adjacent to each other
- The transformation draws L-shaped connecting lines using one of the marker colors
- The L-shape extends from one marker cluster, turns at a right angle, and connects toward the other marker cluster

Key observations:
- One marker color stays in place while its color is used to draw the L-shaped extension
- The extension goes horizontally then vertically (or vice versa) to form an L/corner shape
- The lines extend from the END of each marker segment toward the other marker
- The two L-shaped extensions meet or align at a corner point

Answer ONLY with: YES or NO"""
