HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: HORIZONTAL BAND LINE EXTENSION PUZZLE         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid is divided into horizontal bands of uniform color
• Each band contains one or more "marker" cells (typically the zero/background color)
• For each marker cell found in a band:
  - Extend that marker vertically through the ENTIRE band
  - The line spans from the first row to the last row of that band
  - The column position stays the same as the original marker

KEY OBSERVATIONS:
• Bands are defined by contiguous rows of the same dominant color
• Markers are cells that differ from the band's dominant color
• Each band is processed independently
• The marker color (usually 0) becomes a vertical stripe within its band

YOUR APPROACH:
1. Identify the horizontal bands by finding row ranges with uniform color
2. For each band, find all marker cells (cells different from band color)
3. For each marker's column, fill that entire column within the band with the marker color
"""
