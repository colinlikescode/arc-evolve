HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER EXPANSION WITH CROSS PATTERN           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Each isolated marker cell in the input expands into a 3x3 pattern
• The 3x3 pattern is a "hollow cross" or "corner frame" shape

THE EXPANSION PATTERN (centered on the marker position):
```
M  S  M
S  B  S
M  S  M
```
Where:
- M = Original marker color (at the 4 corners)
- S = Secondary/new color (at the 4 cardinal positions: up, down, left, right)
- B = Background color (center remains background)

KEY OBSERVATIONS:
• The marker itself does NOT stay at center - center becomes background
• A NEW color is introduced for the cross arms
• The original marker color moves to the four diagonal corners
• Patterns may overlap at grid boundaries - handle edge cases appropriately
"""
