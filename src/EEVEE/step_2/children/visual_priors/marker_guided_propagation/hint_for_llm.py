HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER-GUIDED COLOR PROPAGATION               ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the "marker" color (appears as scattered single cells, distinct from shape colors)
• Markers indicate propagation paths/directions for nearby colored shapes
• Each colored shape extends along the path indicated by adjacent markers
• The marker cells themselves are removed in the output
• Colors propagate FROM their original position TOWARD/THROUGH marker positions

HOW TO SOLVE:
1. Find the marker color (scattered single cells, not forming cohesive shapes)
2. For each colored shape, find adjacent/nearby markers
3. Propagate each shape's color along the marker path direction
4. Remove marker columns/cells, consolidating the grid
5. The output grid may be narrower as marker positions collapse

KEY INSIGHT: Markers act as "rails" or "guides" - colors slide along them and replace them.
"""
