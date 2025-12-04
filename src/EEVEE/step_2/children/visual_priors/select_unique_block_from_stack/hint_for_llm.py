HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SELECT THE UNIQUE BLOCK FROM STACKED SECTIONS ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid is divided into N equal horizontal blocks (stacked vertically)
• Each block contains a two-color pattern
• You must SELECT exactly ONE block to output

SELECTION CRITERIA:
• Examine each block's internal pattern structure
• Look for the block where the minority color appears in a UNIQUE, ASYMMETRIC position
• The selected block typically has one color appearing exactly 2-3 times in a non-symmetric arrangement
• Blocks with more symmetric or regular patterns (like diagonal symmetry) are NOT selected

HOW TO IDENTIFY THE CORRECT BLOCK:
• Count color frequencies within each block
• Check for asymmetry in how the minority color is placed
• The "most unique" or "most irregular" pattern wins
• The selected block often has a distinctive L-shape, corner, or scattered minority color pattern
"""
