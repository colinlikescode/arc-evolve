HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS AN "ODD ONE OUT" PATTERN PUZZLE       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains multiple same-sized blocks (arranged in a row or column)
• Each block uses a unique color but shares a structural pattern with most others
• ONE block has a DIFFERENT structural pattern (positions of non-zero cells)
• The output is the block with the UNIQUE structure

HOW TO SOLVE:
1. Divide the input into equal-sized blocks (look at dimensions to find the block size)
2. For each block, extract its BINARY pattern (non-zero vs zero positions)
3. Compare all binary patterns to find which one is different from the majority
4. Return the block with the unique pattern (preserving its original color)

KEY INSIGHT: Ignore the actual color values - compare only the STRUCTURE (which cells are filled vs empty). The unique block is the one whose structure doesn't match the others.
"""
