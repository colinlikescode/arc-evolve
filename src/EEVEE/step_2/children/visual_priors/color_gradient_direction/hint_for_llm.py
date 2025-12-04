HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS PUZZLE DETECTS COLOR GRADIENT DIRECTION  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Analyze how colors are distributed/transition across the input grid
• Output a line of marker color indicating the gradient direction:
  - UNIFORM input (all same color) → horizontal line in top row
  - Colors transition top-left to bottom-right → main diagonal
  - Colors transition top-right to bottom-left → anti-diagonal
• Fill all other cells with background color

HOW TO DETERMINE DIRECTION:
• Check if input is uniform (single color) → use horizontal
• Otherwise, examine where color boundaries/changes occur
• The diagonal that best aligns with color transitions determines output

OUTPUT STRUCTURE:
• Same dimensions as input
• Exactly one line of marker color
• All other cells are background (zero)
"""
