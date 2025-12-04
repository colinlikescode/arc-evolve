HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER-DIRECTED LINE EXTENSION PUZZLE         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find rectangular regions filled with a dominant non-background color
• Each rectangle contains exactly ONE "marker" cell of an accent color
• The marker's position within its rectangle indicates a DIRECTION:
  - The marker points toward the NEAREST edge of its containing rectangle
• Draw a line of the accent color extending FROM the marker:
  - The line continues in that direction
  - It extends OUTWARD beyond the rectangle boundary
  - It stops at the grid edge (or fills to the boundary)

KEY INSIGHT:
• The marker cell is NOT centered - its offset from center determines direction
• The line extends perpendicular to the rectangle's long axis OR toward the closest short edge
• The original rectangle and marker remain; the line is ADDED

YOUR APPROACH:
1. Identify each filled rectangle and locate its marker cell
2. Determine which edge of the rectangle the marker is closest to
3. Extend a line of the marker's color in that direction to the grid boundary
"""
