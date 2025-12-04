HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: RECTANGLE CONNECTION COUNT COLORING           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify all distinct rectangular blocks in the input
• For each rectangle, count how many OTHER rectangles are CONNECTED to it
• Assign an output color based on the connection count
• Different connection counts → different output colors

CONNECTION COUNTING:
• Two rectangles are "connected" if they share an edge or touch each other
• Count the total number of other rectangles each rectangle is connected to
• Rectangles with 0 connections get one color
• Rectangles with 1 connection get another color
• Rectangles with 2 connections get another color
• And so on...

YOUR APPROACH:
1. Find all rectangular regions in the input (connected components or bounded areas)
2. Build a connectivity map: for each rectangle, list which other rectangles touch it
3. Count connections for each rectangle
4. Study the training examples to determine which color maps to which count
5. Recolor each rectangle based on its connection count

KEY OBSERVATIONS:
• The shape and position of each rectangle is preserved exactly
• Only the fill color changes based on connection count
• Background cells remain unchanged
• Look at corner rectangles (likely 0-2 connections) vs interior rectangles (likely 3+ connections)
"""
