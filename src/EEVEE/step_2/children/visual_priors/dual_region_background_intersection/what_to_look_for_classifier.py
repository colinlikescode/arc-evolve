CLASSIFIER_PROMPT = """Does this puzzle involve COMPARING TWO STACKED PATTERN REGIONS?

Look for these indicators:
- The input grid is divided into two equal halves (top and bottom)
- Each half contains a distinct pattern using different non-zero colors
- The output grid is the same size as ONE of the halves
- The transformation appears to compare corresponding cells between the two halves
- The output marks specific cells based on a logical comparison (e.g., where both regions share certain properties like both having background color)

Check if:
- Input height is exactly 2× the output height
- Input width equals output width
- Two different non-zero colors appear, one predominantly in each half
- Output uses a NEW color not present in either input half

Answer ONLY with: YES or NO"""
