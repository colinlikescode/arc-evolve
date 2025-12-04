HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TEMPLATE RECONSTRUCTION FROM MARKERS          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the TEMPLATE: a connected shape with a dominant "connector" color and distinct "marker" colors at endpoints/corners
• Find SCATTERED MARKERS: isolated single cells matching the marker colors elsewhere in the grid
• The template defines SPATIAL RELATIONSHIPS between marker colors

YOUR TASK:
• Remove the original template from the output
• For each group of scattered markers that match the template's marker colors:
  - Determine the relative positions of the markers
  - Fill in the connector color along the paths between them, replicating the template's structure
  - The shape stretches/scales to fit the actual marker positions

CONCEPTUAL APPROACH:
• Template markers define "anchor points" with known relative positions
• Scattered markers define new anchor points
• Draw connector lines between scattered markers following the template's topology
• The connector color forms the "skeleton" between marker endpoints
"""
