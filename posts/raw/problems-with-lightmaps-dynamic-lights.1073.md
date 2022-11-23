Dave82 | 2019-04-04 13:07:43 UTC | #1

Hi ! It seems that dynamic lights + shadow mapping + baked lightmaps doesn't work properly together... i don't know what causes this but here's a picture whats happening :

Left Images : No dynamic lights (OK)    -      Right : Dynamic lights + lightmap (Wrong)

[img]https://i.postimg.cc/hPB9HsFC/dynlights.jpg[/img]

As you can see some faces are lit and some are not. Also the shadow is not visible on unlit faces...(right bottom pic)
I tried to recalculate normals , turn off cast shadows on level , but it didnt helped.
i'm using the DiffLightMap , Diff , DiffLightmapAlpha , DiffAlpha techniques

Any ideas ? What i want is keep the lightmapped mesh unlit but receiving shadows

-------------------------

thebluefish | 2017-01-02 01:05:15 UTC | #2

You should be able to set the light mask on your lights and geometry. That way it won't affect your baked lighting. Then set the shadows on both, and I believe that should do what you want.

-------------------------

Dave82 | 2017-01-02 01:05:15 UTC | #3

Now the dynamic lights are gone , but the shadows are disappeared too...

The shadows are visible on the cube (DiffNormalPacked technique) but not on the level
[img]http://s7.postimg.org/xeiutcvcb/problems3.jpg[/img]

I tried :
[code]level->SetLightMask(1);
level->SetShadowMask(1);

light->SetLightMask(2);
light->SetShadowMask(1);[/code]

-------------------------

friesencr | 2017-01-02 01:05:15 UTC | #4

I haven't tried this...

Try make making a custom technique.  Copy and paste the DiffLightmap stuff and omit the light pass.

-------------------------

Dave82 | 2017-01-02 01:05:16 UTC | #5

Hi ! if i remove the line
[code]<pass name="light" depthtest="equal" depthwrite="false" blend="add" />[/code]

The effect is the same as on my second picture.The dynamic lighting is disabled but the shadows are not visible either.

-------------------------

Dave82 | 2017-01-02 01:05:17 UTC | #6

Hm... i tried modifying the shader as you suggested but still can't get it to work... maybe someone who is more into shader programming can help me out.

-------------------------

Dave82 | 2017-01-02 01:05:19 UTC | #7

Arghh... no matter how i modify the LitSolid shader it just won't work properly... I either end up the scene is unlit but then there's no shadow mapping at all , or i can get shadows but then the lightmapped mesh is lit. I can't turn off the light pass and keep the shadows... I just really wish there is a solution for this as its a really commonly used technique in games it would be a really cool if Urho had this feature...

BTW as i mentioed i'm really a beginner in shader programming so any help/ideas are welcome

-------------------------

Dave82 | 2017-01-02 01:05:20 UTC | #8

Hi , i will create a lightmapped mesh tomorrow somehow , right now i have no tools/editor that can export meshes with 2 texture coords and can be used directly with urho...
I have no project on git either , but as i said i can upload an mdl file tomorrow with materials and techniques.

-------------------------

Dave82 | 2017-01-02 01:05:20 UTC | #9

[quote]Oh, so in the model in your screenshots, is the lightmap literally part of the texturing?[/quote]
no that's my custom format (i wrote a whole scene exporter long ago for irrlicht) and i wrote an importer for Urho. Its in .mod format so Urho can't load them by default

[quote]I did a quick test with a junk lightmap I threw together in 30 seconds, it looks like everything is fine in the shaders out of the box.
Have you tried adjusting the "Brightness Multiplier" of the light. Something like 0.1.[/quote]

Hm i just did a test too in the urho editor.I imported a lightmapped mesh added a cube and a light. If i turn the brightness lower , the shadow cast by the cube also disappears.Also turning the brighness lower would affect models that SHOULD be lit in the scene (e.g characters dynamic objects etc)

