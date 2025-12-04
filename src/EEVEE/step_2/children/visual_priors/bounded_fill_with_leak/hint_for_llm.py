HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: BOUNDED REGION FILL WITH LEAK/ESCAPE         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the rectangular frame/border made of a non-zero color
• Identify any GAPS in the frame (missing border cells)
• Fill the INTERIOR of the frame with a new fill color
• The fill also "LEAKS" through each gap:
  - Extend a line of the fill color from the gap
  - Continue in the outward direction until reaching the grid edge

CONCEPTUAL UNDERSTANDING:
• Think of it like filling a container with water that has a hole
• The interior fills up, and water escapes through the hole
• The escaping stream continues in a straight line outward

YOUR CODE MUST:
1. Locate the rectangular border structure
2. Find where the border has gaps (missing cells)
3. Fill all interior cells with the new color
4. For each gap, draw a line of fill color extending outward to the grid boundary
"""
