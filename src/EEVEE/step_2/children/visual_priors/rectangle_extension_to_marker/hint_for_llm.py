HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CONNECT FRAMES WITH BRIDGES                   ║
╚══════════════════════════════════════════════════════════════╝

THE PATTERN:
- Input has multiple HOLLOW RECTANGULAR FRAMES of the same color
- Output CONNECTS these frames with BRIDGES (lines of the same color)
- Frames that are ALIGNED get connected

ALGORITHM:
1. Find all rectangular frames in the input
2. For each pair of frames, check if they can be connected:
   - If their edges OVERLAP vertically: draw horizontal bridge
   - If their edges OVERLAP horizontally: draw vertical bridge
3. A bridge connects where the frames' projections overlap
4. Draw a line from one frame's edge to the other frame's edge

KEY CONCEPTS:
- Two frames are "connectable" if their ranges overlap on one axis
- The bridge is drawn along the perpendicular axis
- Bridges are straight lines (single row or single column)
- Bridges fill the GAP between the closest edges of aligned frames

EXAMPLE:
- Frame A spans rows 2-5, columns 3-6
- Frame B spans rows 3-7, columns 10-14
- Rows 3-5 overlap, so draw horizontal bridge from col 6 to col 10 along those rows

The result connects all aligned frames into a single connected structure.
"""
