CLASSIFIER_PROMPT = """Does this puzzle show rectangular frames arranged in a GRID LAYOUT where each frame's OUTPUT COLOR depends on its NUMBER OF NEIGHBORING FRAMES?

EXACT PATTERN TO LOOK FOR:

INPUT:
- Multiple rectangular frames (outlines with hollow interiors or small markers inside)
- All frames are the SAME input color
- Frames are arranged touching each other in rows/columns (like tiles)

OUTPUT:
- Each frame is RECOLORED based on POSITION in the arrangement
- Corner frames → one color (they touch fewer neighbors)
- Edge frames → another color (they touch more neighbors)  
- Interior/center frames → yet another color (they touch the most neighbors)

CRITICAL CHECK: In the training examples, look for frames that are the SAME SIZE but in DIFFERENT POSITIONS getting DIFFERENT output colors. This proves the color is based on NEIGHBOR COUNT, not size.

Example: A 3x3 arrangement of frames where corner frames get color A, edge frames get color B, and the center frame gets color C.

Answer ONLY with: YES or NO"""
