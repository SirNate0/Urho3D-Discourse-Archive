spwork | 2019-01-03 16:22:33 UTC | #1

 I have plans to transplant a game that has been written on PC.
Who can give me an example: a simple example of how Urho3d demo can be built into Android programs, using gradle to build, who has a good open source example to tell me the address

-------------------------

weitjong | 2019-01-06 03:47:29 UTC | #2

I don't think there is. I believe if you can find one, it could be in a way not originally intended. As you already know that our new Gradle build system for Android platform was just in early development stage in the master branch around July last year, it has not been officially released yet. Also, I would say we have only just started the process. At the moment it does not provide support for downstream projects to incorporate the Urho3D AAR into their own project yet. Actually in the previous Ant build system for Android in release 1.7 or before, we also did not provide any official support for that. However, last year I have a plan to develop a new custom Gradle plugin for that purpose (but I was side track to do the dockerized build environment and taking a long break after that). I will not make any promise that I will carry out my original plan due to my aging eye problem. So, don't wait for it if you plan to do any Android development soon.

-------------------------

