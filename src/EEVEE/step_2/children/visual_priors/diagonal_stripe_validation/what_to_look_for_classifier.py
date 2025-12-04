CLASSIFIER_PROMPT = """Does this puzzle involve DIAGONAL STRIPE VALIDATION/RECOLORING?

Look for these indicators:
- The input grid has a small fixed number of rows (typically 3) with markers scattered throughout
- There is an implicit diagonal pattern where each column "belongs to" a specific row based on column index modulo the number of rows
- The transformation recolors markers based on whether they fall ON or OFF this repeating diagonal stripe
- Markers on the expected diagonal position keep their original color
- Markers off the diagonal are changed to a different color
- The output has the same dimensions and marker positions, just with some markers recolored

Answer ONLY with: YES or NO"""
