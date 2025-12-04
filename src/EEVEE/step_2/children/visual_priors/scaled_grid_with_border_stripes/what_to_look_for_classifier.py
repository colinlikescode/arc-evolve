CLASSIFIER_PROMPT = """Does this puzzle exhibit SCALED GRID EXPANSION WITH BORDER STRIPE REPLICATION?

This pattern has these characteristics:
- The input is a small grid (e.g., 5x5) with a distinct structure:
  - A main rectangular region (typically 4x4) containing a pattern with a colored shape on a background
  - A rightmost column containing border stripe colors
  - A bottom row containing border stripe colors
  - A corner cell at the bottom-right
- The output is a larger grid where:
  - Each cell in the main region is scaled up proportionally based on the border stripe widths
  - The rightmost column colors become vertical stripes on the right side of the output
  - The bottom row colors become horizontal stripes at the bottom of the output
  - The corner cell color fills the bottom-right corner block
  - The colored shape in the main region is scaled and placed in its corresponding position
  - Diagonal marker lines (using a consistent accent color) appear in the empty/background corners of the scaled main region

Look at the training examples:
- Is there a rightmost column with non-zero colors that define vertical stripe widths?
- Is there a bottom row with non-zero colors that define horizontal stripe widths?
- Does the output show the main pattern scaled up with colored border stripes?
- Are there diagonal lines in the corners of the expanded background region?

Answer ONLY with: YES or NO"""
