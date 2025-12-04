HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SHADOW/TRAIL EXTENSION PATTERN                ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Each small colored block (2xN region) in the input is preserved
• A "shadow" or "trail" extends from each block using a uniform fill color
• The shadow extends DOWNWARD from each block until it reaches either:
  - The bottom edge of the grid, OR
  - Another colored block's row position

KEY OBSERVATIONS:
• Find all distinct colored rectangular blocks in the input
• Each block's shadow has the same width as the block itself
• The shadow uses a single consistent color (not from the original blocks)
• Shadows fill the vertical gap between blocks and extend to grid boundaries
• The shadow occupies the same columns as its source block

APPROACH:
1. Identify all colored blocks and their bounding boxes
2. For each block, determine where its shadow should extend (downward continuation)
3. Fill from the bottom of each block downward with the uniform shadow color
4. Maintain the same column positions as the original block
"""
