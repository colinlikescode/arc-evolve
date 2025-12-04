HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: GRID BLOCK MARKER PROPAGATION PUZZLE          ║
╚══════════════════════════════════════════════════════════════╝

THE STRUCTURE:
• The grid is divided into equal blocks by separator rows/columns (all zeros)
• Each block has a base pattern with occasional "marker" cells (special colors)

THE TRANSFORMATION RULE:
• For each ROW of blocks: find all marker positions and their colors
• For each COLUMN of blocks: find all marker positions and their colors  
• Propagate markers horizontally: if a marker exists at position (r,c) in any block of a row, copy it to the same relative position in ALL blocks of that row
• Propagate markers vertically: similarly for columns of blocks

CONCEPTUALLY:
• Think of it as "union" of markers across aligned blocks
• Each block in a row should have ALL markers that appear in ANY block of that row
• Each block in a column should have ALL markers that appear in ANY block of that column

YOUR APPROACH:
1. Identify the separator lines and block boundaries
2. For each block row and block column, collect all unique marker positions
3. Fill in missing markers in each block based on what exists in aligned blocks
"""
