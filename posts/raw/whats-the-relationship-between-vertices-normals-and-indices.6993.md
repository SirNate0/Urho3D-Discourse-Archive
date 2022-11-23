TonyHack | 2021-09-15 03:36:10 UTC | #1

I'm confused by 3D model structure ,
In opengl , one vertex is mapped to one normal , however , in 3d model , the polygon is constructed by index buffer , 

then the question is ,  if we use index buffer  , some vertices will be indexed more than once obviously ;
is it correctly the normal will be indexed more than once  or  the normals are different in different polygons even they share the same vertices ?

if the normals are different , how could i design my buffer structure in openGL

-------------------------

SirNate0 | 2021-09-15 11:11:40 UTC | #2

If the normals are the same (face smooth shading in Blender) then multiple faces can reuse the same vertex, including the normals. If the normals are different (e.g. the face flat shading in Blender) then you have to have multiple vertices in the buffer - they will have the same position but different normals. The same sort of setup applies to the other vertex elements like vertex colors.

-------------------------

TonyHack | 2021-09-16 06:48:26 UTC | #3

i tried in this way ,  but it's a waste of memory

-------------------------

SirNate0 | 2021-09-16 10:10:53 UTC | #4

It does waste some memory, yes, but I don't think there's any way around it. Keep in mind that if you had separate buffers for the different elements you would have to have multiple index buffers as well in order to realize the memory savings. And as far as I know, that isn't supported (at least in Urho. Perhaps in native OpenGL/Direct X it is, but I'm not sure).

-------------------------

ToolmakerSteve | 2021-12-01 19:31:18 UTC | #5

If the normals are different, then it is a different vertex - when it is sent to the gpu. This is fundamental to gpu pipelining.

A gpu has many cores; design trade-offs are made (regardless of the game engine or whether opengl/directx) so that all the cores can work independently. Sometimes this means "wasting" memory, so that the vertices are independent of each other. This is one of those situations.

------------------------------------

OTOH, its possible (in theory) to have a "source" representation of a model that is more compact. Then do any needed "inflation" when sending the model to the gpu (e.g. a transition to a new scene). 

This would use same gpu memory, but less memory in external storage and in cpu model cache. I don't know what's available to help with such an approach.

-------------------------

