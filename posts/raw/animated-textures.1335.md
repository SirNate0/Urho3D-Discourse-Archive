gabdab | 2017-01-02 01:06:55 UTC | #1

I create a texture2d vector , then switch texture on material on update .
Is this the best way to achieve textures animation on Urho3D ?

-------------------------

codingmonkey | 2017-01-02 01:06:56 UTC | #2

UV offset animation, you must prepare [b]one big texture atlas[/b] with animation frames for this. 
code maybe look something like this:

[pastebin]gizQdYb2[/pastebin]
for mat details see [urho3d.github.io/documentation/H ... erial.html](http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_material.html)

-------------------------

gabdab | 2017-01-02 01:06:56 UTC | #3

Cool ,thanks .
Movie like animation breaking framerate ?

-------------------------

codingmonkey | 2017-01-02 01:06:56 UTC | #4

>Movie like animation breaking framerate ?
I think yes. Old-style tech animation like drawed with pencil flying bird on corner of the book.

and if you needed animation in 2D for this there are exist special 2d urho stuff, like AnimatedSprite2d and so on... there are some modern tech are using for animation.

-------------------------

Mike | 2017-01-02 01:06:56 UTC | #5

Apart from using AttributeAnimation, this can also be made at the shader level.

-------------------------

codingmonkey | 2017-01-02 01:06:56 UTC | #6

> this can also be made at the shader level.
You mean if use custom Uniforms, and calculate UV in vertex shader ? Yes I guess this will be best method. But need some knowledge with shader tweaking.

-------------------------

gabdab | 2017-01-02 01:07:01 UTC | #7

..full option .

-------------------------

