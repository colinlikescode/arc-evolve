CLASSIFIER_PROMPT = """Does this puzzle exhibit CONNECTING RECTANGULAR FRAMES WITH BRIDGES?

This pattern involves:
- Multiple RECTANGULAR FRAMES (hollow outlines) scattered in the input grid
- All frames are the SAME COLOR
- In the output, frames are CONNECTED with lines/bridges of the same color
- Frames that are ALIGNED (share a row or column edge) get connected
- The bridges extend from one frame's edge to reach another frame's edge

Look at the training examples:
- Are there multiple hollow rectangular frames in the input?
- Do frames that are horizontally or vertically aligned get connected in the output?
- Are the connections straight lines along rows or columns?
- Do the bridges fill the GAP between aligned frame edges?
- Do all frames use the same color?

Answer ONLY with: YES or NO"""
