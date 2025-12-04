CLASSIFIER_PROMPT = """Does this puzzle exhibit RECTANGULAR REGION BORDER DECORATION?

This pattern means:
- The input contains one or more solid rectangular regions filled with a single non-background color
- Each rectangle in the output is transformed to have a decorative border pattern
- The border pattern consists of: corners marked with one color, edges marked with another color, and interior filled with a third color
- The transformation creates a "picture frame" or "nested rectangle" effect within each original rectangle

Look at the training examples:
- Are there solid rectangular blocks of a uniform non-background color in the input?
- In the output, do these rectangles get replaced with a 3-color pattern?
- Do the corners of each rectangle have a distinct color?
- Do the edges (non-corner border cells) have a different color?
- Is the interior filled with yet another color?

Answer ONLY with: YES or NO"""
