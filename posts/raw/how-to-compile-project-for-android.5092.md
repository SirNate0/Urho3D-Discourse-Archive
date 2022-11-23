att | 2019-04-11 01:36:31 UTC | #1

I have a game project and I can compile it for iOS, but. I donot know how to compile it for android platform. Should I put it under Samples directory and compile it?

-------------------------

weitjong | 2019-04-11 05:51:07 UTC | #2

It’s not intended to be used like that, but currently that’s the easiest way for one to get it setup. I see whether I can find some time to finish off what I have started with before we prepare the 1.8-RC.

-------------------------

fnadalt | 2019-04-13 01:08:10 UTC | #3

I managed to compile a game prototype for android, 48mb apk. Having the lib at URHO3D_HOME/android/urho3d_lib/build/..., I set up my project dir like this:
* Copy the original android and buildSrc, gradlew script and related files from urho3d home dir, link Source and CMake dirs, write a CMakeLists.txt like dewcripted in the docs
* Set up your own Data dir under android/launcher-app/...
* Restore some header (.h) file links broken somewhere under android/... (look them up, can't remember now which are those)
* ./gradlew build 
Tell me if you succeded or don't understand something...

-------------------------

weitjong | 2019-04-13 02:09:05 UTC | #4

The headers is part of the AAR (depends on how you build the library). Stay tune, it will be much easier than this :)

-------------------------

weitjong | 2019-04-13 04:36:34 UTC | #5

I just created a new account in bintray/jcenter. Will figure out how to push the Urho3D AAR build artifact there.

-------------------------

Miegamicis | 2019-04-13 08:43:21 UTC | #6

That's pretty cool!     .

-------------------------

weitjong | 2019-04-15 02:03:55 UTC | #7

A post was split to a new topic: [Publish Urho3D Android Library to bintray/jcenter](/t/publish-urho3d-android-library-to-bintray-jcenter/5103)

-------------------------

