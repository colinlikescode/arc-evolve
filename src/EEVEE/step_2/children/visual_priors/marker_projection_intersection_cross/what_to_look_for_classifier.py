CLASSIFIER_PROMPT = """Does this puzzle exhibit MARKER-TO-OBSTACLE PROJECTION with PATH TRACING and INTERSECTION MARKERS?

This pattern involves:
- Scattered obstacle blocks of one color (e.g., orange rectangles)
- Isolated "marker" cells of a different color (e.g., magenta single cells)
- From each marker, a line/path extends toward obstacles
- The path may TURN when hitting obstacles (e.g., go UP, hit obstacle, turn RIGHT)
- At intersection/turn points, special colored markers appear (e.g., different colors for each intersection)
- The result may form a ZIGZAG staircase pattern bouncing off obstacles

Look at the training examples:
- Are there scattered blocks/obstacles of one color?
- Are there isolated marker cells of a different color?
- In the output, do paths extend from markers and TURN when hitting obstacles?
- Do colored markers appear at intersection/turning points?
- Does the path alternate direction (UP→RIGHT→UP or similar zigzag)?

Answer ONLY with: YES or NO"""
