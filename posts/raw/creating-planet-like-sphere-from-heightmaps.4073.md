the_little_guy | 2018-03-04 18:15:49 UTC | #1

It's my first post on the forum so I want to say hello to all.

Moving onto my problem, I want to create a planet object using 6 heightmaps arranged in the cube-like structure and mapped to sphere as described in the article [Mapping a Cube to a Sphere](http://mathproofs.blogspot.com.au/2005/07/mapping-cube-to-sphere.html).
 What I would like to know is whether I will have to reimplement some parts of Terrain class or is it possible to do this manipulating some of its data / using other existing features. I haven't seen a definitive answer to the question on the forum. I don't want to waste too much time looking into a solution that might be a dead end so if there is a different, simpler way to reach the same effect, please let me know.

-------------------------

Modanung | 2018-03-04 16:59:40 UTC | #2

Have you seen @vivienneanthony's work? 
https://discourse.urho3d.io/t/custom-terrainpatch-detailed-help/3929/

Also, welcome to the forums! :confetti_ball:

-------------------------

the_little_guy | 2018-03-04 18:20:41 UTC | #3

Thanks for the answer :). 
Yes, I have seen @vivienneanthony’s work, but from what I understand, he has rewritten Terrain class to support cube to sphere mapping (mind you - I'm new to Urho3D and might be wrong). Optimmally, I would like to do this without having to understand the inner workings of the library - 3D simulation is just a part of my project. I have raised the question because in the reported issue [Creating a quad cube planet!](https://github.com/urho3d/Urho3D/issues/1801) @Lumak has written something about the method.

-------------------------

Sinoid | 2018-03-04 20:05:01 UTC | #4

That's not possible without modifying the terrain class.

It only supports a single-axis of displacement so even using the RG 16-bit encoding you won't get a spherical result out of it. Most of its' *support* functions (normals and the like) are also written with the assumption of a heightmap so all of those are now meaningless.

Vertex-shader fudgery to push out the vertices along the face tangent is fudgery and will not work even just for rendering as your patch bounding boxes will be incorrect- nevermind the other issues when you have to deal with collision.

Even if you fudge things to make it work .. you'll already be in there making changes to make the fudgery work so you might as well as deal with it appropriately from the get-go. It's a specialized task.

-------------------------

Lumak | 2018-03-04 20:07:13 UTC | #5

I didn't write anything with the cube-to-sphere conversion, just merely linked what I thought was more direct method using a mathematical conversion compared to the other programmatic approach.  The following cubed terrain picture was just rotation of the nodes for each terrain to shape it into a cube. And I didn't keep any of that code.

-------------------------

the_little_guy | 2018-03-04 21:26:51 UTC | #6

Yeah, I feared that would be the answer :( . Well, I will probably start with trying to understand @vivienneanthony’s work. Nevertheless, thanks again for quick response.

-------------------------

vivienneanthony | 2018-03-05 04:23:06 UTC | #7

[quote="the_little_guy, post:6, topic:4073"]
Yeah, I feared that would be the answer :frowning: . Well, I will probably start with trying to understand @vivienneanthony’s work. Nevertheless, thanks again for quick response.
[/quote]

You can check out the document pdf in https://www.dropbox.com/s/7wlaewgc64ruenx/Procedurus_Source.zip. Right now I'm working with during it using no shader then shaders.

As mentioned, its my work in progress. In some ways a working version would be awesome. Maybe a little game changing. Although some of the code might look similiar to Urho3D Terrain and TerrainPatch. This is a different beast technically. The physics part I think would work the same but the visual part would be different. Since, a working version can possibly lead to planet size Terrain. I think it changes a lot in how Urho3D would handle showing distance.  I can better describe it but check out the pdf because it explains a lot.

-------------------------

