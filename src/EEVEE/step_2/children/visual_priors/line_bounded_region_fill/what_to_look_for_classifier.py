CLASSIFIER_PROMPT = """Does this puzzle exhibit LINE-BOUNDED REGION FILLING?

Line-bounded region filling means:
- The input contains a network of intersecting horizontal and vertical lines made of a single non-zero color
- These lines form a grid-like structure that divides the space into rectangular regions/cells
- The background is the zero/black color
- In the output, the background color is replaced with a "default fill" color everywhere
- Additionally, certain enclosed rectangular regions (bounded on all four sides by the line color) are filled with a distinct "interior fill" color

Look at the training examples:
- Is there a single non-zero color forming horizontal and vertical line segments?
- Do these lines intersect to create enclosed rectangular regions?
- In the output, is the background replaced with one color, while some enclosed regions get a different fill color?
- Are the filled regions specifically those that are completely bounded by lines on all four sides?

Answer ONLY with: YES or NO"""
