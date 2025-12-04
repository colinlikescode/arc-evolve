HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: BORDER-MATCHING CELL MIGRATION PUZZLE         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid has a rectangular FRAME with 4 different border colors (one per side)
• Corners are background (zero)
• Interior cells matching a border color MIGRATE to that border

HOW CELLS MIGRATE:
• If an interior cell matches the LEFT border color → move it to column 1 (same row)
• If an interior cell matches the RIGHT border color → move it to second-to-last column (same row)
• If an interior cell matches the TOP border color → move it to row 1 (same column)
• If an interior cell matches the BOTTOM border color → move it to second-to-last row (same column)

KEY POINTS:
• The frame borders themselves remain unchanged
• All other interior cells become background (zero)
• Migrated cells appear ADJACENT to their matching border (one cell inward)
• Multiple cells can migrate to the same border on different rows/columns
"""
