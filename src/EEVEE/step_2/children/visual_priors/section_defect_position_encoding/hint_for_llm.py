HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SECTION DEFECT POSITION ENCODING PUZZLE       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input is divided into N vertical sections by separator columns
• Each section contains a background color with a possible small "defect" (embedded marker cells)
• The output has N rows, each row is a uniform color
• Each output row's color encodes the VERTICAL POSITION of the defect in the corresponding section

POSITION-TO-COLOR MAPPING:
• Identify all possible vertical positions for the defect
• Each unique vertical position maps to a specific output color
• Learn this mapping from training examples

YOUR APPROACH:
1. Find separator columns to identify section boundaries
2. For each section, locate the small defect pattern (non-background cells inside the section)
3. Determine the vertical position of the defect (top, upper-middle, lower-middle, bottom, etc.)
4. Map each position to the corresponding output color based on training examples
5. Output is a grid where each row represents one section, filled with the mapped color
"""
