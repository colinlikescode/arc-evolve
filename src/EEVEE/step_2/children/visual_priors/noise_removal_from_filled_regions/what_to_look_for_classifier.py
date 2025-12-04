CLASSIFIER_PROMPT = """Does this puzzle involve NOISE REMOVAL FROM FILLED REGIONS?

Look for these indicators:
- The input contains rectangular or blob-like regions filled with a dominant non-background color
- Within these filled regions, there are scattered cells of a DIFFERENT non-background color (noise/outliers)
- These noise cells appear sporadically and inconsistently within the filled shapes
- The noise color also appears scattered in the background area (outside the shapes)
- The output shows the same filled regions but with the noise cells REMOVED (replaced with the region's dominant fill color)
- The noise cells in the background area are also removed (replaced with background color)

Key pattern: There's a "fill color" for shapes and a "noise color" that contaminates both the shapes and background. The transformation cleans up by removing all noise.

Answer ONLY with: YES or NO"""
