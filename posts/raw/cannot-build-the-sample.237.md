nachochip | 2017-01-02 00:59:05 UTC | #1

Hello, I think it may be a silly question but I have a hard time to build the C++ sample, I try

cmake_vs2010 -URHO3D_SAMPLES=1

as states in the documentation and what I get is

E:\Urho3D-master>cmake -E chdir Build cmake  -G "Visual Studio 10" VERSION=10 -U
RHO3D_SAMPLES=1 ..\Source
-- Configuring done
-- Generating done
-- Build files have been written to: E:/Urho3D-master/Build

But where can I find the .sln file for each sample? Thanks!

-------------------------

aster2013 | 2017-01-02 00:59:05 UTC | #2

Use -[b]D[/b]URHO3D_SAMPLES=1.

-------------------------

