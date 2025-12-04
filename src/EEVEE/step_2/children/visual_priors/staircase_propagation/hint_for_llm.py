HINT = """
╔══════════════════════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: STAIRCASE PROPAGATION FROM SOURCE BLOCK                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

THE PATTERN:

1. Find the solid rectangular BLOCK - this is the SOURCE
2. One color shoots DIAGONALLY from the 4 CORNERS of the source block
   - Extends outward until hitting a barrier or grid boundary
3. Another color propagates from the CENTER of each EDGE in a STAIRCASE pattern:
   - Alternates between going OUT and going SIDEWAYS
   - Creates a stepped/zigzag appearance
   - STOPS when hitting a barrier

KEY OBSERVATIONS:
• The source block has 4 corners and 4 edges
• Corner diagonals go in 4 diagonal directions (↗ ↖ ↘ ↙)
• Edge staircases spiral outward in a clockwise pattern
• Barriers block all propagation
• Study the training examples to determine the exact step counts

WHAT TO LOOK FOR IN TRAINING EXAMPLES:
• How many steps out before turning?
• How many steps sideways before turning back out?
• Which direction does each edge's staircase spiral?
• What colors are used for corners vs edges?

The transformation adds new colored cells radiating FROM the source block
in specific geometric patterns (diagonals + staircases).
"""

