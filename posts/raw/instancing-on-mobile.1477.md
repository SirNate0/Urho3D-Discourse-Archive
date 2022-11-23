sabotage3d | 2017-01-02 01:08:02 UTC | #1

Hey guys. I have a scene where mostly my nodes are copies with the same shaders. At the moment is just a around 15-20 boxes moving around and I am already getting quite terrible performance with simple diffuse shader. Is there any good way to use instancing on ES 2.0 . I noticed two extensions that can help  and other ways of faking it like this: [url]http://carloscarrasco.com/faking-mesh-instancing-in-opengl-es-20.html[/url]
[b]Extensions:[/b]
[url]https://www.khronos.org/registry/gles/extensions/EXT/EXT_instanced_arrays.txt[/url]
[url]https://www.opengl.org/registry/specs/EXT/draw_instanced.txt[/url]

Or any others suggestions to reduce the draw calls?

-------------------------

Bananaft | 2017-01-02 01:08:03 UTC | #2

Are you sure, that bottleneck here is number of drawcalls? 15-20 seems ridiculous.

-------------------------

TikariSakari | 2017-01-02 01:08:03 UTC | #3

I also suspect that either the phone you are using is extremely out dated or there is something terribly wrong with the scene / code if 15-20 boxes is enough to completely kill the performance.

You should probably try to figure out what is the true cause of the problem, if its fill rate of screen, cpu bottle neck or gpu one.

-------------------------

sabotage3d | 2017-01-02 01:08:03 UTC | #4

It is definitely the shading as if I put unlit material everything renders at 60 FPS. The GPU is PowerVR SGX540 shouldn't be too bad. I will do a trace tonight and I will post the results.

-------------------------

Bananaft | 2017-01-02 01:08:03 UTC | #5

[quote="sabotage3d"]It is definitely the shading as if I put unlit material everything renders at 60 FPS. The GPU is PowerVR SGX540 shouldn't be too bad. I will do a trace tonight and I will post the results.[/quote]

So it's fill rate then. Try the following:
-lower number of lights.
-Disable specular.
-Switch to per-vertex lighting.

-------------------------

sabotage3d | 2017-01-02 01:08:04 UTC | #6

I already have one directional light the specular is removed from the shader. I would prefer not to use per-vertex lighting. 
This is my PVRTrace analysis: [url]http://codepad.org/36f9P41N[/url]
[img]http://i.imgur.com/9ymKglH.png[/img]
[img]http://i.imgur.com/ohlxeD8.png[/img][img]http://i.imgur.com/mLz4uLw.png[/img]
[img]http://i.imgur.com/5IOChJS.png[/img][img]http://i.imgur.com/0H4m3gI.png[/img][img]http://i.imgur.com/MwvMn1Y.png[/img][img]http://i.imgur.com/ufC6z8r.png[/img]

-------------------------

cadaver | 2017-01-02 01:08:07 UTC | #7

The render enables blending at the midway point, meaning it's doing additive lighting. If you have one directional light only, check that the material techniques you use all define the LITBASE pass, in which case the first (only) light should get rendered in one pass without blending. You may need to debug inside the engine to more clearly find out why it fails to use the LITBASE optimization. The blending in this case will be the framerate killer, and drawcalls or state changes themselves shouldn't be a problem.

For example the environment mapped diffnormal technique doesn't define LITBASE, instead the base pass first renders the ambient + environment, then lights are additive blended. This is a bad technique to use on fillrate limited mobiles.

[code]
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="base" vsdefines="NORMALMAP ENVCUBEMAP" psdefines="NORMALMAP ENVCUBEMAP" />
    <pass name="light" vsdefines="NORMALMAP" psdefines="NORMALMAP" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" vsdefines="NORMALMAP" psdefines="PREPASS NORMALMAP" />
    <pass name="material" vsdefines="NORMALMAP ENVCUBEMAP" psdefines="MATERIAL NORMALMAP ENVCUBEMAP" depthtest="equal" depthwrite="false" />
    <pass name="deferred" vsdefines="NORMALMAP ENVCUBEMAP" psdefines="DEFERRED NORMALMAP ENVCUBEMAP" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>
[/code]

-------------------------

sabotage3d | 2017-01-02 01:08:07 UTC | #8

Thanks a lot guys for stepping in as I am bit lost. This is my GLSL shader that I am testing with:[url]http://codepad.org/YQNt744W[/url]    and this is my technique code: [url]http://codepad.org/j7ERKFfh[/url]  (ENVCUBEMAP is currently unused )
I noticed that I have  blend="add"  but I am not sure what is good alternative for mobile just to remove the blending? I am using the same material on all the prefabs in the scene I am doing clonning the original one and just changing the texture. This is my code: 

[code]    Material* material = cache->GetResource<Material>("Materials/SimpleMobile.xml");
    SharedPtr<Material> mat = material->Clone();
    
    Texture2D* texture = cache->GetResource<Texture2D>("Textures/" + className + ".png");
    mat->SetTexture(TU_DIFFUSE, texture);
    objectNode->GetComponent<StaticModel>()->SetMaterial(mat);[/code]

