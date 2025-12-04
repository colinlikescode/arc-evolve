HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER-GUIDED OBJECT REPOSITIONING            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the main object (a small rectangular block of one color)
• Identify scattered marker cells (single cells of a different color)
• Each marker indicates a direction relative to the main object
• Move each marker to be adjacent to the main object, preserving its relative direction

KEY OBSERVATIONS:
• Markers that are above the object → place above/adjacent to object's top edge
• Markers that are below the object → place below/adjacent to object's bottom edge
• Markers that are left of the object → place to the left of the object
• Markers that are right of the object → place to the right of the object
• The marker's row/column offset from the object determines its exact placement

YOUR APPROACH:
1. Find the bounding box of the main object
2. For each marker, determine its relative position (direction) from the object
3. Reposition each marker to be immediately adjacent to the object in that direction
4. Clear original marker positions that are not adjacent to the object
"""
