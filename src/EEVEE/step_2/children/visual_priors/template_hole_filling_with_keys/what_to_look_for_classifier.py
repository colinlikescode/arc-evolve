CLASSIFIER_PROMPT = """Does this puzzle involve TEMPLATE HOLE FILLING using pattern keys?

Look for these indicators:
- A large rectangular region filled mostly with a dominant/uniform color
- The large region contains several distinct "hole" areas (cells with background/zero color)
- Multiple small pattern "keys" scattered elsewhere in the input
- Each key pattern has the same shape as one of the holes but uses accent colors instead of background
- The keys show how to fill in the corresponding holes

The transformation fills holes in the main region by matching each hole's shape to a key pattern and using the key's colors.

Answer ONLY with: YES or NO"""
