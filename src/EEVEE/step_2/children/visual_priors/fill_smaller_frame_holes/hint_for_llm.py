HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FRAME COMPARISON - FILL HOLES IN SMALLER ONES ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid contains multiple rectangular FRAMES (bordered boxes) of the same color
• Each frame's interior may contain HOLES (background-colored cells)
• Find the frame with the LARGEST contiguous interior hole region - this is the REFERENCE
• For all OTHER frames that have holes: FILL those holes with a marker color
• The reference frame (largest hole) remains UNCHANGED

HOW TO IDENTIFY:
• Frames are closed rectangular borders of a non-background color
• Interior = cells inside the border
• Holes = background-colored cells inside the interior
• Compare hole sizes across all frames
• The frame with the biggest hole area stays as-is; smaller holes get filled

YOUR APPROACH:
1. Identify all rectangular frames in the grid
2. For each frame, calculate the interior hole area
3. Find the frame with the maximum hole area (reference frame)
4. Fill holes in all other frames with the marker color
5. Leave the reference frame unchanged
"""
