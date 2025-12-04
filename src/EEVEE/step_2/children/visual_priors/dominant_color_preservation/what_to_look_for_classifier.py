CLASSIFIER_PROMPT = """Does this puzzle involve DOMINANT COLOR PRESERVATION with MINORITY COLOR REPLACEMENT?

This pattern means:
- The input grid contains multiple different colors
- One color appears more frequently than others (the dominant/majority color)
- In the output, the dominant color cells remain unchanged
- All cells with non-dominant (minority) colors are replaced with a single uniform replacement color

Look at the training examples:
- Does one color appear more frequently than others in each input?
- Do cells with that dominant color stay the same in the output?
- Are all other colors (regardless of what they were) replaced with one consistent color?
- Is the grid structure/size preserved?

Answer ONLY with: YES or NO"""
