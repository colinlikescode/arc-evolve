HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: ROW-WISE COLUMN POSITION MAPPING              ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Each input row contains exactly ONE marker cell (non-background)
• The COLUMN POSITION of that marker determines the output row's color
• Each output row is filled entirely with a single uniform color

THE KEY INSIGHT:
• Column positions map to specific colors:
  - Leftmost column position → one specific color
  - Middle column position → another specific color  
  - Rightmost column position → a third specific color

YOUR APPROACH:
1. For each row, find which column contains the marker
2. Map that column index to the corresponding output color
3. Fill the entire output row with that color

NOTE: The marker's own color is irrelevant - only its POSITION matters!
"""
