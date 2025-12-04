CLASSIFIER_PROMPT = """Does this puzzle involve TEMPLATE COMPLETION WITH ORIENTATION MARKERS?

This pattern has these characteristics:
- Multiple similar skeletal shapes made of one dominant connector color (forming L-shapes, lines, or crosses)
- Each shape has a single "marker" cell of a distinct accent color at one end or corner
- ONE shape is "complete" - it has additional decorative elements (other colors) around the skeleton
- OTHER shapes are "incomplete" - they have only the skeleton and marker, missing the decorations
- The transformation fills in the incomplete shapes by copying the decoration pattern from the complete template
- The marker position determines the orientation/reflection of how decorations are placed

Look at the training examples:
- Are there multiple similar skeletal structures of one color?
- Does each structure have a single marker cell of another color?
- Is one structure more decorated than the others?
- In the output, do the incomplete structures gain decorations matching the complete one?

Answer ONLY with: YES or NO"""
