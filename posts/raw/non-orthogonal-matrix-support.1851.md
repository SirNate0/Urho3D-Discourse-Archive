cheese54 | 2017-01-02 01:10:43 UTC | #1

Hello, Urho3d (as many game engines around) defines object transform throught position, rotation and scale, this is very limiting from my perspective, advanced animation techniques require full controll over the object's matrix, although it is not of immediate use in usual game development , removing that limitation would open the doors to new possibilities

-------------------------

cadaver | 2017-01-02 01:10:43 UTC | #2

Welcome to the forums.

If you go low-level enough, using the Graphics class directly, you can build your own scene graph and rendering architecture which can feed whatever data to the shaders you want.

To support arbitrary matrices in the scene graph would require that the pos/rot/scale operations continually decompose the object's local matrix, which would imply worse performance for the usual "game" use cases. Therefore it's unlikely to appear in the engine's built-in scene model.

-------------------------

cheese54 | 2017-01-02 01:10:43 UTC | #3

thanks for the prompt response, one way to implement it without continually decomposing the object's local matrix is to add an additional 3x3 matrix to the current pos/rot/scale parameters, another way is to add shear/skew parameters (as Adobe Flash does),, but i understand that adding those parameters to the entire scene graph model of urho3d will result in an increase in memory and a decrease in performance. 
i will find another way to do what i am trying to do

-------------------------

