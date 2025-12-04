CLASSIFIER_PROMPT = """Does this puzzle involve DIAGONAL LINE PROPAGATION FROM MARKERS?

Look for these indicators:
- The grid is divided into rectangular regions/blocks of different colors
- There are isolated "marker" cells - single cells with a color different from their surrounding region
- In the output, diagonal lines extend from these marker positions
- The diagonal lines propagate in both directions (like an X pattern) from each marker
- Lines continue across region boundaries, changing the cells along the diagonal path

Key questions:
- Are there 1-2 isolated special cells within larger uniform regions?
- Does the output show diagonal patterns emanating from where those special cells were?
- Do the diagonal lines extend across the entire grid from each marker?

Answer ONLY with: YES or NO"""
