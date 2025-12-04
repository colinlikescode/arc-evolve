HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A BLOCK PATTERN MASKING PUZZLE        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input has TWO components:
  1. A large pattern of uniform-colored rectangular blocks arranged in an N×M grid layout
  2. A small "key" grid of varied colors (also N×M)

• Analyze the block pattern to determine which grid positions have blocks vs. empty space

• Create output by copying the key grid, BUT:
  - Where a block EXISTS in the pattern → output becomes 0 (background)
  - Where NO block exists in the pattern → preserve the key value

CONCEPTUAL STEPS:
1. Find the uniform-colored block pattern and determine block size
2. Map the blocks to an N×M boolean grid (filled vs. empty)
3. Find the small multi-colored key grid
4. Output = key values WHERE blocks are ABSENT, zero WHERE blocks are PRESENT
"""
