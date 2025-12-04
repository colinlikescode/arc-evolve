CLASSIFIER_PROMPT = """Does this puzzle involve FILLING A RECTANGULAR VOID with a highlight color?

Look for these indicators:
- The input grid contains a pattern made of one non-zero color on a background color (typically black/zero)
- There is a large rectangular region that is entirely the background color (all zeros)
- This rectangular void appears to be "missing data" or an "empty gap" in the pattern
- The void spans multiple rows AND columns, creating a clear rectangular absence

In the output:
- The rectangular void is filled with a distinct highlight color (different from both the pattern color and background)
- The original pattern remains unchanged outside the void
- The highlight color marks/identifies where the void was located

This is NOT about symmetry or tiling - it's about detecting and marking empty rectangular regions within a patterned grid.

Answer ONLY with: YES or NO"""
