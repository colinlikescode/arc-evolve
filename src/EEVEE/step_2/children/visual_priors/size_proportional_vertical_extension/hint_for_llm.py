HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SIZE-BASED VERTICAL EXTENSION PUZZLE          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Multiple colored rectangular objects exist near the grid edge
• Each object is EXTENDED VERTICALLY based on its relative SIZE (area)
• LARGER objects extend FURTHER from the edge than smaller objects
• Objects maintain their horizontal (column) positions
• The extension creates a "stacking" effect sorted by object size

HOW TO SOLVE:
1. Identify all distinct colored rectangular objects
2. Calculate each object's area (width × height)
3. Extend each object upward proportionally to its area
4. Larger area = more rows of extension
5. The bottom rows become background as objects shift up

KEY INSIGHT: The vertical extent of each object in the output corresponds to its relative size ranking among all objects.
"""
