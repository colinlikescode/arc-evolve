CLASSIFIER_PROMPT = """Does this puzzle exhibit COLUMN MARKER REGION ASSIGNMENT?

This pattern involves:
- A header row (typically the first row) containing several distinct colored markers at different column positions
- Multiple rectangular regions below filled with a uniform placeholder/template color
- Each placeholder region needs to be recolored based on which column marker it aligns with horizontally

Look at the training examples:
- Is there a row (usually the first) with several distinct non-zero colored cells spaced apart?
- Are there rectangular blocks below filled with a single repeated "placeholder" color?
- In the output, do those placeholder blocks get replaced with colors matching the markers above them?
- Does each region's new color correspond to the marker whose column position overlaps with that region?

Answer ONLY with: YES or NO"""
