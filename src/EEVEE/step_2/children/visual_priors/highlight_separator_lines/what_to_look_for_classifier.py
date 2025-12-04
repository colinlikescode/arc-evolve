CLASSIFIER_PROMPT = """Does this puzzle involve HIGHLIGHTING SEPARATOR LINES (all-background rows/columns)?

Look for these indicators:
- The input grid contains one or more complete rows that are entirely filled with the background color (typically zeros)
- The input grid may also contain one or more complete columns that are entirely filled with the background color
- These all-background rows/columns act as "dividers" or "separators" splitting the grid into regions
- In the output, these separator rows/columns are replaced with a different highlight color
- The rest of the grid remains unchanged

Key observations:
- Check if any rows consist entirely of a single color (usually the background/zero color)
- Check if any columns consist entirely of that same background color
- The output should show those specific rows/columns changed to a new marker color
- Non-separator cells retain their original values

Answer ONLY with: YES or NO"""
