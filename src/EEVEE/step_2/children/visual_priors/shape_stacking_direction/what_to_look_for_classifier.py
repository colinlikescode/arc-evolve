CLASSIFIER_PROMPT = """Does this puzzle involve STACKING SHAPES based on a DIRECTION INDICATOR?

Look for these indicators:

1. INPUT structure:
   - A HORIZONTAL SEPARATOR LINE dividing the grid into sections
   - A CROSS or ARROW shape that indicates a DIRECTION (up or down)
   - Multiple shapes in different colors

2. The DIRECTION INDICATOR:
   - A cross or T-shaped marker (often in red/color 2)
   - Points either UP or DOWN
   - Determines where to place shapes relative to each other

3. OUTPUT shows:
   - Shapes have been STACKED or placed ADJACENT to each other
   - The stacking direction matches the direction indicator
   - One section of the input becomes the base, shapes from another section get added

4. Key characteristics:
   - Grid is divided into template/reference section and working section
   - Direction indicator tells whether to stack above or below
   - Shapes are aligned and placed touching each other

What to look for:
- Is there a separator line dividing the grid?
- Is there a cross/arrow shape indicating direction?
- Are shapes being combined or stacked in the output?

Answer ONLY with: YES or NO"""

