"""Mass mutation prompts organized into three sets (A, B, C).

SET A (0-99): Technical debugging - off-by-one errors, boundary conditions, code fixes
SET B (100-199): Pattern recognition - geometric, structural, algorithmic approaches  
SET C (200-299): Abstract thinking - different mental models, perspectives, creative reframing
"""

# =============================================================================
# SET A: Technical Debugging Hints (0-99)
# Focus: Low-level code fixes, off-by-one errors, boundary conditions
# Used by: Grok Round 1
# =============================================================================
SET_A_PATTERNS = [
    # Off-by-one and boundary errors (0-9)
    "CHECK OFF-BY-ONE ERRORS: Your indices might be off by 1. Try adding or subtracting 1 from key coordinates. Check if you're using 0-based vs 1-based indexing consistently.",
    "FIX BOUNDARY CONDITIONS: The edges and corners often need special handling. Check if row==0, col==0, row==height-1, or col==width-1 need different logic.",
    "INCLUSIVE VS EXCLUSIVE RANGES: Your loops might include/exclude endpoints incorrectly. Try changing < to <=, or range(n) to range(n+1), or vice versa.",
    "INVERT YOUR CONDITION: Try flipping a key condition. Change > to <, or == to !=, or 'and' to 'or'. One logical inversion might fix everything.",
    "SWAP COMPARISON ORDER: If you're comparing a < b, try b < a. The relationship direction might be backwards.",
    "NEGATE A BOOLEAN: One of your True/False checks might be inverted. Try adding 'not' to a key condition.",
    "SWAP ROW AND COLUMN: You might have row/col or x/y swapped somewhere. Try transposing coordinates in your key calculations.",
    "REVERSE DIRECTION: Try reversing the direction of iteration. If going left-to-right, try right-to-left. If top-to-bottom, try bottom-to-top.",
    "FLIP VERTICAL: The transformation might be vertically flipped. Try inverting row indices: use (height - 1 - row) instead of row.",
    "FLIP HORIZONTAL: The transformation might be horizontally flipped. Try inverting column indices: use (width - 1 - col) instead of col.",
    
    # Arithmetic and rounding (10-19)
    "CHANGE ROUNDING: If using division, try floor() instead of ceil(), or round() instead of int(). Rounding direction matters.",
    "INTEGER DIVISION: Check if you need // instead of /, or vice versa. Integer vs float division can cause off-by-one in positions.",
    "ARITHMETIC SIGN: Try changing a + to - or vice versa in your coordinate calculations. An offset might have the wrong sign.",
    "SWAP TWO COLORS: Try swapping the two most common non-background colors. The color assignment might be reversed.",
    "CHECK BACKGROUND COLOR: Make sure you're treating 0 as background correctly. Some cells that should stay 0 might be getting modified.",
    "OFF-BY-ONE COLOR: The output color might be the input color ±1. Try adding or subtracting 1 from color values.",
    "HANDLE EMPTY CASE: Check if there's a special case when a region is empty, has one cell, or has no matching elements.",
    "FIRST/LAST ELEMENT SPECIAL: The first or last element in a sequence might need special handling different from the middle elements.",
    "CORNER CASE: Corners (0,0), (0,w-1), (h-1,0), (h-1,w-1) might need explicit special handling.",
    "SIMPLIFY AND RETRY: Your solution might be overcomplicating things. Try the simplest possible interpretation of the pattern.",
    
    # Low-level debugging (20-34)
    "CHECK MODULO OPERATIONS: If using %, the divisor might be wrong. Try n-1, n+1, or a completely different value.",
    "ABSOLUTE VS RELATIVE OFFSET: An offset might need to be absolute (from grid origin) instead of relative (from object), or vice versa.",
    "CHECK MIN/MAX CONFUSION: You might be taking min when you should take max, or vice versa. Swap them and see if it helps.",
    "WRONG COMPARISON BASE: When comparing sizes/counts, you might be comparing to the wrong reference value.",
    "CHECK ARRAY INITIALIZATION: Your output array might be initialized with the wrong values. Try 0 instead of copy of input, or vice versa.",
    "WRONG LOOP BOUNDS: Your loop might start at 1 instead of 0, or end at n instead of n-1. Check carefully.",
    "EARLY TERMINATION: Your loop might be breaking/returning too early. The condition for early exit might be wrong.",
    "WRONG NEIGHBOR SET: When checking neighbors, you might be using 4-connectivity when 8-connectivity is needed, or vice versa.",
    "CONDITION ORDER MATTERS: If you have chained conditions (if/elif/else), the order might matter. Try reordering them.",
    "ACCUMULATOR INITIALIZATION: A sum or count variable might need different initial value (0 vs 1 vs len vs -1).",
    "WRONG ARRAY DIMENSION: When accessing nested arrays, you might have the indices in wrong order [i][j] vs [j][i].",
    "EMPTY CONTAINER CHECK: Before accessing [0] or using max/min, check if the container is empty.",
    "DOUBLE COUNTING: Items might be counted twice in loops. Check if iteration covers same elements multiple times.",
    "MISSING CASE: There might be a case you haven't handled (e.g., single-cell objects, zero values, negative indices).",
    "VARIABLE SHADOWING: A variable name might be reused inside a loop, hiding the outer value you intended.",
    
    # Pattern interpretation fixes (35-54)
    "RE-EXAMINE OBJECT BOUNDARIES: The objects in the grid might extend further than you think. Check if diagonal neighbors should be included in connected components.",
    "CHECK OBJECT CENTER CALCULATION: The center of an object might be calculated differently. Try using min/max bounds vs. centroid vs. first cell found.",
    "RELATIVE VS ABSOLUTE POSITIONS: Your code might be using absolute grid coordinates when it should use positions relative to an object, or vice versa.",
    "INSIDE VS OUTSIDE: If you're filling or marking regions, check whether you're operating on the interior, exterior, or boundary of shapes.",
    "CROSS PATTERN COMPLETION: Look for clusters of cells that form partial crosses (+). The transformation may complete these into 3x3 cross shapes.",
    "RECTANGLE TRANSFORMATION: Look for rectangular regions that may be filled, moved, or transformed. Solid color rectangles may be markers.",
    "TILING/REPETITION: The grid may contain a repeating tile pattern. A smaller pattern may be repeated across the grid.",
    "GRID DIVISION: The grid may be divided into distinct sub-regions with separator lines. Process each sub-region independently.",
    "PROPAGATION: Colors may spread from a source block following diagonal, staircase, or ray patterns.",
    "BORDER/FRAME: The outer edge may be a uniform color defining the output area. Extract and process the interior region.",
    "TEMPLATE MATCHING: A marker color may mark specific content regions. Find matching regions and add markers at those locations.",
    "OBJECT EXTRACTION: The output may be smaller - a specific region or object may be selected and cropped tightly.",
    "COLOR REMAPPING: The structure/shape may stay the same while colors are transformed according to a rule. Find the color mapping.",
    "DOMINANT COLOR: One color may be significantly more common. The transformation may use the dominant color as background or fill reference.",
    "MAJORITY VS MINORITY COLOR: You might be using the wrong color frequency criterion. Try the opposite (most common vs. least common).",
    "SCALING FACTOR: The transformation might involve scaling by a factor you haven't considered. Try 2x, 3x, or input-derived scaling.",
    "ROTATION AMOUNT: If rotation is involved, try 90°, 180°, or 270° instead of what you're currently using.",
    "OUTPUT SIZE DERIVATION: The output grid size might be derived from the input differently. Check if it should match input, be fixed, or be computed from objects.",
    "CLOCKWISE VS COUNTERCLOCKWISE: If rotation is involved, try the opposite direction.",
    "DIAGONAL SYMMETRY: The grid might have symmetry along the main diagonal (row i, col j equals row j, col i).",
    
    # Symmetry and patterns (55-69)
    "ANTI-DIAGONAL SYMMETRY: Check for symmetry along the anti-diagonal (top-right to bottom-left).",
    "REFLECTION AXIS: The reflection axis might be horizontal, vertical, or along a diagonal.",
    "PARTIAL SYMMETRY: Only part of the grid might have symmetry. Find the symmetric region.",
    "SHAPE COMPLETION: Incomplete shapes might need to be completed based on their partial structure.",
    "PATTERN CONTINUATION: A pattern started in part of the grid might need to be continued/extended.",
    "OVERLAY OPERATION: Multiple patterns might need to be overlaid. Check the order of overlay.",
    "MASK DERIVATION: The mask for the operation might come from a different part of the grid than expected.",
    "REFERENCE CELL: One specific cell might define the rule for the entire transformation.",
    "CONNECTED COMPONENT SIZE: The size threshold for what counts as an 'object' might be different.",
    "ASPECT RATIO: Objects might be identified by their aspect ratio (tall vs wide vs square).",
    "DIAGONAL LINES: Look for diagonal lines that might be extended, completed, or used as dividers.",
    "ALTERNATING PATTERN: Every other cell/row/column might be treated differently.",
    "BREAK INTO SUBPROBLEMS: Can the transformation be broken into independent steps? Try identifying what happens first, second, third.",
    "PROCESS OBJECTS INDEPENDENTLY: Each object might be transformed separately. Apply the same rule to each object in isolation.",
    "LAYER-BY-LAYER: The output might be built in layers. First the background, then one type of object, then another.",
    
    # Algorithmic approaches (70-99)
    "MASK THEN APPLY: Create a mask of which cells should be affected, then apply the transformation only to masked cells.",
    "CHANGE PROCESSING ORDER: You might be processing objects/cells in the wrong order. Try: largest first, smallest first, top-to-bottom, or by color.",
    "TWO-PASS ALGORITHM: First pass to collect information, second pass to make changes. Don't modify while iterating.",
    "REVERSE THE TRANSFORMATION: Think about how to go from output back to input. This might reveal the forward transformation.",
    "APPLY RULE ITERATIVELY: The transformation might need to be applied repeatedly until no more changes occur.",
    "USE INPUT AS TEMPLATE: The input grid structure might define WHERE to place things, not WHAT to place.",
    "FIND THE REFERENCE OBJECT: One object in the grid might be the 'template' that defines how others should look.",
    "COPY AND MODIFY: Start with an exact copy of input, then make specific modifications. Don't build output from scratch.",
    "OUTPUT MIRRORS INPUT STRUCTURE: The output grid might have the same spatial structure as input, just with different values.",
    "COMPARE OBJECTS PAIRWISE: The transformation might depend on relationships BETWEEN objects, not just individual objects.",
    "FIND THE ODD ONE OUT: One object might be different from others and treated specially (removed, highlighted, etc.).",
    "PROPAGATE FROM SOURCE: There might be a source cell/object that propagates influence to others (flood fill, ray casting).",
    "INHERIT FROM NEIGHBORS: Each cell's output might be determined by a specific neighbor (e.g., cell above, cell to the left).",
    "CHECK FOR GRID-WITHIN-GRID: The grid might be divided into regions that each follow the same sub-pattern.",
    "LOOK FOR IMPLICIT LINES: There might be invisible dividing lines (horizontal, vertical, diagonal) that partition the grid.",
    "BOUNDING BOX MATTERS: The bounding box of an object might determine something important (position, size of result).",
    "GRAVITY/STACKING: Objects might need to 'fall' in a direction (down, left) until they hit something.",
    "FLOOD FILL VARIANT: Try flood fill with different connectivity (4 vs 8) or different stopping conditions.",
    "DYNAMIC PROGRAMMING: The solution might require building up from smaller subproblems.",
    "GREEDY APPROACH: Try solving greedily (take best option at each step) instead of searching for global optimum.",
    "BACKTRACKING: If your current approach doesn't work, you might need to backtrack and try alternatives.",
    "SIMULATION: The transformation might be simulating some physical process (movement, growth, decay).",
    "STATE MACHINE: Each cell might transition through states based on its current state and neighbors.",
    "CELLULAR AUTOMATON: Apply rules based on local neighborhood, like Game of Life.",
    "PATHFINDING: There might be a path from one point to another that determines the output.",
    "MORPHOLOGICAL OPERATIONS: Try erosion, dilation, opening, or closing operations on shapes.",
    "DISTANCE TRANSFORM: Cells might need to know their distance to the nearest edge, object, or special cell.",
    "SCANLINE ALGORITHM: Process the grid line by line, maintaining state between lines.",
    "DIVIDE AND CONQUER: Split the grid into quadrants/sections and solve each independently.",
    "UNION-FIND: Objects might need to be merged based on connectivity or proximity.",
]

