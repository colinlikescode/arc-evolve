HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: VERTICAL PATTERN EXTENSION WITH RECOLORING    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a BASE UNIT that repeats vertically (find the smallest repeating block)
• The input shows N repetitions of this base unit
• The output shows N+1 repetitions of the same base unit
• All NON-ZERO cells are replaced with a DIFFERENT non-zero color

HOW TO SOLVE:
1. Identify the base repeating unit by finding the smallest vertical block that tiles to form the input
2. The base unit height = input_height ÷ number_of_repetitions
3. Create output by stacking ONE MORE copy of the base unit than was in the input
4. Replace all non-zero values with the new non-zero color (typically the "next" color)

EXAMPLE STRUCTURE:
Input (2 reps):     Output (3 reps):
[unit A]            [unit A'] 
[unit A]      →     [unit A']
                    [unit A']

Where A' is unit A with non-zero color changed.
"""
