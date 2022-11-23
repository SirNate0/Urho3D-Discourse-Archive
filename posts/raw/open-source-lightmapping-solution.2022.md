namic | 2017-01-02 01:12:20 UTC | #1

Does anyone know any good open-source lightmapping tool? Something like Unity's Beast, but obviously not with that many features. I've recently migrated from the Darkplaces engine to Urho3D and my maps looked great with the q3map compiler. Unfortunately, the realtime lighting and shadows in Urho are not that good in comparison to Darkplaces, mostly because of the lightmapping in BSP.

-------------------------

1vanK | 2017-01-02 01:12:21 UTC | #2

blender?

-------------------------

magic.lixin | 2017-01-02 01:12:21 UTC | #3

[github.com/ands/lightmapper](https://github.com/ands/lightmapper)

-------------------------

namic | 2017-01-02 01:12:21 UTC | #4

Blender requires me to build the levels inside of it, instead of allowing me to create independent modular pieces and build the level inside the editor (which was one of the biggest reasons i switched to Urho).

-------------------------

rasteron | 2017-01-02 01:12:21 UTC | #5

[quote="namic"] the realtime lighting and shadows in Urho are not that good in comparison to Darkplaces, mostly because of the lightmapping in BSP.[/quote]

What's the matter, you don't like Urho3D's new PBR?  :wink: 

[video]https://www.youtube.com/watch?v=tz7p-VzaFbU[/video]

-------------------------

namic | 2017-01-02 01:12:22 UTC | #6

PBR was already released? Anyway, PBR won't exclude the need for a lightmapping solution. They can only improve each other.  :smiley: 

ands/lightmapper looks really nice, i'm going to explore how it works and see if i can integrate it.

-------------------------

Dave82 | 2017-01-02 01:12:22 UTC | #7

[quote="magic.lixin"]https://github.com/ands/lightmapper[/quote]

This library looks absolutely awesome ! Too bad it's OGL only . Very amazing that its only a single header...
Would be cool if someone could test the performance

-------------------------

sabotage3d | 2017-01-02 01:12:22 UTC | #8

This looks pretty cool. I wonder how fast is it, anyone tried it yet?

-------------------------

rasteron | 2017-01-02 01:12:23 UTC | #9

[quote="sabotage3d"]This looks pretty cool. I wonder how fast is it, anyone tried it yet?[/quote]

I already build this with Ubuntu 14.04 but have not tried as I'm just using VBox and it's throwing out ARB profile errors due to a dummy gfx setup.

When building the example: CMake also throws out Missing Vulkan library if it is not installed and I'm not sure if it is required. There's also C99 errors so I made a bit of changes on the makefile.

I think I'll try this again with Win7 and VStudio, I'm getting a file not found 'xinput.h' on MinGW..

-------------------------

rasteron | 2017-01-02 01:12:23 UTC | #10

[b]@namic[/b]

[quote="namic"]PBR was already released? Anyway, PBR won't exclude the need for a lightmapping solution. They can only improve each other.  :smiley: [/quote]

Yes, just clone git master. Agreed, but that will really depend on your scene. 

BTW, you already got the best FOSS Lightmapper using Blender and even better if you're gonna use [b] Cycles Baking[/b] (search "cycles lighmapping or baking")

Here's a live demo in three.js with Cycles lightmapping

[charliehoey.com/threejs-demos/cy ... ing-2.html](http://charliehoey.com/threejs-demos/cycles-baking-2.html)

[img]http://i.imgur.com/Y5rLMcVl.jpg[/img]

More examples using cycles lightmapping:

[blenderguru.com/tutorials/i ... ng-cycles/](https://www.blenderguru.com/tutorials/introduction-baking-cycles/)

[img]https://s3.amazonaws.com/blenderguru.com/uploads/2014/07/LivingRoomFrame-673x402.jpg[/img]

-------------------------

namic | 2017-01-02 01:12:24 UTC | #11

Yeah, i'm aware of Cycles. I actually use Blender as my DCC tool. Unfortunately, lightmapping in Blender requires me to build the levels inside of it, instead of allowing me to create independent modular pieces and build the level inside the editor (which was one of the biggest reasons i switched to Urho).

Back in Darkplaces, i had to build the levels inside the editor and bake from there. I don't want to use Blender for this, because i want to be able to use modular pieces: [wiki.polycount.com/wiki/Modular_environments](http://wiki.polycount.com/wiki/Modular_environments)

-------------------------

rasteron | 2017-01-02 01:12:24 UTC | #12

[quote="namic"]Yeah, i'm aware of Cycles. I actually use Blender as my DCC tool. Unfortunately, lightmapping in Blender requires me to build the levels inside of it, instead of allowing me to create independent modular pieces and build the level inside the editor (which was one of the biggest reasons i switched to Urho).

Back in Darkplaces, i had to build the levels inside the editor and bake from there. I don't want to use Blender for this, because i want to be able to use modular pieces: [wiki.polycount.com/wiki/Modular_environments](http://wiki.polycount.com/wiki/Modular_environments)[/quote]

Um ok that's great, but apparently there's no integrated lightmapping solution in Urho3D unless you make one your own. I remember there was an attempt before but it was discontinued.

[topic1103.html](http://discourse.urho3d.io/t/lightmapping/1072/1)

Either way, any opensource lightmapping solution out there you'll still have to build your scene on that tool's editor, unless you port existing solution like magiclixin suggested, which I think should be the easiest one so far with just a header.

-------------------------

