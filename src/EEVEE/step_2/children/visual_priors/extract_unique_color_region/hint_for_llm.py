HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: EXTRACT THE UNIQUE/MINORITY COLOR REGION      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid is divided into multiple regions by bands of background (zero) cells
• Each region contains a pattern using one non-zero color mixed with zeros
• One color appears in ONLY ONE region (the "unique" or "minority" color)
• Another color appears in MULTIPLE regions (the "common" or "majority" color)

YOUR TASK:
• Identify the separator bands (rows/columns of all zeros)
• Locate each distinct region
• Determine which non-zero color appears in the fewest regions
• Extract the region containing that unique color as the output
• The output preserves the exact pattern (including zeros) from that region

KEY INSIGHT: Find the color that appears in only one quadrant/region - extract that entire region as output.
"""
