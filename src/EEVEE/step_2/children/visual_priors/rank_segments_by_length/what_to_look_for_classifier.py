CLASSIFIER_PROMPT = """Does this puzzle involve RANKING LINE SEGMENTS BY LENGTH and assigning colors based on rank?

Look for these indicators:
- The input contains multiple separate line segments (horizontal or vertical) made of a single non-zero color
- All segments use the same color in the input
- The output replaces each segment with a DIFFERENT color
- The color assigned to each segment appears to depend on its LENGTH relative to other segments
- Longer segments get one color, medium segments get another, shorter segments get a third color

The pattern involves:
- Identifying distinct line segments (connected cells in a row or column)
- Measuring/comparing their lengths
- Assigning output colors based on length ranking (longest, middle, shortest)

Answer ONLY with: YES or NO"""
