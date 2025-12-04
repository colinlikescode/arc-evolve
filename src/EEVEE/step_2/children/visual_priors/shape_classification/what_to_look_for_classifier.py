CLASSIFIER_PROMPT = """Does this puzzle involve SHAPE CLASSIFICATION / PATTERN CATEGORIZATION?

Shape classification means:
- The input is a small grid containing non-zero cells forming a specific geometric pattern
- The output is a single cell containing a numeric code/category
- The same geometric shape always maps to the same output code, regardless of which color is used
- Different geometric arrangements of non-zero cells map to different codes

Look at the training examples:
- Is the output always a single 1x1 cell?
- Do inputs with the same spatial arrangement of non-zero cells (ignoring the actual color value) produce the same output?
- Do inputs with different spatial patterns produce different outputs?
- Does the specific color used in the input seem irrelevant to the output?

Answer ONLY with: YES or NO"""
