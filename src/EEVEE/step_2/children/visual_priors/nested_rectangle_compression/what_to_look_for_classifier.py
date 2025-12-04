CLASSIFIER_PROMPT = """Does this puzzle exhibit NESTED CONCENTRIC RECTANGLES that get COMPRESSED/MINIATURIZED?

Look for these indicators:
- The input has multiple rectangular regions nested inside each other (like layers of an onion)
- Each rectangle is filled with a uniform color and surrounds a smaller rectangle of a different color
- There is a clear hierarchy: outermost background → middle layers → innermost region
- The output is significantly smaller than the input
- The output preserves the same nesting structure but with each layer reduced to minimal thickness (typically 1 cell)
- The relative positions and containment relationships are maintained

This is essentially a "compression" or "miniaturization" of a layered/nested structure where thick borders become thin borders.

Answer ONLY with: YES or NO"""
