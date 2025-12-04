CLASSIFIER_PROMPT = """Does this puzzle exhibit RUN-LENGTH DEDUPLICATION / UNIQUE STRIPE EXTRACTION?

This pattern means:
- The input grid contains repeated rows or repeated columns forming "stripes" or "bands"
- Consecutive identical rows/columns are collapsed into a single row/column
- The output extracts one representative from each group of consecutive identical rows/columns
- Additionally, within each row/column, consecutive identical values may also be deduplicated

Look at the training examples:
- Are there groups of identical consecutive rows that get reduced to one row?
- Are there groups of identical consecutive columns that get reduced to one column?
- Does the output appear to be a "compressed" version showing only unique consecutive stripes?
- Is the output significantly smaller than the input in one or both dimensions?

Answer ONLY with: YES or NO"""
