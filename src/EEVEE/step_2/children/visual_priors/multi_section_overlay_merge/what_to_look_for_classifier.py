CLASSIFIER_PROMPT = """Does this puzzle involve MERGING MULTIPLE SECTIONS separated by divider columns?

Look for these indicators:
- The input grid is wide and contains vertical separator columns (a single repeating color forming vertical lines)
- The separators divide the input into multiple equal-width sections
- Each section contains a different "active" color pattern against a background color
- The output grid has the same dimensions as ONE section
- The output appears to combine/overlay non-zero cells from all sections

The transformation merges information from parallel sections, filling in gaps using data from other sections.

Answer ONLY with: YES or NO"""
