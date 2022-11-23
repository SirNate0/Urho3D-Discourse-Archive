DavTom | 2017-01-02 01:12:16 UTC | #1

Start with a texture image (with [u]multiple paths[/u] e.g. [color=#0000BF]path1 [/color]is a list of Vector2 coordinates). Along each path is a [color=#0000FF]2D sprite[/color] (e.g. Circle or diamond shape). The texture image will be mapped onto a plane as in the sample "RenderToTexture". When user click on the[color=#0000FF]2D sprite[/color] (which could be a circle or diamond shape sprite placed on top or drawn) on the texture image, the [color=#004080]sprite[/color] move along the e.g.  [color=#0000BF]path1 [/color] along the polygon line defined by the list of Vector2 coordinates. I am not sure if this animation could be achieved in similar way as the sample MaterialAnimation. 

Urho2D Question(1):
How to use Urho2D to draw vector graphics (e.g. polyline, filled polygon diamand 2D shape onto a Texture Image? Please point to Forum discussion. 

MaterialAnimation Question(2):
For each user click on 3D space on the Plane, the 3D coordinate is mapped onto the 2D coordinate of the 2D texture. If the click position corresponds to one of the 2D sprite or 2D vector polygon, a callback event is triggered that the final position (P2) and the path which the sprite (e.g. sprite2) will follow (e.g. Path1) will be retrieved from a database.

How could we create e.g. ValueAnimation or perhaps something else, to pass the information of the new coordinate position for sprite2 to move along  e.g path1 at each frame?



MaterialAnimation Question(3):
Is there something similar to Material.SetShaderParameterAnimation that will accept paramters ( sprite to move (sprite2), coordinate for each frame). 

[b][color=#008000]Would the community think this is a useful "use case" to combine Urho2D and Urho3D in way as describe above to add new features to the already fantastic Urho framework?[/color][/b]
 
Perhaps something similar has been discussed as I just started to learn Urho and I have not read all the forum discussion. Please point me to the relevant forum links. Thnx.

-------------------------

cadaver | 2017-01-02 01:12:16 UTC | #2

You can use the SplinePath component or simply set a ValueAnimation to a scene node's Position attribute to move a node along a path.

Urho2D's purpose is sprite and tilemap drawing. We don't have dedicated existing functions to draw vector graphics to textures, but there are ways to do that on your own:
- Plot the pixels on the CPU to an Image, then SetData() to the texture.
- Use Graphics class to perform drawcalls into a texture rendertarget. This requires using C++.

For the engine official repo itself, I prefer simple examples that demonstrate one thing. But there's nothing stopping you publishing combined examples elsewhere.

-------------------------

DavTom | 2017-01-02 01:12:16 UTC | #3

Thnx cadaver, the combination of SplinePath and ValueAnimation is most likely what I need. Instead of drawing vector graphics, I could turn the vector graphics into sprite images and use that for moving along the SplinePath. I will see if I could figure enough to try this using the MaterialAnimation sample. Thnx for your valuable feedback.

-------------------------

DavTom | 2017-01-02 01:12:16 UTC | #4

Do we have a shared code on 3D paint similar like this found on ogre3D [Squamster-Mesh viewer/painter ]?
[url]http://www.ogre3d.org/forums/viewtopic.php?f=11&t=46297&start=75[/url] or something [url]https://www.youtube.com/watch?v=D_6jgMJNceQ[/url]

-------------------------

