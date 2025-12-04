HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CROSS CONSOLIDATION AROUND CENTERS            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify "center" cells and their associated "marker" cells
• Markers are cells that share a row OR column with a center (same color markers go with same center)
• For each center-marker group, find the closest marker distance
• Create a cross pattern: place markers in the 4 cardinal directions adjacent to the center
• The cross uses the marker color, centered on the center cell
• Remove all original scattered markers - only the consolidated crosses remain

KEY INSIGHT:
• Each unique center has markers of a specific color forming a loose cross pattern
• Output consolidates these into a tight cross directly touching the center
• The cross extends only 1 cell in each cardinal direction from the center

YOUR APPROACH:
1. Find cells that appear to be "centers" (have markers aligned in rows/columns)
2. Group markers with their associated centers
3. For each group, draw a plus/cross pattern with marker color adjacent to center
4. Clear all other non-zero cells
"""
