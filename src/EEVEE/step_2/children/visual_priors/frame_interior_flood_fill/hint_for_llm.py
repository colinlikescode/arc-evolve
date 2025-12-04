HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FRAME INTERIOR FLOOD FILL WITH MARKER COLOR  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Each rectangular frame has a BORDER COLOR and contains a single MARKER cell of a different color
• The frame border has a GAP (missing cells) on one side
• Fill the INTERIOR of the frame (all background cells inside) with the MARKER color
• EXTEND the marker color outward through the gap, creating a row/column that spans the frame width

KEY OBSERVATIONS:
• The border color remains unchanged
• The marker cell indicates which color to use for filling
• The gap in the frame indicates the direction to extend the fill
• The extension creates a line of marker color outside the frame, aligned with the gap

YOUR APPROACH:
1. Identify rectangular frames made of a consistent non-background color
2. Find the unique marker color inside each frame
3. Fill all background cells inside the frame with the marker color
4. Extend the marker color outward through any gap in the frame border
"""
