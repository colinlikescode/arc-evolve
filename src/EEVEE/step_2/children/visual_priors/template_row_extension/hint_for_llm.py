HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TEMPLATE-BASED ROW EXTENSION PATTERN          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• One row spans the full width with a complete pattern - this is the TEMPLATE
• Other rows have partial fills (values only in first few columns)
• The template defines a POSITIONAL STRUCTURE of distinct values

HOW TO EXTEND PARTIAL ROWS:
• Identify the template row (full-width non-zero row)
• For each partial row, identify its distinct non-zero colors
• Create a mapping: partial row's colors correspond to template's colors by position
• Extend the partial row by following the template's pattern, substituting colors

EXAMPLE CONCEPT:
Template:  [A B A B B A B A]  (defines the positional pattern)
Partial:   [X Y 0 0 0 0 0 0]  (X maps to A-positions, Y maps to B-positions)
Output:    [X Y X Y Y X Y X]  (same structure as template, with new colors)

The template's structural pattern (which positions match which) determines how each partial row gets completed.
"""
