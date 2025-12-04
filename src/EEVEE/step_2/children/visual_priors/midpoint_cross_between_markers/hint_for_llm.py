HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MIDPOINT CROSS BETWEEN PAIRED MARKERS         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the TWO non-zero marker cells in the input (they have the same color)
• These markers are aligned either horizontally (same row) or vertically (same column)
• Calculate the MIDPOINT between the two markers
• Draw a PLUS/CROSS shape centered at that midpoint using a NEW color
• The cross extends 1 cell in each cardinal direction from the center (5 cells total)
• Keep the original marker cells unchanged

CROSS SHAPE STRUCTURE:
```
    X
  X X X
    X
```
(centered at the midpoint between the two markers)

KEY OBSERVATIONS:
• The markers define the axis of alignment
• The midpoint is equidistant from both markers
• The fill color for the cross is different from the marker color
• Both original markers are preserved in the output
"""
