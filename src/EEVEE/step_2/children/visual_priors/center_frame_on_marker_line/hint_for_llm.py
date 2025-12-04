HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CENTER FRAME ALONG MARKER LINE               ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the rectangular FRAME (border cells surrounding a center cell)
• Identify the LINE OF MARKERS (same color as center, extending in one direction)
• The markers form a line passing through where the frame's center should be

TO SOLVE:
• Find all marker positions along the line (including the frame's center marker)
• Calculate the MIDPOINT of the marker line
• Reposition the frame so its center aligns with the midpoint of all markers
• The frame shifts along the marker line direction to achieve balance
• Equal (or near-equal) number of markers should appear on each side of the frame

KEY INSIGHT:
• Count markers before and after the frame's center position
• Shift the frame so markers are evenly distributed on both sides
• Only the frame moves; individual markers stay in place
"""