# =============================================================================
# SET B: Pattern Recognition (100-199)
# Focus: Geometric transformations, structural analysis, specific techniques
# Used by: Grok Round 3
# =============================================================================
SET_B_PATTERNS = [
    # Color and value manipulations (0-19)
    "COLOR CYCLE: Colors might cycle through a sequence. If you see 1,2,3 the next might be 1 again, not 4.",
    "XOR COLORS: Try XORing color values between input regions to get output colors.",
    "COLOR MAPPING TABLE: Build an explicit mapping table from input to output colors based on examples.",
    "BINARY ENCODING: Colors 0/1 might represent binary values that encode some information.",
    "TERNARY LOGIC: With 3 colors, there might be a ternary operation (like min, max, or median).",
    "COLOR FREQUENCY RANK: Recolor based on frequency rank (most common = 1, second = 2, etc.).",
    "PARITY CHECK: Even/odd row, column, or cell count might determine color or behavior.",
    "COLOR GRADIENT: Colors might represent distances or intensities in a gradient pattern.",
    "COMPLEMENT COLOR: Output color might be (max_color - input_color) for some max value.",
    "CONDITIONAL COLORING: Color depends on multiple conditions (row AND column, neighbor AND self).",
    "LAYER PRIORITY: When colors overlap, there's a priority order determining which shows.",
    "COLOR PRESERVATION: Some specific color values must be preserved exactly in the output.",
    "NEUTRAL ELEMENT: One color might act as 'transparent' or 'identity' in operations.",
    "ABSORBING ELEMENT: One color might 'absorb' or override all others when combined.",
    "COLOR BOUNDARIES: Trace the boundaries between different colored regions.",
    "INTERIOR VS BOUNDARY COLOR: Interior cells get one color, boundary cells get another.",
    "MARKER COLOR: One color marks positions where operations should occur.",
    "ANCHOR COLOR: One color serves as reference points for alignment or positioning.",
    "SIGNAL COLOR: A rare color might signal a special operation or rule change.",
    "BACKGROUND REPLACEMENT: Background color might be determined by the surrounding context.",
    
    # Geometric transformations (20-39)
    "SHEAR TRANSFORMATION: Objects might be sheared (skewed) horizontally or vertically.",
    "STRETCH IN ONE DIRECTION: Objects might be stretched only horizontally or only vertically.",
    "COMPRESS/SQUEEZE: Objects might be compressed to fit a smaller space.",
    "MIRROR WITHIN BOUNDS: Objects might be mirrored within their own bounding box.",
    "ROTATE AROUND CENTER: Rotation might be around the center of each object, not the grid.",
    "TRANSLATE BY OFFSET: Objects might be shifted by a constant or computed offset.",
    "SCALE FROM CENTROID: Scaling might happen relative to each object's centroid.",
    "FOLD ALONG AXIS: The grid might fold along an axis, overlapping onto itself.",
    "UNFOLD/EXPAND: A compact representation might unfold into a larger pattern.",
    "TESSELLATION: A pattern might tile/tessellate to fill the output grid.",
    "PERSPECTIVE TRANSFORM: The pattern might have perspective-like depth transformation.",
    "AFFINE COMBINATION: Multiple transformations might be combined (rotate then scale).",
    "SYMMETRY AXIS POSITION: The axis of symmetry might not be at the center.",
    "PARTIAL ROTATION: Only part of the grid might be rotated while rest stays fixed.",
    "ROTATION PIVOT: The pivot point for rotation might be at a specific cell, not center.",
    "TRANSLATE WRAP: Objects that go off edge might wrap around to the other side.",
    "SPIRAL PATTERN: The transformation might follow a spiral path from center or corner.",
    "ZIGZAG TRAVERSAL: Elements might be read/written in a zigzag pattern.",
    "DIAGONAL TRAVERSAL: Process the grid along diagonals rather than rows/columns.",
    "CONCENTRIC RINGS: Process the grid in concentric rectangular rings from outside in.",
    
    # Structural patterns (40-59)
    "BRACKET MATCHING: Look for paired elements that 'match' like opening/closing brackets.",
    "HIERARCHY/NESTING: Objects might be nested inside each other with parent-child relationships.",
    "SPANNING TREE: Find a tree that connects all objects with minimum total distance.",
    "CONVEX HULL: The convex hull of points/objects might define the output region.",
    "VORONOI REGIONS: Each cell belongs to the nearest seed point, creating regions.",
    "SKELETON/MEDIAL AXIS: Extract the skeleton or centerline of shapes.",
    "CONTOUR TRACING: Trace the outer contour of shapes to get their outline.",
    "HOLE DETECTION: Find and handle holes (enclosed background regions) in objects.",
    "CONCAVITY/CONVEXITY: Distinguish between convex and concave regions of shapes.",
    "PERIMETER CALCULATION: The perimeter length might determine some property.",
    "AREA RATIO: The ratio of areas between objects might determine the transformation.",
    "DENSITY: The density of colored cells in a region might be significant.",
    "COMPACTNESS: How compact (circular vs elongated) a shape is might matter.",
    "ECCENTRICITY: The elongation direction and amount might affect the transformation.",
    "ORIENTATION ANGLE: Objects might need to be analyzed for their orientation angle.",
    "PRINCIPAL AXIS: Transform relative to the principal axis of shapes.",
    "MOMENT OF INERTIA: Shape distribution around center might determine behavior.",
    "TOPOLOGY PRESERVATION: The transformation preserves topological relationships.",
    "EULER NUMBER: The number of objects minus holes might be significant.",
    "GENUS: The topological complexity of shapes might determine the transformation.",
    
    # Sequence and order patterns (60-79)
    "SEQUENCE NUMBER: Objects might be numbered in sequence (1st, 2nd, 3rd) affecting output.",
    "READING ORDER: Process in reading order (left-to-right, top-to-bottom) matters.",
    "REVERSE SEQUENCE: The sequence might need to be reversed from expected order.",
    "INTERLEAVE: Two sequences might be interleaved (A1, B1, A2, B2, ...).",
    "DEINTERLEAVE: A single sequence might need to be split into two alternating parts.",
    "SUBSEQUENCE: Extract a specific subsequence based on some criterion.",
    "CIRCULAR SHIFT: Elements in a sequence might be circularly shifted.",
    "SORT BY PROPERTY: Objects might be sorted by size, color, position, etc.",
    "STABLE SORT: When sorting, original order is preserved for equal elements.",
    "PARTIAL ORDER: Some elements have defined order, others are incomparable.",
    "TOPOLOGICAL SORT: Elements might need to be ordered based on dependencies.",
    "LEXICOGRAPHIC ORDER: Compare element by element, like dictionary ordering.",
    "PRIORITY QUEUE: Process elements in order of priority, not position.",
    "STACK BEHAVIOR: Last-in-first-out processing of elements.",
    "QUEUE BEHAVIOR: First-in-first-out processing of elements.",
    "FIBONACCI-LIKE: The pattern might follow Fibonacci or similar recursive sequence.",
    "ARITHMETIC SEQUENCE: Values might follow arithmetic progression (add constant).",
    "GEOMETRIC SEQUENCE: Values might follow geometric progression (multiply constant).",
    "PRIME NUMBERS: Positions or values at prime indices might be special.",
    "MODULAR ARITHMETIC: Use mod operation to create cyclic patterns.",
    
    # Constraint satisfaction (80-99)
    "SUDOKU-LIKE CONSTRAINTS: Each row/column/region must have unique values.",
    "N-QUEENS CONSTRAINT: No two marked cells can be in same row, column, or diagonal.",
    "GRAPH COLORING: Adjacent regions must have different colors.",
    "EXACT COVER: Select subsets that cover every element exactly once.",
    "BIN PACKING: Fit objects into containers without overlap.",
    "KNAPSACK: Select items to maximize value within capacity constraint.",
    "SATISFIABILITY: Find assignment that satisfies all Boolean constraints.",
    "CONSTRAINT PROPAGATION: Deduce values by propagating constraints.",
    "ARC CONSISTENCY: Each value must be consistent with some value in neighbors.",
    "LOCAL CONSISTENCY: Check consistency in local neighborhoods.",
    "GLOBAL CONSTRAINT: A constraint that applies to entire grid at once.",
    "SOFT CONSTRAINT: Constraints that should be satisfied 'as much as possible'.",
    "PREFERENCE ORDERING: Some solutions are preferred over others.",
    "PARETO OPTIMAL: No improvement on one criterion without worsening another.",
    "MINIMAX: Minimize the maximum of some quantity.",
    "MAXIMIN: Maximize the minimum of some quantity.",
    "NASH EQUILIBRIUM: Each part of solution is optimal given the others.",
    "BALANCED PARTITION: Divide into parts with equal or similar properties.",
    "MATCHING CONSTRAINT: Elements must be paired according to some rule.",
    "FLOW CONSTRAINT: Total flow in must equal total flow out at each node.",
]

