CLASSIFIER_PROMPT = """Does this puzzle involve FINDING THE UNIQUE PATTERN among multiple same-sized blocks?

Look for these indicators:
- The input grid can be divided into multiple equal-sized blocks (either stacked vertically or arranged horizontally)
- Each block uses a single distinct color (plus background/zero cells)
- Most blocks share the same structural pattern (same arrangement of colored vs background cells)
- ONE block has a different structural pattern from the others
- The output is a single block matching the size of the individual input blocks

The task is to identify which block is structurally unique (the "odd one out") and return that block.

Answer ONLY with: YES or NO"""
