CLASSIFIER_PROMPT = """Does this puzzle involve QUADRANT-BASED COLOR MAPPING with corner markers?

Look for these indicators:
- The input grid is divided into quadrants by lines of a uniform separator color (forming a cross/grid pattern)
- The four corners of the input contain distinct marker colors (different from background and separator)
- The interior region (bounded by separator lines) contains a pattern made with a single indicator color
- The output is smaller than the input, matching the size of the interior pattern region
- The output shows the same pattern as the interior, but the indicator color is replaced by the corner marker colors based on quadrant position

Key structural elements:
- Separator lines dividing the grid into sections
- Four distinct corner markers acting as "color keys"
- An interior pattern that gets recolored by quadrant

Answer ONLY with: YES or NO"""
