gawag | 2017-01-02 01:04:49 UTC | #1

There are three things about Urho's shadows that or bugging me:

[img]http://vignette3.wikia.nocookie.net/urho3d/images/b/b6/USP_terrain-mesh_vertex_colors.jpg/revision/latest/scale-to-width/320[/img]
[url]http://vignette2.wikia.nocookie.net/urho3d/images/b/b6/USP_terrain-mesh_vertex_colors.jpg/revision/latest?cb=20150422212706[/url]
- there is some blocky flickering when the shadow is close to the shadow caster, as can be seen in this image on the orange mountain edge in the lower part of the screen. This is typical for self shadowing. Here it's also causing some stripes. This seems to have to do with the fifth(?) parameter of CascadeParameters that sets the shadow starting distance, but I want the shadows to start close.

[img]http://vignette3.wikia.nocookie.net/urho3d/images/e/ec/USP_terrain-mesh_vertex_colors3.jpg/revision/latest/scale-to-width/320[/img]
[url]http://vignette3.wikia.nocookie.net/urho3d/images/e/ec/USP_terrain-mesh_vertex_colors3.jpg/revision/latest?cb=20150422215037[/url]
- Urho seems to use four images(?) for shadow with different resolution for different distances: There is always a thin, black, blurry edge between those "zones". You can see this "dotted" edge here starting directly right of the "Esc = quit." text at top and going through the whole image. It's much more visible and annoying when the camera is moving.

- can there be more of those "zones"? I'm using these parameters: "light->SetShadowCascade(CascadeParameters(5.0f,10.0f,50.0f,1000.0f,0.01f,0.5f));" and the jump to 1000 is quite big, but when making the lower values bigger, the closer shadows get too blurry. Two to four more zones would make this much better.

Can the shadows be improved somehow?
I'm using a relative up to date Git version but those issues have been the same in the latest stable.

-------------------------

cadaver | 2017-01-02 01:04:49 UTC | #2

The blocky self-shadowing filtering close to the camera is due to the combination of using slope-scale depth bias, hardware shadow maps, and the hardware filtering. You could try converting the shadow maps to eg. R32F format and doing all filtering manually in the shader. This requires engine modifications. The effect will also possibly be reduced if you reduce or zero the slope-scale depth bias, and adjust instead the constant depth bias higher. This will lead to uglier peter-panning, though.

You should be able to make smooth "transition zones" in the shadow sampling shader code by sampling both cascades when close to the transition distance. 

Increasing the amount of directional light cascades to more than 4 will also need engine and shader modifications.

None of these modifications are likely to be made in Urho's official version, as they would worsen performance and complicate the code.

-------------------------

gawag | 2017-01-02 01:04:49 UTC | #3

