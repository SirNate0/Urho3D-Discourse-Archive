anako126n | 2017-01-02 01:04:03 UTC | #1

I have been trying to search/figure out how to interact with 3D model through code without any luck. Lets say I have a board with a frame and some fields. Position of these fields changes depending on texture loaded. A simple example would be chess board and pawn on top of it.

How should I get the coordinates of face below the field to place another model on top of it? I have been thinking about defining the coordinates of field position in texture, and than finding model vertices related.

How can i get texture coordinates from static model?  Maybe a solution already exists to find a polygon under a specific point of texture?

Any help on this problem would be greatly appreciated!

-------------------------

thebluefish | 2017-01-02 01:04:03 UTC | #2

A 3D model is just some art, nothing more. While you could technically pull various data from it, that's not what they're for and you're going to have a bad time.

Instead you would want to export some data alongside your model. For your chessboard example, I would center the board around origin (0,0,0), and then separately define the cell size, offset, and layout. In my code, I could then build the chess grid using some simple information. Placing the pawn then becomes a simple matter of looking up the coordinates for what space I want to put it on, and then creating the pawn node at that coordinate

-------------------------

anako126n | 2017-01-02 01:04:03 UTC | #3

Thats really helps. Never though of it that way. Seems to be really easy solution for a chess board. 

However, what if we would take a chest as an example. One model and several areas for interaction (e.g. key hole, 4 latches) Where each latch could act differently on the chest, findind where did we touch isnt a problem, the question is which part of texture was actually in the touch.

I could define parts in texture (e.g point 20,20 to 40,40 is a latch no 1., in other case 35,20 to 55,40 is a latch no 1), they can vary (the same model, different texture means different places)

I have been thinking about such solution in this case.

Create a chest model, add 4 polygons (seperate models), export it from maya. Load the model into a StaticModel it would give me a model with 5 geometries, 4 of them would represent the transparent polygons and 5th one a visible model. Can i somehow pull the geometries by names as named in maya? Looking at the *.mdl file i dont think so as the names of meshes arent exported. I could still base on the amount of vertices to find related geometries, however it still doesnt sort the problem of latches order. 

I really dont want to over complicate the problem, but i cant seems to figure it out. I get your idea, cant think how to apply it in this case. would defining an offset from the center and size of each latch for each texture be the easiest solution?

-------------------------

