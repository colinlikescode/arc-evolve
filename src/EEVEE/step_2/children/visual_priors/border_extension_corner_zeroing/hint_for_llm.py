HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: BORDER EXTENSION WITH CORNER ZEROING          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Output dimensions = (input_height + 2) × (input_width + 2)
• The input is placed in the center region (rows 1 to H, cols 1 to W)
• For each row in the output (except top and bottom):
  - Left edge cell = duplicate of leftmost input cell in that row
  - Right edge cell = duplicate of rightmost input cell in that row
• Top row = first input row values, with edge extension
• Bottom row = last input row values, with edge extension
• ALL FOUR CORNERS are set to zero (background color)

STRUCTURE:
```
[0]  [top-left]  ...  [top-right]  [0]
[L1] [-------- input row 1 -------] [R1]
[L2] [-------- input row 2 -------] [R2]
...
[0]  [bot-left]  ...  [bot-right]  [0]
```

Where L/R are duplicates of the leftmost/rightmost cells of each row.
"""
