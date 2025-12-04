CLASSIFIER_PROMPT = """Does this puzzle involve SHAPE DOCKING / CONNECTOR REMOVAL?

Shape docking means:
- There are two distinct rectangular regions of different colors
- One region is connected to the other by a thin line (1 cell wide) of the same color as one of the regions
- The line acts as a "connector" or "arm" extending from one shape toward the other
- The transformation removes the connector line and moves the smaller/secondary shape to be directly adjacent to the primary shape

Look at the training examples:
- Are there two separate colored rectangular regions?
- Is there a thin line (single cell width) connecting or extending from one region toward the other?
- In the output, is the connector removed and the shapes positioned adjacent to each other?
- Does the smaller shape "dock" against the larger shape where the connector was pointing?

Answer ONLY with: YES or NO"""
