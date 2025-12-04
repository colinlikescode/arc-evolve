CLASSIFIER_PROMPT = """Does this puzzle involve finding the SMALLEST ISOLATED RECTANGULAR REGION?

Look for these characteristics:
- The input contains multiple distinct colored rectangular regions on a background
- Some rectangles OVERLAP or TOUCH each other (partially sharing edges/corners)
- Some rectangles are COMPLETELY ISOLATED (surrounded only by background, not touching any other colored region)
- The output extracts ONE specific rectangle - typically the smallest one that is fully isolated from others

Key indicators:
- Multiple solid-colored rectangular blocks of different colors scattered in the grid
- At least one rectangle that does NOT overlap or connect with any other non-background region
- The output is a small solid rectangle filled with a single color
- The output dimensions match one of the isolated rectangles in the input

Answer ONLY with: YES or NO"""
