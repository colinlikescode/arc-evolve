CLASSIFIER_PROMPT = """Does this puzzle involve SHAPE-MATCHING colored blocks to HOLLOW REGIONS in a template?

Look for these indicators:
- A template shape (e.g., blue/color 1) at the top defines HOLLOW rectangular regions (background cells inside)
- Below the template, there are colored blocks/groups (e.g., grey/color 5) of various shapes
- The transformation converts MATCHING blocks (those whose shape fits the hollow interior) to a marker color (red/2)
- Blocks that DON'T MATCH the hollow region's shape remain unchanged

Key pattern:
- Compare the SHAPE of each colored block group to the SHAPE of the hollow interior in the template
- Blocks that can "fit" into the hollow region → get converted to the marker color
- Blocks that cannot fit (different shape) → remain their original color

Answer ONLY with: YES or NO"""
