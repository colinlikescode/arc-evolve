HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A BLOCK COMPRESSION PUZZLE            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid is divided into equal-sized square blocks
• Output dimensions = input dimensions ÷ block size
• Each block maps to ONE cell in the output

FOR EACH BLOCK:
• Identify the "marker" color (appears as isolated cells across the grid)
• Ignore the marker color and background color (zeros)
• If the block contains a uniform non-marker, non-background color → output that color
• If the block is mostly background → output background (zero)

KEY INSIGHT:
• The marker color is a "distractor" - it should be excluded from consideration
• Look for the dominant solid-fill color in each block (ignoring markers)
• The output is essentially a thumbnail showing which regions contain colored objects
"""
