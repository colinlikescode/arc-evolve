CLASSIFIER_PROMPT = """Does this puzzle involve TWO VERTICAL LINE SEGMENTS (BARS) WITH MARKER-BASED HORIZONTAL LINE EXTENSION?

Look for these indicators:
- Two separate vertical line segments of the same color, positioned on opposite edges (left vs right) or different regions of the grid
- Scattered single marker cells of a different color within the grid
- The markers appear in rows that correspond to rows of one of the vertical bars
- The transformation draws horizontal lines connecting bars to markers or extending fully across

Key pattern:
- One bar has markers at various distances - lines extend from bar to marker, marker changes to a third color
- The other bar (without nearby markers) gets full-width horizontal lines at the same relative row positions within its span

Answer ONLY with: YES or NO"""