-------------------------

cadaver | 2017-01-02 01:08:07 UTC | #9

A "good" technique should look like this (this is Diff.xml)

[code]
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
</technique>
[/code]

It only uses the "light" (additive) pass from second per-pixel light onward, while "litbase" renders the first per-pixel light without additive blending. Read [urho3d.github.io/documentation/1.5/_shaders.html](http://urho3d.github.io/documentation/1.5/_shaders.html) for more clarification.

-------------------------

sabotage3d | 2017-01-02 01:08:07 UTC | #10

Thanks cadaver. I tried your technique and but I am not getting any performance increase the FPS is exactly the same.

-------------------------

sabotage3d | 2017-01-02 01:08:07 UTC | #11

Thanks Sinoid. I did the trace on mobile using PVRtrace. This is the PVRTune benchmark if it is of any use: [url]http://i.imgur.com/X7CYczE.png[/url]. I tried applying the same material without cloning and texture to all the assets and the FPS is the same it must be the batching. I think the moving nodes are killing the GPU quickly. I don't think Urho3d is batching together assets with the same model and material like Unity does. I am thinking of investigating this types of batching: [url]http://docs.unity3d.com/Manual/DrawCallBatching.html[/url]  and  what Smash Hit is using which is similar [url]http://tuxedolabs.blogspot.se/2014/04/smashing-tech.html[/url]

-------------------------

boberfly | 2017-01-02 01:08:08 UTC | #12

A good read is here as well:
[gdcvault.com/play/1015331/Bringi ... -to-Mobile](http://gdcvault.com/play/1015331/Bringing-AAA-Graphics-to-Mobile)

If you want shadows then something like what's explained here is what you may need to do. Sure it's not accurate (it just multiplies over the top of the background) and doesn't have self-shadowing either, but the SGX540 is fairly old now. Urho3D won't do this approach out of the box either.

I remember porting Horde3D for the first time and using only one forward light on an N900 with the 'knight' test demo (which cadaver might know of the one), 2-3fps on an SGX535 800x480 res :slight_smile: it could only do one rendered pass with some baked lighting on it, and Horde3D wasn't as flexible and didn't do the litbase optimisation out of the box either. The spec and forward light would also benefit from baking down to a lookup texture instead of doing a pow operation. 

This has some info of what I mean, and baking phong shaders to a lookup texture:
[aras-p.info/texts/files/FastMobi ... ph2011.pdf](http://aras-p.info/texts/files/FastMobileShaders_siggraph2011.pdf)

For my app Pugsy I opted to just bake in a pre-defined light direction on the dog's head in Maya with an unlit shader instead of doing any lighting dynamically, however the eyes had a transparent spec dot on the lenses and used the regular forward renderer for those only, as it only rendered to a tiny fraction of the screen. I got 60fps on any decent mobile hardware for the time back in late 2012/early 2013, and like 30fps on crappy mobiles (arm6-level hardware which had ES2.0 and early ipads).

Good luck!

-------------------------

sabotage3d | 2017-01-02 01:08:08 UTC | #13

Thanks a lot guys. Sinoid I am would try static batching but I am not entirely sure how to update the animated transforms on the nodes. I am thinking of tagging instances with id attribute and then in the batching stage I will just merge all the instances in one vertex buffer and apply the transforms based on the id attribute either in glsl or C++. What I am after is one draw call per material. boberfly I know the hardware is old but I am comparing it to other games which run quite smoothly on the same device like Smashhit. I just want to make my game more friendly to older devices. Sinoid helped me with PBR shader for mobile it works great but is killing the FPS if I reduce the draw calls I might have a shot at it. Shadowing is not a big problem for me ideally it would just work on higher-end devices. In terms of CPU and memory usage Urho3d is performing amazing so far.

-------------------------

sabotage3d | 2017-01-02 01:08:16 UTC | #14

Thanks a lot Sinoid I will try it out tonight.

-------------------------

sabotage3d | 2017-01-02 01:08:17 UTC | #15

Thanks a lot Sinoid I will try it on mobile and see if it makes difference or worth the effort to investigate dynamic batching.

-------------------------

sabotage3d | 2017-01-02 01:08:49 UTC | #16

Hey guys I am doing some tests with static and dynamic batching I am getting some promising results that I would like to share. In my test I have 900 cubes with 512x512 uv texture grid. I am testing creating nodes vs merging in one vertex buffer and transforming in the shader. On my old tablet I am getting 25-30 FPS looking at all the cubes and it gives me 900 batches, when I do the fake instancing I am getting good 60 FPS with 1 single batch. The same stats apply when I animate the transforms of the cubes.
[b]Static[/b]
[img]http://i.imgur.com/fKHCOqv.png[/img]

[b]Animated[/b]
[img]http://i.imgur.com/SCdwAWU.png[/img]

-------------------------

