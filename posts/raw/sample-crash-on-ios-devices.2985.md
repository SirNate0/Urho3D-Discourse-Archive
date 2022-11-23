artgolf1000 | 2017-04-14 00:58:05 UTC | #1

Hi,

I had reported the issue to Github, when I enable sound, the app will crash on iOS devices every time.

I guess that the issue was introduced recently, for it does not exist before I pulled the latest master branch.

How to repeat the issue:

Modify any of the samples codes, enable sound in the engine, build and run, the app will crash.

It reports that 'AudioQueue EXC_BAD_ACCESS', I can not figure it out.

-------------------------

artgolf1000 | 2017-04-08 03:22:07 UTC | #2

I have tried to check out an earlier version to test if it is a bug.

cd Urho3D
git checkout f1cb469a34c13c56e9d6a9a75c38539cf2de8bd2 .

This version was committed on Nov 9, 2016, it can work without any issues, so it is a bug.

-------------------------

weitjong | 2017-04-09 04:31:11 UTC | #3

[quote="artgolf1000, post:2, topic:2985"]
f1cb469a34c13c56e9d6a9a75c38539cf2de8bd2
[/quote]

Could you do git bisect until you find the first commit that caused your issue?

-------------------------

artgolf1000 | 2017-04-09 10:24:48 UTC | #4

Hi,

I traced the commit log, and found the commission:

commit e071b2096768221fcb4b21259cd4a5cf624185e2
Author: Yao Wei Tjong 姚伟忠 <weitjong@gmail.com>
Date:   Wed Nov 30 01:51:24 2016 +0800

    Another attempt to auto-detect clock_gettime() on Apple platforms.
    It is strange that Apple does not honour the deployment target and only based on base SDK when defining __CLOCK_AVAILABILITY internally.
    [ci only: OSX]

Art

-------------------------

artgolf1000 | 2017-04-12 12:41:41 UTC | #5

I rolled back to the previous version (Source/ThirdParty/Civetweb/CMakeLists.txt), the issue disappears.

-------------------------

weitjong | 2017-04-10 02:04:33 UTC | #6

Either way is not bulletproof, I am afraid.

-------------------------

artgolf1000 | 2017-04-14 00:57:52 UTC | #7

This issue has been fixed by weitjong yesterday.

-------------------------

