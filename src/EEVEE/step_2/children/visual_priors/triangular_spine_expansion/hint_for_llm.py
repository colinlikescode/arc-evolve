HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TRIANGULAR EXPANSION FROM VERTICAL SPINE      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the vertical line (spine) of non-zero cells in the input
• The spine color and a NEW secondary color alternate in a checkerboard pattern
• Create a triangular expansion that grows from the spine

TRIANGLE SHAPE:
• At the TOP row of the spine: expand to fill the entire row width
• Each row DOWN: the triangle narrows by one cell on each side
• At the BOTTOM of the spine: only the spine cell remains colored
• The expansion is SYMMETRIC around the spine column

ALTERNATING PATTERN:
• Colors alternate in a checkerboard fashion (both horizontally and vertically)
• The spine column keeps its original color at each row
• Adjacent cells alternate with a secondary fill color

BOUNDARY RULES:
• The triangle only exists in rows where the spine was present
• Below the spine (empty rows), output remains all zeros
• The triangle cannot extend beyond grid boundaries
"""
