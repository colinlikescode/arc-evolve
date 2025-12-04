HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: HORIZONTAL CONCATENATION WITH REFLECTION      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The output is the input concatenated horizontally with its mirror image
• Output dimensions: same height, 2× width

STRUCTURE:
```
Input:        Output:
A B C    →    A B C | C B A
D E F         D E F | F E D
G H I         G H I | I H G
```

The right half is the left half flipped horizontally (columns reversed).

KEY INSIGHT:
• For each row: output_row = input_row + reversed(input_row)
• The pattern creates bilateral symmetry around the vertical center
"""
