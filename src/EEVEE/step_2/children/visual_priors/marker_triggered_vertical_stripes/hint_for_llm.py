HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER-TRIGGERED VERTICAL STRIPE FILL         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the single non-background cell (the "marker") in the input
• The marker stays in its original position
• Fill ALL rows ABOVE the marker's row with vertical stripes
• The stripe pattern: columns with the SAME PARITY as the marker's column get a fill color
• Columns with DIFFERENT parity remain background color
• Rows at or below the marker remain unchanged (background only)

CONCEPTUAL PATTERN:
```
Before:          After:
. . . . .        F . F . F    ← stripes above marker
. . . . .        F . F . F
. . M . .   →    F . F . F    ← row just above marker
. . . . .        . . M . .    ← marker row (unchanged)
. . . . .        . . . . .    ← below marker (unchanged)
```

KEY INSIGHT:
• The marker's column determines which columns get stripes (same column parity)
• The marker's row determines how many rows get filled (all rows above it)
• The fill color is a specific secondary color, distinct from the marker
"""
