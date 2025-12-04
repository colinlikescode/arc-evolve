CLASSIFIER_PROMPT = """Does this puzzle involve COMBINING TWO STACKED REGIONS using a LOGICAL OR OPERATION?

Look for these indicators:
- The input grid is divided into two regions of equal size, separated by a horizontal divider row (a row filled with a single uniform color)
- The output grid has the same dimensions as each of the two regions (excluding the divider)
- The output appears to mark cells where EITHER region has a non-zero/non-background value
- A new color is used in the output to indicate the combined result
- Cells that are background/zero in BOTH regions remain background in the output

Key structural pattern:
- Input: [Region A] + [Divider Row] + [Region B]
- Output: Logical OR of Region A and Region B, with a new indicator color

Answer ONLY with: YES or NO"""
