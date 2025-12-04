CLASSIFIER_PROMPT = """Does this puzzle involve FRAME-BOUNDED REGION EXTRACTION WITH PATTERN FILLING?

Look for these indicators:
- There is a rectangular frame/border marked by a specific "corner" color (appearing at exactly 4 corners)
- The frame defines a target output region with two vertical "side" colors between the corners
- Somewhere else in the input, there is a small pattern/shape made of the SAME two colors as the frame sides
- The output extracts the framed region and fills it by expanding/replicating the small pattern to match the frame dimensions
- The corner markers appear in all 4 corners of the output
- Each side color's pattern is stretched/tiled to fill its respective half of the output

Key structural elements:
- A rectangular frame with 4 corner markers of one color
- Two different colors forming the vertical sides of the frame
- A separate small pattern elsewhere using those same two side colors
- Output size matches the frame dimensions

Answer ONLY with: YES or NO"""
