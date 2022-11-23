suppagam | 2019-11-02 10:48:36 UTC | #1

I'm using this technique to build my levels: https://blender.stackexchange.com/questions/77264/how-can-i-bake-a-lightmap-and-use-it-in-blender-game-engine

Every object has it's own UV, with it's own texture, but I'm baking the lighting information for the whole level in their UV2. Each objects is it's own .blend, and then I have a .blend for the entire level. It works well and I get really high-resolution shadows, which is awesome.

However, I can't find a way to make Urho read my second UV and the lightmap texture. Is there a default shader that I can use, or I have to build one from scratch?

-------------------------

Modanung | 2019-07-25 14:14:56 UTC | #2

Could this answer your question?
https://discourse.urho3d.io/t/solved-how-to-use-one-lightmap-for-many-objects/553/2?u=modanung

-------------------------

suppagam | 2019-07-25 15:45:07 UTC | #3

The problem is that this does not allow me to have normal materials for my other objects, like normal and specular.

-------------------------

Modanung | 2019-07-25 18:11:54 UTC | #4

It seems to me that `DiffLightMap.xml` + `DiffNormalSpec.xml` would make:
[details=DiffNormalSpecLightMap.xml]

```
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="base" vsdefines="LIGHTMAP" psdefines="LIGHTMAP" />
    <pass name="litbase" vsdefines="NORMALMAP" psdefines="AMBIENT NORMALMAP SPECMAP" />
    <pass name="light" vsdefines="NORMALMAP" psdefines="NORMALMAP SPECMAP" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" vsdefines="NORMALMAP" psdefines="PREPASS NORMALMAP SPECMAP" />
    <pass name="material" psdefines="MATERIAL SPECMAP" depthtest="equal" depthwrite="false" />
    <pass name="deferred" vsdefines="NORMALMAP" psdefines="DEFERRED NORMALMAP SPECMAP" />
    <pass name="depth" vs="Depth" ps="Depth" psexcludes="PACKEDNORMAL" />
    <pass name="shadow" vs="Shadow" ps="Shadow" psexcludes="PACKEDNORMAL" />
</technique>
```
[/details]
Admitting I am no shader expert and did not test the resulting `Technique`.

-------------------------

suppagam | 2019-07-25 18:50:28 UTC | #5

Now I'm confused... so you can combine passes like that? The engine will just merge stuff? Where in the XML is it specifying to use UV2?

-------------------------

Modanung | 2019-07-25 18:59:13 UTC | #6

UV2 is reserved to be used with light maps, so that would be the `LIGHTMAP` part which tells the _shader_ to add the lightmap to the final color:
[quote=From LitSolid.glsl]
```
#ifdef LIGHTMAP
    finalColor += texture2D(sEmissiveMap, vTexCoord2).rgb * diffColor.rgb;
#endif
```
[/quote]

I believe `Technique`s can also be constructed through code, I’ll have to browse source to tell you more.

-------------------------

Modanung | 2019-07-25 19:02:20 UTC | #7

https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Technique.h#L187-L272

-------------------------

suppagam | 2019-07-25 21:55:03 UTC | #8

Thanks for the info! Really useful.

-------------------------

Modanung | 2019-07-25 22:54:44 UTC | #9

I'm glad to hear that. Did the [`DiffNormalSpecLightMap.xml`](https://discourse.urho3d.io/t/how-to-read-uv2/5344/4) solve your immediate issue?

-------------------------

