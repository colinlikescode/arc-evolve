CLASSIFIER_PROMPT = """Does this puzzle exhibit SIZE-BASED VERTICAL EXTENSION/STACKING?

Look for these indicators:
- Multiple distinct colored rectangular objects positioned near the bottom or edge of the grid
- Objects have different areas/sizes
- In the output, objects are extended or repositioned vertically
- Larger objects extend further (occupy more vertical space) than smaller objects
- The relative horizontal positions of objects are preserved
- Objects appear to be "stacked" or "sorted" vertically by size

The transformation reorders/extends objects based on their area, with larger objects getting more vertical extent.

Answer ONLY with: YES or NO"""
