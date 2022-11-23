dev4fun | 2018-03-21 22:41:44 UTC | #1

Hey guys, Im using a same skeleton to separate my character on many parts of meshes (body, hands, etc), but I got a problem and I dont found any solution until now.

Body:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/8/8445ec853892e6f64400d44b8d44eb09ce214662.png'>

Hands:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/c/caa23cd029eb54645369007288993240efff6c88.png'>

I want to combine both models to share same animation.. The problem its:
when I import firstly body, this will be the master model, but Urho selects only used bones, and body dont use same bones of hands...

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/9/904df3a6dccce1438a82febe3e0d6ee1e22b3b0f.png'>

This way I get the hands imported, but not your bones. I need exactly this way, because it isnt a clothes, so will not have a "master model" with all bones. I've already tried to made a custom mesh using all bones, change RootNode and nothing worked.

Demonstration of the problem:
https://puu.sh/zMI0h/95af1304c5.mp4

Someone knows what I should to do?
Thanks.

-------------------------

Lumak | 2018-03-21 23:50:15 UTC | #2

If you're using AssetImporter, use the **-s** option - 
[code]
"-s <filter> Include non-skinning bones in the model's skeleton. Can be given a\n"
[/code]
Example 1: include all
[code]
AssetImporter model mymodel.fbx mymodel.mdl -s
[/code]

Example2: only specific joints/bones
[code]
AssetImporter model mymodel.fbx mymodel.mdl -s "Leftfinger01;Leftfinger02;Rightfinger01;RightFinger02"
[/code]

It's easier to **go with the example1** to import the body model and same for gloves.

-------------------------

johnnycable | 2018-03-22 17:13:20 UTC | #3

By the way...
Can I use a full rig with just part of the mesh hidden? I mean

![45|293x500](upload://pwvNz92APGoGs41TKaPu1fF0mtJ.png)

Just import the rig and selectively hide/unhide body parts at will? I haven't tried it yet in Urho...

-------------------------

Sinoid | 2018-03-22 18:46:50 UTC | #4

Nope. Shouldn't be particularly hard to implement if you really need it though, it'd just be changing the batch and transform management in StaticModel and AnimatedModel I believe.

-------------------------

