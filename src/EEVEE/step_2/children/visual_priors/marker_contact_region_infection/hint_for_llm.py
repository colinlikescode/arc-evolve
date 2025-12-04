HINT = """
╔══════════════════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER LINE EXTENSION WITH CONTACT INFECTION              ║
║  USE THIS HINT ONLY - IGNORE ANY OTHER CONFLICTING HINTS                 ║
╚══════════════════════════════════════════════════════════════════════════╝

THE EXACT TRANSFORMATION:
1. Find all MARKER cells (isolated single cells, often near edges/corners of the grid)
2. Find all REGION shapes (rectangular blocks of a different color)
3. From EACH marker, extend lines HORIZONTALLY and VERTICALLY across the entire grid
4. Any region that is TOUCHED by these lines (adjacent or passing through) gets INFECTED
5. Infected regions are completely filled with the marker color

STEP-BY-STEP ALGORITHM:
```
1. Identify marker cells (the isolated single-color cells, often at grid edges)
2. Identify region shapes (the rectangular blocks of another color)
3. For each marker at position (row, col):
   - Draw a HORIZONTAL line across the entire row (from col 0 to last col)
   - Draw a VERTICAL line down the entire column (from row 0 to last row)
4. For each region:
   - Check if ANY cell of the region is ADJACENT to the extended lines
   - Adjacent = directly touching (up/down/left/right) OR diagonally touching
   - If adjacent → fill the ENTIRE region with the marker color
5. Regions NOT touched remain unchanged
```

CRITICAL DETAILS:
- Markers extend BOTH horizontally AND vertically (forming a + cross through the grid)
- Contact includes SIDE ADJACENCY - if a line passes right NEXT TO a region, that counts!
- The ENTIRE connected region converts, not just the cells that touch
- Regions with no adjacent marker lines stay their original color

WHAT "TOUCHING BY THE SIDE" MEANS:
- If the extended line is in row 5, and a region has cells in row 4 or row 6 at the same columns, that's side contact
- If the extended line is in column 3, and a region has cells in column 2 or column 4 at the same rows, that's side contact
- Diagonal adjacency also counts as contact

IGNORE any hints about "staircase", "row-by-row", or "diagonal fill" - those do NOT apply here!
"""
