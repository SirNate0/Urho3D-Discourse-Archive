SoNewBee | 2022-03-11 01:28:40 UTC | #1

Greetings.
I am a noob and I want to use c# with rbfx.
I am trying to build this engine from source code,but there are problems.
I am using vs2017 and I have installed .net framework 4.7.1-4.7.2.
But cmake point out it can not find dot net execute file.I don't know what it is.I searched my computer but there was nothing called "dotnet.exe".
So I installed .net 6.0,then I can add "dotnet.exe" filepath to cmake,then I can generate project with cmake.But vs2017 can not recognize .net 6.0.
Then I installed vs2022.
But it can not build eastl.lib.
I like this project and I really want to try it.So any advice please？
Thanks a lot!

-------------------------

Batch | 2022-03-11 20:57:33 UTC | #2

When I build rbfx I encounter errors that I have to fix myself before it builds successfully, although I don't recall the exact changes I made. It was simple stuff like missing includes.

Is there an error message being output when it fails to build eastl?

-------------------------

SoNewBee | 2022-03-12 05:03:51 UTC | #3

Thanks for your reply.
Here are errors.
![image|690x251](upload://opUpkR4RGyLHkVRiENRNfJEMDG7.jpeg)

-------------------------

SirNate0 | 2022-03-12 19:16:39 UTC | #4

Looks like the same error as reported here, with a suggested fix.

https://github.com/microsoft/vcpkg/pull/21538

-------------------------

