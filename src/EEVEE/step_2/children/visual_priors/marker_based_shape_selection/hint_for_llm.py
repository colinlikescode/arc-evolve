HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER-BASED SHAPE SELECTION PUZZLE           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains MULTIPLE separate shapes of the same color
• There is ONE special marker cell of a DIFFERENT unique color
• The marker cell indicates WHICH shape to select
• The output is the shape closest to/associated with the marker

HOW TO SOLVE:
1. Identify all distinct connected regions of the primary non-background color
2. Find the single marker cell (the unique different-colored cell)
3. Determine which shape the marker is closest to or touching
4. Extract that shape's bounding box as the output
5. The marker cell itself is NOT included in the output

IMPORTANT:
• The marker acts as a "pointer" or "selector"
• Only the selected shape appears in output, cropped to its bounding box
• Other shapes are ignored entirely
"""
