CLASSIFIER_PROMPT = """Does this puzzle exhibit GRAVITY STACKING WITH RIGHT ALIGNMENT?

This pattern means:
- There is a "floor" or "anchor" row at the bottom that spans the full width
- Above it are various horizontal line segments (contiguous non-zero cells) scattered at different positions
- The transformation collects all these segments, sorts them by length, and stacks them
- Shorter segments end up higher, longer segments end up lower (just above the anchor)
- All segments are right-aligned (touching the right edge of the grid)
- The anchor/floor row remains fixed at the bottom

Look at the training examples:
- Is there a consistent full-width row at the bottom?
- Are there horizontal segments of varying lengths scattered above it?
- In the output, are these segments sorted by length and right-aligned?
- Does the bottom row stay unchanged?

Answer ONLY with: YES or NO"""
