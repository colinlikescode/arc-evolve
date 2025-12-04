HINT = """
╔══════════════════════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SHAPE STACKING WITH DIRECTION INDICATOR                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

THE PATTERN:

1. The grid has a HORIZONTAL SEPARATOR LINE dividing it into sections
2. A CROSS or T-SHAPE acts as a DIRECTION INDICATOR
3. One section contains shapes that need to be STACKED
4. The direction indicator determines UP vs DOWN stacking

KEY CONCEPTS:

• SEPARATOR LINE: A horizontal line (often gray/5s) dividing the grid
  - Separates the "template" section from the "base" section

• DIRECTION INDICATOR: A cross or T-shaped marker
  - If the vertical part points UP → stack shapes ABOVE
  - If the vertical part points DOWN → stack shapes BELOW
  - Look at which way the cross "extends" from its horizontal bar

• STACKING: Placing shapes adjacent to each other
  - Shapes touch but don't overlap
  - Horizontal alignment is preserved
  - Vertical placement determined by direction indicator

WHAT TO DETERMINE FROM TRAINING EXAMPLES:
• Which section is the "base" output (usually bottom section)?
• Which shapes from the template section get stacked?
• How to read the direction indicator (cross orientation)?
• How to align shapes horizontally when stacking?

APPROACH:
1. Find the separator line to identify sections
2. Determine direction from the cross/T-shape indicator
3. Use one section as the base output
4. Take shapes from the other section
5. Stack them above or below existing shapes based on direction
6. Align horizontally to match positions
"""

