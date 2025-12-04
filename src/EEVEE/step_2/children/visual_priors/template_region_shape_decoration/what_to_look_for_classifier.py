CLASSIFIER_PROMPT = """Does this puzzle have a NON-BLACK TEMPLATE REGION containing decorated shapes, and a BLACK REGION with plain shapes that need the same decorations applied?

CRITICAL indicators:

1. TWO DISTINCT REGIONS in the input:
   - A TEMPLATE REGION with a non-zero background color (e.g., green/3)
   - A BLACK (0) REGION with scattered plain shapes

2. TEMPLATE REGION contains DECORATED SHAPES:
   - Shapes with frames/borders around them
   - Shapes with colored centers inside
   - Multi-color combinations (e.g., blue frame + cyan center, red frame + yellow center)

3. BLACK REGION contains PLAIN SHAPES:
   - Simple solid color blocks (e.g., just blue, just cyan, just red)
   - These shapes MATCH parts of the templates (same color, similar size)

4. OUTPUT applies templates to the black region:
   - Plain shapes in black region get decorated like the templates
   - A cyan block becomes a cyan center with blue frame (if that's the template)
   - A red block gets a yellow center added (if that's the template)

Think: "Is there a colored region showing how shapes should be decorated, and a black region with shapes waiting to be decorated the same way?"

Answer ONLY with: YES or NO"""

