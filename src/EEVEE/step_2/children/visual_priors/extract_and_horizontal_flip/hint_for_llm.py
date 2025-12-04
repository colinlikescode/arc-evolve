HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: EXTRACT AND HORIZONTALLY FLIP PATTERN         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid contains a rectangular region of non-background cells
• This region is surrounded by background (zero) cells
• STEP 1: Find the bounding box of all non-zero cells
• STEP 2: Extract this rectangular subgrid
• STEP 3: Flip the extracted region HORIZONTALLY (mirror left-to-right)

CONCEPTUAL EXAMPLE:
Input has pattern:     Output is horizontally flipped:
A B C D                D C B A
E F G H       →        H G F E
I J K L                L K J I

YOUR APPROACH MUST:
1. Identify the bounding box containing all non-zero values
2. Crop/extract that rectangular region
3. Reverse each row (or equivalently, reverse column order)
4. Return the flipped extracted region as output
"""
