HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A DIRECTIONAL RAY EXTENSION PUZZLE    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the shape made of the dominant non-background color
• Identify the single "marker" cell (a different color within/on the shape)
• Determine the direction the shape is "pointing" (like an arrow or triangle)
• The marker cell is typically at the BASE of the arrow, opposite the tip
• Draw a ray/line from the marker cell in the direction the shape points
• Extend this ray to the edge of the grid using the marker color

KEY OBSERVATIONS:
• The shape acts like an ARROW indicating direction
• The marker color is used for the extended ray
• The original shape remains unchanged
• The ray extends through empty space until hitting the grid boundary

DIRECTION DETECTION:
• Find where the shape tapers to a point (the "tip")
• The ray extends in the OPPOSITE direction from the tip (away from where the arrow points)
• OR equivalently: from the marker toward the open space on the opposite side
"""
