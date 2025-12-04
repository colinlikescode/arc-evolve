CLASSIFIER_PROMPT = """Does this puzzle involve SHAPE OUTLINING AND INTERIOR FILLING?

Look for these indicators:
- The input contains multiple rectangular shapes/frames made of a non-background color
- Some shapes may be "hollow" (have background color inside their boundaries) while others are "solid"
- In the output, each shape receives an additional border/outline in a new color surrounding it
- The interior holes of hollow shapes (background cells enclosed by the shape) are filled with another distinct color
- Solid shapes (no interior holes) just get the border added without interior filling

Key observations:
- Are there distinct rectangular regions made of the same non-background color?
- Do some regions have "holes" (background color enclosed within)?
- Does the output show borders added around shapes and holes filled in?

Answer ONLY with: YES or NO"""
