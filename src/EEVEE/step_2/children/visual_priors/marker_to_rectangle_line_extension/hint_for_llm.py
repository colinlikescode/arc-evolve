HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER-TO-RECTANGLE LINE DRAWING PUZZLE       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the solid rectangular region (non-background, non-marker color)
• Identify scattered single-cell markers (a different non-background color)
• For each marker that is ALIGNED with the rectangle (shares a row or column):
  - Draw a line of the marker's color FROM the rectangle edge TO the marker
  - The line extends horizontally if the marker is left/right of the rectangle
  - The line extends vertically if the marker is above/below the rectangle
• Markers NOT aligned with the rectangle are left unchanged (no line drawn)
• The line fills the gap between the rectangle boundary and the marker position

KEY INSIGHT:
- Only markers whose row intersects the rectangle's row range OR whose column intersects the rectangle's column range get connected
- The line uses the marker's color, not the rectangle's color
"""
