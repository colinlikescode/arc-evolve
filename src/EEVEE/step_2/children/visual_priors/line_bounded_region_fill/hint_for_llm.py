HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: LINE-BOUNDED REGION FILLING PUZZLE            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input has a network of horizontal/vertical lines (one non-zero color)
• These lines create a grid structure with various rectangular cells

OUTPUT CONSTRUCTION:
1. Replace ALL background (zero) cells with a "default exterior" color
2. Keep the line color unchanged
3. Find rectangular regions that are FULLY ENCLOSED by lines on all 4 sides
4. Fill those enclosed interior regions with a distinct "interior" color

KEY INSIGHT:
• A region is "enclosed" if it has continuous line boundaries on top, bottom, left, and right
• Regions that touch the edge of the grid or have gaps in their boundaries stay the default color
• Only truly bounded rectangular areas get the special interior fill

YOUR CODE MUST:
• Identify the line color (the non-zero color forming the grid)
• Find all rectangular cells bounded by complete line segments
• Fill enclosed cells with the interior color, others with the exterior color
"""
