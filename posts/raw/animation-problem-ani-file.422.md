kestli | 2017-01-02 01:00:18 UTC | #1

hello people..
I have a ploblem with .ani files...
I have a blender file FPS animation width many actions (shoot, reload, etc..) I export this actions separately (shoot.ani, reload.ani, etc).
Wen I load this animation (.ani files) in Urho3D some look good and others not. 
Why?
I use AnimationController::Play(...); and assetimporter utility. 
Thanks. 

IMG 1 reload.ani
[img]http://kaestli.000a.biz/buffer/urho3d_shoot_ok.jpg[/img]

IMG 2 shoot.ani 
[img]http://kaestli.000a.biz/buffer/urho3d_shoot_bad.jpg[/img]

-------------------------

friesencr | 2017-01-02 01:00:18 UTC | #2

This looks like old blender screwing up bone weights.  Get blender 2.71.

-------------------------

kestli | 2017-01-02 01:00:31 UTC | #3

Problem solved ...  thanks  friesencr.
I have also used [url]https://github.com/reattiva/Urho3D-Blender[/url]


[video]https://www.youtube.com/watch?v=koVHJFRz-yE[/video]

-------------------------

