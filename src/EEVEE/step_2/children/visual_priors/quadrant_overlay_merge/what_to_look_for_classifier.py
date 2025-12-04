CLASSIFIER_PROMPT = """Does this puzzle involve QUADRANT OVERLAY/MERGING?

Look for these indicators:
- The input grid is divided into four equal quadrants (2x2 arrangement of regions)
- Each quadrant contains a sparse pattern using a distinct color against a black/zero background
- The output is the same size as one quadrant
- The output appears to combine/overlay the patterns from all four quadrants
- Each position in the output reflects which quadrant(s) had non-zero values at that relative position

Check if:
- Input dimensions are exactly 2x the output dimensions in both height and width
- Each quadrant uses a different non-zero color
- The output contains colors from multiple quadrants merged together

Answer ONLY with: YES or NO"""
