archwind | 2017-01-19 02:05:51 UTC | #1

I happened on this engine a couple days ago. I downloaded, compiled and ran some demos. Looks great.

Now the questions :slight_smile:

I can't get it to compile with any bat file in 64 bit. Does it compile 64 bit or just 32.

Is there commands to bat file for 64?

Got a link to this information?

I am at this time reviewing it for a project that I am working on right now but need 64 bit version.

-------------------------

George1 | 2017-01-19 03:23:21 UTC | #2

It's working fine for both 64 and 32 bit.

I'm using CMake to create a VS2015 64 bit solution and Lib.

Search youtube or Google, there a lots of info about this.

-------------------------

archwind | 2017-01-19 04:42:58 UTC | #3

Okay thanks I never used cmake before but I will get it configured.

-------------------------

JimSEOW | 2017-07-07 10:28:08 UTC | #4

Hi George1, is it possible to compile VS2015 for x64 and ARM (W10M)? If u can share some links, it would be great.

-------------------------

George1 | 2017-07-08 03:54:34 UTC | #5

Hi Jim,
I have not compile for ARM. So I'm not sure.

But for your information. Compile for VS 2017 also works for 32 and 64 bit.

The simplex way  is to use the CMake gui to create VS solution file.

Select source: /Urho3D-master
Where to build binaries: Select a Path Location.

Click on configure --> Select solution version --> check options --> click on configure again to make sure that there is no red items.
Now click on generate. 

That's all.

-------------------------

