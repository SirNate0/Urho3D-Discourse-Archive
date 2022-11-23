Don | 2018-01-24 06:03:23 UTC | #1

Hi all,

I had an issue with compiling the Urho library on Windows yesterday. A quick search didn't bring anything up, so has anyone else had the same issue? Here's the compile log for reference. Thanks.

https://pastebin.com/ZZCs6uWM

Best,
Don

-------------------------

weitjong | 2018-01-24 07:37:21 UTC | #2

Our CI at AppVeyor is using VS2017 now and the last CI build passed. Have you tried to delete and regenerate the build tree?

-------------------------

George1 | 2018-01-24 08:24:51 UTC | #3

CMake generate 2017 solution file works fine at my end.
You need to delete and rebuild the tree like weitjong said.

-------------------------

