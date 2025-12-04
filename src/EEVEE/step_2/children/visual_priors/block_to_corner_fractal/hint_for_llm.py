HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: BLOCK-TO-CORNER FRACTAL REDUCTION             ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input has solid rectangular blocks arranged in a grid pattern
• Identify the block size (e.g., 3×3) and the meta-grid arrangement (e.g., 3×3 positions)
• Create output where each block position maps to a block-sized region

FOR EACH BLOCK POSITION:
• If the input block is FILLED (non-zero): 
  → Output a "corner pattern" - place the non-zero color at corners/edges, zeros at center
  → The corner pattern has non-zero at positions where row AND column indices are both even or both at edges
• If the input block is EMPTY (all zeros):
  → Output all zeros for that block

THE CORNER PATTERN (for a 3×3 block):
```
X . X
. X .
X . X
```
Where X = non-zero color, . = zero

YOUR APPROACH:
1. Find all solid blocks and determine block size
2. Determine the meta-grid arrangement of blocks
3. For each block position, check if filled or empty
4. Generate output: filled blocks → corner pattern, empty → zeros
"""
