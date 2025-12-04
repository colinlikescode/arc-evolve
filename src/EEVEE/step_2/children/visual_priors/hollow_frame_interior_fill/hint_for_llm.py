HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: HOLLOW FRAME INTERIOR EXTRACTION              ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all rectangular frames (hollow rectangles) made of non-background color
• Each frame has a border and an interior region (filled with background color)
• In the output: REMOVE the frame borders entirely
• FILL the interior region with a new output color
• Solid rectangles (no interior hole) are removed completely

HOW TO IDENTIFY INTERIORS:
• A hollow frame has outer border cells and inner background cells
• The interior is the rectangular region INSIDE the border (excluding the border itself)
• Interior dimensions = (frame_height - 2) × (frame_width - 2)

OUTPUT CONSTRUCTION:
• Start with a blank grid (all background)
• For each hollow frame found: fill its interior region with the output color
• Ignore/skip any solid filled rectangles (they produce nothing)
"""
