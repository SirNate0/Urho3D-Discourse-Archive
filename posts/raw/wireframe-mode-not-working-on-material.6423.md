btschumy | 2020-10-08 20:28:21 UTC | #1

I and trying to draw some nodes using the "wireframe" fillmode.  It doesn't seem to be working for me.  Here is my C# code:

		private void CreateStellaHaloNode()
		{
			stellarHaloNode = universeNode.CreateChild();
			stellarHaloNode.Scale = new Vector3(130000.0f, 130000.0f, 130000.0f);

			var haloComp = stellarHaloNode.CreateComponent<StaticModel>();
			haloComp.Model = CoreAssets.Models.Sphere;
			var haloMaterial = Material.FromColor(new Color(1.0f, 0.5f, 0.0f, 0.75f));
			var tech = ResourceCache.GetTechnique(NO_TEXTURE_UNLIT_ALPHA);
			haloMaterial.SetTechnique(0, tech);
			haloMaterial.FillMode = FillMode.Wireframe;
			haloMaterial.RenderOrder = RENDER_ORDER_BULGE;
			haloComp.SetMaterial(haloMaterial);
		}

This is what I'm trying to get:

![B5D85DAE-EA7A-497E-8A52-4B8314D97E7B_1_105_c|666x500](upload://yLo9LOztVeamShxOYPXJYIqxiyg.jpeg) 

This is what the above code yields.  Is there something else I need to set?

![C9C63F8E-08F1-4B39-8221-84DF332CBCDD_1_105_c|666x500](upload://lcrF8zCin39NtzZVcz5oVlZvzZw.jpeg)

-------------------------

btschumy | 2020-10-12 14:46:05 UTC | #2

So no one has any ideas on this?  Is what I'm doing supposed to work, or am I misunderstanding the (limited) documentation?

-------------------------

Eugene | 2020-10-12 14:58:16 UTC | #3

I don't see any issues with code.
However, wireframe and point modes do not exist on some platforms (on GLES, to be specific).

-------------------------

btschumy | 2020-10-12 15:23:21 UTC | #4

Ah, that must be the problem.  I am doing this on iOS which (I believe) is using OpenGL ES.

Is there any other way I can achieve this?

Seems like this limitation should be added to the docs.

-------------------------

Eugene | 2020-10-12 15:39:02 UTC | #5

[quote="btschumy, post:4, topic:6423"]
Is there any other way I can achieve this?
[/quote]
Make `StaticModel` with custom `Model` that uses line primitives instead of triangles.
I didn't test it but it should work in theory.
Maybe there's another way but I don't know about.

-------------------------

btschumy | 2020-10-12 16:06:49 UTC | #6

Eugene,

I appreciate your help but I don’t have a clue how to do this. Is this some simple setting, or do I need to create my own models in Blender or something?

Bill

-------------------------

Lys0gen | 2020-10-12 16:15:25 UTC | #7

I think he means you will have to create your model from a custom geometry with Vertex/IndexBuffers. See [sample 34](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp). Instead of using tris with

        geom->SetDrawRange(TRIANGLE_LIST, 0, numVertices);

you would use a LINE_LIST to define the geometry

        geom->SetDrawRange(LINE_LIST, 0, numVertices);

-------------------------

Eugene | 2020-10-12 16:51:35 UTC | #8

Second that ^^^
I forgot that we have sample for creating model.
It's not easy process, but it's straightforward.
You may get C#-specific issues tho.

-------------------------

btschumy | 2020-10-12 17:09:51 UTC | #9

Thanks for pointing me to the sample.  That may really tax my understanding but I can try.

Don't laugh, remember I really don't understand much about this.  However, I was playing around with the SetDrawRange and got something that almost works.

		private void CreateStellarHaloNode()
		{
			stellarHaloNode = universeNode.CreateChild();
			stellarHaloNode.Scale = new Vector3(130000.0f, 130000.0f, 130000.0f);

			var haloComp = stellarHaloNode.CreateComponent<StaticModel>();
			haloComp.Model = CoreAssets.Models.Sphere.Clone();
			var geometry = haloComp.Model.GetGeometry(0, 0);
			geometry.SetDrawRange(PrimitiveType.LineList, 0, 3840);
			var haloMaterial = Material.FromColor(new Color(0.0f, 1.0f, 0.0f, 1.0f), false);
			var tech = ResourceCache.GetTechnique(NO_TEXTURE_UNLIT_ALPHA);
			haloMaterial.SetTechnique(0, tech);
			haloMaterial.RenderOrder = RENDER_ORDER_STRUCTURE;
			haloComp.SetMaterial(haloMaterial);
		}

I don't really understand what SetDrawRange does, but the above code does yield this.

![FB18E1A5-EC09-495D-8951-D06B6B918199_1_105_c|666x500](upload://llBMz03TVVZNqJ5WteEDsz3N2Oj.jpeg) 

Obviously the lines it is using are not really right, but it does give a type of wireframe sphere.

Is there some modification of this that might get the wireframes looking correct?

-------------------------

Eugene | 2020-10-12 17:36:23 UTC | #10

[quote="btschumy, post:9, topic:6423"]
Is there some modification of this that might get the wireframes looking correct?
[/quote]
I don't think I can cover the whole topic of rendering 3D geometry in one reply.

You have to fix indices in index buffer.
Indices are either 16bit or 32bit integers, index buffer data is accessible in public interface.
The easiest modification is for each (a b c) triplet in index buffer create three pairs (a b) (b c) (c a) instead. You should get double size of bufer for lines comparing to triangles. You may later remove duplicate edges.

-------------------------

Modanung | 2020-10-13 09:54:42 UTC | #11

I don't know where you're going with that sphere, but there's benefits to basing it on [triacontahedron](https://en.wikipedia.org/wiki/Rhombic_triacontahedron):

- Easy (relatively uniform) cube UV mapping
- Most even distribution of vertices
- Used in geomatics

But if you're creating [plasmoids](https://en.wikipedia.org/wiki/Plasmoid), the polar coordinates of a UV sphere might be more convenient.

-------------------------

btschumy | 2020-10-13 15:30:06 UTC | #12

Ok, thanks for Eugene's last hint, I think I have this working.  I take the IndexBuffer for the triangles of a StaticModel Sphere, and convert them into sets of lines.

This code is not really optimized and is designed more for clarity.  I also don't (yet) throw away duplicate lines.

		private void CreateStellarHaloNode()
		{
			stellarHaloNode = universeNode.CreateChild();
			stellarHaloNode.Scale = new Vector3(130000.0f, 130000.0f, 130000.0f);

			var haloComp = stellarHaloNode.CreateComponent<StaticModel>();
			haloComp.Model = CoreAssets.Models.Sphere.Clone();
			var geometry = haloComp.Model.GetGeometry(0, 0);
			var indexBuffer = geometry.IndexBuffer;
			var indexCount = indexBuffer.IndexCount;
			var triangleCount = indexCount / 3;

			unsafe
			{
				var newIndices = new short[indexCount * 2];
				var shadowData = (short *)indexBuffer.ShadowData;
				for (var i = 0; i < triangleCount; i++)
				{
					var a = shadowData[i * 3];
					var b = shadowData[i * 3 + 1];
					var c = shadowData[i * 3 + 2];
					newIndices[i * 6 + 0] = a;
					newIndices[i * 6 + 1] = b;
					newIndices[i * 6 + 2] = b;
					newIndices[i * 6 + 3] = c;
					newIndices[i * 6 + 4] = c;
					newIndices[i * 6 + 5] = a;
				}

				indexBuffer.SetSize(indexCount * 2, false, false);
				fixed (short *indexPtr = &newIndices[0])
				{
					indexBuffer.SetDataRange(indexPtr, 0, indexCount * 2, true);
				}
				geometry.SetDrawRange(PrimitiveType.LineList, 0, indexCount * 2);
			}

			var haloMaterial = Material.FromColor(new Color(0.0f, 1.0f, 0.0f, 0.25f), false);
			var tech = ResourceCache.GetTechnique(NO_TEXTURE_UNLIT_ALPHA);
			haloMaterial.SetTechnique(0, tech);
			haloMaterial.RenderOrder = RENDER_ORDER_STRUCTURE;
			haloComp.SetMaterial(haloMaterial);
		}

Here is what it looks like:

![1B070475-EB11-446D-8C16-29327FF70E0D_1_105_c|666x500](upload://oeSq7uhJLG3kA5v3c72LUw7FRsU.jpeg) 

I don't necessarily like the way this is tessellated compared to SceneKit's way (see image in initial posting), but I can live with it.

Thanks again for the help.  I couldn't have done this without you.

-------------------------

Modanung | 2020-10-13 19:08:55 UTC | #13

This looks like an [icosphere]([/details]), whereas the vertex arrangement in your OP is referred to as a [UV sphere](https://en.wikipedia.org/w/index.php?title=UV_sphere&redirect=no).

-------------------------

btschumy | 2020-10-13 20:35:31 UTC | #14

Thanks for that information on the different meshes for a sphere.

I tried creating a UVSphere in Blender and saved it.  When I try to load it to use in my app I get a:

*System.Exception: Models/UVSphere.blend is not a valid model file.* 

Can you tell me how this needs to be saved such that I can use it?

-------------------------

Modanung | 2020-10-13 20:45:33 UTC | #15

Urho comes with a UV sphere model.

-------------------------

btschumy | 2020-10-13 21:22:34 UTC | #16

Are you sure?  Code completion for CoreAssets.Models. doesn't show it.  I also don't see it in the CoreAssets directory of the Urho3D-1.7.1 source.

What's is called?

I would like to know how to do this in Blender because I also need to make a custom Cylinder.  I don't like the way that is tessellated.

-------------------------

Modanung | 2020-10-13 21:33:58 UTC | #17

AFAIK there is no CoreAssets folder.

-------------------------

vmost | 2020-10-13 21:52:50 UTC | #18

Part of the difference between your recent attempt and SceneKit is scenekit only seems to be rendering a hemisphere, so the lines in the background aren't showing up.

-------------------------

btschumy | 2020-10-13 22:07:04 UTC | #19

Sorry, you are right.  It was called SourceAssets.

![image|545x500](upload://kVKwQg3QdgDYEWfJhV5rypTgEbF.png) 

So what is the name of the UVSphere and how is it accessed?

-------------------------

btschumy | 2020-10-13 22:09:38 UTC | #20

That is a good point.  In SceneKit it only renders the front.  I think that is because I specify:

		material.isDoubleSided = false

Is there an equivalent in Urho?  Is it culling?

-------------------------

Modanung | 2020-10-14 08:49:12 UTC | #21

https://github.com/urho3d/Urho3D/tree/master/bin/Data/Models

-------------------------

btschumy | 2020-10-14 14:10:48 UTC | #22

Ah, so Urho uses .mdl files as their native model format?  I think I need to install an export extension to export as .mdl.  Is there another format that Urho can read?  I guess I can just try the standard and se what happens.

-------------------------

Eugene | 2020-10-14 14:51:14 UTC | #23

[quote="btschumy, post:22, topic:6423"]
Is there another format that Urho can read?
[/quote]
Nope, Urho itself can work only with its own data format.
AssetImporter tool or Blender plugin is usually used to convert models into native model format.

-------------------------

btschumy | 2020-10-14 15:20:55 UTC | #24

Well, the plugin that seems recommended is here: https://github.com/reattiva/Urho3D-Blender

Following the instructions, I installed the plugin but get a warning that I need to update to Blender 2.8.x (I am on 2.90.1)

![image|602x500](upload://wl7eoESRZVjnaiPjftap5EA24hO.png) 

Despite the warning, I enabled it with the checkbox.  However, I don't see any export options in the Render Properties page (which is where the instruction say it should be).  Maybe this doesn't work on Mac?

![image|363x500](upload://4ny4Vvxh28cb4cp2k15nyLN5iwf.png) 

As far as the AssetImporter tool, I don't see how to use that.  Do I need to compile it?  Is it a command line tool?

-------------------------

Eugene | 2020-10-14 15:23:45 UTC | #25

I used plugin long time ago and I don’t remember how it works.
AssetImporter is command line tool distributed alongside Urho3D and used e.g. by Editor. Maybe it even has command line on wiki, although I didn’t check it.

-------------------------

btschumy | 2020-10-14 15:24:37 UTC | #26

Maybe I should just construct these programmatically in code?  Generating the vertices for a UV Sphere doesn't seem that difficult.

-------------------------

SirNate0 | 2020-10-14 18:14:33 UTC | #27

It might be easier to generate them in code, especially since you'd have to adapt it for rendering as lines anyways. Though I think if you use the 2.8 (2.83 is an LTS release) version of blender the exporter should work. Blender 2.9 just came out a month and a half ago, so I'm not surprised it doesn't work yet.

-------------------------

btschumy | 2020-10-14 18:41:37 UTC | #28

I had 2.8.<something> initially.  When I got the error saying it needs 2.8.x, I decided to update to 2.9 to see if that fixed anything.  Same problem with both.

I will take a stab at doing it in code.

As "vmost" pointed out, my SceneKit examples had the material set to "doubleSided = false", rendering only the from-facing part of the sphere.  I think the equivalent in Urho is to set culling to something other than NONE.  However this doesn't seem to work for drawing lines.  Is does if you are filling the surface.  I can probably live with it as is, but is there any way to have the lines work that way?

-------------------------

Lys0gen | 2020-10-14 19:44:53 UTC | #29

[quote="btschumy, post:28, topic:6423"]
I think the equivalent in Urho is to set culling to something other than NONE. However this doesn’t seem to work for drawing lines. Is does if you are filling the surface. I can probably live with it as is, but is there any way to have the lines work that way?
[/quote]

Lines have neither a winding order nor a orthogonal (normal). As such there is nothing to cull.
I suppose you could manually calculate the normals based on the old tri vertices and pass that information together with the line vertices in the geometry. Then you need a custom shader that calculates whether the line should be hidden based on the normal and the camera projection.

Though if this is just necessary for testing purposes I would question whether doing all this is worth the effort first ;)

-------------------------

vmost | 2020-10-14 21:29:56 UTC | #30

You could just create a hemisphere shape then set its position relative to the camera node + distance to galaxy center.

-------------------------

jmiller | 2020-10-16 01:30:45 UTC | #32

[quote="btschumy, post:24, topic:6423"]
Well, the plugin that seems recommended is here: https://github.com/reattiva/Urho3D-Blender
[/quote]
FYI: @dertom's exporter continues to work here (Blender 2.90.1 (L)), and I updated the [wiki](https://github.com/urho3d/Urho3D/wiki) editors a bit.  https://discourse.urho3d.io/t/blender-2-8-exporter-with-additonal-features-e-g-urho3d-materialnodes-and-components/5240

-------------------------

btschumy | 2020-10-16 18:37:47 UTC | #33

I just tried dertom's plugin and it gives errors installing as well.  Maybe no one tests these things on a Mac.

If someone that has an exporter working could create a basic UVSphere in Blender and export to a Urho .mdl file, I'd appreciate it.

-------------------------

btschumy | 2020-10-16 20:53:12 UTC | #34

Never mind.  I finally figured out how to do it using AssetImporter.

-------------------------

jmiller | 2020-10-17 03:43:53 UTC | #35

Typically I install addons by repo cloning or extracting from zip so the main folder with `__init__.py` is in user `blender/script/addons`, and did `pip install pyzmq` etc. as instructed... Glad you got something working, anyway.

-------------------------

