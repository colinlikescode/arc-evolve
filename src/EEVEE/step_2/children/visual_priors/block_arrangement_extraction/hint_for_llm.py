HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: EXTRACT BLOCK ARRANGEMENT PATTERN             ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a large shape made of rectangular BLOCKS arranged in a grid pattern
• This shape is composed of uniformly-sized blocks, some positions filled, some empty
• There's also a "marker" color scattered as noise pixels throughout the grid

YOUR TASK:
1. Identify the dominant shape color (forms the large connected blocks)
2. Identify the marker/noise color (scattered individual pixels)
3. Determine the block grid dimensions (e.g., 3x3 arrangement of blocks)
4. For each position in the block grid:
   - If that block position is EMPTY (no main shape): mark with the marker color
   - If that block position is FILLED: mark with background (zero)

OUTPUT: A small grid showing the "negative" of the block arrangement
- The marker color appears where blocks are MISSING from the shape
- Background (0) appears where blocks ARE present
"""
