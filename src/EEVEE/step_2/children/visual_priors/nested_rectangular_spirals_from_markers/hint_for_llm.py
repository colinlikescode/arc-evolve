HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: NESTED RECTANGULAR SPIRALS FROM MARKERS       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input contains scattered single-cell markers of one color on empty background
• Markers define corners/turning points for nested rectangular frames
• Each marker's position determines where one rectangle "turns" or has its corner

KEY OBSERVATIONS:
• Find all non-zero marker positions - they form a diagonal/staircase pattern
• The innermost marker is the center of the nested structure
• Each successive marker (moving outward) defines the next rectangular frame
• Rectangles are drawn as single-pixel-width outlines
• The spacing between markers determines the gap between successive rectangles

CONSTRUCTION APPROACH:
• Sort markers by their distance from a reference corner (e.g., bottom-right or top-left)
• The innermost marker may just be a single point
• Each outer marker defines a rectangular frame that passes through that point
• Frames extend from grid edges or previous frame boundaries to the marker position
• The pattern creates a spiral-like nested rectangle structure
"""
