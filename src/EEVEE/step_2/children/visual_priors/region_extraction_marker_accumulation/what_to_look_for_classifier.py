CLASSIFIER_PROMPT = """Does this puzzle involve EXTRACTING A REGION BOUNDED BY DIVIDER LINES AND ACCUMULATING MARKERS?

Look for these indicators:
- The input grid has complete rows and/or columns filled with a single distinct color (divider lines)
- These dividers partition the grid into rectangular regions
- Within regions, there are scattered marker cells of a particular color on a background
- The output is smaller than the input, representing one extracted region
- The output has divider colors forming its borders
- Inside the output, scattered markers appear to be "accumulated" or "stacked" toward one edge (like gravity was applied)

Key questions:
- Are there full rows/columns of uniform color acting as separators?
- Does the output appear to be a bounded sub-region with markers consolidated?
- Do the border colors of the output match the divider line colors from the input?

Answer ONLY with: YES or NO"""