Hm, that's unfortunate.
Found an article describing some technical details about shadow maps, that may help to understand the issues: [msdn.microsoft.com/en-us/librar ... 85%29.aspx](https://msdn.microsoft.com/en-us/library/windows/desktop/ee416324%28v=vs.85%29.aspx)
Would be good if the shadow functions would be better documented. What is this shadow focus thing? (Light::SetShadowFocus(FocusParameters))

[quote]...The effect will also possibly be reduced if you reduce or zero the slope-scale depth bias, and adjust instead the constant depth bias higher.[/quote]
That made everything much worse (added much more artifacts).

[quote]You should be able to make smooth "transition zones" in the shadow sampling shader code by sampling both cascades when close to the transition distance. [/quote]
Can that be done without spending a lot of time editing the engine and/or writing super special shaders?

I made more experiments with the parameters. Currently I'm using these:
[code]
light->SetShadowBias(BiasParameters(0.0000025f,1.0f));
light->SetShadowCascade(CascadeParameters(20.0f,60.0f,180.0f,560.0f,0.1f,0.1f));
light->SetShadowResolution(1.0);
[/code]
Observations:
- increasing the first parameter of BiasParameters causes peter-panning (the shadow to be detached / to far away from the caster).
- setting the second parameter below 0.1 causes a lot of artifacts depending on the face angle relative to the light
- the first four parameters of CascadeParameters should not increase too fast. 2 is good (like 10, 20, 40...), over 3 makes the cascade differences too big and ugly.
- the last two parameters of CascadeParameters seem to do nothing at all. Tried with values like 0, 1 and 100 and nothing changed?
- SetShadowResolution can be set between 0.25 and 1.0 (as the documentation says), 0.25 makes the shadow resolution go very low and this should be kept at / set to 1.0.

Can the shadow resolution be increased? Or set (globally) somewhere else? That would make more cascades less important.

Is there really no way of making these artifacts less bad? I mean these blocky stripes left of the player at the column:
[img]http://oi60.tinypic.com/zwhv6p.jpg[/img]
Big: [url]http://i.imgur.com/Kcyh4Tp.jpg[/url]

[quote]None of these modifications are likely to be made in Urho's official version, as they would worsen performance and complicate the code.[/quote]
Yeah but it looks quite terrible as it is now (unless I'm missing something), see screenshot.
It could be made optional/adjustable like most games are offering settings to adjust the quality depending on the machine performance. Like picking between 4 and 8 cascades.

-------------------------

cadaver | 2017-01-02 01:04:50 UTC | #4

Shadow focusing means "zooming in" the shadow camera so that only the casters / receivers are tightly rendered into the shadow map. This may aid shadow resolution, but also makes it more dependent on the camera angle and the objects that are being shown.

You can set the shadow map base pixel size by calling Renderer::SetShadowMapSize().

The cascade transition thing should be possible to make with lighting shader changes only and it shouldn't be too hard. 

You see the same kinds of self-shadowing artifacts also in AAA games; shadow mapping is almost never problem-free. It's also a question of art style, non-photorealistic graphics with solid color textures will show the artifacts worse.

-------------------------

friesencr | 2017-01-02 01:04:50 UTC | #5

John Carmack stated he thinks shadow maps will be the tipping force to raycasting.

-------------------------

gawag | 2017-01-02 01:04:50 UTC | #6

Oh that's a very interesting topic   :laughing: 

The shadow maps default size seems to be 1024. Settings it to 4096 made the shadows super sharp and everything much better.  :mrgreen: (and still 60 FPS)
Increasing it to 16384 increased the loading time I think but I couldn't see any further improvement (still 60FPS). 

Also found a Renderer::SetShadowQuality setting and tried values like 0.1, 1 and 10 and could not see any difference?

The issues are all still there but a bit better. The biggest is still the blocky, flickering stripes at some faces when in a very flat angle towards the light. (EDIT: Saw that "Space Engineers" has the same issue but more blurry)
The cascade transition line is super thin. I tried enabling anti aliasing / multi sampling with engineParameters_["Multisample"]=16; and values like 2, 8 and 16 in the hope that this would improve something but I can't see any difference at all.
Is engineParameters_["Multisample"]=16; the right way to enable anti aliasing?
The other parameters work:
[code]
    virtual void Setup()
    {
        engineParameters_["FullScreen"]=false;
        engineParameters_["WindowWidth"]=1280;
        engineParameters_["WindowHeight"]=720;
        engineParameters_["WindowResizable"]=true;
        engineParameters_["Multisample"]=16;
    }
[/code]

-------------------------

cadaver | 2017-01-02 01:04:51 UTC | #7

Hardware antialiasing will help eliminating jaggy polygon edges, but only in the backbuffer. It will not help shadow maps, which are non-antialiased textures.

SetShadowQuality expects the SHADOWQUALITY bit combinations defined in GraphicsDefs.h. That only controls shadow map filtering & 1 vs 4 samples mode. You can see its proper use in the samples' common code, which allows cycling through the quality modes by pressing the key '6'. It's not an enum due to internal bit logic tied to it.

-------------------------

