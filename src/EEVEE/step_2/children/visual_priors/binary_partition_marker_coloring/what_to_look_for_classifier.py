CLASSIFIER_PROMPT = """Does this puzzle involve a BINARY BASE PATTERN (two dominant colors) with COLORED OVERLAY MARKERS that determine region fills?

CRITICAL indicators:

1. INPUT has TWO LAYERS:
   - A BASE PATTERN made of the TWO MOST COMMON colors (forming a complex partition)
   - OVERLAY MARKERS: scattered single cells of OTHER colors (minority colors)
   - The markers are placed ON TOP of cells of either dominant color

2. OUTPUT fills the ENTIRE grid:
   - The two dominant colors are REPLACED by colors from the overlay markers
   - Each connected region of dominant-color-A gets ONE marker's color
   - Each connected region of dominant-color-B gets ANOTHER marker's color
   - The output is completely filled with the marker colors

3. KEY RULE - Marker Position Determines Fill:
   - If a colored marker sits on a cell of dominant-color-A → that marker color fills the A-regions
   - If a colored marker sits on a cell of dominant-color-B → that marker color fills the B-regions
   - Multiple markers of different colors may fill different sub-regions

Think: "Are the two most common colors forming a binary partition, with rare colored markers indicating what color each partition becomes?"

Answer ONLY with: YES or NO"""

