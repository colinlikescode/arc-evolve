HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: COLUMN MARKER REGION ASSIGNMENT PUZZLE        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The first row contains COLOR MARKERS at specific column positions
• Below are rectangular regions filled with a PLACEHOLDER color
• Each placeholder region is RECOLORED based on which marker's column it falls under

HOW TO DETERMINE REGION COLOR:
• For each placeholder region, look at which columns it spans
• Find the color marker in the header row that overlaps with those columns
• Replace all placeholder cells in that region with the marker's color

KEY OBSERVATIONS:
• The header row markers remain unchanged
• Only the placeholder-colored regions are transformed
• A region inherits the color of the marker whose column intersects it
• Background (zero) cells remain unchanged
"""
