HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MINORITY COLOR FREQUENCY RANKING PUZZLE       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a grid of small blocks separated by zeros
• Identify the DOMINANT color (the one appearing in the most blocks)
• Identify all MINORITY colors (non-dominant, non-background colors)
• Count how many blocks contain each minority color
• Output the minority colors as a column, ordered by FREQUENCY (most frequent first)

HOW TO SOLVE:
1. Parse the grid to find all distinct block colors (ignore zeros/background)
2. Count occurrences of each color
3. The most frequent color is the "dominant" - exclude it
4. Rank remaining colors by their count (descending)
5. Output as a single column: most frequent minority → least frequent minority

NOTE: If two colors have equal frequency, check the examples for tie-breaking (may be by color value or position).
"""
