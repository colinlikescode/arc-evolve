HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DENSITY-BASED CROSS PATTERN DETECTION         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid contains scattered non-zero cells
• Divide the input into regions corresponding to a 3x3 output structure
• Count the density of non-zero cells in each directional region (top, bottom, left, right, center)
• The output is a 3x3 cross/plus pattern where:
  - The center cell is always filled (indicator color)
  - Arms extend toward regions with higher concentrations of colored cells
  - The cross orientation reflects the dominant directional bias of the input distribution

OUTPUT STRUCTURE:
• Always 3x3 with an indicator color (replacing original color)
• Forms a cross shape: vertical bar, horizontal bar, T-shape, L-shape, or full plus
• The specific shape depends on which edges/corners of the input have more colored cells

KEY INSIGHT:
• Analyze which halves/quadrants of the input have more non-zero cells
• The output cross points toward the denser regions
• Center column of output is filled if input has vertical concentration
• Center row of output is filled if input has horizontal concentration
"""
