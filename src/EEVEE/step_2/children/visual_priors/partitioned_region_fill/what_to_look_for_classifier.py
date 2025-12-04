CLASSIFIER_PROMPT = """Does this puzzle involve PARTITIONED REGION FILLING based on divider lines?

Look for these indicators:
- The input grid contains lines of a single non-background color that divide the grid into rectangular regions
- These divider lines form a network (like a cross-hatch or grid pattern with some segments)
- The divider lines create enclosed rectangular "pockets" or cells of varying sizes
- In the output, different rectangular regions are filled with different colors based on their size or enclosure properties
- The divider lines themselves remain unchanged between input and output
- Larger bounded regions get one fill color, smaller enclosed pockets get another color

Answer ONLY with: YES or NO"""
