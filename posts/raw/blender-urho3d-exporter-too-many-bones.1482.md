practicing01 | 2017-01-02 01:08:05 UTC | #1

Hello, I've bought a bunch of animated models and the blender urho3d exporter complained that there are too many bones.  Is there a way around this without destroying the model?  Thanks for any help.

[img]http://img.ctrlv.in/img/15/11/11/5642d78106ec0.png[/img]

-------------------------

codingmonkey | 2017-01-02 01:08:05 UTC | #2

How much bones ? You are doing export only with deform bones or all ?

-------------------------

practicing01 | 2017-01-02 01:08:05 UTC | #3

A plethora of bones, it's just the nature of the beast.  I'm telling the exporter to export all actions.  I'm pretty sure there aren't any unused bones.

[img]http://img.ctrlv.in/img/15/11/11/56437bffdff08.png[/img]

-------------------------

thebluefish | 2017-01-02 01:08:05 UTC | #4

There are a maximum of 64 bones per for hardware skinning. It sounds like the model that you purchased just uses one big mesh for the entire thing. You will likely need to break up the model to keep each mesh under the 64 bone limit.

-------------------------

codingmonkey | 2017-01-02 01:08:05 UTC | #5

>I'm pretty sure there aren't any unused bones
You need select the armature and enter into edit mode then look on blender window menu (header) there placed: info about: blender current version, verts/faces/tris/objects/lamps ect. There is will be a [u]bones number [/u]used by this armature.

after all, you may use my fork, it supporting 128 bones by default
[url=http://savepic.su/6456389.htm][img]http://savepic.su/6456389m.png[/img][/url]

-------------------------

