HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: L-SHAPED PATH BETWEEN TWO MARKERS             ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the TWO non-zero marker cells in the input (they have different colors)
• These markers define a rectangular region by their positions
• Draw an L-shaped path connecting them using a NEW connector color

PATH CONSTRUCTION:
• From one marker: draw horizontally to reach the column of the other marker
• Then draw vertically to reach the other marker (or vice versa)
• The path forms a right angle at the corner where row of one meets column of the other
• The connector color fills the path BETWEEN the markers (not replacing them)

KEY OBSERVATIONS:
• The original marker colors remain unchanged at their positions
• The connector color is consistent (a third color not used by markers)
• The path follows grid lines (horizontal then vertical segments)
• One marker is at the horizontal end, the other at the vertical end of the L

YOUR CODE MUST:
1. Locate both marker positions
2. Draw horizontal segment from one marker toward the other's column
3. Draw vertical segment from that corner to the other marker
4. Use a new color for the path segments (excluding the marker positions themselves)
"""
