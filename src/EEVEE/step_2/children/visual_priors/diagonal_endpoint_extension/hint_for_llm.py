HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL CONTINUATION WITH ENDPOINT MARKERS   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all diagonal line segments (connected non-zero cells along a diagonal)
• For each segment, identify its direction (e.g., going down-right or down-left)
• Extend the diagonal conceptually in BOTH directions (before and after the segment)
• Place a SECONDARY color marker at the cell positions just beyond each endpoint
• The markers continue the diagonal trajectory by one step in each direction
• Original cells remain unchanged; only add the new marker cells

CONCEPTUAL PATTERN:
```
Before:           After:
    ·                 M ← marker
    X                 X
      X         →       X
                          M ← marker
```

The markers show where the diagonal "would go next" if extended.

KEY INSIGHT:
• Find the bounding box or endpoints of each diagonal segment
• Calculate the next position along the same diagonal direction
• Place markers at those continuation points using a secondary color
"""
