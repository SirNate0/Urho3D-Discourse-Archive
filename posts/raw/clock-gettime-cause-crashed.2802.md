att | 2017-02-18 09:41:56 UTC | #1

I compiled my project for iPad(9.3.2) using  iOS sdk 10.2, but crashed at clock_gettime() calling.
I think iOS sdk 9.3.2 or below has no function named clock_gettime(). How can I use gettimeofday() instead of clock_gettime() on older devices?

-------------------------

johnnycable | 2017-04-06 18:08:23 UTC | #2

Same Here. You have to patch the civetweb.c file manually, the function is already implemented in os x.
Find Urho3D-1.6/Source/ThirdParty/Civetweb/src/civetweb.c and comment out clock_gettime definition and declaration.

-------------------------

weitjong | 2017-04-07 01:44:05 UTC | #3

This issue has been fixed in the master branch.

-------------------------

