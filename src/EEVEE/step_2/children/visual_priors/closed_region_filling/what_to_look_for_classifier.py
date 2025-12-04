CLASSIFIER_PROMPT = """Does this puzzle exhibit CLOSED REGION FILLING?

Closed region filling means:
- The input contains shapes drawn with a non-background "boundary" color
- Some of these shapes form CLOSED regions (completely enclosed areas)
- The output fills the interior of closed regions with a different "fill" color
- Open shapes or incomplete boundaries remain unfilled
- The boundary color itself is preserved, only the interior background cells get filled

Look at the training examples:
- Are there shapes made of connected non-zero cells that form closed loops or rectangles?
- Do some regions have complete boundaries while others are open/incomplete?
- In the output, are the interiors of ONLY the closed shapes filled with a new color?
- Do open or incomplete shapes remain unchanged (unfilled)?

Answer ONLY with: YES or NO"""
