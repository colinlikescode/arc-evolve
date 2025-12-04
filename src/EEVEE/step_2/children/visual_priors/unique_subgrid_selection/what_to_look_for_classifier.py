CLASSIFIER_PROMPT = """Does this puzzle involve a GRID DIVIDED INTO SUB-REGIONS WITH UNIQUE REGION SELECTION?

Look for these characteristics:
- The input grid is divided into multiple sub-regions by continuous separator lines (rows and/or columns of a single repeated color)
- This creates a grid of sub-regions (e.g., 3x3 arrangement of smaller grids)
- Each sub-region contains scattered non-zero colored cells
- The output preserves the separator structure but clears most sub-regions to background
- Only ONE sub-region retains its colored content in the output
- The retained sub-region appears to be selected based on some uniqueness criterion (e.g., it has content at positions where all other sub-regions have background)

Answer ONLY with: YES or NO"""
