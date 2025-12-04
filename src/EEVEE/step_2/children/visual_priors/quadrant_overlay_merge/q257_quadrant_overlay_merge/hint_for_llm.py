HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A QUADRANT OVERLAY/MERGE PUZZLE       ║
╚══════════════════════════════════════════════════════════════╝

THE STRUCTURE:
• Input is divided into 4 quadrants by separator lines (single-color row and column)
• Each quadrant has its own dominant color pattern
• Output size equals one quadrant's size

THE TRANSFORMATION RULE:
• Start with one quadrant as the base (typically the one with the most common color)
• For each cell position, check all 4 quadrants
• Where the base quadrant has background (zero), fill with non-zero values from other quadrants
• Each quadrant contributes its non-zero cells to the final merged output

PRIORITY LOGIC:
• One color acts as the primary/base layer
• Other quadrant colors fill in where the base has gaps (zeros)
• The result is a composite overlay of all four quadrant patterns

YOUR APPROACH:
1. Identify and remove the separator lines to isolate the 4 quadrants
2. Determine which quadrant/color serves as the base layer
3. Overlay non-zero cells from other quadrants onto positions where base is zero
"""
