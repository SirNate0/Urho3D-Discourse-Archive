friesencr | 2017-01-02 01:05:03 UTC | #1

I didn't even notice we didn't have IntVector3.

-------------------------

GoogleBot42 | 2017-01-02 01:05:03 UTC | #2

I would like this too :slight_smile:

-------------------------

cadaver | 2017-01-02 01:05:03 UTC | #3

Can you describe where you would need it? Just want to understand the use case. Minecraft? Historically we have IntVector2 for handling pixel-sized 2D UI elements, screen resolutions etc.

-------------------------

friesencr | 2017-01-02 01:05:04 UTC | #4

I am implementing a voxel system.  I have three sets of ints and it is working just fine.  I am trying to match as much of the API to the terrain system.  I can see having it might causing more confusion than it is worth.

-------------------------

GoogleBot42 | 2017-01-02 01:05:04 UTC | #5

[quote="cadaver"]Can you describe where you would need it? Just want to understand the use case. Minecraft? Historically we have IntVector2 for handling pixel-sized 2D UI elements, screen resolutions etc.[/quote]

Yep.  A minecraft clone is exactly why I want it.  Casting between types makes the source code harder to read and in cases when I am not passing this vector to the urho3d engine the casting is causing the code to run slower due to unneeded conversions. :slight_smile:

-------------------------

cadaver | 2017-01-02 01:05:04 UTC | #6

The only real problem I see with it is that because the engine itself doesn't have any use for it, it would be a largely untested class (except by client applications). On the other hand, I don't like the idea of adding overloads to eg. Node::SetPosition(), as internally the scene graph uses floats.

-------------------------

sabotage3d | 2017-01-02 01:05:05 UTC | #7

It might be an overkill but wouldn't templatization of the math library solve this issue ?

-------------------------

cadaver | 2017-01-02 01:05:05 UTC | #8

Templating to choose between float and double for example would make quite a lot of sense. Templating between float and int is somewhat ugly as you get operations like normalization that won't work correctly with ints.

-------------------------

