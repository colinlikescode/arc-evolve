HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: OBJECT ATTRACTION / MOVE-TO-ADJACENT PUZZLE   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• There are TWO distinct non-background objects
• One object is the ANCHOR (typically smaller, often a 2x2 square) - it stays fixed
• One object is MOVABLE (typically larger/irregular) - it translates toward the anchor
• The movable object slides until it becomes ADJACENT to the anchor (touching it)
• Both objects retain their original shapes

HOW TO IDENTIFY WHICH IS WHICH:
• The anchor is usually the smaller, more compact object
• Look for a simple rectangular block vs. an irregular shape

YOUR APPROACH:
1. Identify the two distinct colored objects
2. Determine which is the anchor (smaller/compact) and which moves
3. Calculate the translation needed to make them adjacent
4. Move the movable object toward the anchor, stopping when edges touch
5. Keep the anchor in its original position
"""
