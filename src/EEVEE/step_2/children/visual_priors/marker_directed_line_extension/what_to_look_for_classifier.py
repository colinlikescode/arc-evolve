CLASSIFIER_PROMPT = """Does this puzzle exhibit MARKER-DIRECTED LINE EXTENSION?

Marker-directed line extension means:
- There are rectangular regions filled with a dominant color
- Within these regions, there are single "marker" cells of a different accent color
- The marker cells indicate a direction (based on their position within the rectangle)
- Lines of the accent color extend FROM the marker cell in the direction it points (toward the edge of the rectangle that is closest)
- The line extends outward beyond the rectangle, continuing until it reaches the grid boundary or another obstacle

Look at the training examples:
- Are there solid rectangular blocks of one color with a single different-colored cell inside?
- Does the accent cell sit near one edge of its containing rectangle?
- In the output, does a line of the accent color extend from that marker toward and beyond the nearest edge?
- Do multiple rectangles each have their own marker that extends in its own direction?

Answer ONLY with: YES or NO"""
