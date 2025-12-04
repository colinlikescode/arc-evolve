HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: EXTRACT AND 2× SCALE PATTERN                  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the bounding box of all non-zero cells in the input
• Extract that rectangular region (crop to minimal bounds)
• Scale the extracted pattern by 2× in both dimensions
• Each cell becomes a 2×2 block of the same value

CONCEPTUALLY:
Input pattern:     Output (2× scaled):
  A B                A A B B
  C D       →        A A B B
                     C C D D
                     C C D D

YOUR APPROACH MUST:
1. Find the minimal bounding box containing all non-zero cells
2. Extract that region from the input
3. Create output with 2× height and 2× width
4. For each cell in extracted region, fill a 2×2 block in output with that cell's value
"""
