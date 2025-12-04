HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SCALED EXPANSION WITH BLOCK PLACEMENT         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Output dimensions = 2 × input dimensions (both height and width)
• Each non-zero cell in the input becomes a filled square block in the output
• Block size is fixed (same for all cells) - determine by examining output/input ratio

POSITION MAPPING:
• A cell at input position (row, col) maps to a block in the output
• The block's top-left corner is at (row × scale_factor, col × scale_factor)
• Scale factor = output_size / input_size (typically 2)
• Block dimensions = scale_factor × scale_factor

YOUR APPROACH:
1. Determine the scale factor from input/output dimensions
2. Create output grid filled with background (zeros)
3. For each non-zero cell at (r, c) with value V:
   - Calculate block position: top-left at (r × scale, c × scale)
   - Fill a scale × scale block with value V at that position
4. Zero cells in input remain as zeros in output (no block placed)
"""
