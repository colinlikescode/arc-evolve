HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A DUAL-PATTERN XOR COMPARISON PUZZLE  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input is split into TWO equal halves (top and bottom)
• Each half contains a different non-zero color forming a pattern
• Convert each half to a binary mask (non-zero = 1, zero = 0)
• The output marks cells where EXACTLY ONE half has a non-zero value (XOR)

CONCEPTUALLY:
• Top pattern: cells with first non-zero color → mask A
• Bottom pattern: cells with second non-zero color → mask B
• Output: mark with a NEW color where (A XOR B) is true
  - Where mask A has 1 and mask B has 0 → mark
  - Where mask A has 0 and mask B has 1 → mark
  - Where both are same (both 0 or both 1) → background

YOUR APPROACH:
1. Split input into top half and bottom half
2. Create binary masks for each (non-zero vs zero)
3. Find XOR difference between the masks
4. Output uses a new color to mark difference positions
"""
