CLASSIFIER_PROMPT = """Does this puzzle involve HOLLOW RECTANGLE INTERIOR EXTRACTION?

Look for these indicators:
- The input contains one or more rectangular frames/borders made of a non-background color
- These rectangles have hollow interiors (like picture frames) with background color inside
- There may also be solid filled rectangles (no interior hole)
- The output shows the same grid size but the frames are removed
- The interior regions of hollow frames are filled with a different color
- Solid rectangles (with no interior) disappear entirely in the output

Key pattern: The transformation extracts and fills the interior space of hollow rectangular frames while removing the frame borders themselves.

Answer ONLY with: YES or NO"""
