TheGreatMonkey | 2018-11-04 08:32:44 UTC | #1

I'm trying to compile from the latest commit to the master branch, but I keep getting the following error when building the Urho3D project.

Error    LNK1179    invalid or corrupt file: duplicate COMDAT '??_9File@Urho3D@@$BBA@AA'    Urho3D    \Urho3D\IOAPI.obj

-------------------------

S.L.C | 2018-11-04 10:39:05 UTC | #2

See if this helps https://github.com/urho3d/Urho3D/issues/2362#issuecomment-420070574

-------------------------

TheGreatMonkey | 2018-11-04 18:28:58 UTC | #3

Yeah, that thread helped a lot. We're not using Angel script so I just disabled it.

-------------------------

mrchrissross | 2018-11-04 22:34:40 UTC | #4

I'm having the same problems unfortunately, 

My error seems to be: LNK1104 cannot open file C:\Users\Chris Ross\Documents\GitHub\Urho3DProject\Project\Build\bin\UrhoProject_d.exe

Some PC's build, and some don't :confused:

-------------------------

TheGreatMonkey | 2018-11-04 23:17:38 UTC | #5

Is that the only error you're getting on the PC's that don't build?

The only time I ever get that error is if the executable is still open for some reason blocking Visual Studio from writing to it.

-------------------------

