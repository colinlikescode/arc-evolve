HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CHECKERBOARD EXTENSION / MASK REMOVAL         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input has TWO regions: a checkerboard pattern region + a solid "mask" color region
• The mask color fills borders/margins (bottom, right, or L-shaped areas)
• Output REMOVES the mask and EXTENDS the checkerboard to fill entire grid

KEY INSIGHT - PHASE SHIFT:
• The checkerboard pattern uses 2+ alternating colors
• Each cell's color depends on (row + col) parity
• The output pattern appears SHIFTED by one cell compared to input
• This means: output[r][c] uses the OPPOSITE color of what input[r][c] would have

HOW TO SOLVE:
1. Identify the mask color (the uniform solid color in border regions)
2. Identify the pattern colors (the alternating colors in the checkerboard)
3. Determine the pattern's period/cycle (how many colors alternate)
4. Fill the ENTIRE output grid with the extended checkerboard pattern
5. Apply a phase shift: swap which color goes at even vs odd positions

The output is a pure checkerboard with NO mask color remaining.
"""
