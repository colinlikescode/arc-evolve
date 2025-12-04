HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: QUADRANT PATTERN ASSEMBLY PUZZLE              ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains 4 small L-shaped patterns (3 non-zero cells each in a 2x2 area)
• Each pattern is scattered in a different region of the input grid
• The output is a 4x4 grid composed of 4 quadrants (2x2 each)

ASSEMBLY LOGIC:
• Identify which quadrant of the input each pattern belongs to (top-left, top-right, bottom-left, bottom-right)
• Extract each 2x2 bounding box containing the L-pattern
• Place each pattern in the corresponding quadrant of the output:
  - Top-left input region → Output rows 0-1, cols 0-1
  - Top-right input region → Output rows 0-1, cols 2-3
  - Bottom-left input region → Output rows 2-3, cols 0-1
  - Bottom-right input region → Output rows 2-3, cols 2-3

KEY INSIGHT:
• The L-shapes point toward the center when assembled
• The center 2x2 area of the output will have the "missing corners" (zeros)
"""
