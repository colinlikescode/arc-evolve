CLASSIFIER_PROMPT = """Does this puzzle involve RECTANGULAR FRAME DUPLICATION/REPLICATION?

Look for these indicators:
- There is a rectangular frame/border made of a distinctive color in the input
- The frame encloses an interior region filled with a different color (often the background color)
- In the output, an ADDITIONAL identical frame appears at a different location
- The new frame is placed around a region that has a similar cluster of the same interior fill color
- The original frame remains unchanged; only a copy is added elsewhere

The transformation duplicates a rectangular frame structure to another location where a matching interior pattern exists.

Answer ONLY with: YES or NO"""