This is how it looks Brightness 0.1 :
[img]http://s22.postimg.org/84wrenqzl/lmap01.jpg[/img]

And brightness 0.75 :
[img]http://s12.postimg.org/bhsdqhukd/lmap2.jpg[/img]

-------------------------

rasteron | 2017-01-02 01:05:20 UTC | #10

Quick question Dave82, What software tool are you using in generating Lightmaps? I've always been curious with lightmap techniques since this is a big part of asset optimization.

I tried to contribute some samples before but [url=http://discourse.urho3d.io/t/lightmap-on-dynamic-shadows/678/1]my thread[/url] was somehow buried  :unamused:

really curious how this turns out.

-------------------------

rasteron | 2017-01-02 01:05:20 UTC | #11

I'm not sure if these can help in anyway but found some discussion from other engines, this one in Irrlicht forums from member [b]Mel[/b]..

[quote]I have a suggestion for the dynamic/static shadow blending. Basically, If you use lightmapping, you can multiply the shadowmap by the lightmap, and calculate the luminance of the result to blend it with the ambient lighting. This, obviously, overrides the lightmap color, but almost blends perfectly the shadowmap with the lightmap.
 
[code]lightmapColor*=shadowmapValue;
colorIntensity = (lightmapColor.r+lightmapColor.g+lightmapColor.b)/3.0;
lightCol = (1-colorIntensity)*ambient+(colorIntensity)*lightmapColor;[/code]

[/quote]

Full Thread:
[b]How to mix static shadow with dynamic shadow[/b]
[irrlicht.sourceforge.net/forum/v ... 70#p259025](http://irrlicht.sourceforge.net/forum/viewtopic.php?f=4&t=45070#p259025)


[b]About Lightmaps[/b]
[irrlicht.sourceforge.net/forum/v ... hp?t=26220](http://irrlicht.sourceforge.net/forum/viewtopic.php?t=26220)

-------------------------

globus | 2017-01-02 01:05:20 UTC | #12

ow, It looks as problem exist only in calculating for mixing.
In general - it work.

For rasteron:
[spoiler][quote="rasteron"]Quick question Dave82, What software tool are you using in generating Lightmaps? I've always been curious with lightmap techniques since this is a big part of asset optimization.

I tried to contribute some samples before but [url=http://discourse.urho3d.io/t/lightmap-on-dynamic-shadows/678/1]my thread[/url] was somehow buried  :unamused:

really curious how this turns out.[/quote]

[img]http://i.piccy.info/i9/8af60cd9b62cabd8aa248baa4f57e931/1432727186/65192/912050/555.jpg[/img]

3DMax , Maya, Blender3D and other programs can do it.

Quick theory from Wiki
[url]http://en.wikipedia.org/wiki/Lightmap[/url]

Lightmap can be baked directly to Diffuse texture in 3D editor.
In this case is not necessary for game engine calculate mix for Diffuse and Lightmap.
It can be used if you not want change static lights/objects positions.

Lightmap can be baked separatly to other UV coordinates.
Object need have one UV for Diffuse and other UV for Lightmap.
In this case, game engine calculate mix Diffuse/Lightmap by himself.
But, you have the ability to change only Lightmap when change level to level.
Level "morning" <-to-> Level "evening"
or in realtime.

If litemaps used for shadows only it can be greyscale (limited number of colors)
This textures lightweight for hardware loading process than loading diffuse textures.
Additionally this textures can be used for specular calculating or other targets.

Blender "blender lightmap"
[url]http://www.youtube.com/results?search_query=blender+lightmap[/url]
Blender "blender bake"
[url]http://www.youtube.com/results?search_query=blender+bake[/url]
Variants for Blender "TextureAtlas Add-on"
[url]http://www.blendernation.com/2012/09/13/textureatlas-add-on-baking-entire-scenes/[/url]
Introduction to Baking in Cycles
[url]http://www.blenderguru.com/tutorials/introduction-baking-cycles/[/url][/spoiler]
Look also to:
[img]http://i.piccy.info/i9/1bbf7d157365957a9a5a8daee706e72e/1432731235/186542/912050/u3dshadows.jpg[/img]
[b]Warboat[/b] (Local Multiplayer Boat Battle)
[b]Use Blender and Urho3D for shadowmap.[/b]
[url]http://forums.tigsource.com/index.php?topic=41689.20[/url]

-------------------------

Dave82 | 2017-01-02 01:05:20 UTC | #13

[quote]Quick question Dave82, What software tool are you using in generating Lightmaps? I've always been curious with lightmap techniques since this is a big part of asset optimization.[/quote]
I'm using lots of softwares , but my favorite is 3ds max. I'm using it 7-8 years now and i think it gives the best results. It's a really big optimisation but the reason i really like static lightmaps is that literally everything is possible.You can bake Global illumination + color bleeding + edge detection + soft shadows in one lightmap texture. I mean dynamic lighting with dynamic shadow mapping looks really great but not even close to baked global illumination.Thats the main reason why i want to use static lightmaps.

[quote]really curious how this turns out.[/quote]

Me too :smiley: but the more i think about this the more i came to a conclusion that is impossible to do it..
The shadow mapping is not "Rendering dark shadows on top of the level" but "rendering light on top of the level and leave out the shadowed areas" 
So shadows in fact are non-lit parts of the scene.
So it goes something like this :

1 render the scene unlit (pass1)
2 render the scene lit and calculate shadows (pass2)

This would be possible only if we could render the level non lit with lightmap texture , and on top of that render shadow maps (subtract from current frame)
So what we will have is completely the oposite , but this way we can specify custom shadow color>

1 render the scene unlit
2 render the scene but instead of calculating the lighting we simply use black color for the whole image EXCEPT where the shadows should be.There we can use shadowColor

Here's my idea :
[img]http://s22.postimg.org/slpdbpye9/lightmaps_shadows.jpg[/img]


Is possible to do something like this with shaders ??? This way the lightmapped meshes are unaffected by lights still dynamic shadows will be possible.

-------------------------

cadaver | 2017-01-02 01:05:20 UTC | #14

It's not directly possible without engine code modifications, because like you say now the purpose of light pass is to add light.

Some engines like Unity build a shadow mask texture for the screen, which may allow more versatility in the shadow blending equation. But it doesn't allow unlimited amount of shadowed lights because of limited channels (RGBA) in the shadow mask.

-------------------------

Dave82 | 2017-01-02 01:05:20 UTC | #15

[quote]It's not directly possible without engine code modifications, because like you say now the purpose of light pass is to add light.[/quote]

Yeah now that i'm thinking further it will disable lighting in the whole engine as each material would use this approach , which disables lighting...

-------------------------

rasteron | 2017-01-02 01:05:21 UTC | #16

@globus

Thanks for the reference. I'm already very familiar and knowledgeable with lightmapping process, in fact it is one of my favorite topics when it comes to engine and game optimization. :smiley: I'm not a shader guy though..

This one I did for testing months ago:

[img]http://media.indiedb.com/cache/images/engines/1/1/641/thumb_300x150/global_illumination.jpg[/img]

It is the pipeline and the technique of blending dynamic shadows and static lightmaps [u]with Urho3D[/u] that I'm curious with, which is why I was planning to contribute to as samples, and apparently this has not been a feature with the engine [yet]. :wink:

-------------------------

rasteron | 2017-01-02 01:05:21 UTC | #17

[quote]
I mean dynamic lighting with dynamic shadow mapping looks really great but not even close to baked global illumination.Thats the main reason why i want to use static lightmaps.
[/quote]

Same reason here and I couldn't agree more. Not a fan of using dynamic shadow mapping on all objects as well  :smiley: 

Realtime GI and other lighting effects is really nice but if you can save up and another reason not to make the graphic card or system overheat, it is a must have.

-------------------------

rasteron | 2017-01-02 01:05:21 UTC | #18

I tried to work on a small demo with Godot engine for a bit, particularly when I found out that they got their baked GI working months ago. It was really awesome but still having problems with their editor and it's only GLES2 for Godot at the moment :unamused:  so I stopped my work there and got back to my old engine. :slight_smile:

Here's the Godot editor interface with their baked GI feature..

[img]http://i.imgur.com/GxdRqS4l.jpg[/img]

-------------------------

Dave82 | 2017-01-02 01:05:21 UTC | #19

Well i just give it up... i will just simply disable the lightpass on lighmapped meshes and use a simple blob shadow under the character's feet.
It is unfortunate that a feature like this not included in Urho3d

-------------------------

globus | 2017-01-02 01:05:23 UTC | #20

[quote="rasteron"]
..., in fact it is one of my favorite topics when it comes to engine and game optimization. :smiley: I'm not a shader guy though..
[/quote]

I fully support your attitude towards optimization.
Lightmapping big step in that direction.

I like the old style of game engines. (Old-Gen engines)
There are a lot of old games that are fun to replay again.
Previously, developers were limited in resources and do miracles of optimization.

And there's a huge mass of modern games they look very best
but with mercilessly loaded hardware and which are not fun to play.

[spoiler][img]http://i.piccy.info/i9/60f787468146686ccbbf5ee0c26aa7af/1432838852/129240/912050/complete.jpg[/img]

Also, Fable: The Lost Chapters, Rune and mass of other old games.

Not very old but well optimized:
COD: Modern Warfare 2 and Dead Space 2-3[/spoiler]

-------------------------

rasteron | 2017-01-02 01:05:26 UTC | #21

[quote="globus"][quote="rasteron"]
..., in fact it is one of my favorite topics when it comes to engine and game optimization. :smiley: I'm not a shader guy though..
[/quote]

I fully support your attitude towards optimization.
Lightmapping big step in that direction.

I like the old style of game engines. (Old-Gen engines)
There are a lot of old games that are fun to replay again.
Previously, developers were limited in resources and do miracles of optimization.

And there's a huge mass of modern games they look very best
but with mercilessly loaded hardware and which are not fun to play.

[spoiler][img]http://i.piccy.info/i9/60f787468146686ccbbf5ee0c26aa7af/1432838852/129240/912050/complete.jpg[/img]

Also, Fable: The Lost Chapters, Rune and mass of other old games.

Not very old but well optimized:
COD: Modern Warfare 2 and Dead Space 2-3[/spoiler][/quote]

Thanks globus, I'm sure a lot of game devs appreciate this and are also using it with other engines. But in the case with Urho3d, there's still a lot of improvement needed to accomplish this seamless and optimized pipeline.  :wink:

-------------------------

globus | 2017-01-02 01:05:29 UTC | #22

For me is strange when:

I play game FarCry 1-2 on computer -
i see the beauty with the high settings.

Then i play FarCry 3 - disconnect all that is possible disable including shadows. 
Make resolution to 800x600. FPS is low and it look like Quake1.

For me, this is an indicator that the new engines are not very optimized. 
Probably because, they initially made for powerful computers.

-------------------------

cadaver | 2017-01-02 01:05:29 UTC | #23

Far Cry 3 runs more complex content (and AI, physics) than the previous, and there's limits on how low you can scale, e.g. you can disable things like particles, decals and extra clutter, but you can't scale AI and player/enemy physics down without changing fundamentally how it plays. Also, it depends on realtime fullscreen effects like ambient occlusion to look good, while the previous don't.

You're right that because they started with a more powerful minimum spec, they probably can afford to be a little lazy. Or they optimize for different things, that don't scale well for older computers, like taking advantage of multiple cores. Probably the converse is also true, that if you'd try to run FC3 content/world in the FC2 engine, it'd run like shit, because it was not made ready for that.

-------------------------

flintza | 2017-01-02 01:08:38 UTC | #24

Has anyone worked out a nice solution to this yet? 
I've tried adding a lighting pass  and just applying the shadows as suggested on the first page, but as someone else also mentioned since the lighting is additive there's really no way to do it there.
So at this point I'm trying to see if I can introduce the shadows in the base pass by modifying the output color there, which is proving tricky (I'm no shader expert :slight_smile: )

-------------------------

codingmonkey | 2017-01-02 01:08:38 UTC | #25

Hi, i'm do not working yet with this issue, but I guessing what we are have free alpha channel in viewport RT until we drawing opaque passes and not alpha passes.
if we try to write to alpha by default 0 (black) and if technique has lightmap technique we write precomputed AO from texture (0-255)
after all opaque passes we will have some sort of BW map in alpha channel.
and then we add quad command pass exactly after post opaque pass and do blending with substract with this BW from viewport, or custom screen shaded with multiplying (in case mul I guessing we must write 1 by default instead 0)

-------------------------

flintza | 2017-01-02 01:08:39 UTC | #26

I did get a working solution, though it feels like a bit of a hack. I use the lighting pass, but set it to subtractive:
[code]
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="base" vsdefines="ENVCUBEMAP LIGHTMAP" psdefines="ENVCUBEMAP LIGHTMAP" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="light" vsdefines="LIGHTMAP" psdefines="LIGHTMAP" depthtest="equal" depthwrite="false" blend="subtract" />
    <pass name="material" vsdefines="ENVCUBEMAP LIGHTMAP" psdefines="MATERIAL ENVCUBEMAP LIGHTMAP" depthtest="equal" depthwrite="false" />
    <pass name="deferred" vsdefines="ENVCUBEMAP LIGHTMAP" psdefines="DEFERRED ENVCUBEMAP LIGHTMAP" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>

[/code]
And then in the pixel shader I use the LIGHTMAP define to essentially output the inverse of the shadow:
[code]
#if defined(LIGHTMAP) && defined(SHADOW)
    float diff = 1-GetShadow(iShadowPos, iWorldPos.w);

    finalColor = diff * diffColor.rgb * cAmbientColor;

    oColor = float4(GetLitFog(finalColor, fogFactor), diffColor.a);
#else
    float diff = GetDiffuse(normal, iWorldPos.xyz, lightDir);

    #ifdef SHADOW
        diff *= GetShadow(iShadowPos, iWorldPos.w);
    #endif

    #if defined(SPOTLIGHT)
        lightColor = iSpotPos.w > 0.0 ? Sample2DProj(LightSpotMap, iSpotPos).rgb * cLightColor.rgb : 0.0;
    #elif defined(CUBEMASK)
        lightColor = SampleCube(LightCubeMap, iCubeMaskVec).rgb * cLightColor.rgb;
    #else
        lightColor = cLightColor.rgb;
    #endif

    #ifdef SPECULAR
        float spec = GetSpecular(normal, cCameraPosPS - iWorldPos.xyz, lightDir, cMatSpecColor.a);
        finalColor = diff * lightColor * (diffColor.rgb + spec * specColor * cLightColor.a);
    #else
        finalColor = diff * lightColor * diffColor.rgb;
    #endif

    #ifdef AMBIENT
        finalColor += cAmbientColor * diffColor.rgb;
        finalColor += cMatEmissiveColor;
        oColor = float4(GetFog(finalColor, fogFactor), diffColor.a);
    #else
        oColor = float4(GetLitFog(finalColor, fogFactor), diffColor.a);
    #endif
#endif
[/code]

-------------------------

rasteron | 2017-01-02 01:08:40 UTC | #27

[quote="flintza"]I did get a working solution, though it feels like a bit of a hack. I use the lighting pass, but set it to subtractive:
[code]
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="base" vsdefines="ENVCUBEMAP LIGHTMAP" psdefines="ENVCUBEMAP LIGHTMAP" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="light" vsdefines="LIGHTMAP" psdefines="LIGHTMAP" depthtest="equal" depthwrite="false" blend="subtract" />
    <pass name="material" vsdefines="ENVCUBEMAP LIGHTMAP" psdefines="MATERIAL ENVCUBEMAP LIGHTMAP" depthtest="equal" depthwrite="false" />
    <pass name="deferred" vsdefines="ENVCUBEMAP LIGHTMAP" psdefines="DEFERRED ENVCUBEMAP LIGHTMAP" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>

[/code]
And then in the pixel shader I use the LIGHTMAP define to essentially output the inverse of the shadow:
[code]
#if defined(LIGHTMAP) && defined(SHADOW)
    float diff = 1-GetShadow(iShadowPos, iWorldPos.w);

    finalColor = diff * diffColor.rgb * cAmbientColor;

    oColor = float4(GetLitFog(finalColor, fogFactor), diffColor.a);
#else
    float diff = GetDiffuse(normal, iWorldPos.xyz, lightDir);

    #ifdef SHADOW
        diff *= GetShadow(iShadowPos, iWorldPos.w);
    #endif

    #if defined(SPOTLIGHT)
        lightColor = iSpotPos.w > 0.0 ? Sample2DProj(LightSpotMap, iSpotPos).rgb * cLightColor.rgb : 0.0;
    #elif defined(CUBEMASK)
        lightColor = SampleCube(LightCubeMap, iCubeMaskVec).rgb * cLightColor.rgb;
    #else
        lightColor = cLightColor.rgb;
    #endif

    #ifdef SPECULAR
        float spec = GetSpecular(normal, cCameraPosPS - iWorldPos.xyz, lightDir, cMatSpecColor.a);
        finalColor = diff * lightColor * (diffColor.rgb + spec * specColor * cLightColor.a);
    #else
        finalColor = diff * lightColor * diffColor.rgb;
    #endif

    #ifdef AMBIENT
        finalColor += cAmbientColor * diffColor.rgb;
        finalColor += cMatEmissiveColor;
        oColor = float4(GetFog(finalColor, fogFactor), diffColor.a);
    #else
        oColor = float4(GetLitFog(finalColor, fogFactor), diffColor.a);
    #endif
#endif
[/code][/quote]

First of, welcome! :slight_smile: This looks interesting, could you post some screenshots of this result and perhaps a working sample? 

Thanks!

-------------------------

flintza | 2017-01-02 01:08:40 UTC | #28

Hmm, I don't have a screenshot I could share just yet (NDA and all that), I'll see what I can organize. As for a working sample, I'm doing this in Atomic Game Engine, and we do have a material sample level we hope to put into examples repo sometime next year but not just yet :slight_smile:

-------------------------

Dave82 | 2017-01-02 01:08:48 UTC | #29

Hmmm.... this seems interesting , however the problem is way more complicated. If you use subtractive shadows on a material, that will disable additive light pass (e.g you can't have flashlight in the game... ) This probably has to be solved on light level. Maybe lights should have a flag of using it as a pure additive (default) or a lightmap light.

LIGHTMODE_ADDITITVE, // default behavior
LIGHTMODE_LIGHTMAP, // This light casts subtractive shadow on materials that have LIGHTMAP defined , but works normal on other materials

But (i assume) this requires 2 separate depth maps for shadows (additive and subtractive at the same time)

-------------------------

Dave82 | 2019-03-04 21:02:08 UTC | #30

Ok , so finally i think i found a solution for this. It's a workaround and it is a level editor/modeller software dependant. So instead of subtracting the shadows , i will disable direct lighting and bake only the global illumination (AO , indirect lighting , color bleeding , etc). And use dynamic lighting for direct lights. This will lit and cast shadows properly on lightmapped meshes , and it's possible to combine with shaders. And it could work perfectly with dragonCASTjosh's PBR

-------------------------

