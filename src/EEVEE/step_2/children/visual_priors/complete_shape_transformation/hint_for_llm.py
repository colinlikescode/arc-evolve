HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: COMPLETE vs INCOMPLETE SHAPE DISCRIMINATION   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid contains multiple shapes of the same non-zero color
• Some shapes are "COMPLETE" templates (e.g., 3x3 hollow squares/frames)
• Some shapes are "INCOMPLETE" (partial patterns, fragments, different sizes)

WHAT HAPPENS:
• COMPLETE shapes → Transform to a NEW color in a COMPLEMENTARY pattern
  (e.g., hollow square becomes a plus/cross shape in a second color)
• INCOMPLETE shapes → Stay exactly as they are (unchanged)

HOW TO IDENTIFY COMPLETE SHAPES:
• Look for the largest recurring pattern that forms a recognizable template
• A "complete" shape typically has a specific size and structure (like a 3x3 frame)
• Shapes missing cells or having wrong dimensions are "incomplete"

THE COMPLEMENTARY TRANSFORMATION:
• The complete shape's pattern is essentially "inverted" within its bounding box
• Where the original had the border, the new color fills the interior cross/plus
"""
