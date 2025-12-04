CLASSIFIER_PROMPT = """Does this puzzle involve BLOCK PATTERN MASKING?

Block pattern masking means:
- The input contains a large pattern made of uniformly-colored rectangular blocks arranged in a grid-like configuration
- The blocks are all the same size and form an N×M arrangement where some positions have blocks and some don't
- Separately, there is a small "key" grid of multi-colored cells elsewhere in the input
- The key grid has the same dimensions (N×M) as the block arrangement
- The output is derived by masking the key grid based on where blocks are present/absent

Look at the training examples:
- Is there a pattern of same-colored rectangular blocks forming a larger grid structure?
- Is there a separate small grid with varied colors?
- Does the small grid's dimensions match the block arrangement dimensions?
- In the output, are some values from the key preserved while others become zero?

Answer ONLY with: YES or NO"""
