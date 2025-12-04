HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: NESTED CONCENTRIC FRAME COMPOSITION          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input contains multiple HOLLOW RECTANGULAR FRAMES of different colors/sizes
• Each frame is scattered somewhere on a uniform background
• One isolated cell may mark the CENTER point of the final composition

YOUR TASK:
1. IDENTIFY all distinct frame shapes (hollow rectangles) by their colors
2. DETERMINE the SIZE of each frame (bounding box dimensions)
3. FIND the center marker (often a single isolated cell of unique color)
4. SORT frames by size (largest to smallest)
5. NEST frames concentrically - largest on outside, smallest near center
6. Place the center marker at the exact center
7. Output should be SYMMETRIC (both horizontally and vertically)

KEY INSIGHT:
• The output size is determined by the LARGEST frame
• Each frame layer wraps around the inner layers
• The structure is like nested boxes or an onion with layers
• Background color fills gaps between frame elements
"""
