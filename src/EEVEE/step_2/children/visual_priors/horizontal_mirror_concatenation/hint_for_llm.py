HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: HORIZONTAL MIRROR CONCATENATION PUZZLE        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Output dimensions: same height, 2× width
• Each output row = original row + horizontally mirrored row

CONSTRUCTION:
• Left half of output: the original input (unchanged)
• Right half of output: the input flipped horizontally (each row reversed)

VISUALLY:
Input:          Output:
A B C    →      A B C | C B A
D E F           D E F | F E D
G H I           G H I | I H G

The result creates bilateral (left-right) symmetry in the output, with the axis of symmetry at the center between the two halves.
"""
