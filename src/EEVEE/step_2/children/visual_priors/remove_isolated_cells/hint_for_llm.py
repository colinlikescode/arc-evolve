HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: REMOVE ISOLATED CELLS, KEEP CONNECTED GROUPS  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Grid dimensions remain unchanged
• For each non-zero cell, check if it has ANY adjacent non-zero neighbor
• Adjacency includes all 8 directions (orthogonal + diagonal)
• If a non-zero cell has NO non-zero neighbors → remove it (set to 0)
• If a non-zero cell has AT LEAST ONE non-zero neighbor → keep it

CONCEPTUALLY:
• Isolated/singleton cells are noise → remove them
• Connected clusters (2+ adjacent non-zero cells) are signal → preserve them

YOUR APPROACH:
1. For each non-zero cell in the input
2. Check all 8 neighboring positions
3. If at least one neighbor is also non-zero → keep the cell
4. If all neighbors are zero/background → set cell to zero in output
"""
