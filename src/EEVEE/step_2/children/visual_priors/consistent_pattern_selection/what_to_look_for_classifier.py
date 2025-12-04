CLASSIFIER_PROMPT = """Does this puzzle involve IDENTIFYING THE CONSISTENT PATTERN among multiple scattered patterns?

Look for these indicators:
- The input is a larger grid containing several small distinct patterns (typically 3x3 regions)
- Multiple colors are present, each forming small pattern instances scattered across the grid
- Some colors have pattern instances that are IDENTICAL to each other (same shape repeated)
- Other colors have pattern instances that DIFFER from each other (inconsistent shapes)
- The output is a small grid (typically 3x3) showing one of these patterns

The key question: Are there multiple small patterns of different colors, where you need to identify which color has consistent/identical instances?

Answer ONLY with: YES or NO"""
