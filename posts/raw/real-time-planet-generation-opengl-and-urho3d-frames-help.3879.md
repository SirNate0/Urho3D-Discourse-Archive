vivienneanthony | 2017-12-24 19:21:42 UTC | #1

Hi

Im trying to implement real time procedural planet code which uses shaders for computation. Partially its working but Im stuck. 

How can I implement a different framebuffer and let the code switch beween Urho3D default and another? Do I have to rewrite the Shader and ShaderProgram or add some framebuffer detection? Where do I have to add post frame code to update the backend or other frame buffer, so geometry or other data can be copied to urho geometry?

The base code is in place but I think missing a few things. I want to get it running then modify.

Viv

-------------------------

vivienneanthony | 2017-12-24 19:30:24 UTC | #2

I'm looking to implement. Something like

https://youtu.be/rL8zDgTlXso

-------------------------

Bananaft | 2017-12-26 15:44:23 UTC | #3

Hi, your question is a bit confusing. What you need different framebuffer for? To render heightmap into it? Or you want like two viewports each showing same or different planet? Can you describe in more detail waht you want to make and what goes wrong with it?

-------------------------

orefkov | 2017-12-26 19:00:55 UTC | #4

Perhaps you must more detailed learn render pathes?

-------------------------

vivienneanthony | 2017-12-28 21:26:31 UTC | #5

The framebuffer would be used to generate position and heightmaps for real time processing and creating geometry detail data which is faster.

In detail, a basic topology is generated and passed onto the GPU that creates a position map using perlin noise for faster processing. Once the information is produced a accurate height map is generated on the GPU side. The CPU creates enougth information for physics but the GPU does the heavy work to create larger geometry using camera position.

The code I have uses quadtree format. Each side of a cube has a node. Each node has a member NW, NE, SW,SE with a topology patch. Depending on camera decision each node can be subdivided by four.  There is a hard limit of the number of splits.  I'm looking at a default split no matter the camera (server side), on the client (x number of split max).


As to what I with the help of another programmer. We are looking to implement this system in a client/server environment. Basic topology is created on a need be basis on a server and client but on a client details are made for visual expects.

A pdf of the process is here https://drive.google.com/open?id=1pMkiKikuD0tkTFc0e7S-olPw2-dfKPrm and sample source is https://drive.google.com/open?id=11s1bQOC9P4nalZSUBBCG1arTXg1Vzte1

I think it used the GPU/CPU very different then Urho3D graphic system and the demo code is opengl so it requires a bit of work but if the results is close to the video. It would be a huge plus.

So far I made addition Urho3D backend could for OpenGL and a new Vector3<type> meaning type=unsigned int in some additional code and hopefully pull into the code advance math libraries more towards sciencetific.

Vivienne

-------------------------

JTippetts | 2017-12-29 08:30:02 UTC | #6

I did a quick skim of the project source and PDF in question, and it looks like they're generating the actual vertex geometry on the CPU, but they also generate a heightmap texture (mimicking the technique used on the CPU to generate the geometry, as a fragment program) and normalmap texture to be used for coloration and lighting. These heightmap and normalmap textures are created using basic render-to-texture; the texture is bound as the render target, a vertex and fragment shader are bound, and a full-screen rectangle is drawn to fill the texture with data. This is easily enough done in Urho3D, as shown in the [Render to Texture Sample](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/10_RenderToTexture/RenderToTexture.cpp).

-------------------------

vivienneanthony | 2017-12-30 05:12:20 UTC | #7

I tried that method. There was a issue with how the recursive nature of the quad tree is working with the code we have. Issue 1 we are having. The only and primary difference is directly using opengl and a shader without using the technique xml. Issue 2 we are having.

-------------------------

JTippetts | 2017-12-30 15:22:12 UTC | #8

I've read this reply a couple times, but I'm just not getting what you're trying to say.

If you have quad-tree recursion issues, that's really not a problem on Urho3D's end. Once you fix those issues, you should be able to lock your geometry vertex buffers and upload vertex data, just as you would using base GL calls, only using the Urho API to avoid GL dependency.

The only real potential issue I see is ensuring that the heightmap and normalmap textures are created only once, at app startup, rather than being updated every frame. Once you figure out that part, and debug your quadtree recursion issues, you should be golden.

-------------------------

coldev | 2018-01-01 18:16:36 UTC | #9

No mans sky .. 

create a new Urho3d spherical terrain C++ Class   :star_struck:

[Video Spherical Terrain](https://www.youtube.com/results?search_query=spherical+terrain)

-------------------------

vivienneanthony | 2018-01-09 23:59:02 UTC | #10

I'm trying. :-/ I decided to take some old code I did that created a sphere and change that to fit the procedural planet part while adding features.

-------------------------

coldev | 2018-01-11 16:24:13 UTC | #11

Lumak writes nice code for you...

[Spherical Phys](https://discourse.urho3d.io/t/spherical-and-cubic-world-physics-samples/2703)

[Cilinder Phys](https://discourse.urho3d.io/t/cylinderical-level-inspired-by-nier-automata/2892)

-------------------------

vivienneanthony | 2018-01-19 03:32:07 UTC | #12

That's pretty awesome.  

I left a message on a minor issue I had getting a face to show. 

I sucessfully created a model Sphere(planet hopefully) before. https://imgur.com/a/jpGMw

Now I'm trying to convert it to a more node-patch-topology friendly code structure similiarly to how terrain and terrainpatch works. Which fails. I think I'm missing something for the patch code which uses a face. Failing as in not rendering.

So I'm thinking something is missing.

-------------------------

