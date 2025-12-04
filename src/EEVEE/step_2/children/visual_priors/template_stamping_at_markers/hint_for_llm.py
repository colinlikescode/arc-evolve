HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TEMPLATE STAMPING AT MARKER POSITIONS         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid has two regions separated by a divider (a line of a consistent color)
• Region 1: Contains a small rectangular TEMPLATE pattern
• Region 2: Contains scattered MARKER cells (single isolated colored cells)

FOR EACH MARKER CELL:
• The marker indicates WHERE to stamp the template
• The marker's position within its local "block" determines the alignment
• Stamp the template so that the marker position aligns with the corresponding cell in the template

KEY OBSERVATIONS:
• The template stays in place in the output
• The divider line remains unchanged
• Each marker gets replaced by the full template (centered on or aligned to the marker)
• Identify the template dimensions first
• The region to the right of the divider is divided into blocks matching template size
• Find which block each marker is in, and which cell within that block
• Stamp the template into that block

YOUR APPROACH:
1. Identify the divider line and extract the template pattern
2. Find all marker positions in the target region
3. Determine the block structure based on template dimensions
4. For each marker, stamp the template into the corresponding block
"""
