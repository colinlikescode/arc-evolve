HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A 2x2 CELL SCALING PUZZLE             ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Output dimensions = (input_height × 2, input_width × 2)
• Each cell in the input becomes a 2×2 block in the output
• The color of each 2×2 block matches the original input cell exactly

CONCEPTUAL MAPPING:
Input cell at (row, col) → Output block at (row×2 : row×2+2, col×2 : col×2+2)

```
Input:           Output:
[A][B]    →     [A][A][B][B]
[C][D]          [A][A][B][B]
                [C][C][D][D]
                [C][C][D][D]
```

KEY INSIGHT:
• This is simple nearest-neighbor upscaling by factor of 2
• ALL cells are treated identically regardless of their color value
• No special handling for zero/background vs non-zero cells
"""
