HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS PUZZLE FRAMES CLUSTERS OF NEARBY CELLS   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all non-zero marker cells in the input
• Identify CLUSTERS: groups of markers that are near each other (within ~2-3 cells distance)
• For each cluster containing 2+ markers:
  - Find the bounding box of all markers in that cluster
  - Draw a rectangular FRAME around this bounding box using a secondary color
  - The frame is drawn on cells adjacent to the bounding box (1 cell outward)
• Isolated single markers (not near others) remain unchanged - NO frame
• Original marker cells are PRESERVED (not overwritten by the frame)

KEY INSIGHT:
• Only clusters with multiple nearby markers get framed
• The frame color is different from the marker color
• The frame forms a hollow rectangle around the cluster's extent
"""
