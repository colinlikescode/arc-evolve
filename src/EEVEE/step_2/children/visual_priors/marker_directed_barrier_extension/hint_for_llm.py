HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER-DIRECTED BARRIER EXTENSION PUZZLE      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the solid rectangular BARRIER region (uniform non-background color)
• Identify scattered MARKER cells (different non-background color)
• The barrier extends toward each marker location

HOW EXTENSION WORKS:
• Find the edge of the barrier closest to each marker
• Extend the barrier color from that edge to reach the marker's position
• If barrier is horizontal: extend vertically to marker's column
• If barrier is vertical: extend horizontally to marker's row
• The marker cells themselves are replaced with the barrier color

OUTPUT CONSTRUCTION:
1. Start with background everywhere except the barrier
2. Keep the original barrier intact
3. For each marker position: draw barrier color from the nearest barrier edge to that position
4. Remove all original marker colors

The markers act as "targets" telling the barrier where to grow protrusions.
"""
