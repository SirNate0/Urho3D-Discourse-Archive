kanneblei | 2017-01-02 01:15:00 UTC | #1

TL;DR: Is there a way to get vertex group names from loaded Models?

Right now I have an idea for a game that will involve basically joining different models based on character parameters.
I would have a "library of body parts" and the models should be composed at load-time, because they can pretty much be any assembly of different parts.
The idea is to have clues from the modelling software embedded on the object data, I was thinking of named vertex groups.

As an example, think about Skyrim. Suppose we have a single Mesh for the torso of all humanoid characters. At the base of the neck we create a vertex group with a known shape, and we name that group something useful, like "Head.Connection". Now, for the different races, we have just models of the heads with a vertex group with the same name and of the same size, and we sew those together at load time.

I've read the dynamic geometry example, which was greatly enlightening towards that goal, but while it modifies the raw vertex data from the geometry, it does not actually assemble different geometry via connections.
The problem is I cannot figure out how to get the vertex group names from the models.

I took a look at the APIs for Model, Geometry and some other classes, trying to figure out if I could grab a vertex group name from it, but could not find that info.
I don't know if this is a limitation form assimp or Urho's API.
What I did see was that when exporting from blender to wavefront (.obj) it did list a group (line that was like "o Head.Vertices"), though I might have done something wrong and it didn't seem to have any vertices within.

Another possibility I was thinking about is using the scene graph to compose the objects, and loading the connection information from a json or xml file. But this would be kind of a pain to do by hand, and it seems like it would not allow for a proper mesh-deforming skeleton, please correct me if I'm wrong here.

Anyway, any insight is greatly appreciated!  :smiley: 
Lucas

-------------------------

rbnpontes | 2017-01-02 01:15:00 UTC | #2

If i'm understand what did say, you need a Customization Character in runtime, i have this problem when i'm working in unity, because i'm loaded realtime meshes at the Objects.
In urho its possible but is more complicated, First you need all Objects has a bone and rig for Sync parts and deform at realtime, or you modify vertex by runtime, anyway what you need is more complicated. Look around in the source code of mesh in Urho3d, try First to generate geometry at runtime for understand urho.
In urho3d exists a CustomGeometry component in order to facilitate a generation of mesh, i have created a code for make the work of generation, but the diference is, my code Will export generated models, CustomGeometry no.
[url]http://discourse.urho3d.io/t/mesh-generator/2361/1[/url]
Good Lucky with your project, and sorry for the english

-------------------------

kanneblei | 2017-01-02 01:15:00 UTC | #3

Thanks for the quick reply! 
I had found your code, and I didn't think it solved my entire problem, but can't remember what was the issue. I'll take a second look.

I found this promising thread outside the forums:
[github.com/urho3d/Urho3D/issues/470](https://github.com/urho3d/Urho3D/issues/470)

I'll try it out later today if I can

-------------------------

