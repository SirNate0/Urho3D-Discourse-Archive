rogerdv | 2017-01-02 01:01:06 UTC | #1

LAst week I tried to install Windows 8 at home. When started setting up the development environment, I found I could not install DirectX SDK: it says that Net framework was required. Tried to install a net framework, all of the say that it is already integrated in the system. Went to several places and got several frameworks that worked for my friends: none of them could be installed on my system. After 3 days, I had to go back to Windows 7. Has somebody successfully used Windows 8/8.1 as development platform?

-------------------------

cadaver | 2017-01-02 01:01:06 UTC | #2

When you use a recent Visual Studio such as 2012 and 2013, which includes the Windows SDK, you should be able to build software such as Urho without the DirectX SDK, as all needed headers and libs are in the Windows SDK.

-------------------------

rogerdv | 2017-01-02 01:01:07 UTC | #3

Thanks, Im downloading now Visual Studio Express 2012, will try with that one.

-------------------------

