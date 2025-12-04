HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CROSS-PATTERN EXPANSION PUZZLE                ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Each input contains cross/plus patterns with a CENTER color and ARM color
• The cross has: center cell + 4 cells in cardinal directions (up/down/left/right)

EXPANSION LOGIC:
• Keep the original cross pattern intact
• EXTEND the arms: add more ARM color cells continuing in cardinal directions
• ADD CENTER color at DIAGONAL positions around the pattern
• The result is a larger diamond shape centered on the original cross

CONCEPTUAL STRUCTURE:
Original:        Expanded:
    A               C . A . C
  A C A      →      . C A C .
    A               A A C A A
                    . C A C .
                    C . A . C

Where C = center color, A = arm color

The center color propagates to corners/diagonals, while arm color extends the cross arms.
"""
