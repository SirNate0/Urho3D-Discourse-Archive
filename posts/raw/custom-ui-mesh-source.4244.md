Lumak | 2018-05-24 19:27:55 UTC | #1

A method to use models(flat models) and custom shaders in UI:
repo: https://github.com/Lumak/Urho3D-Custom-UI-Mesh

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/7/76d1bb2b52cb61b7b015bebb5e184bff6b1fa773.gif[/img]

---
Post any issues here.

-------------------------

Lumak | 2018-05-20 10:38:52 UTC | #2

There might be frequent code updates, as I'm still optimizing it but I think I got the last of what I wanted to change for now.

-------------------------

Miegamicis | 2018-05-21 06:32:43 UTC | #3

I'm was seeing errors while compiling this against the master branch but I was able to fix them very quickly. Anyway here's the fixed version for the builds against the Urho3D master branch
https://github.com/ArnisLielturks/Urho3D-Custom-UI-Mesh

When building against the latest master branch I see these results:
![image|400x220](upload://vB7JreYOZP21xUlUftMdWHfJe8C.jpg)

For the 1.7 version everything works as expected

-------------------------

Lumak | 2018-05-21 08:42:46 UTC | #4

The bubble that you're seeing is from JTippetts healthmana bubble resource - there's actually two versions of it. I looked at your repo and you're using the resourcebubble.xml material file from my repo. You must be using the healthmana material in your own sandbox.

edit: I thought there were two, but I've must grabbed the earlier version of his resource, or maybe from his 1st gist post.

-------------------------

Miegamicis | 2018-05-21 07:36:03 UTC | #5

Yes, thanks. That indeed was the case. Everything look great now!

-------------------------

Lumak | 2018-05-24 11:19:54 UTC | #6

Another use case for disk/wheel UIMesh:

https://youtu.be/NMB03HPx7ts

-------------------------

elix22 | 2018-05-24 14:11:38 UTC | #7

The Racer HUD  looks great 
How did you do it ?

-------------------------

Lumak | 2018-05-24 15:52:31 UTC | #8

The tachometer uses a similar method as the red-wheel in the gif.

-------------------------

Pencheff | 2019-03-24 12:28:12 UTC | #13

In my opinion this feature should be added to Urho3D. Currently there's no way to modify the material an UIElement uses, since UIBatch has no material or shader parameters.

-------------------------

Pencheff | 2019-03-27 17:03:03 UTC | #14

![custom-ui-mesh|690x373](upload://b3fO6aBMsl3XtzZIV3cAX27QwlN.png) 

[https://github.com/PredatorMF/Urho3D/tree/CustomUIShader](https://github.com/PredatorMF/Urho3D/tree/CustomUIShader)

I've tried to simplify, seems to be working great, thanks @Lumak for your work.
UIBatch now has custom_material_ member so custom components could use it and also BorderImage has Material attribute. Updated AngelScript bindings.

-------------------------

Lumak | 2019-03-28 14:38:16 UTC | #15

That's a nice, clean implementation. Good work!

-------------------------

WangKai | 2019-05-26 09:10:14 UTC | #16

I used to use alpha-test value to draw the HP ball in DX9 time. The short coming is that alpha test is only 0~255 values.

-------------------------

