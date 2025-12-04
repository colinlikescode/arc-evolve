CLASSIFIER_PROMPT = """Does this puzzle involve EXTRACTING A SOLID RECTANGULAR REGION from noise?

Look for these indicators:
- The input grid contains many scattered non-zero cells (appears noisy/random)
- Hidden within the noise is ONE solid rectangular block filled entirely with the SAME non-zero value
- This rectangular block is larger than typical single cells or small clusters
- The output grid is mostly background (zeros) except for this one rectangular region
- The rectangular region is preserved in its exact position in the output

The key insight is finding a contiguous rectangular area where ALL cells have the same non-zero value, which stands out from the random noise around it.

Answer ONLY with: YES or NO"""
