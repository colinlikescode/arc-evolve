CLASSIFIER_PROMPT = """Does this puzzle involve NESTED CONCENTRIC FRAME COMPOSITION?

This pattern means:
- The input contains multiple distinct rectangular frame/border shapes scattered across a background
- Each frame shape has a different non-background color and different size
- The frames have an "outline" structure (hollow rectangles with gaps/openings)
- There may be a single isolated cell of a unique color marking the center point
- The output combines ALL frames into a single NESTED structure, centered concentrically
- Smaller frames are placed INSIDE larger frames, creating concentric layers
- The output has point symmetry (180° rotational symmetry) or reflection symmetry

Look at the training examples:
- Are there multiple hollow rectangular frame patterns in different colors?
- Do the frames have different sizes (some larger, some smaller)?
- Does the output show these frames nested inside each other like concentric rectangles?
- Is the output symmetric (usually both horizontally and vertically)?
- Is there a special marker cell that becomes the center of the output?

Answer ONLY with: YES or NO"""
