CLASSIFIER_PROMPT = """Does this puzzle involve DISTINGUISHING COMPLETE vs INCOMPLETE SHAPES and TRANSFORMING only the complete ones?

Look for these indicators:
- The input contains multiple separate shapes/objects made of the same non-zero color
- Some shapes appear to be "complete" versions of a template (e.g., a 3x3 hollow square frame)
- Other shapes are "incomplete" or partial versions (missing cells, different sizes, fragments)
- In the output, the COMPLETE template shapes are transformed (e.g., converted to a different pattern using a new color)
- The INCOMPLETE shapes remain unchanged in the output

The transformation identifies which shapes match a "complete" template and applies a color/pattern change only to those, leaving partial shapes untouched.

Answer ONLY with: YES or NO"""
