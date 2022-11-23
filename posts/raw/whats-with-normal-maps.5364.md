GoldenThumbs | 2019-07-29 21:21:27 UTC | #1

So I was working on a new PBR shader, and I noticed that the lighting looked off due to normals. I was like "Ok, must be the wrong form of normal map." And I tried a different orientation of normal map. Same issue, just looks slightly different. "Ok, maybe there's some special orientation Urho uses". I made 4 different normal maps with different channels flipped. None looked right. It looks like the red and green channels are swapped. Nothing I've come across before swapped the channels like this. Typically green is top/bottom and red is left/right. Looks like red is supposed top/bottom and green left/right. I also tested this with standard workflow shaders that come with the engine and I got the same result. Am I doing something wrong or is it just that Urho does things weirdly? Maybe an engine issue with my version that messes with world or object space positions? It's not customized in any way so this is really confusing me. I even looked at the normal maps that are already in the engine for reference.

-------------------------

SirNate0 | 2019-07-29 22:42:21 UTC | #2

Not sure what the issue might be, and I certainly don't know enough about normal map conventions to say anything about that. You do have vertex tangents exported, right? Other than that, perhaps the section on normal maps here will help [https://urho3d.github.io/documentation/HEAD/_materials.html#Materials_Textures](https://urho3d.github.io/documentation/HEAD/_materials.html#Materials_Textures)

-------------------------

Modanung | 2019-07-30 00:50:27 UTC | #3

Maybe @extobias could [shine a light](https://discourse.urho3d.io/t/random-projects-shots/2431/119?) on this?

-------------------------

GoldenThumbs | 2019-07-30 02:45:32 UTC | #4

So, uh... I found out that the plane mesh that comes with Urho3D doesn't have tangents exported with it. Exported a new plane from blender and it fixed it.

-------------------------

Modanung | 2019-09-05 10:23:16 UTC | #5

### *It's polling time!* :memo: 
Do *you* think the default **plane** model that comes with Urho3D should contain tangent information?
[poll type=regular results=always public=true]
* Yes
* No
* Yes, but as a *separate* model file
[/poll]

-------------------------

extobias | 2019-07-30 03:12:53 UTC | #6

I have arrived late, I'm glad that solution was found :slightly_smiling_face:

-------------------------

Dave82 | 2019-07-30 15:40:06 UTC | #7

Please note there is a generateTangents function defined in tangent.h which can be used to generate tangents on the fly for any vertexbuffer.  I consider tangents as optional data so i generate them if needed.

-------------------------

