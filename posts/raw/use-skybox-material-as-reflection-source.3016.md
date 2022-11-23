godan | 2017-04-17 17:13:02 UTC | #1

Is it possible to use the Skybox material as the environment map for reflective materials? Ideally this would also work with the PBR pipeline. My understanding is that currently only a TextureCube resource can be used - and in the case of PBR, only the texture cube associated with the Zone is used.

My goals is just interact with the Skybox material (say, something like this):

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/19febbe260deee27c58d67e55888a7c85306d55a.jpg" width="690" height="396">

-------------------------

godan | 2017-04-17 17:19:01 UTC | #2

For instance, in the "ForwardDepth" render path, it looks like the viewport is being sampled for a pass called "Refract". I don't know what that does, but it seems close-ish to what I'm after....

```
<renderpath>
    <rendertarget name="depth" sizedivisor="1 1" format="lineardepth" />
    <command type="clear" color="1 1 1 1" depth="1.0" stencil="0" output="depth" />
    <command type="scenepass" pass="depth" output="depth" />
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
</renderpath>
```

-------------------------

godan | 2017-04-17 18:37:19 UTC | #3

Kind of getting the idea now...

https://youtu.be/pGPO16j-IFM

-------------------------

godan | 2017-04-20 10:52:46 UTC | #4

So, rather than using some kind of screen space hack, I wrote a reflection probe component. This ties in beautifully with the existing PBR pipeline. Check it out:

https://youtu.be/01OzZ-pSkV0

-------------------------

sabotage3d | 2017-04-18 15:29:57 UTC | #5

Nice! Is there any slowdown it is hard to say from the video?

-------------------------

godan | 2017-04-18 15:37:08 UTC | #6

> Nice! Is there any slowdown it is hard to say from the video?

I haven't run the profile on this, but qualitatively, no noticeable performance hit. I'm using 1024 px^2 for each cube face, which might not be optimal on all platforms/hardware configs.

Also, I haven't totally figured out the question of when to update the reflection probe. If nothing is changing, then it is overkill to update every from or even on a fixed update loop. Also, you might just want to have this in the editor and bake the probe to a texture on disk...For now, I've just implemented an Update() function that I have tied in to my specific use case.

I was thinking of doing a PR for this - would it be useful to anyone else?

-------------------------

Modanung | 2017-04-18 19:58:44 UTC | #7

_Very_ nice
For less-shiny (or smaller) objects you wouldn't need as high a resolution since it gets blurred anyway, but this would still make the objects fit really nice into the environment.
And I guess it would need some interpolation to work well on moving objects?

-------------------------

godan | 2017-04-20 10:52:46 UTC | #8

Too much fun:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/307fc7dd7900e7a5ae83cf62c6436bf041d5a433.jpg" width="690" height="359">

-------------------------

cmd | 2020-06-25 14:26:08 UTC | #9

I've been pondering implementation of a reflection probe component for Urho3D (something like what you get builtin to Unity) So, I would love to see a PR for this, or at least a look at your code? I could help with testing and tweaks if you wanted to try and make a PR out of it.

-------------------------

godan | 2020-06-25 14:50:09 UTC | #10

Sure, here you go: https://github.com/MeshGeometry/IogramSource/blob/master/Components/ReflectionProbe.cpp

-------------------------

cmd | 2020-06-25 15:13:43 UTC | #11

Excellent. Thank you.

-------------------------

cmd | 2020-06-26 13:46:54 UTC | #12

Seems to be working well for me. Thank you again.

![ReflectionProbeTest|682x500](upload://1ggMk4DYXP0uXTWVKMZhnGWDKwu.png)

-------------------------

cmd | 2021-06-03 11:36:07 UTC | #13

Sorry for bumping this conversation again a year later, but I was wondering if anyone had any ideas about fixing a reflection scaling issue when using this probe technique. 

I'm using it to simulate mirrors in a scene, and while I can see that the technique can only ever be an approximation of a real reflection, I noticed that in Unity, the reflection probe has a option for "box projection" which seems to help a lot in making scale in reflections look more correct.
 
More info here:
https://docs.unity3d.com/Manual/AdvancedRefProbe.html

So, I'm wondering about the feasibility of implementing something like this for Urho, but I'm feeling a bit out of my depth. Would this need some work at the shader level to implement?

-------------------------

