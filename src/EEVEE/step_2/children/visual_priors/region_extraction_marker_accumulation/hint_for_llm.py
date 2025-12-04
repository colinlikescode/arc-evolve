HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  REGION EXTRACTION WITH MARKER ACCUMULATION              ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
1. IDENTIFY DIVIDER LINES: Find complete rows/columns filled with a single non-background color - these partition the grid

2. SELECT A REGION: Extract the rectangular region bounded by specific divider lines (typically the region containing scattered marker cells)

3. ACCUMULATE MARKERS: For each row (or column) in the extracted region:
   - Count how many marker cells exist in that row
   - Stack/fill that many cells from one edge (the edge determined by the divider orientation)
   - The markers "collapse" toward one side like gravity

4. PRESERVE BORDERS: The divider lines become the borders of the output grid

CONCEPTUAL VISUALIZATION:
- Input region:  [divider] . . X . X . . [divider]
- Output row:    [divider] X X . . . . . [divider]
  (2 markers consolidated to one side)

The output dimensions are determined by the spacing between the selected divider lines.
"""
