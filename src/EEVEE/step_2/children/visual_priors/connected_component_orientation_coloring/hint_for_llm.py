HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CONNECTED COMPONENT COLORING BY ORIENTATION   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all marker cells (the non-background scattered cells)
• Group them into connected components (cells sharing an edge)
• Color each component based on its SHAPE/ORIENTATION:

  → ISOLATED single cells → one distinct color
  → HORIZONTAL pairs (side by side) → second distinct color  
  → VERTICAL pairs (stacked) → third distinct color

• The background color remains unchanged throughout

HOW TO IDENTIFY WHICH COLOR MAPS TO WHICH SHAPE:
• Look at the output and find obvious horizontal pairs → note their color
• Find obvious vertical pairs → note their color
• Find isolated singles → note their color
• Apply consistently to all marker cells

YOUR APPROACH:
1. Identify all marker cell positions in input
2. Find connected components using flood-fill or union-find
3. Classify each component by shape (single, horizontal pair, vertical pair)
4. Assign the appropriate output color to each component
"""
