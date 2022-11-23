yushli | 2017-01-02 01:08:22 UTC | #1

I can't find the APIs in the document. Thanks in advance.

-------------------------

yushli | 2017-01-02 01:08:22 UTC | #2

A little bit more specific. That is, how to support the background moves toward one direction while keep repeating? like simulating a plane flying in the dark sky with some stars. the plane is still, and the dark sky keeps moving backwards.

-------------------------

codingmonkey | 2017-01-02 01:08:22 UTC | #3

>I can't find the APIs in the document
[urho3d.github.io/documentation/H ... tated.html](http://urho3d.github.io/documentation/HEAD/annotated.html)

-------------------------

Bananaft | 2017-01-02 01:08:23 UTC | #4

Dejavu: [post6616.html?hilit=background%20repeating#p6616](http://discourse.urho3d.io/t/solved-how-to-make-a-2d-repeating-background/1096/3%20repeating#p6616)

-------------------------

yushli | 2017-01-02 01:08:23 UTC | #5

Thanks for the remaining. The reason I asked again is that I managed to find a simpler way by calling StaticSprite2D::SetRectangle(deltaX,deltaY, textureWidth+deltaX,textureHeight+deltaY) and calculate the delatX and delatY by the time step in scene update. That way it works as expected to have the texture moves and repeats. But not in a smooth way. The move is sometimes slow and sometimes fast. I wonder whether calling SetRectangle is the same to using Material uv transform or in a less efficient way. I am still learning urho3d so a sample code on how to add material and perform the uv transform to staticsprite2d is highly appreciated.

-------------------------

1vanK | 2017-01-02 01:08:23 UTC | #6

Just create textured plane (or node with child nodes if you want more than one plane) and move it in the scope of the camera. If the texture has a small size you do not need to create a lot of planes, but tuning UOffset and VOffset in material for repeating.

-------------------------

yushli | 2017-01-02 01:08:23 UTC | #7

Do you have sample code on how to use material to animate the uv values?

-------------------------

Bananaft | 2017-01-02 01:08:23 UTC | #8

[quote="yushli"] But not in a smooth way. The move is sometimes slow and sometimes fast.[/quote]
So that's your actual problem here?
Is this change of speed fps-dependent? Are you sure, you are using timeStep right? What happens if you turn on vsync?

-------------------------

1vanK | 2017-01-02 01:08:23 UTC | #9

[quote="yushli"]Do you have sample code on how to use material to animate the uv values?[/quote]
This question was asked to me? My way is not using UV animation :) But you can see the UV animation in the Water shader

-------------------------

