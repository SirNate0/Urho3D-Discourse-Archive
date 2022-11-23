WangKai | 2020-12-29 13:58:24 UTC | #1

I cannot run Samples on Ubuntu, though I can play youtube on Firefox. Please help!

```log
./01_HelloWorld 
[Tue Dec 29 21:51:15 2020] ERROR: Failed to initialise SDL subsystem: No available audio device
[Tue Dec 29 21:51:15 2020] ERROR: Failed to initialise SDL subsystem: No available video device
[Tue Dec 29 21:51:15 2020] INFO: Opened log file /home/indie/.local/share/urho3d/logs/HelloWorld.log
[Tue Dec 29 21:51:15 2020] INFO: Created 3 worker threads
[Tue Dec 29 21:51:15 2020] INFO: Added resource path /home/indie/dev/man/Urho3D/BUILD_OGL_codeblocks/bin/Data/
[Tue Dec 29 21:51:15 2020] INFO: Added resource path /home/indie/dev/man/Urho3D/BUILD_OGL_codeblocks/bin/CoreData/
[Tue Dec 29 21:51:15 2020] INFO: Added resource path /home/indie/dev/man/Urho3D/BUILD_OGL_codeblocks/bin/Autoload/LargeData/
[Tue Dec 29 21:51:15 2020] ERROR: Could not create window, root cause: 'No available video device'
```

|Distributor ID:|Ubuntu|
|---|---|
|Description:|Ubuntu 20.04.1 LTS|
|Release:|20.04|
|Codename:|focal|

It seems no big progress for desktop after so many years...

-------------------------

SirNate0 | 2020-12-29 14:12:17 UTC | #2

Did you build from source or is this one of the releases? If you did build from source, did you install all of the dependencies?

-------------------------

WangKai | 2020-12-29 14:19:26 UTC | #3

Thanks for the reply.

Yes, I built from source. I installed anything missing when the build process cannot be continued.

-------------------------

weitjong | 2020-12-30 00:40:52 UTC | #4

[quote="WangKai, post:3, topic:6643"]
Yes, I built from source. I installed anything missing when the build process cannot be continued.
[/quote]

That might be where your problem was. You cannot do that. CMake caches the past detection result in the build tree. You have to remember to nuke the build tree and redo the initial configuration again after you make changes to the system (like installing earlier missing package). Or, just rm the CMakeCache.txt in the build tree.

-------------------------

WangKai | 2020-12-30 00:40:41 UTC | #5

Thank you @weitjong! That was the issue.

![screenshot|662x500](upload://cNAHpS9CW9dCeQnliDUAL6a2fg5.jpeg) 

*When three are walking together, I am sure to find teachers among them.*

-------------------------

dertom | 2020-12-30 00:50:14 UTC | #6

[quote="WangKai, post:1, topic:6643"]
It seems no big progress for desktop after so many years…
[/quote]

Is it rude to say,that I find comments like this pathetic from people that are not even able to compile a cmake-project

-------------------------

WangKai | 2020-12-30 06:28:07 UTC | #8

Yes, it is very rude.

-------------------------

1vanK | 2020-12-30 12:45:03 UTC | #9

[quote="WangKai, post:1, topic:6643"]
It seems no big progress for desktop after so many years…
[/quote]

Then put in more effort

-------------------------

Modanung | 2020-12-30 19:00:46 UTC | #10

https://www.youtube.com/watch?v=j_QLzthSkfM&disable_polymer=true

-------------------------

