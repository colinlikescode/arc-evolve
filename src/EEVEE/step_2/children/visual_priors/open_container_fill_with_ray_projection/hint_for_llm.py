HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: OPEN CONTAINER FILL WITH RAY PROJECTION       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a partial enclosure (frame/container with an opening)
• The enclosure is made of non-zero colored cells

TWO THINGS HAPPEN:
1. FILL INTERIOR: The region inside the enclosure is filled with a new color
2. PROJECT RAYS: From the opening/gap, rays extend outward into empty space

RAY DIRECTION:
• Rays project in the direction the opening faces
• They continue diagonally or linearly from the gap edges
• Rays extend until they reach the grid boundary

PRESERVE:
• Original shape cells keep their color
• Background cells outside the fill region and rays remain unchanged

IDENTIFY:
• Find the enclosure shape and locate its opening
• Determine which direction the opening faces
• Fill interior + draw extending rays in that direction
"""
