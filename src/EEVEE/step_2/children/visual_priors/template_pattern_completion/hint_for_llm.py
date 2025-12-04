HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: PATTERN COMPLETION BY TEMPLATE REFERENCE      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the "template" - a pattern that spans the full width of the grid
• Find "incomplete" patterns - similar structures that are truncated/shorter
• The incomplete patterns share the same shape/structure as the template
• Complete each incomplete pattern to match the template's full extent
• Use a SECONDARY COLOR for the filled-in portions (not the original color)

KEY OBSERVATIONS:
• The template defines the "target" extent for all similar patterns
• Incomplete patterns preserve their original cells in the original color
• Only the MISSING portions are filled with the secondary color
• The fill follows the same structural pattern (e.g., if template is checkered, fill is checkered)

APPROACH:
1. Find the pattern that extends furthest (the template)
2. Identify similar but shorter patterns
3. For each incomplete pattern, extend it to match template length
4. Mark extensions with the secondary/fill color
"""