# =============================================================================
# SET C: Abstract Thinking & Alternative Perspectives (200-299)
# Focus: Different mental models, creative reframing, unconventional approaches
# Used by: Grok Round 5
# =============================================================================
SET_C_PATTERNS = [
    # Perspective shifts (0-19)
    "THINK LIKE A CHILD: What's the most obvious, simple thing a 5-year-old would see? Sometimes the answer is embarrassingly simple.",
    "THINK BACKWARDS: Instead of 'what transforms input to output', ask 'what makes the output special compared to input?'",
    "IGNORE THE GRID: Forget it's a grid. What if these were instructions? A story? A map? What narrative makes sense?",
    "PRETEND YOU'RE WRONG: Assume your current understanding is completely wrong. What's the OPPOSITE interpretation?",
    "ZOOM OUT: Step back. Don't look at cells - look at the WHOLE picture. What's the overall 'feeling' or 'gesture' of the change?",
    "ZOOM IN: Pick ONE cell that changes. Why THAT cell? What makes it special? Build outward from that single insight.",
    "THE LAZY SOLUTION: What's the MINIMUM effort transformation? The puzzle designer probably chose something elegant, not complex.",
    "WHAT STAYS THE SAME: Instead of focusing on what changes, obsess over what DOESN'T change. That's often the key constraint.",
    "THE PUZZLE DESIGNER'S INTENT: This was created by a human for humans. What concept were they trying to teach or test?",
    "PHYSICAL INTUITION: If this grid were physical objects on a table, what would naturally happen? Gravity? Magnets? Water flow?",
    "ARTISTIC INTERPRETATION: If an artist made this, what were they drawing? What's the 'before and after' of their artwork?",
    "THE COPY-PASTE TEST: Could you describe the output purely in terms of 'copy this, paste there, delete that'?",
    "COUNT EVERYTHING: Count colors, objects, rows, columns, distances. Is there a number that appears suspiciously often?",
    "FIND THE ANCHOR: Is there ONE element that everything else is defined relative to? Find that anchor point.",
    "WHAT'S THE QUESTION: If the input is a question, what question is it asking? The output is the answer to THAT question.",
    "ROLE REVERSAL: What if background is foreground? What if the 'objects' are actually the 'holes'?",
    "TIME DIMENSION: What if this shows before/after of a process? What process? Growth? Erosion? Movement?",
    "MUSICAL THINKING: If cells were notes, what's the melody? Is there rhythm, repetition, harmony?",
    "GAME RULES: If this were a board game, what are the rules? What move was just made?",
    "COMPRESSION/DECOMPRESSION: Is the output a compressed version of input, or vice versa? What's the encoding?",
    
    # Mental model switches (20-39)
    "THE FILTER METAPHOR: Imagine a physical filter over the input. What does it let through? What does it block?",
    "THE STAMP METAPHOR: Is something being 'stamped' onto the grid? What's the stamp? Where does it go?",
    "THE MASK METAPHOR: Is there an invisible mask that determines where changes happen?",
    "THE RECIPE METAPHOR: What's the recipe? List the steps in plain English before coding anything.",
    "THE MIRROR METAPHOR: Where are the mirrors? What's being reflected, and where?",
    "THE SHADOW METAPHOR: Is something casting a shadow? In what direction? How long?",
    "THE ECHO METAPHOR: Is something repeating? Getting fainter? Getting stronger?",
    "THE RIPPLE METAPHOR: Is there a disturbance spreading outward from somewhere?",
    "THE MAGNET METAPHOR: Are things being attracted to or repelled from something?",
    "THE GRAVITY METAPHOR: Which way is 'down'? Are things falling, floating, or rising?",
    "THE INFECTION METAPHOR: Is something spreading like a disease? What's immune? What's not?",
    "THE EVOLUTION METAPHOR: Is this showing generations? What's the 'fitness' being selected for?",
    "THE COMMUNICATION METAPHOR: Is the input a message? What's it saying? Who's the audience?",
    "THE TRANSLATION METAPHOR: Is this translating between two 'languages'? What's the dictionary?",
    "THE VOTING METAPHOR: Are cells 'voting'? Does the majority/minority win?",
    "THE NEGOTIATION METAPHOR: Are different parts of the grid 'competing'? Who wins and why?",
    "THE INHERITANCE METAPHOR: Do children inherit from parents? What gets passed down?",
    "THE RELATIONSHIP METAPHOR: What relationships exist between objects? Siblings? Parent-child? Neighbors?",
    "THE SOCIAL METAPHOR: If objects were people at a party, what social dynamics would explain their behavior?",
    "THE TERRITORIAL METAPHOR: Are objects claiming territory? How do borders get decided?",
    
    # Creative problem-solving (40-59)
    "SOLVE A SIMPLER VERSION: What if the grid were 3x3? Can you solve that and generalize?",
    "SOLVE THE EXTREME CASE: What happens with all zeros? All ones? One cell? The answer might be obvious then.",
    "BREAK THE RULES: What if you ignored one constraint you've been assuming? Does that open up possibilities?",
    "COMBINE TWO IDEAS: Take your two best guesses. What if BOTH are partially right? How would they combine?",
    "THE OPPOSITE APPROACH: Whatever you've been trying, try the exact opposite strategy.",
    "START FROM OUTPUT: Given the output, how many different inputs could produce it? Work backwards.",
    "THE DELETION TEST: Remove each element one by one. Which removal would break the pattern? That's important.",
    "THE ADDITION TEST: What if you added one more object? Where would it go? What would change?",
    "THE SWAP TEST: Swap two objects. Does the output change predictably? That reveals the logic.",
    "THE SCALE TEST: If the grid were 2x bigger, would your solution still work? If not, what's scale-dependent?",
    "THE ROTATION TEST: Rotate the whole problem 90°. Does your solution still make sense?",
    "FIND THE CONTRADICTION: What assumption, if false, would explain why your solution doesn't work?",
    "THE EDGE CASE ORACLE: Focus ONLY on edge cases. Solve those first; the middle usually takes care of itself.",
    "OCCAM'S RAZOR: The simplest explanation is probably right. What's the ONE-SENTENCE description of the rule?",
    "THE ANALOGY HUNT: What's this LIKE? Is it like sorting? Filtering? Copying? Merging? Name the concept.",
    "REVERSE ENGINEERING: Pretend someone else wrote the solution. Read the input/output. What code did they write?",
    "THE INVARIANT HUNT: What property is ALWAYS true in all examples? That's your starting constraint.",
    "THE EXCEPTION HUNT: Is there ONE example that doesn't fit your theory? Focus on understanding that one.",
    "THE SYMMETRY HUNT: Where is symmetry expected but broken? Where is asymmetry expected but present?",
    "THE BOUNDARY HUNT: Where are the boundaries of regions? How are they defined? What happens AT the boundary?",
    
    # Unconventional thinking (60-79)
    "EMBRACE AMBIGUITY: Maybe there are multiple valid interpretations. Which one is most 'elegant'?",
    "THINK IN LAYERS: What if the transformation happens in multiple passes? First pass does X, second does Y.",
    "THINK IN PHASES: Is there a phase transition? Threshold? Critical point where behavior changes?",
    "THINK PROBABILISTICALLY: What if the rule is 'usually X, but sometimes Y'? What triggers the exception?",
    "THINK LOCALLY THEN GLOBALLY: Solve for one small region perfectly, then figure out how to generalize.",
    "THINK GLOBALLY THEN LOCALLY: Understand the overall pattern first, then figure out the local details.",
    "THE NULL HYPOTHESIS: Assume there's no pattern. What would random look like? How does this differ?",
    "THE MAXIMUM ENTROPY VIEW: What's the 'most uncertain' state? How does the transformation reduce uncertainty?",
    "THE MINIMUM DESCRIPTION LENGTH: What's the shortest way to describe the input→output mapping?",
    "THE INFORMATION FLOW: Where does information come FROM in the input? Where does it GO in the output?",
    "THE CONTEXT SENSITIVITY: Does the same local pattern produce different results in different contexts?",
    "THE ATTENTION MECHANISM: If you had to pick 3 cells to look at, which would they be? Why those?",
    "THE SALIENCE TEST: What's the most visually striking thing? That's probably important.",
    "THE BORING PARTS: What's the most boring, predictable part? Ignore that. Focus on the surprises.",
    "THE FIRST PRINCIPLES: Forget everything. If you knew nothing about ARC, what would you guess?",
    "THE EXPERT INTUITION: If you were a world expert in this puzzle, what would be obvious to you?",
    "THE BEGINNER'S MIND: Pretend you've never seen a puzzle before. What patterns jump out immediately?",
    "THE DEBUGGING MINDSET: Your code is probably 90% right. Where's the 10% bug?",
    "THE PATTERN INTERRUPT: You might be stuck in a mental loop. Do something completely different for a moment.",
    "THE FRESH EYES: Describe the puzzle to someone who can't see it. What do you SAY? That's the pattern.",
    
    # Abstract reasoning (80-99)
    "WHAT IS THIS A METAPHOR FOR: Every puzzle is about something. What real-world concept does this represent?",
    "THE COGNITIVE LEAP: What's the non-obvious connection? The 'aha!' insight that makes everything click?",
    "THE HIDDEN VARIABLE: Is there something not shown that you need to infer? A rule? A reference point?",
    "THE GESTALT: The whole is more than the sum of its parts. What emerges from the whole that isn't in any part?",
    "THE FIGURE-GROUND: What's figure? What's ground? Try reversing your assumption about which is which.",
    "THE EMERGENT PROPERTY: Is there a property that EMERGES from the arrangement that doesn't exist in individual cells?",
    "THE CATEGORY SHIFT: You might be categorizing objects wrong. What if you categorized by a different property?",
    "THE LEVEL CONFUSION: Are you solving at the wrong level of abstraction? Go higher or lower.",
    "THE REPRESENTATION MISMATCH: Your internal representation might not match the puzzle's. Try a different data structure.",
    "THE GOAL CLARITY: What EXACTLY is the goal? State it as precisely as possible. Vague goals lead to vague solutions.",
    "THE DECOMPOSITION: Can you break this into completely independent subproblems?",
    "THE COMPOSITION: Can you solve simpler pieces and compose them into the full solution?",
    "THE DUAL PROBLEM: Every problem has a dual. What's the dual of this problem? Is it easier to solve?",
    "THE SYMMETRY BREAKING: Perfect symmetry is boring. What breaks the symmetry? That's the interesting part.",
    "THE CONSERVATION LAW: What's conserved between input and output? Total color count? Object count? Some invariant?",
    "THE TRANSFORMATION GROUP: What group of transformations leaves the solution unchanged? That's a clue.",
    "THE FIXED POINT: Is there something that stays exactly the same? A fixed point of the transformation?",
    "THE ATTRACTOR: If you applied the transformation repeatedly, what would it converge to?",
    "THE INSTABILITY: What small change would completely change the output? That's where the rule's essence is.",
    "THE COMPLETENESS CHECK: Have you considered ALL possible interpretations, or just the first one that came to mind?",
]

