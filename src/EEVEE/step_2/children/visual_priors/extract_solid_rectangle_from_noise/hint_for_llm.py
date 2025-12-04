HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: EXTRACT SOLID RECTANGLE FROM NOISE           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains scattered random non-zero cells (noise)
• Hidden in the noise is ONE solid rectangular block of identical values
• This rectangle has ALL cells filled with the SAME non-zero color
• The rectangle is typically larger than 2x2 (stands out from noise)

YOUR TASK:
• Find the rectangular region where EVERY cell has the same non-zero value
• This is the ONLY contiguous solid-color rectangle in the grid
• Output: Clear everything to background (zeros)
• Preserve ONLY this solid rectangular block in its original position

HOW TO IDENTIFY:
• Look for rectangular regions (not just lines or scattered cells)
• All cells within must be identical and non-zero
• It will be the largest such uniform rectangular area
"""
