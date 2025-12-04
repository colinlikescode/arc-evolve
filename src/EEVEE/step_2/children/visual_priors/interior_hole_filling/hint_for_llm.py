HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS AN INTERIOR HOLE FILLING PUZZLE       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the background color (typically zero)
• Find all background cells that are connected to the grid boundary (flood-fill from edges)
• Background cells NOT reachable from the boundary are "interior holes"
• Replace all interior hole cells with a fill value (look for a consistent replacement value in examples)
• Leave boundary-connected background cells unchanged

CONCEPTUAL APPROACH:
1. Start from all edge cells that have the background value
2. Flood-fill to find all background cells connected to the boundary
3. Any background cell NOT reached by this flood-fill is interior
4. Replace interior background cells with the fill color
5. Keep all non-background cells and boundary-connected background cells as-is

The fill value is typically a specific non-zero color that appears in the output where zeros used to be.
"""
