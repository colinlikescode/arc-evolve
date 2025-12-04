HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A REPEATING TILE EXTRACTION PUZZLE    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input is a grid made of IDENTICAL TILES repeated in a regular pattern
• The output is the SINGLE UNIT TILE that was repeated to create the input
• The repetition can be horizontal, vertical, or both

HOW TO FIND THE TILE:
• Look for the smallest rectangular region that, when tiled, reproduces the input
• Check if input_height is divisible by some factor → that's the tile height
• Check if input_width is divisible by some factor → that's the tile width
• The tile is typically in the top-left corner of the input

VERIFICATION:
• The extracted tile, when repeated N times, should exactly match the input
• All repeated copies in the input should be identical to each other

YOUR APPROACH:
1. Find divisors of input height and width
2. Test candidate tile sizes starting from smallest
3. Verify the tile repeats perfectly across the entire input
4. Output the single unit tile (usually top-left portion)
"""
