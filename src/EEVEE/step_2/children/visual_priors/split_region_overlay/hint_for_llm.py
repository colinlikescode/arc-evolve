HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A SPLIT REGION OVERLAY PUZZLE         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid is split into TWO separate regions by an empty (zero) strip in the middle
• Identify the LEFT region and the RIGHT region (or TOP and BOTTOM)
• The output combines/overlays these two regions using logical OR
• Output dimensions match the size of ONE region (not the full input)

HOW TO MERGE:
• For each position in the output:
  - If EITHER corresponding position in the left OR right region has a non-zero value, output that value
  - If BOTH regions have zeros at that position, output zero
  - The two regions complement each other to form a complete pattern

KEY INSIGHT:
• The empty middle strip is a SEPARATOR, not part of the pattern
• The two halves contain PARTIAL information that must be combined
• Think of it as overlaying two transparent sheets with partial drawings
"""
