ppsychrite | 2017-05-28 14:39:41 UTC | #1

From the Dynamic Geometry Sample at when it makes the 3d triangle it only uses Normal Coordinates and Vertex Coordinates. 
     
What I want to do is make a custom object that can set a texturemap so that wrap around some polys.
(Like this for example: http://i103.photobucket.com/albums/m143/WarKirby/fig1-1.jpg)
Is Urho3d's custom geometry able to do this?

-------------------------

cadaver | 2017-05-26 10:49:46 UTC | #2

The CustomGeometry component itself can only define single 2-dimensional UV's, by using DefineTexCoord() function for each vertex.

If you define vertex / index buffers yourself, like the dynamic geometry example "from scratch" part does, you could define your vertex declaration just like you want, for example using multiple UV's, 3D UV's etc.

-------------------------

ppsychrite | 2017-05-26 11:13:25 UTC | #3

Thank you! After looking into it, I think the custom geometry class is what I'll need :grinning:

-------------------------

slapin | 2017-05-26 11:24:57 UTC | #4

I wonder if anybody have the example on what are possibilities with vertex/index buffer.
This topic is not quite documented. I guessed some things around, looked-up some things in AssetImporter,
but that all doesn't make single picture. What I'm mostly interested in is relation between
Model, Geometry and Vertex/Index buffer. Some combinations do not work, i.e. one can't have lod vertex buffer separate. There are many such examples. Because of that procedural generation of assets is very painful thing,
as it does have too much of trial and error. There are people who understand this stuff, but they are silent.

For example, I try to split Model in 2 using some criteria, this looks like insane task, as I don't know too many things,
like how bone transforms are represented, how morphs are represented, the limitations (4 boneindices per vertex), etc.
Another thing is generating model with LODs - what are relations of LOD geometries with normal geometries,
can I have LODs in separate IBs or they should be the same, etc.
So as I see somebody written all this cool stuff and forgot all about it and now somebody else need to guess it all out,
like archaeologists guessed Egypt hieroglyphs before Rosetta stone was found. But there is no Rosetta stone for this case.

-------------------------

ppsychrite | 2017-05-26 16:19:33 UTC | #5

If I get something working with CustomGeometry I'll get back to you. :wink:

-------------------------

ppsychrite | 2017-05-27 01:27:01 UTC | #6

What's the correct way of doing it?
(EDIT) It turns out I defined it counter clockwise so it appeared the wrong way. My bad. :stuck_out_tongue:

-------------------------

ppsychrite | 2017-05-27 01:39:44 UTC | #7

After a while I found a good way to do it.
Only problem is the fact that the color is gray for some reason and when you move your camera above it it turns black. :confused:

    node = scene_->CreateChild("Triangle");

	ur::CustomGeometry *geometry = node->CreateComponent<ur::CustomGeometry>();
	geometry->BeginGeometry(0, ur::TRIANGLE_LIST);

	geometry->DefineVertex({ 0,0,0 });
	geometry->DefineTexCoord({ 1,0 });
	geometry->DefineColor({ 255,0,0 });

	geometry->DefineVertex({ 10,0,0 });
	geometry->DefineTexCoord({ 0,1 });
	geometry->DefineColor({ 255,0,0 });

	geometry->DefineVertex({ 10,10,0 });
	geometry->DefineTexCoord({ 0,0 });
	geometry->DefineColor({ 255,0,0 });

	geometry->Commit();

After I did that, voila! It loads! http://prntscr.com/fckn0w
Don't know how to fix the colors though

-------------------------

Modanung | 2017-05-28 14:39:18 UTC | #8

[quote="ppsychrite, post:7, topic:3163"]
...when you move your camera above it it turns black.
[/quote]
Might be a normals issue. Try `DefineNormal`.

[quote="ppsychrite, post:7, topic:3163"]
Don't know how to fix the colors though
[/quote]
When using vertex colours, the geometry should have a `VCol` technique applied to it for the colours to show up.

-------------------------

ppsychrite | 2017-05-27 15:07:52 UTC | #9

What Vector3 value should the Normals be?
Because right now I do
    geometry->DefineNormal({0,0,0});
It sets the triangle to black no matter what color I set the vertex to

-------------------------

Modanung | 2017-05-27 15:20:15 UTC | #10

Basically anything but all-zero. ;)
It should preferably be a normalized vector (hence the name), which means it should have a length of 1. In most cases you'll want it to be perpendicular to the surface, pointing out. In the [DynamicGeometry](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp#L204-L217) sample the normals are calculated after the vertex position data is collected.

