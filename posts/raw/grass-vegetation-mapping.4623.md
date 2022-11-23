JTippetts | 2018-10-29 15:47:12 UTC | #1

I am in the process of developing a grass/ground vegetation mapping scheme as outlined [here](https://www.shamusyoung.com/twentysidedtale/?p=23354), using a static mesh with billboard structures that follows the player around. The mesh draws vegetation info from a texture overlaid on the terrain, which describes how to draw/place it. The technique phases in the vegetation at a certain radius, by increasing a scale factor from 0 to keep things from visibly popping into place.

So far, I have been able to implement it fairly well in Urho3D. 

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/c/cb3fbf10a0be7b6a7d75d969859db63d56ed9ce0.jpeg[/img]

(I'm using a very quickly made experimental mesh, so it doesn't look the greatest yet; just trying to figure the technique out before I spend a bunch of time refining it.)I do have a couple issues, though, that I'm unable to sort out:

1) Because the mesh is being deformed in the vertex shader using a vertex texture fetch from the heightmap, the actual geometry is clipped from view if, for example, the player is on a high hill, since the 'real' bounding box of the grass structure still sits at Y=0 and is not very tall. I can hack my way around this by adding a small bit of degenerate geometry to the grass mesh, placing it at some arbitrary high point (Y=300 works well) above the rest of the mesh to artificially inflate the height of the mesh bounding box, but I was wondering if there was a less hackish way of ensuring the grass mesh is drawn even if the 'real' bounding box is out of frustum. Is there some way to mark a model as "do not cull for any reason" or something like that? I don't like having to blow up the size of the bounding box, since that can play hell with shadow mapping when looking out horizontally on the terrain.

2) I created a GrassShadow.glsl shader to implement a VS for the shadow pass, that implements the same texture fetch and translation as the main shader, but it doesn't seem to work. If I use the default Shadow.glsl I get shadows as if the grass were always at the Y=0 plane, but the shadows do not 'follow' the grass as it translates upward due to the heightmap. However, if I use a modification of Shadow.glsl that includes the texture fetch and translation, I get no shadows at all, even at Y=0, which makes me wonder if the Shadow shader isn't getting all of the uniforms I'm sending the main shader.

Can anybody confirm whether or not the shadow pass gets the same set of uniforms as the main shader? I am setting the HeightData uniform, the HeightMap texture and the CoverMap texture manually through code after the material is loaded.

The main shader can be seen at https://pastebin.com/NdRufTKZ while the shadow shader can be seen at https://pastebin.com/DLKV4ThW

I am passing 2 textures (the heightmap and the foliage coverage map) as well as a vec4 uniform that contains the heightmap dimensions and the terrain sampling sizes (x/z sample spacing and height) that are passed to Terrain::SetSpacing. The shader uses the sampling parameters and size to calculate texture coordinates, then indexes the heightmap texture to calculate a vertical translation that is applied to the vertex. The coverage map currently encodes X and Z offsets in the R and B channels, to translate the billboard geometry by a small amount to help alleviate the rigid grid-like structure.

Edit: I have uploaded a repo demonstrating the issue: https://github.com/JTippetts/Urho3DGrassTest

-------------------------

Sinoid | 2018-10-29 02:09:27 UTC | #2

[quote="JTippetts, post:1, topic:4623"]
Can anybody confirm whether or not the shadow pass gets the same set of uniforms as the main shader?
[/quote]

Yes. They use the same batch management stuff as everything else, so `Batch::Prepare` takes care of it.

-------------------------

Alan | 2018-10-29 23:21:15 UTC | #3

After a lot of building nonsense as rant on gitter, I had 5 minutes to very quickly take a look at it, and after some changes in the shader I got working shadows:
![image|690x486](upload://qTCUIeCRpj2crSSZ358x2sYcOEF.jpeg) 
I'm still trying to determine what's exactly the problem though, I don't really understand why the x/z of the verts are being changed and the var names aren't helping much :trolleybus:

-------------------------

JTippetts | 2018-10-29 22:22:05 UTC | #4

The X/Z displacement was an attempt (not real successful) to pull the billboards off the grid somewhat. The coverage map would hold randomized offsets in R and B. You can see in your screenshot, the grid bias is horrendous using this technique, so something needs to be done to make it workable.

-------------------------

JTippetts | 2018-10-29 22:23:31 UTC | #5

I note you have shadows on the displaced terrain. That's.... uh.... weird. Because I don't, hence this topic.

-------------------------

Alan | 2018-10-30 03:05:12 UTC | #6

This was solved on Gitter and I'm updating here so others can benefit from the solution.
The problem was that when rendering the shadows the built-in cCameraPos uniform is the position of the shadow caster, not the actual camera that's rendering the scene, and since that position was used to calculate the size of the bushes in this case, that was the cause of the problem.
For completeness, here's how I fixed that issue, it's probably not the most elegant way to do that but I believe it's the simplest:
https://github.com/Alan-FGR/Urho3DGrassTest/commit/cde33e427962a1637bdf0e59d8b7c61542025cb1

----
EDIT: Oops... actually, I was thinking this thread was just for the shadows problem... it's confusing now, sorry guys :sweat_smile:

-------------------------

