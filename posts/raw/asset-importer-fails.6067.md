CatPawns | 2020-04-06 23:36:41 UTC | #1

Hello am using blender- Urho exporter and this shows up 
ERROR: Failed to execute AssetImporter to import model

cannot even import a basic cube!

-------------------------

Lumak | 2020-04-07 15:53:52 UTC | #2

I think you're using the wrong exporter. There's exporter specifically written for Blender: https://github.com/reattiva/Urho3D-Blender

-------------------------

CatPawns | 2020-04-08 19:59:56 UTC | #3

Thanks, i read a bit the source code in the end and figured my mistake.

-------------------------

SirNate0 | 2020-04-08 20:08:12 UTC | #4

Glad you got it fixed! For the sake of future users who might encounter a similar issue, was the problem just using the wrong exporter or was it something else?

-------------------------

CatPawns | 2020-04-09 02:01:45 UTC | #5

I was using the wrong exporter, the documention its a bit unclear of what to do, fbx seems to import fine by the way, blender exporter lacks of proper a tutorial there are a wiki but it suposes that you already knows about urho3d.

-------------------------

1vanK | 2020-04-09 05:11:52 UTC | #6

[quote="Lumak, post:2, topic:6067"]
https://github.com/reattiva/Urho3D-Blender
[/quote]

This is obsolete. I sent a PR https://github.com/reattiva/Urho3D-Blender/pull/97 , but it seems that reattiva is no longer interested in the exporter. Use https://github.com/1vanK/Urho3D-Blender/tree/2_80 instead. 

[quote="CatPawns, post:5, topic:6067"]
blender exporter lacks of proper a tutorial
[/quote]

May be small video helps you https://www.youtube.com/watch?v=O0h12-2Hnq0

-------------------------

Modanung | 2020-04-09 12:48:52 UTC | #7

@1vanK I assume you are aware of @dertom's work as well?
Maybe you could combine your efforts, if you aren't already.

https://github.com/dertom95/Urho3D-Blender

I also made a [short video](https://discourse.urho3d.io/t/information-source-how-to-exporting-lods-with-blender/2083) about exporting LODs a while ago, for when you get to that point.

-------------------------

1vanK | 2020-04-09 12:48:43 UTC | #8

There are no plans, because in my free time I do auto-bindings

-------------------------

dertom | 2020-04-10 00:15:18 UTC | #9

[quote="Modanung, post:7, topic:6067"]
I assume you are aware of @dertom’s work as well?
[/quote]

Im also a bit busy atm. We just started Early Access last week and it was a bit stressy and still kind of is, but I think I can go back to normal soon ;)

The exporter's stability is actually ok (maybe because I know what to use and how). The problem with my exporter fork is that I broke it up in several blender addons (beside the urho3d-exporter, one for creating blender-nodes from json(universally usable no dependencies to urho) and one for using a message queue as communication between the blender and an urho3d-runtime that creates the previews. for that I rely on pyzmq what needs to be added as module in blender's python. I had and still have in mind to connect more functionality from other 'nodes' and interconnect them via this message-queue. e.g. some kind of project-deployment-system,... some asset-transformation-system(e.g. to create assets for different deployments...).... not sure if that will ever happen ;) ).
you see my approach is not very user friendly and I'm not very enthusiatic in promoting the thing because I'm not too kind of doing support for the cases that don't work ;) Eventhough I see it more as 'take it or leave it'-ware :D, I will try to answer any constructive question ;) The project is still alive and I will go on working on it...but @1vanK 's approach is much more user friendly.

-------------------------

jmiller | 2020-04-10 01:54:55 UTC | #10

Anecdotally, I have used the various branches (now default) of @dertom's addon(s) under linux since inception and feel a bit spoiled.. as it has set some high marks for how flexible and fast a workflow can be *and I'm willing to offer help as well where I can.

-------------------------