-------------------------

ppsychrite | 2017-05-27 15:25:18 UTC | #11

Is there a way of getting the normalized vector?
Setting it to ({1,1,1}) for time's sake doesn't seem to work either.

-------------------------

Modanung | 2017-05-27 15:27:44 UTC | #12

You can call `Normalize` or `Normalized` on a `Vector3`.

-------------------------

ppsychrite | 2017-05-27 15:55:31 UTC | #13

Even with that it's still a black triangle. :neutral_face:

    node = scene_->CreateChild("Triangle");

	ur::CustomGeometry *geometry = node->CreateComponent<ur::CustomGeometry>();
	geometry->BeginGeometry(0, ur::TRIANGLE_LIST);

	geometry->DefineVertex({ 0,10,0 });
	geometry->DefineNormal(GetNormal({ 0,10,0 }));
	geometry->DefineColor(ur::Color::GREEN);
	
	geometry->DefineVertex({ 10,0,0 });
	geometry->DefineNormal(GetNormal({ 10,0,0 }));
	geometry->DefineColor(ur::Color::RED);


	geometry->DefineVertex({ 0,0,0 });
	geometry->DefineNormal(GetNormal({ 0,0,0 }));
	geometry->DefineColor(ur::Color::BLUE);
	
	geometry->Commit();

Function I'm using: 

    ur::Vector3 GetNormal(ur::Vector3 vector){
	ur::Vector3 normal = vector;
	normal.Normalize();
	return normal;

    }

-------------------------

Modanung | 2017-05-27 20:23:22 UTC | #14

Since your triangle is defined within the XY-plane the normal should either be 0,0,1 or 0,0,-1.

-------------------------

ppsychrite | 2017-05-27 21:49:03 UTC | #15

Neither of those vector3s show the color either but if it helps, 0,0,1 makes the vertex black and 0,0,-1 makes the vertex grey.

-------------------------

Modanung | 2017-05-28 04:31:27 UTC | #16

[quote="ppsychrite, post:15, topic:3163"]
Neither of those vector3s show the color either...
[/quote]
Like I said, for the _vertex colours_ to show you'll need to assign a material that uses a **VCol** technique.

-------------------------

ppsychrite | 2017-05-28 14:38:11 UTC | #17

Ah I didn't know what you mean't at first.
Assigned material VColUnlit.xml and it worked perfectly!
Thanks man

-------------------------

Modanung | 2017-05-28 14:45:01 UTC | #18

[quote="ppsychrite, post:17, topic:3163"]
Thanks man
[/quote]

_You're welcome!_ :)

-------------------------

ppsychrite | 2017-05-29 18:43:01 UTC | #19

Also, sorry for changing the subject but I didn't think it would be a good idea to post tons of threads onto a subforum.

Lighting doesn't seem to work with it.
Here's a few rectangles I've drawn: http://prntscr.com/fdiheu
There is lighting been shown at them but no shadows show and the edges aren't visible. 
Incase it was just a lighting glitch I also tried red lighting: http://prntscr.com/fdiins
That doesn't work either.
The normals are calculated correctly, too, I believe so I don't know the issue

-------------------------

lezak | 2017-05-29 19:29:47 UTC | #20

It's because You're using unlit material. I don't think that there is build in lit material with vertex colors, You have to create new one using one of the VCol techniques

-------------------------

ppsychrite | 2017-05-29 19:36:13 UTC | #21

Oh yeah I'm using VColUnlit.
How would I go around to making VColLit?

-------------------------

lezak | 2017-05-29 19:48:53 UTC | #22

There already are several techniques with VCol in folder "CoreData/Techniques", just pick one and make new material using this technique.

-------------------------

ppsychrite | 2017-05-29 20:05:51 UTC | #23

One of them worked, thank you.
While there's some issue where LIGHT_DIRECTIONAL isn't affecting it but LIGHT_SPOT is, I think I can find a way to fix it.

-------------------------

