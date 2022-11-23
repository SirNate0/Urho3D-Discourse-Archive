Lumak | 2017-01-02 01:06:22 UTC | #1

I'm trying to add 3rd party provided header file, lib, and dll that I need to link and run with in my Urho3D build but lost as to which CMake file to add it to.

I'm looking at Urho3D-CMake-common.cmake file and I think that's where it should go but just not sure. 

If anyone can provide me with some instructions on how to do this, I'd appreciate it.  Thanks.

-------------------------

Lumak | 2017-01-02 01:06:22 UTC | #2

I figured it out.

-------------------------

gooses | 2017-08-16 16:25:43 UTC | #3

I have a similar problem, how did you go about doing this?

-------------------------

SirNate0 | 2017-08-21 00:59:22 UTC | #4

You can look at some of my branches in GitHub for pointers on how I did it. I'm not certain it's exactly what your looking for, but I think this might point you in the right direction. For the fmt branch look at the first commit I added for it, and see what I did with the CMake files.

https://github.com/SirNate0/Urho3D/tree/fmt

-------------------------

