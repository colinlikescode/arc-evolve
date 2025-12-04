HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A VERTICAL FLIP AND STACK PUZZLE      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Output height = 2 × input height
• Output width = input width (unchanged)
• The output is formed by stacking two versions of the input:
  - FIRST: The input with rows reversed (vertical flip)
  - THEN: The original input below it

THE RESULT:
• Creates a vertically symmetric pattern
• The middle of the output is where the two versions meet
• Row 0 of output = last row of input
• Last row of output = last row of input

YOUR APPROACH:
1. Reverse the order of rows in the input (flip vertically)
2. Append the original input rows below the flipped version
3. The combined result is the output
"""
