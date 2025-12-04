CLASSIFIER_PROMPT = """Does this puzzle involve FINDING THE REGION WITH THE MOST ANOMALIES?

Look for these indicators:
- The input grid is divided into distinct rectangular regions, each with its own dominant/background color
- Within some regions, there are scattered "marker" or "anomaly" cells of a different color
- The output is a single cell (1x1 grid)
- The output color matches the dominant color of one of the input regions

The task appears to be: identify which region contains the most anomaly/marker cells, then output that region's dominant color.

Look at the training examples:
- Is the grid partitioned into colored rectangular zones?
- Do some zones contain cells of a contrasting color scattered within them?
- Does the output correspond to the background color of the zone with the most such scattered cells?

Answer ONLY with: YES or NO"""
