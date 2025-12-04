HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: COLOR-TRIGGERED CROSS/DIAGONAL DECORATIONS   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Two specific marker colors in the input trigger decorative patterns
• MARKER TYPE A → adds a CROSS pattern (cardinal neighbors: ±1 in row OR column)
  - Uses a specific output color for the cross arms
• MARKER TYPE B → adds a DIAGONAL pattern (diagonal neighbors: ±1 in BOTH row AND column)
  - Uses a different specific output color for the diagonal corners
• All other colored cells remain UNCHANGED (no decoration added)
• Original markers are PRESERVED in their positions

HOW TO IDENTIFY WHICH IS WHICH:
• Look at the training examples to see which input color gets crosses vs diagonals
• Note which output color is used for each pattern type
• Apply consistently to all instances of each marker type

PATTERN VISUALIZATION:
Cross (around marker A):     Diagonal (around marker B):
    . X .                        X . X
    X A X                        . B .
    . X .                        X . X
"""
