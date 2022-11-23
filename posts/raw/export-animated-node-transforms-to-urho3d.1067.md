sabotage3d | 2017-07-10 22:10:37 UTC | #1

Is it currently possible to export animated node transforms to Urho3d, from Blender or any other package ?
I wonder if we can use the .ani format for animating transforms of nodes ?

-------------------------

cadaver | 2017-07-10 22:10:32 UTC | #2

Engine functionality-wise, the .ani file is suitable for this; it's not tied to skinned models only. Look for "Node animations" in the documentation ( [urho3d.github.io/documentation/1 ... ation.html](http://urho3d.github.io/documentation/1.4/_skeletal_animation.html) )

Your mileage on getting a correctly working .ani file exported may vary, though. In theory if you have a rigid node animation created in e.g. Blender and you run it through AssetImporter (either model or scene mode) it should write out the animation also.

-------------------------

sabotage3d | 2017-01-02 01:05:11 UTC | #3

Thanks will try this out .

-------------------------

amit | 2017-01-02 01:05:41 UTC | #4

[quote="sabotage3d"]Thanks will try this out .[/quote]

Sorry to bump this, but did you get it to work?

I am able to use blender to export skinned mesh, but since my model is a robot, and i need to also do some functionality to certain parts individually, i prefer to do node base animation.
One way is to get bone animation at runtime and use individual bones position and orientation to place individual nodes to same position and orient, but i suppose there would be better ways of doing same. Also as i read the Documents, there is node animation, but no idea how to use is or export it (i am using blender plugin to export).

Any ideas?

-------------------------

Mike | 2017-01-02 01:05:43 UTC | #5

Works perfectly with blender > fbx > AssimpImporter (doesn't work with raw blender file or blender to collada)  :stuck_out_tongue: 
Integrating this feature in reattiva's blender exporter should be straightforward.

-------------------------

sabotage3d | 2017-07-10 22:10:25 UTC | #6

Yeah it works pretty well. It is really fast.

https://vimeo.com/136425837

-------------------------

stark7 | 2017-09-29 15:05:56 UTC | #7

Hey @sabotage3d s there anything special we need to do either in blender or with AssetImporter? 
When I run AssetImporter on the .fbx file as @Mike  wrote above, I get 4 .ani exports and a couple of them seem to somehow be added as children of my camera node or something along those lines.

-------------------------

