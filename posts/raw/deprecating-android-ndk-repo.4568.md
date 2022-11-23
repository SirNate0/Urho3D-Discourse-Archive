weitjong | 2018-09-26 13:49:44 UTC | #1

I am wondering why this deprecated repo https://github.com/urho3d/android-ndk got quite a number of stars/forks lately. With the new Android SDK manager the NDK can be installed easily and quite fast too. So, why do you still want to use this “hack” to get the NDK?

-------------------------

johnnycable | 2018-09-26 14:56:23 UTC | #2

What if you need two of them?
If something has not changed since last time I did, you will end up with a "ndk-bundle" dir which is a symlink for ndk-bundle-release-somethin and some other ndk-bundle-release-somethin-else
Now I don't know about _that_ repos in particular. Just about ndk installer :grimacing:

-------------------------

weitjong | 2018-09-26 16:05:19 UTC | #3

I just want to know whether I can safely nuke the repo one day and not getting whack or something.

-------------------------

rku | 2018-09-29 11:52:04 UTC | #4

Fun fact: a while back i was looking up information on android builds on CI. I came upon a random guide on the internets recommending pulling NDK from urho3d repo. This guide was in no way related to gamedev/3d/urho3d.

-------------------------

