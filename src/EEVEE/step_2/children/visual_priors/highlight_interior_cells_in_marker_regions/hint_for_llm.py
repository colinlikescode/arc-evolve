HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: HIGHLIGHT INTERIOR CELLS IN MARKER REGIONS   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the "marker color" (a color that appears in small scattered clusters)
• Find connected regions/clusters containing this marker color
• Within each cluster's bounding area, locate cells of the dominant grid color
• These dominant-colored cells that are INSIDE the marker region get replaced with a NEW highlight color
• The marker color cells themselves stay unchanged
• Everything outside marker regions stays unchanged

WHAT TO LOOK FOR:
• Marker color forms small irregular patches mixed with the dominant color
• The dominant color cells WITHIN these patches become highlighted
• Think of it as: "color the dominant cells that are trapped inside marker boundaries"

KEY INSIGHT:
• For each marker cluster, find its rectangular bounds
• Cells of the dominant color within those bounds → change to highlight color
• The marker color acts as a "container" and the dominant color inside gets marked
"""
