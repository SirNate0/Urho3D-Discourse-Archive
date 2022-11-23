GodMan | 2021-11-25 18:00:24 UTC | #1

So browsing GitHub. Can I build the latest master branch of Urho3d with VS2013? Or do I need a newer version of VS?

-------------------------

weitjong | 2021-11-26 16:49:30 UTC | #2

The support has been removed like 4 years ago. You may get it to compile with VS2013 as it still has partial C++11 support and our current master branch is actually only using half-baked C++11. The migration to C++11 could not be completed properly as we have lost the project lead at the time and it is difficult to get everyone to agree and converge on simple things on what modern C++ means to the project.

https://github.com/urho3d/Urho3D/commit/912df7381c2b534b6add8b2840934ae21ce14fe2

-------------------------

GodMan | 2021-11-26 17:22:21 UTC | #3

okay thanks for the update. I will just stick with 1.71 for now.

-------------------------

