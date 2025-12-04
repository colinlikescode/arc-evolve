HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: PAIRED BARS WITH MARKER-DISTANCE PROJECTION   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Two vertical bars of the same color exist on opposite sides of the grid
• One bar has marker cells at various horizontal distances from it
• The other bar has NO nearby markers

FOR THE BAR WITH MARKERS:
• Draw a horizontal line from the bar toward each marker
• Fill cells between bar and marker with a line color
• Replace the marker itself with a third "endpoint" color

FOR THE BAR WITHOUT MARKERS:
• For each row that had a marker relative to the other bar:
  - Draw a full-width horizontal line from this bar to the opposite edge
• The relative row positions within each bar's span are preserved

KEY INSIGHT:
• The markers define distances/patterns for one bar
• Those same row-offset patterns get "projected" as full lines for the other bar
• Line color and endpoint color are distinct from bar color and marker color
"""
