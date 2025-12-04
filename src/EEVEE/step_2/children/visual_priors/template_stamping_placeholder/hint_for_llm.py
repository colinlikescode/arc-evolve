HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A TEMPLATE STAMPING PUZZLE            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the TEMPLATE: a rectangular region containing multiple distinct colors (the complex pattern)
• Identify PLACEHOLDER REGIONS: uniform rectangular blocks filled with a single repeated color
• The placeholder regions have the same dimensions as the template
• REPLACE each placeholder region with a copy of the template pattern
• Keep the original template unchanged

HOW TO FIND THE TEMPLATE:
• Look for a rectangular region where cells have 2+ different non-background colors
• This is your "stamp" pattern

HOW TO FIND PLACEHOLDERS:
• Look for rectangular regions filled entirely with ONE non-background color
• These regions should match the template's dimensions
• This uniform color acts as a "fill here" marker

YOUR APPROACH:
1. Find the bounding box of the multi-colored template
2. Extract the template pattern
3. Find all uniform rectangular regions matching the template size
4. Copy the template over each placeholder region
"""
