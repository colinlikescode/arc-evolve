HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CONNECTED COMPONENT SIZE-BASED COLORING       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input has multiple disconnected clusters of the same non-zero color
• Each connected component must be identified separately
• Clusters are RANKED by their size (cell count)
• Each cluster is recolored based on its size rank:
  - LARGEST cluster → first distinct color
  - SECOND LARGEST → second distinct color  
  - THIRD LARGEST → third distinct color
  - And so on...

YOUR APPROACH MUST:
1. Find all connected components (4-connectivity or 8-connectivity)
2. Count the number of cells in each component
3. Rank components from largest to smallest
4. Assign colors in order based on size ranking
5. Preserve the exact shape and position of each cluster

NOTE: If clusters have equal size, use spatial ordering (top-to-bottom, left-to-right by topmost-leftmost cell) as a tiebreaker.
"""
