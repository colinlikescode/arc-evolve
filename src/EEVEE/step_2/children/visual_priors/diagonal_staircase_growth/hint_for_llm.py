HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A DIAGONAL STAIRCASE GROWTH PUZZLE    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input: A single row with K non-zero cells on the left, followed by zeros
• Output: Multiple rows where the colored region grows by 1 cell per row

PATTERN STRUCTURE:
• Row 0: Same as input (K colored cells)
• Row 1: K+1 colored cells
• Row 2: K+2 colored cells
• ...continues until colored cells would exceed the grid width

NUMBER OF OUTPUT ROWS:
• Count how many zeros are in the input
• The output has (number_of_zeros + 1) rows, OR stops when the row is fully colored

VISUAL PATTERN:
```
Input:  [C C C 0 0 0 0]

Output: [C C C 0 0 0 0]  ← original
        [C C C C 0 0 0]  ← +1 colored
        [C C C C C 0 0]  ← +2 colored
        [C C C C C C 0]  ← +3 colored
        [C C C C C C C]  ← +4 colored (fills row)
```

The diagonal boundary forms from the initial colored count growing rightward row by row.
"""