# Combine all sets into single list for backward compatibility
MASS_MUTATION_PATTERNS = SET_A_PATTERNS + SET_B_PATTERNS + SET_C_PATTERNS


def get_mass_mutation_pattern(index: int, round_num: int = 0) -> str:
    """
    Get a mass mutation pattern by index with rotation based on round.
    
    Round rotation:
    - Round 0 (Grok 1): Set A patterns (0-99)
    - Round 2 (Grok 2): Set B patterns (100-199)
    - Round 4 (Grok 3): Set C patterns (200-299)
    
    Args:
        index: Pattern index (0-99 within each set)
        round_num: Round number (0, 2, 4 for 100-call rounds)
    
    Returns:
        Pattern hint string
    """
    # Calculate offset based on round
    # Round 0 -> Set A (offset 0, patterns 0-99)
    # Round 2 -> Set B (offset 100, patterns 100-199)
    # Round 4 -> Set C (offset 200, patterns 200-299)
    offset = (round_num // 2) * 100
    actual_index = (offset + index) % len(MASS_MUTATION_PATTERNS)
    return MASS_MUTATION_PATTERNS[actual_index]


def get_set_name(round_num: int) -> str:
    """Get the name of the pattern set for a round."""
    set_names = {0: "A", 1: "A", 2: "B", 3: "B", 4: "C", 5: "C"}
    set_letter = set_names.get(round_num, "A")
    return f"Set {set_letter}"


def build_mass_mutation_hint(pattern: str) -> str:
    """
    Build a mass mutation debugging hint to insert into the prompt.
    
    Args:
        pattern: Refinement-focused debugging hint
    
    Returns:
        Formatted hint section
    """
    return f"""
╔══════════════════════════════════════════════════════════════╗
║              DEBUGGING REFINEMENT - YOU'RE CLOSE!             ║
╚══════════════════════════════════════════════════════════════╝

Your previous attempts may be VERY close to correct. Focus on this specific fix:

{pattern}

Look at your best previous solution and apply this specific debugging check.
The answer is likely a small tweak away from what you already have.

"""
