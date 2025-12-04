CLASSIFIER_PROMPT = """Does this puzzle involve DIAGONAL LINE EXTENSION WITH OFFSET MARKERS?

Look for these characteristics:
- A diagonal line of a non-background color running through the grid
- A triangular or stepped region of a different "marker" color (often gray) adjacent to the diagonal
- The marker region appears to indicate a gap or offset distance
- The output shows the diagonal line extended/continued AND parallel copies of the diagonal at specific offsets
- The marker color is removed in the output

Key indicators:
- Input has exactly two non-background colors: one forming a diagonal, one forming a triangular fill
- The triangular fill is adjacent to and "touches" the diagonal line
- Output has only the diagonal color (marker color removed)
- Output shows multiple parallel diagonal lines

Answer ONLY with: YES or NO"""
