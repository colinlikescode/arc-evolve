HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SECTIONED GRID WITH UNIQUE MARKER DETECTION   ║
╚══════════════════════════════════════════════════════════════╝

THE STRUCTURE:
• The input grid is divided into sections by divider lines (a distinct separator color forming complete rows/columns)
• This creates a grid of regions (e.g., 3×3 arrangement of sections)
• Each section contains scattered marker cells on a background

THE TRANSFORMATION RULE:
• The output has one cell per section in the input
• For each section, examine the positions of marker cells
• Compare marker positions across ALL sections
• A section gets marked (non-zero) in the output if it contains a marker at a position where NO OTHER section has a marker

CONCEPTUAL APPROACH:
1. Identify the divider color (forms complete rows/columns)
2. Extract each section between dividers
3. For each relative position within sections, count how many sections have a marker there
4. If a section has a marker at a position where it's the ONLY one → mark that section in output

The output essentially flags sections that have "unique" marker placements not found elsewhere.
"""
