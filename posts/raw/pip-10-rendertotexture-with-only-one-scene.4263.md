Virgo | 2018-05-26 12:07:23 UTC | #1

I was wondering if we can achieve PIP in Urho3D and so I added camera control for rttCameraNode_ in sample 10_RenderToTexture.
It worked just find if rttCamerNode_ is in a different scene from the cameraNode_, but if i used it in the same scene, any camera rotation or movement can easily lead to application crash.
![Sketch|690x412](upload://iW9NXt8J3Cit8Zka8ycKNPOb9e.png)
Anyone got a solution for this?

using:
Windows 10 Home 1803
Qt creator as ide (not using any Qt library)
visual studio 2017 as compiler

-------------------------

Eugene | 2018-05-25 18:27:16 UTC | #2

1. What's the PIP?
2. What GAPI is used?
3. If you have a crash, please show callstack.
4. I moved everything into main scene in this sample, works fine.

![10_RenderToTexture_d%202018-05-25%2021-23-10-233|666x500](upload://dDKJEkO65wBfhZ4v5MNEMVbREwy.jpg)

-------------------------

Virgo | 2018-05-25 21:56:14 UTC | #3

1  PIP is "Picture in Picture".
Trying to understand terms in 2 and 3, maybe update this reply later. 
4  Did you try to rotate or move the rttCameraNode_?

I'm a middle school drop-out doing programming for hobbies, kinda uneducated, sry for my ignorance. xD

-------------------------

Virgo | 2018-05-25 23:07:29 UTC | #4

Build in Debug mode encountered tons of LNK2038 mistmatch errors

-------------------------

Virgo | 2018-05-26 11:40:18 UTC | #5

![Sketch|690x426](upload://1YyG2Ra3ZeBUKIFjOeh5Ep8dWwM.jpg)
Sry for the late reply! i finally found a way to compile in debug mode. not sure if this is the so called callstack?

-------------------------

Eugene | 2018-05-26 11:55:39 UTC | #6

[quote="Virgo, post:3, topic:4263"]
4 Did you try to rotate or move the rttCameraNode_?
[/quote]

Still works fine.
https://gist.github.com/eugeneko/e6b2752b07d863a96fc6bee7546befd4

-------------------------

Virgo | 2018-05-26 12:02:27 UTC | #7

strange, i just replaced my RenderToTexture.cpp with your code, and the application just crashed on startup!

-------------------------

Eugene | 2018-05-26 13:00:22 UTC | #8

[quote="Virgo, post:7, topic:4263, full:true"]
strange, i just replaced my RenderToTexture.cpp with your code, and the application just crashed on startup!
[/quote]

I tested things on DX9. What API do you use?
Anyway, I recommend to build Urho from source in Debug configuration.
It's quite hard to guess where and why it crashed.

-------------------------

Virgo | 2018-05-26 15:02:23 UTC | #9

![Sketch|690x427](upload://4Kfu5aE5igd7A8xQbzdonlGm3CH.jpg)
Im using Dx11, and this is the debug build, finally.


edit:
okay stupid me dont know how to track the one called this function

-------------------------

Eugene | 2018-05-26 22:17:56 UTC | #10

Fixed.
https://github.com/urho3d/Urho3D/commit/b78992ba433f2c20b3db2b8fa1cbd200b13cc78f

-------------------------

Virgo | 2018-05-26 22:17:44 UTC | #11

Just add a pointer validation check huh? :joy: never imagine the solution to my problem could be simple like this

Thanks <3

-------------------------

