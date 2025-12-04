HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIRECTIONAL DIAGONAL TRAIL EXTENSION          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the 2x2 block containing non-zero cells
• Identify TWO colors: the "marker" color and the "primary" color
• The marker color indicates DIRECTION - its position relative to the primary color shows which diagonal to extend
• Replace the marker with the primary color in the 2x2 block
• Extend a diagonal trail of the primary color from the block position
• The trail continues until hitting grid boundaries, maintaining the 2x2 shape as it moves diagonally

DIRECTION LOGIC:
• Marker in top-right of primary → trail goes UP and RIGHT
• Marker in bottom-right of primary → trail goes DOWN and RIGHT  
• Marker in top-left of primary → trail goes UP and LEFT
• Marker in bottom-left of primary → trail goes DOWN and LEFT

The trail consists of overlapping 2x2 blocks of the primary color, offset diagonally by 1 cell each step.
"""
