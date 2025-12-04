HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: U-SHAPE OPENING PROJECTION TO BOTTOM ROW     ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify all "U-shaped" or "bracket" patterns in the input
• Pattern structure: 3 cells in a row (X X X) with 2 cells below leaving middle gap (X 0 X)
• The "opening" of each U-shape is the center cell of the top row (the gap position)

WHAT TO DO:
• Keep the entire input grid unchanged
• For EACH U-shaped pattern found:
  - Find the column position of its center/opening (middle of the 3-cell top)
  - Place a marker cell at the BOTTOM ROW of the grid in that column
• Use a consistent marker color (distinct from pattern colors) for all markers

VISUAL:
```
X X X        Pattern detected
X 0 X        Opening at middle column
  ↓
  ↓          Project downward
  ↓
  M          Marker at bottom row
```
"""
