CLASSIFIER_PROMPT = """Does this puzzle exhibit SOLID RECTANGLE TO HOLLOW FRAME transformation?

This pattern means:
- The input contains one or more solid filled rectangles of non-background colors
- Each solid rectangle is transformed into a hollow frame/border
- The interior of each rectangle is replaced with the background color
- Only the outermost border (perimeter) of each rectangle retains the original color

Look at the training examples:
- Are there solid rectangular regions filled with a single non-background color?
- In the output, do these rectangles become hollow (only the border remains)?
- Is the interior of each rectangle cleared to the background color?
- Does the first and last row/column of each rectangle stay filled while middle rows/columns are hollowed?

Answer ONLY with: YES or NO"""
