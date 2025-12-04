CLASSIFIER_PROMPT = """Does this puzzle involve BORDER INTERSECTION GRID FILLING?

Look for these indicators:
- The grid has two distinct border colors forming L-shaped or corner regions (one color dominates one edge, another dominates an adjacent edge)
- There is a rectangular interior region filled with a neutral/background color
- The borders are irregular (jagged/stepped edges into the interior)
- The output adds a new color forming horizontal and vertical lines (a cross or grid pattern) within the interior region
- These lines appear to mark "transition boundaries" based on where the irregular borders change depth

The pattern involves drawing lines through the interior that correspond to the deepest penetration points of each border region.

Answer ONLY with: YES or NO"""
