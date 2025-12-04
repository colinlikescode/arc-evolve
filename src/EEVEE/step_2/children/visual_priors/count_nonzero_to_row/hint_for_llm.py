HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: COUNT NON-ZERO CELLS → OUTPUT AS SINGLE ROW   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Count all non-zero cells in the input grid
• Identify the non-zero color value (there is only one unique non-zero color)
• Create an output grid with dimensions 1 × (count of non-zero cells)
• Fill the entire output row with the non-zero color

CONCEPTUAL EXAMPLE:
Input (scattered cells):     Output:
. X .                        [X X X]  (3 non-zero cells → row of 3)
X . .
. X .

KEY INSIGHT:
• The output WIDTH equals the TOTAL COUNT of non-zero cells
• The output HEIGHT is always 1
• The output is uniformly filled with the non-zero color from input
"""
