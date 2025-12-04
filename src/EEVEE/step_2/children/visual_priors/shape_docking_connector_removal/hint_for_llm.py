HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A SHAPE DOCKING / CONNECTOR REMOVAL   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• There are two rectangular regions of different colors
• One region has a thin "connector" line extending toward the other region
• The connector indicates WHERE and HOW the shapes should dock together

YOUR APPROACH MUST:
1. Identify the two main rectangular regions (different colors)
2. Find the thin connector line (1 cell wide strip of one color)
3. Remove the connector line entirely
4. Move the smaller/secondary shape to be directly adjacent to the primary shape
5. Position it where the connector was pointing (the docking location)

KEY INSIGHT:
• The connector line shows the PATH - remove it and collapse the gap
• The secondary shape slides along the connector direction until it touches the primary shape
• Both shapes retain their original dimensions in the output
"""
