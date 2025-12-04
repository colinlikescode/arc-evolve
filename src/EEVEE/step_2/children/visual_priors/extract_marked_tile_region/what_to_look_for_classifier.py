CLASSIFIER_PROMPT = """Does this puzzle involve EXTRACTING A MARKED REGION from a tiled/repeating pattern?

Look for these indicators:
- The input is a large grid with a repeating tile pattern separated by grid lines of a consistent color
- There is ONE rectangular region where the separator/border lines have been changed to a DIFFERENT color (a "marker" color)
- This marker color forms a rectangle that highlights/frames a specific tile or region
- The output is much smaller than the input
- The output appears to be the extracted marked region, with the marker color forming its border

The pattern involves:
1. A regular tiled structure with separator lines
2. One region marked by replacing separator lines with a distinct color
3. Extraction of that marked region as the output

Answer ONLY with: YES or NO"""
