najak3d | 2022-01-17 09:32:04 UTC | #1

We're wanting to establish the best path from "3D artist" to Urho3D, so that we can pay for custom models, or get them from turbosquid.

Currently, our favorite path is to just ask for .blend files directly so that they can be readily viewed from inside Blender without modification.  (or another format that Blender also works super well with)

Currently, there appears to be several competing plugins for Blender:

1. The original plugin that works with Blender 2.73.

2. Another repo which seems to say it now support Blender 2.8.
https://github.com/reattiva/Urho3D-Blender/tree/2_80

3. Another repo from @1vanK, which he says works for Blender 2.8.
https://github.com/1vanK/Urho3D-Blender/tree/2_80

4. @dertom repo : Expounded version with in-Blender renderer, and he seems to say it works for 3.0 now.
https://github.com/dertom95/Urho3D-Blender/releases

5. OR -- should we instead be using AssetImporter.exe, and if so, which model formats are best to use?

(By default, we tend to prefer Blender method, because it allows us to do some quick QA on the model BEFORE converting it to Urho, which helps narrow down "root cause" of any issues; ie.. was it the 'source', the 'converter', or Urho itself.)

===
**We were hoping to skip the phase of "trying them all out", and instead see if we can first get some hints/opinions from the forums experts who might be able to steer us better.**

What of these is currently "the best" and why?

-------------------------

1vanK | 2022-01-17 10:27:56 UTC | #2

[quote="najak3d, post:1, topic:7129"]
Another repo from @1vanK, which he says works for Blender 2.8.
[GitHub - 1vanK/Urho3D-Blender at 2_80](https://github.com/1vanK/Urho3D-Blender/tree/2_80)
[/quote]

This is just a fork I made to create a PR https://github.com/reattiva/Urho3D-Blender/pull/97
The request was never accepted because reattiva was missing. The original version is not finished and does not export materials in Blender 2.8

-------------------------

dertom | 2022-01-17 11:22:07 UTC | #3

With my addon is the problem that you would have to create materials specifially for urho3d. I have a material-nodetree inside of blender that let you create those (selecting techniques, textures and such).
So this might to be tedious work....(*)
Are we talking about animated or static meshes? Static meshes should (once you have the urho3d-materials attached) work. But I guess there are also constallations constellations that will not. 

With animated meshes I have problems all the time....
I consider my addon in proof of concept-state (especially the code got a bit messy, mea culpa ;) ). From time to time it even crashes blender but other than that it has some nice features (noone knows of) ;)

(*)
I actually have an "unstable" feature that tries(!) to create urho3d-materials from principled nodesetup (without guessing the right technique) but(!) as I just found out it is broken and I haven't it actually really used by myself. (Created the feature and never really used it). Seems my json2nodetree plugin doesn't produce input/output-sockets anymore...But still this setup is no fun. I will have a look after work but can't promise anything.

-------------------------

Modanung | 2022-01-17 13:27:20 UTC | #4

AssImp could also be built into your editor/viewer. It needn't be artist repelling terminal magic.

-------------------------

throwawayerino | 2022-01-17 15:26:05 UTC | #5

I did update upstream Assimp to import models, but materials are still broken and someone needs to update Urho's AssetImporter

-------------------------

najak3d | 2022-01-17 21:47:42 UTC | #6

We too are experiencing issues with AssetImporter, but it's hard to tell root-cause, or how to fix.  We get varied behavior depending upon model types -- 3ds, vs dae vs fbx, etc...    And none seem to "really work"; all methods seem to have failures/issues, but I'm new, so figure I'm missing something.

So I figured it was worth a shot asking around here, to see "what are Urho3D users using that does work best?"

The reason we like .blender, is that this is also a great place to create new assets, and many of the assets we're seeking were created in blender.   Also, blender can import all formats pretty well... 

So we believe the best pipeline might be reliant upon Blender.
1. Import (or create) assets in Blender. (Here we have a solid QA checkpoint.)
2. Export from Blender to Urho3D.
3. Done.

Then the pipeline is relatively short, and you have a very clear "QA checkpoint" with blender itself, because we could make Blender vs. Urho3D work in WYSWYG fashion.

**Our current view is that @dertom has something that is the closest to what we're looking for, if only we can get it working, reliable, and documented.**

==
We are working on a new game platform called "Urholonia" which combines Urho3D and Avalonia -- invented by @elix22 who did the heavy lifting so far.   With Urholonia, you will be able to write In-Game UI's as well as the Moddding-toolset all using Avalonia UI.   All in .NET/C#, aiming to become the preferred solution for .NET game developers, or anyone needing 3D visualizations/simulations.

-------------------------

najak3d | 2022-01-17 20:37:59 UTC | #7

In the meantime, we'll just export from Blender to intermediate format, then use AssetImporter to convert to Urho format.    Which is the favored intermediate format?   IIRC, both DAE and FBX seemed to be the best from our experience.

-------------------------

