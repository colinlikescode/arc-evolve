CLASSIFIER_PROMPT = """Does this puzzle involve FILLING ENCLOSED RECTANGULAR REGIONS?

Look for these indicators:
- The input contains rectangular regions bounded by a non-background color (forming closed borders/frames)
- Some rectangular regions have a marker/dot inside them (a single cell of the border color within the interior)
- Some rectangular regions are empty inside (only background color in the interior)
- The transformation fills the interior of certain rectangles with a new fill color
- Rectangles WITH a marker inside get filled, while rectangles WITHOUT a marker stay empty (or vice versa)

Key observations:
- Are there clearly defined rectangular borders made of a single color?
- Do some rectangles contain an interior marker while others don't?
- In the output, are the interiors of marked rectangles filled with a different color?
- Does the marker remain visible after filling (not overwritten)?

Answer ONLY with: YES or NO"""
