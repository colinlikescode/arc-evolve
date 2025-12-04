HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SHAPE-MATCHING BLOCKS TO HOLLOW TEMPLATE      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• A template shape (color 1/blue) at the top contains HOLLOW REGIONS (background cells inside the border)
• Below the template, there are multiple colored block groups (color 5/grey)
• Each block group has a specific SHAPE (the pattern of its cells)
• MATCHING blocks: If the block's shape matches the hollow interior → convert to color 2 (red)
• NON-MATCHING blocks: If the block's shape doesn't match → keep original color (5/grey)

HOW TO SOLVE:
1. Identify the template shape (usually color 1) and find its HOLLOW INTERIOR (background cells inside)
2. Extract the SHAPE of the hollow interior (the pattern of 0s enclosed by 1s)
3. Find all separate block groups of color 5 below the template
4. For each block group, compare its shape to the hollow interior shape:
   - Consider ALL ROTATIONS (0°, 90°, 180°, 270°) when matching
   - If shapes match → change that block to color 2
   - If shapes don't match → keep as color 5

KEY INSIGHT: This is a SHAPE FITTING puzzle. Imagine trying to fit each grey block into the hollow region of the blue template. Only blocks that would fit (same shape, any rotation) get converted to red.

ALGORITHM:
```python
def solve(grid):
    # 1. Find the hollow interior shape of the template (1s region)
    # 2. Find all connected components of 5s
    # 3. For each component:
    #    - Normalize its shape (translate to origin)
    #    - Check if it matches hollow_shape in any rotation
    #    - If match → convert to 2, else keep as 5
```

WATCH OUT FOR:
• Multiple hollow regions in the template - check against ALL of them
• Rotations matter - a shape rotated 90° is still a match
• Connected components - cells must be 4-connected (up/down/left/right)
"""
