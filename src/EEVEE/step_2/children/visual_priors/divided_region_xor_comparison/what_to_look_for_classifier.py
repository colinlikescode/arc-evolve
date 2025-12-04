CLASSIFIER_PROMPT = """Does this puzzle involve COMPARING TWO REGIONS SEPARATED BY A DIVIDER?

Look for these indicators:
- The input grid has a vertical or horizontal line/column of a single distinct color that divides it into two equal regions
- Each region contains a different non-background color forming a pattern
- The output grid is the same size as ONE of the divided regions
- The output appears to show some comparison or logical operation between the two regions (like XOR, AND, OR, or difference)

Check the training examples:
- Is there a clear dividing line splitting the input into two halves?
- Are there two distinct pattern colors, one in each half?
- Does the output size match one half of the input?
- Does the output mark cells based on comparing corresponding positions in both halves?

Answer ONLY with: YES or NO"""
