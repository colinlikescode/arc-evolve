CLASSIFIER_PROMPT = """Does this puzzle involve COUNTING ADJACENCY RELATIONSHIPS BETWEEN BLOCK PAIRS?

Look for these indicators:
- The input contains multiple 2x2 blocks of two different non-background colors
- One color forms "marker" blocks and another forms "target" blocks
- The output is a single row with length equal to the number of marker blocks
- Each cell in the output appears to be binary (two possible values)
- The output seems to encode whether each marker block is adjacent to (touching) a target block

Check if:
- There are exactly two non-background colors forming 2x2 blocks
- The output length matches the count of one type of 2x2 block
- Output values indicate presence/absence of adjacency to the other block type

Answer ONLY with: YES or NO"""
