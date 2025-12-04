CLASSIFIER_PROMPT = """Does this puzzle involve COMPARING TWO STACKED REGIONS separated by a divider?

Look for these indicators:
- The input grid has a horizontal divider row (a row of uniform color) splitting it into sections
- There are two regions of equal size above and below the divider
- Each region contains a pattern using a distinct non-background color
- The output grid is the same size as one of these regions
- The output appears to mark differences or relationships between the two patterns

Specifically, check if:
- The input has 3 parts: top pattern, separator row, bottom pattern
- Top and bottom patterns use different colors for their non-zero cells
- The output marks positions based on comparing these two patterns

Answer ONLY with: YES or NO"""
