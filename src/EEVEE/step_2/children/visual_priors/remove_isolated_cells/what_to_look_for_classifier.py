CLASSIFIER_PROMPT = """Does this puzzle involve REMOVING ISOLATED CELLS while keeping connected groups?

This pattern means:
- The input and output grids have the same dimensions
- Non-zero cells that have NO adjacent non-zero neighbors (isolated/singleton cells) are removed (set to zero)
- Non-zero cells that ARE adjacent to at least one other non-zero cell (forming clusters/groups) are preserved
- Adjacency can be orthogonal (up/down/left/right) or diagonal

Look at the training examples:
- Do some scattered non-zero cells disappear in the output?
- Do cells that form clusters or pairs remain in the output?
- Are the removed cells those that stand alone with no non-zero neighbors?

Answer ONLY with: YES or NO"""
