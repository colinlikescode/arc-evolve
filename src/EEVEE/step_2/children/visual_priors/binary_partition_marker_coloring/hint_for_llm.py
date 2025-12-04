HINT = """
╔══════════════════════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: BINARY PARTITION WITH OVERLAY MARKER COLORING                ║
╚══════════════════════════════════════════════════════════════════════════════╝

THE PATTERN:

1. The input has TWO LAYERS:
   - BASE LAYER: The TWO MOST COMMON colors form a binary partition (e.g., 0s and 1s)
   - OVERLAY MARKERS: Rare colored cells placed on top of the base pattern

2. The output FILLS the entire grid based on marker positions:
   - If a marker is ON a cell of dominant-color-A → fill the A-regions with that marker color
   - If a marker is ON a cell of dominant-color-B → fill the B-regions with that marker color

HOW TO SOLVE:

1. IDENTIFY THE BASE PATTERN:
   - Count cell frequencies - the TWO MOST COMMON colors form the partition
   - These two colors form connected regions that divide the grid

2. IDENTIFY OVERLAY MARKERS:
   - Find all cells with MINORITY colors (not the two dominant colors)
   - Note which DOMINANT COLOR is underneath each marker

3. DETERMINE WHICH LAYER EACH MARKER COLORS:
   - Check the base value at each marker's position
   - Marker on dominant-A → colors all connected A-regions
   - Marker on dominant-B → colors all connected B-regions

4. FLOOD FILL EACH REGION:
   - For each connected component of dominant-A: fill with the marker that was on an A-cell
   - For each connected component of dominant-B: fill with the marker that was on a B-cell
   - If multiple markers for same base value, each fills its own connected sub-region

5. OUTPUT: The entire grid is filled - only marker colors remain

KEY INSIGHT: The position of the overlay marker (on which dominant color) determines which "layer" of the partition gets that color!
"""

