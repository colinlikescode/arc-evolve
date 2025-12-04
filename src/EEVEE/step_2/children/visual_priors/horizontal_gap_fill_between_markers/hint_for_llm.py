HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FILL GAPS BETWEEN HORIZONTAL MARKERS          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find rows that contain multiple instances of the same non-zero marker color
• These markers appear in pairs or sequences along the same row
• Fill the background cells BETWEEN consecutive markers with a secondary fill color
• The original markers stay unchanged

CONCEPTUAL PATTERN:
Input row:   [marker] [gap] [marker] [gap] [marker]
Output row:  [marker] [fill] [marker] [fill] [marker]

WHAT TO DO:
1. Scan each row for non-zero marker cells
2. For each pair of consecutive markers on the same row:
   - Fill all background cells between them with the fill color
3. Keep the original markers in place
4. Leave all other cells unchanged

The fill color is a NEW color that doesn't appear in the input (typically the next color in sequence).
"""
