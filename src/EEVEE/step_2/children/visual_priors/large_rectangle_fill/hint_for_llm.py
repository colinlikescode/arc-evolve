HINT = """
╔══════════════════════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: LARGE SOLID RECTANGLES → FILL WITH NEW COLOR                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

THE PATTERN:

1. Find all LARGE SOLID RECTANGLES of uniform color in the input
2. A rectangle is "solid" if ALL cells within its bounding box are the SAME color
3. Change ALL cells in those large rectangles to a specific fill color
4. Smaller shapes and irregular shapes remain UNCHANGED

KEY CONCEPTS:

• SOLID RECTANGLE: A rectangular region where every cell has the same color
  - Does NOT have to be a square! Can be 6x5, 4x7, 5x4, etc.
  - Any width × height combination that meets the size threshold
  - Not just the border, but the ENTIRE interior filled with same color

• SIZE THRESHOLD: Only rectangles above a minimum size get filled
  - Study the training examples to determine the threshold
  - Could be minimum width AND height (e.g., at least 4 wide AND 4 tall)
  - Examples: 4x4 ✓, 6x5 ✓, 4x7 ✓, 3x10 ✗ (too narrow)

• HANDLING OVERLAPS: If rectangles could overlap, larger ones take priority

WHAT TO DETERMINE FROM TRAINING EXAMPLES:
• What is the minimum WIDTH and HEIGHT for a rectangle to qualify?
• What color are the rectangles filled with?
• Are there any special cases (colors to ignore, etc.)?

APPROACH:
1. Scan the grid for potential rectangular regions of any aspect ratio
2. For each candidate, verify it's completely filled with the same color
3. Check if BOTH width and height meet the minimum threshold
4. Fill qualifying rectangles with the target color
5. Handle any overlapping cases appropriately
"""

