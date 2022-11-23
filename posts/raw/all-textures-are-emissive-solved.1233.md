practicing01 | 2017-01-02 01:06:15 UTC | #1

Hello, in blender, the model has diffuse, normal, specular, emission and ambient occlusion maps.  The urho exporter didn't export the ambient occlusion map.  It also set the technique to use to be DiffNormalEmissive, is it possible to have DiffNormalEmissiveSpecularAmbientOcclusion?  I don't see an Ambient Occlusion texture slot, is that what the Environment slot is for?

Regardless of all of the above, some techniques make the model all white and the DiffNormalEmissive makes all of the diffuse emit.  Thanks for any help.

[img]http://img.ctrlv.in/img/15/08/03/55bfd018cfd8e.png[/img]

-------------------------

codingmonkey | 2017-01-02 01:06:15 UTC | #2

> I don't see an Ambient Occlusion texture slot
AO it's per-frame calculated post-effect based on angles between various objects in scene from depth texture

The light mapping it's baked static light from many objects on scene into one common big texture, these objects must have a second uv-layer for using light mapping.

[quote]...put diffuse texture normally to diffuse slot, and the shared lightmap texture to emissive slot...[/quote]
[url]http://discourse.urho3d.io/t/solved-how-to-use-one-lightmap-for-many-objects/553/2[/url]

-------------------------

1vanK | 2017-01-02 01:06:15 UTC | #3

Post-effect is named SSAO [github.com/reattiva/r/tree/master/r_AO](https://github.com/reattiva/r/tree/master/r_AO)
In this case, I think, other. In CoreData\Techniques\ many techniques with AO slot, but I never did not use them, and can not give any advice

EDIT: [github.com/urho3d/Urho3D/commit ... 71ceaf61da](https://github.com/urho3d/Urho3D/commit/d113be3bb26c580b1cfbbe74b0289771ceaf61da)
 Added ambient occlusion LitSolid permutations. These read the emissive texture and use the second texcoord, like lightmapped permutations.

-------------------------

practicing01 | 2017-01-02 01:06:21 UTC | #4

I tried all of the techniques and some make the model white, others make it invisible, none give the correct results.  Here is the blend file if anyone is interested in attempting to get the emission map to work correctly:  [dropbox.com/s/p48rmylvsmiid ... ar.gz?dl=0](https://www.dropbox.com/s/p48rmylvsmiidwa/terry.tar.gz?dl=0)

-------------------------

codingmonkey | 2017-01-02 01:06:21 UTC | #5

You need joint terryD.png and terryD_a.png into one texture. Use terryD_a.png as overlay on terryD.png and you got one texture diffTexture with AO affects on it. 
[url=http://savepic.net/7104904.htm][img]http://savepic.net/7104904m.png[/img][/url]

I guessing that the thing is, that in the shader AO and Emissive (also LIGHTMAP) use the same TextureUnit and that's why they working are exclusive or you use AO or you use Emissive not in same time. 
[code]
        #ifdef AO
            // If using AO, the vertex light ambient is black, calculate occluded ambient here
            finalColor += Sample2D(EmissiveMap, iTexCoord2).rgb * cAmbientColor * diffColor.rgb;
        #endif[/code]

[code]
        #ifdef LIGHTMAP
            finalColor += Sample2D(EmissiveMap, iTexCoord2).rgb * diffColor.rgb;
        #endif
        #ifdef EMISSIVEMAP
            finalColor += cMatEmissiveColor * Sample2D(EmissiveMap, iTexCoord.xy).rgb;
        #else
            finalColor += cMatEmissiveColor;
        #endif
[/code]

-------------------------

practicing01 | 2017-01-02 01:06:22 UTC | #6

I added the AO into the diffuse as an overlay in gimp and changed the technique to DiffuseNormalSpecularEmissive but the entire model still emits.  Are you using the latest blender-urho exporter?

-------------------------

codingmonkey | 2017-01-02 01:06:22 UTC | #7

The thing is that PSShader use RGB channels of EmissiveMap and you put to it RGBA. A - alpha is ignored in this case by Shader, it grab RGB values from texture and work with it, but you see that image fine and you see only emission regions in texture. But actually there are still white color that discarded by alpha in gimp or ps. You better for this use only RGB or BW images and make non-emission part of texture with full black color.

[url=http://savepic.net/7128530.htm][img]http://savepic.net/7128530m.png[/img][/url]

EmissiveMap
[url=http://savepic.net/7119314.htm][img]http://savepic.net/7119314m.png[/img][/url]

 >Are you using the latest blender-urho exporter?
Yes, actually I have a fork of this exporter with my additional functionality. But there still need to do material setup in Urho3D editor.

ps. Actually this maybe need to be fixed in master to allow users use EmissiveMap with alpha or clip Emissive pixels by alpha value from EmissiveMap

changes for LitSolid.hlsl if you want clip EmissiveMap by alpha value
[code]
        #ifdef EMISSIVEMAP
			float4 emissiveColor = Sample2D(EmissiveMap, iTexCoord.xy);
			float a = lerp(1, 0, step(emissiveColor.a, 0.1));
			finalColor += cMatEmissiveColor * emissiveColor.rgb * a;
        #else
            finalColor += cMatEmissiveColor;
        #endif
[/code]

-------------------------

practicing01 | 2017-01-02 01:06:22 UTC | #8

Thanks!  Changing the alpha to black did the trick: 
[img]http://img.ctrlv.in/img/15/08/09/55c690e25dbc6.png[/img]

-------------------------

