CLASSIFIER_PROMPT = """Does this puzzle involve MIDDLE ROW ALTERNATING PATTERN within solid rectangles?

Look for these characteristics:
- The input contains one or more solid rectangular regions filled with non-zero colors
- Each rectangle has exactly 3 rows (height of 3)
- The rectangles are otherwise uniform/solid (all cells same color within each)
- In the output, the TOP and BOTTOM rows of each rectangle remain unchanged
- The MIDDLE row of each rectangle gets an alternating pattern: every other cell is replaced with the background color

Key indicators:
- Multiple solid 3-row-tall rectangles of various colors
- Output shows checkerboard/striped pattern ONLY in the middle row of each rectangle
- First and last rows of rectangles stay solid

Answer ONLY with: YES or NO"""
