AlCaTrAzz | 2017-01-02 01:13:23 UTC | #1

Hey all,

So i've ran into an interesting issue with urho3D and my current project. i'm looking to use the playfab API to handle player authentication as well as online matchmaking and server management for a title i'm working on. unfortunately, i'm running into issues when i try to directly use their SDK with Urho3D, with the problem looking like it's because of both playfab and urho3d using rapidJSON. because of this, i've decided to just use urho3Ds implementation of HTTP requests to access the api myself. 

however, the playfab api requires an SSL connection, and the current implementation of civetweb in urho3D does not support this. 

in HttpRequest.cpp there's this ->  \todo SSL mode will not actually work unless Civetweb's SSL mode is initialized with an external SSL DLL

my question is, how do i actually do this?

i've looked at [github.com/hdunderscore/Urho3D](https://github.com/hdunderscore/Urho3D) a branch called opensslclean that seems to do exactly what i'm trying to do, except it was last updated for version 1.31 not 1.5, and i cant seem to get it to work (i'm fairly inexperienced with CMake so i'm assuming it's more likely i'm doing something wrong here)

any advice?

-------------------------

miz | 2017-01-02 01:15:01 UTC | #2

Hi, I've just run into a similar issue and found this question did you find a way to do this?

-------------------------

rasteron | 2017-01-02 01:15:01 UTC | #3

Hey guys,

Have you tried looking at this doc on how to properly setup OpenSSL with CivetWeb?

[github.com/civetweb/civetweb/bl ... OpenSSL.md](https://github.com/civetweb/civetweb/blob/master/docs/OpenSSL.md)

-------------------------

