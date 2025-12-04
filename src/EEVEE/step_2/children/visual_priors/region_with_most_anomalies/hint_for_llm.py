HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FIND REGION WITH MOST ANOMALY MARKERS         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid is partitioned into rectangular REGIONS
• Each region has a DOMINANT COLOR (the majority of cells in that region)
• Some regions contain MARKER/ANOMALY cells (cells with a different color)
• Count how many marker cells appear in each region
• The OUTPUT is the dominant color of the region that has the MOST markers

HOW TO IDENTIFY:
• Find the distinct rectangular regions by their dominant colors
• For each region, count cells that differ from the region's dominant color
• The region with the highest anomaly count → output its dominant color

NOTE: One region may have zero anomalies (completely uniform) - this is NOT the answer.
"""
