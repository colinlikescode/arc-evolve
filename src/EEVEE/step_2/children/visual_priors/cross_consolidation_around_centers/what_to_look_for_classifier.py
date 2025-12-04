CLASSIFIER_PROMPT = """Does this puzzle involve CONSOLIDATING SCATTERED MARKERS INTO A CROSS PATTERN around center cells?

Look for these indicators:
- The input has isolated "center" cells with a distinct color
- There are "marker" cells of another color scattered at various positions, some sharing a row or column with a center
- The output shows a cross/plus pattern formed directly adjacent to each center cell
- Scattered markers are removed and replaced by a compact cross using the marker color
- Each center-marker pair forms its own cross pattern independently

The transformation identifies which markers belong to which center and creates a minimal cross pattern around each center.

Answer ONLY with: YES or NO"""
