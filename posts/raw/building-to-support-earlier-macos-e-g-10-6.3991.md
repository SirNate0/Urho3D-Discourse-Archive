voidhawk | 2018-02-06 02:34:26 UTC | #1

According to the docs (https://urho3d.github.io/documentation/HEAD/_building.html) I should be able to build Urho for 10.5 or newer. However, I seem to be limited to building Urho for 10.9 and newer. If I try to build for earlier versions, XCode can no longer find C++ headers such as type_traits and initializer_lists. 

Is this intended - or am I doing something wrong? If it is relevant, I can generating an XCode project, and then modifying the Deployment target from within XCode instead of using CMAKE_OSX_DEPLOYMENT_TARGET


Thanks!

-------------------------

weitjong | 2018-02-06 11:05:36 UTC | #2

That is an omission in our documentation update after we have modernized our code base to use C++11 standard in the master branch. If you need to target such an old version of macOS then you may have to stay with previous releases of Urho3D.

-------------------------

weitjong | 2018-02-06 14:23:04 UTC | #3

I also find this [link](https://blog.michael.kuron-germany.de/2013/02/using-c11-on-mac-os-x-10-8/) from a quick Google search. So, bumping the minimum supported version to 10.9 sounds sensible to me.

-------------------------

voidhawk | 2018-02-06 19:36:39 UTC | #4

Thanks for your response. 

For your information I could build support for 10.8 or later by specifying std=c++11 and stdlib=libc++. 
However according to the steam hardware survey, supporting 10.9 or later will cover a very high percentage of mac users, so that seems advisable.

-------------------------

