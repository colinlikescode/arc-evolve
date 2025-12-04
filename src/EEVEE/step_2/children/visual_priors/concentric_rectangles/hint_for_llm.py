HINT = """
⚠️ SPIRAL FROM CROSS PATTERN DETECTED ⚠️

This pattern creates a SPIRAL emanating from a cross/plus shaped marker.

KEY OBSERVATIONS:
1. The input contains a CROSS shape with an EMPTY CENTER
2. The cross has arms extending up, down, left, and right
3. The output creates a SPIRAL that winds outward from the cross center
4. The spiral alternates between filled and empty bands
5. The spiral continues until it reaches the grid edges

APPROACH:
1. Find the center of the cross (the empty cell surrounded by cross arms)
2. Start the spiral from this center point
3. Wind outward in a rectangular spiral pattern
4. Alternate between drawing the line and leaving gaps
5. Continue until the spiral fills the grid

The spiral grows outward from the cross center, creating a maze-like pattern of alternating paths.
"""
