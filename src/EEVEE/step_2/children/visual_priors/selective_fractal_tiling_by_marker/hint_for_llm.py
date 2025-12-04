HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SELECTIVE FRACTAL TILING BY MARKER COLOR     ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Output size = N × N blocks, where each block has same dimensions as input
• One non-zero color acts as the "marker" (identify which one by checking examples)
• For each position (r, c) in the input:
  - If input[r][c] == marker_color: copy the ENTIRE input pattern to block (r, c)
  - Otherwise: that block remains all zeros

HOW TO IDENTIFY THE MARKER COLOR:
• Look at which non-zero color's positions in the input match where the pattern copies appear in the output
• The marker color is typically one of two non-zero colors present
• Count the copies in output and match to positions of each candidate color

STRUCTURE:
Input (N×N) → Output (N²×N²) divided into N×N blocks
Each block at (r,c) = full input pattern if input[r][c] is the marker, else zeros
"""
