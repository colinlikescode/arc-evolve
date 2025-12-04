HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A NOISE REMOVAL PUZZLE                ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid contains filled rectangular regions of a PRIMARY FILL COLOR
• A SECONDARY "NOISE" COLOR appears scattered both:
  - Inside the filled regions (contaminating them)
  - Outside in the background area
• The noise color is typically less frequent than the fill color

TO SOLVE:
1. Identify the background color (most common, usually zero)
2. Identify the primary fill color (forms coherent rectangular shapes)
3. Identify the noise color (scattered sporadically, disrupts patterns)
4. REMOVE ALL NOISE:
   - Replace noise cells INSIDE filled regions with the fill color
   - Replace noise cells OUTSIDE filled regions with background color

The output preserves the shape boundaries exactly but makes all filled regions uniform (no internal noise) and cleans the background completely.
"""
