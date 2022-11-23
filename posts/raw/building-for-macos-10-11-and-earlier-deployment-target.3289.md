elissa-ross | 2017-06-27 14:29:04 UTC | #1

Hello! 
I'm having problems building Urho for a macOS deployment target of 10.11 and earlier. I am using Xcode, and running 10.12. I am building for Standard architectures. When I select the 10.11 deployment target I get number of linker errors (see image). Any suggestions gratefully received....
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/4ff148e302265ba03991465c10cd5054863d41ee.png" width="690" height="321">

-------------------------

weitjong | 2017-06-27 14:58:31 UTC | #2

Instead of selecting the deployment target within the Xcode IDE, use the Urho3D build option "CMAKE_OSX_DEPLOYMENT_TARGET" when configuring/generating the build tree (Xcode project). See [here](https://urho3d.github.io/documentation/HEAD/_building.html#Build_Options) for more details.

-------------------------

elissa-ross | 2017-06-27 15:14:22 UTC | #3

Thank you weitjong. 
Indeed I found this shortly after posting my question. However, the build fails for 10.10 (and earlier). It does work for macOS 10.11, but when I build for 10.10 (using the cmake build option) the errors return.

-------------------------

weitjong | 2017-06-28 04:17:32 UTC | #4

Are you reusing the same build tree location for different deployment target? If you are then you need to clean the CMake cache first before reconfiguring. It is easier to use separate build tree locations for each target.

-------------------------

