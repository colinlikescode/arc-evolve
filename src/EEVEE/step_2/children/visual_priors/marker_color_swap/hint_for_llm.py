HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A MARKER-BASED COLOR SWAP PUZZLE      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains exactly TWO colors: a "marker" color and a "content" color
• The marker color is a SPECIAL color that appears consistently across examples
• The content color is the OTHER color (varies per example)

OUTPUT CONSTRUCTION:
• Where the MARKER color appears in input → place the CONTENT color
• Where the CONTENT color appears in input → place background (zero)

IDENTIFYING THE COLORS:
• Find the two unique colors in the input
• The marker color is the one that acts as a "selector" (often gray/neutral)
• The content color is the one you want to preserve in a new arrangement

RESULT: The output shows the content color ONLY at positions where the marker was, with everything else becoming background.
"""
