JTippetts | 2017-01-02 01:11:55 UTC | #1

I've got a tri-planar shader in my game, that applies diffuse and normal maps to an object based on fragment position and normal. The code of the shader is at [pastebin.com/ySFYG5Ka](http://pastebin.com/ySFYG5Ka) .

The shader takes the incoming fragment position and uses the X and Z coordinates to calculate a texture coordinate for the detail textures and normal maps. Then it uses the normal to blend between three mappings of the detail shader, projecting the detail along each of the 3 axes. So far, it has worked well.

My issue now is that I am attempting to provide a variation of the shader that combines the detail normal map with a model-specific normal map. In the shader code posted above, I have enclosed the model-normal specific sections in #ifdef MODELNORMAL blocks, with the MODELNORMAL being defined in the technique. For objects that want to use the model's normal map, I use a technique with MODELNORMAL defined, and provide a normal

The problem is that, while the shader works as expected with MODELNORMAL undefined, when MODELNORMAL is defined, somehow the fog coordinate gets stomped on. Here is a shot of the shader with MODELNORMAL not defined:

[url=http://i.imgur.com/R6QD7El.jpg]http://i.imgur.com/R6QD7El.jpg[/url]

Here is a shot with MODELNORMAL defined:

[url=http://i.imgur.com/yieq5Ur.png]http://i.imgur.com/yieq5Ur.png[/url]

You can see that in the second shot, the mountain model has the detail from its normal map, as well as the detail from the detail texture. However, the fog color is incorrect. The fog shading on the model stays constant, regardless of distance from the camera.

I have tried using TEXCOORD11 and TEXCOORD9 semantics for the input model normal, with no change. I'm not really a graphics programmer or shader expert, so I'm not really sure how to fix this, or even what exactly is going wrong. Anyone have any ideas?

-------------------------

cadaver | 2017-01-02 01:11:55 UTC | #2

Are you on D3D11? Possibly for some reason the VS and PS disagree on the interpolators (mismatching defines?) Remember that on D3D11 their order has to be exactly same, ie. the semantics actually don't help ordering them properly. The order in the shaders (assuming correct defines in both) seemed to be right, though.

If it helps you, nothing prevents you defining input and output structs for VS -> PS communication, even if the Urho inbuilt shaders don't use them.

-------------------------

JTippetts | 2017-01-02 01:11:55 UTC | #3

The error occurs, even if I use structs to pass to the PS:

[pastebin.com/Z058yA5z](http://pastebin.com/Z058yA5z)

Is it possible for there to be a mis-match even if using structs like this?

-------------------------

rasteron | 2017-01-02 01:11:55 UTC | #4

There is gawag's tri-planar wikia article and shader, maybe you can use this instead or at least get some information:

[urho3d.wikia.com/wiki/Tri-Planar_Texturing](http://urho3d.wikia.com/wiki/Tri-Planar_Texturing)

-------------------------

JTippetts | 2017-01-02 01:11:56 UTC | #5

The problem isn't with the tri-planar part, it's with the combining it with a normal-mapped model that's giving me issues.

Doing some further tinkering, I discovered something interesting. When I disable all lights (directional world lighting and player's torch) and use only ambient, then it seems to work as expected (albeit boring because of no light):

[i.imgur.com/L7tWmsU.png](http://i.imgur.com/L7tWmsU.png)

If I then cast a Light Torch spell, it initially appears that I have the correct result:

[i.imgur.com/nspkeWh.png](http://i.imgur.com/nspkeWh.png)

However, if I rotate the camera a little bit, the error pops in and out, ie moving the camera a little bit from the above view makes the incorrect fogging appear:

[i.imgur.com/Flp45MV.png](http://i.imgur.com/Flp45MV.png)

This leads me to believe something is uninitialized or using bad data somewhere, since I can get a similar effect from not having a texture bound to a needed slot in other shaders. I have verified that all necessary textures are being bound.

-------------------------

cadaver | 2017-01-02 01:11:56 UTC | #6

The problem could also be defining texcoord interpolators out of order. Make sure you have the correct defines and vertex+pixel shader combination set also in your lighting pass. For troubleshooting you could try unconditionally defining the interpolator right after the interpolators used by the lighting, even if it's only used in the "modelnormal" mode.

-------------------------

JTippetts | 2017-01-02 01:11:57 UTC | #7

Oh, man. Okay, looks like defining input/output structures DID actually do the trick. I missed changing the VS designator in a Technique I was using, so it was still pointing to the old vertex shader, rather than the new one. Everything seems to be working great, now, with the side effect of the shader code being much neater, after having the parameters separated out into structures.

[i.imgur.com/hDI2lQx.jpg](http://i.imgur.com/hDI2lQx.jpg)

Let this be a lesson: always double-check your techniques when doing shader modifications.

-------------------------

JTippetts | 2017-01-02 01:12:01 UTC | #8

There still seems to be something wrong that I can't pin down.

I'm working on my game's quest map (hence the weird usage of models in these following tests). I am currently using the tri-planar shader (without model normals) for landscape cells, and I am attempting to do the quest map as a render-to-texture scene, using normal-mapped mountain scenery. The mountains in this case are basic models using the DiffNormal technique. I whipped together a quick scene of mountains and built a Map Table, and this is the result:

[i.imgur.com/utjWvb7.jpg](http://i.imgur.com/utjWvb7.jpg)

Weird, right? And that's just using the mountain model with a DiffNormal shader. so, I made a test of using the mountain model as a piece in the main world map, and this was the result:

[i.imgur.com/baMwOiE.jpg](http://i.imgur.com/baMwOiE.jpg)

So here, the mountain works correctly, but now the tri-planar shader for the hex cells is borked. (It looks like the normals are wonky.)

I quit, and re-ran the exe with no changes, and the result was then this:

[i.imgur.com/PKRp50d.jpg](http://i.imgur.com/PKRp50d.jpg)

The tri-planar worked again, but this time the mountain was borked.

Tried it with the hex cell model using the mountain's shader:

[i.imgur.com/7gIPoWd.jpg](http://i.imgur.com/7gIPoWd.jpg)
[imgur.com/lx5QHI9](http://imgur.com/lx5QHI9)

It seems to be random which version will show up each time (DiffNormal borked or tri-planar borked). But it only affects models mapped with DiffNormal during the level generation phase. The units, including the goblin, also use DiffNormal and they are unaffected regardless of which way the terrain pieces are screwed up.

Remembering cadaver's many comments on how D3D11 interpolators sometimes get confused, and remembering how using shader input and output structures helped me before, I modified the LitSolid hlsl shader to use structures, but the result was exactly the same.

To me, it looks as if the normals are getting fouled up. Also, the mottled pattern of lighter and darker areas in the quest map screen shot makes me wonder if the blending texture used for terrain texture type splatting is also getting mixed in there somehow.

The full shader code for the tri-planar shader is at [pastebin.com/b78ymBCN](http://pastebin.com/b78ymBCN)

I understand this is kind of a complex issue to try to debug, so I'm not really expecting any hard answers. But if anyone has any ideas on things I can try to track this down, I'd appreciate it.

EDIT: Looks like it is somehow breaking the model normal. I modified the shader to output model normals as diffuse.

Unborked:
[i.imgur.com/HSCBYZF.jpg](http://i.imgur.com/HSCBYZF.jpg)

Borked:
[i.imgur.com/zrWZyTl.jpg](http://i.imgur.com/zrWZyTl.jpg)


Interestingly, I tried a GL build, and the model normals get borked there also, but in a different way:
[i.imgur.com/L7D4oPR.jpg](http://i.imgur.com/L7D4oPR.jpg)

I'm not sure how relevant this is to the current problem, since the GL shader was a quick job and I haven't tested it thoroughly yet.

Further Edit: Looks like the GL problem is related to lights somehow not affecting all instances of the hex cell model, rather than whatever is going on with the D3D11 version.

Another Edit:

If I disable the normal-mapping for the tri-planar shader, then everything works the way I expect it, in both D3D11 and GL, and both Forward and Deferred. (Note that the problem shows up in both Forward and Deferred modes, with normal-mapping enabled on the tri-planar.)

[i.imgur.com/Ex2Et2e.png](http://i.imgur.com/Ex2Et2e.png)

-------------------------

cadaver | 2017-01-02 01:12:02 UTC | #9

If you can, try the HLSL shader in D3D9 (you'll have to adapt the code since you used explicit SM4+ constructs, and naturally you can't read texture arrays, but just to debug if the normals break or not), which has simpler generation of vertex declarations that doesn't depend on the shader being used. In D3D11 there could be a hash collision bug when generating input layout for the shader + vertex buffers combination.

Note that I'm testing with code past the merge of the arbitrary vertex declarations (current master branch), which changed instancing texcoord from TEXCOORD2 to TEXCOORD4, and I'm talking about hash collisions in terms of that code. Urho doesn't backport fixes, so if a bug is uncovered and fixed, you will have to update to the latest master to gain benefit of that.

-------------------------

cadaver | 2017-01-02 01:12:02 UTC | #10

In current master branch input layout hashing is performed now so that vertex shader hash goes to upper 32 bits and vertex buffer hash to lower 32 bits. However this may not have anything to do with your issue. I tested your shader (though with no proper textures) and the vertex input elements shouldn't actually be different to a standard LitSolid normalmapped shader.

-------------------------

JTippetts | 2017-01-02 01:12:02 UTC | #11

After pulling the latest master, it looks like it is working properly for D3D11.

[i.imgur.com/gUFliii.jpg](http://i.imgur.com/gUFliii.jpg)

However, the GL build is completely broken:

[i.imgur.com/9zDtaFo.png](http://i.imgur.com/9zDtaFo.png)

No errors logged to the logfile when trying to build the shaders or anything, just doesn't work. If I disable the spawning of anything weird (ie, anything using a non-base Urho3D shader) it still doesn't work. I get the fog color, I get the water planes, I get the characters, but the trees and plants and doodads tend to flicker in and out of existence as the camera moves around, or just plain not show up at all.

-------------------------

cadaver | 2017-01-02 01:12:02 UTC | #12

Good to hear it's working for D3D11. That points to the input layout hashes potentially having been the culprit.

Check that your GL shaders conform to the arbitrary vertex element semantics, which are now zero-based:
- first texcoord: iTexCoord0 (0 can be omitted)
- second texcoord: iTexCoord1
- instance matrix: iTexCoord4, iTexCoord5, iTexCoord6

-------------------------

JTippetts | 2017-01-02 01:12:02 UTC | #13

Okay, there was a little bit of breakage on my part (I changed/munged/hosed a LOT of stuff trying to figure this issue out) but I think I got it sorted. Was using an old version of some shader code for the GL build. Just cleaned out some stuff, and it looks like it is working as expected. This little sideroad was horrendously disruptive to my already chaotic process. :smiley:

Thanks a LOT for your help, cadaver.

-------------------------

JTippetts | 2017-01-02 01:12:02 UTC | #14

Looks like it is working pretty well now:

[i.imgur.com/eFlB7UP.jpg](http://i.imgur.com/eFlB7UP.jpg)
[i.imgur.com/gJ5gejI.jpg](http://i.imgur.com/gJ5gejI.jpg)

Again, thanks for your help.

-------------------------

