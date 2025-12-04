CLASSIFIER_PROMPT = """Does this puzzle involve EXTRACTING A UNIQUE REGION FROM A MULTI-REGION GRID?

Look for these indicators:
- The input grid is divided into multiple regions/quadrants by bands of background (zero) cells
- Different regions contain patterns using different non-zero colors
- One color appears in only ONE region while another color appears in multiple regions
- The output is a single extracted rectangular region (smaller than the input)
- The output contains only one non-zero color plus background

Check if:
- There are clear horizontal and/or vertical separator bands of zeros dividing the grid
- The regions have distinct color signatures
- The output matches the dimensions and content of exactly one input region

Answer ONLY with: YES or NO"""
