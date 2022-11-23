Syberyn | 2019-05-24 00:06:16 UTC | #1

I compiled Urho3D for 4 hours straight today, and when it was done the samples are a bit...off.

![sad|405x500](upload://zBGqmS0nku0313Zv38SXHE8ytam.jpeg) 

[I was following the MinGW Windows guide.](https://github.com/urho3d/Urho3D/wiki/Compiling-Urho3D-on-Windows)

If you know what happened help would be much appreciated, thank you.

Specs: (if needed) 
OS: Windows 10
Processor: AMD FX(tm)-6300 Six-Core Processor, 3500 Mhz, 3 Core(s), 6 Logical Processor(s)
System Type: x64-based PC
GPU: GeForce GTX 760

-------------------------

S.L.C | 2019-05-24 13:18:12 UTC | #2

Just a GCC 8 issue. See:

https://discourse.urho3d.io/t/problems-with-3d-samples-on-win10/4894
https://github.com/urho3d/Urho3D/issues/2388
https://github.com/urho3d/Urho3D/pull/2344
https://github.com/urho3d/Urho3D/issues/2326

-------------------------

S.L.C | 2019-05-24 06:26:52 UTC | #3

A new release should probably be made to get rid of the 1.7 release. Or instruct people to  use the repository since that's more stable anyways.

-------------------------

Leith | 2019-05-24 06:30:47 UTC | #4

Ideally, we should be performing regular builds, and publishing a link to the latest build, with a more informed version identifier. But there is in my mind, a real need to maintain a link to the last known stable version as well, because as we've seen recently, sometimes bugs creep in that break core stuff like the editor, while the older version may still be usable even in the context of the latest codebase.

-------------------------

weitjong | 2019-05-24 07:27:28 UTC | #5

I have seen enough of this. I see if I can do a backport of the fix to 1.7 and release it as 1.7.1. We don’t do backporting in the past, but I think we can make an exception just for this one. It will be a good exercise anyway before we release 1.8.

-------------------------

Miegamicis | 2019-05-24 07:12:12 UTC | #6

@weitjong Mentioned that we could create 1.8rc. Is that still an option? It's been almost 2 years since the last release and I think we need to proceed with that.

-------------------------

weitjong | 2019-05-24 07:21:53 UTC | #7

Think we need to close a number of critical open issues and PR before we are ready to talk about releasing 1.8-RC. On my side this include the Gradle custom plugin development, SDL2 upgrade, fixing Web-build with latest EMSDK.

-------------------------

Leith | 2019-05-24 12:32:57 UTC | #8

Stop poisoning this poor guys post already!
Dear Original Poster, I am willing to take your hand and guide you to Hello World stage for free.

-------------------------

Modanung | 2019-05-24 13:22:03 UTC | #9

[quote="Leith, post:8, topic:5179"]
Stop poisoning this poor guys post already!
[/quote]

I guess this question seems solved enough - even though OP has not responded - that the matter it brought up can be discussed according to several people. I'll whip out my chartreuse marker - or poison green, if you will - to pin the solution.

@Syberyn  Oh, and welcome to the forums! :confetti_ball: :slight_smile:

-------------------------

Leith | 2019-05-24 13:37:04 UTC | #10

Today, I bottled my 51 white ghosts hot sauce, so my decision making skills may be delayed, also its for sale, if you are the right buyer who likes +1million scu that also tastes good, special blend, 13 carefully selected and rare chilli varieties

-------------------------

Modanung | 2019-05-24 13:47:59 UTC | #11

@Leith, are you familiar with [Gitter](https://gitter.im/urho3d/Urho3D)?

-------------------------

weitjong | 2019-05-24 16:56:01 UTC | #12

The new tag 1.7.1 is pushed. Let's see the release automation still works as good today as two years ago.

EDIT: Sorry, I have to redo it again because of wrong annotation.

-------------------------

restless | 2019-05-24 17:03:01 UTC | #13

@weitjong, Thanks for the release!

Btw, you might want to announce the release on all the usual channels:

https://urho3d.github.io/latest-news.html
https://discourse.urho3d.io/c/announcements

//*literally registered to say thanks :)*

-------------------------

weitjong | 2019-05-24 17:06:42 UTC | #14

This is actually only a bug fix release of 1.7. But I could post something there as well after I verified all the release automation still functions as expected.

-------------------------

Syberyn | 2019-05-24 20:12:16 UTC | #15

Should I use the repo?

-------------------------

JTippetts1 | 2019-05-24 20:27:10 UTC | #16

I highly recommend all to use the repo. It's pretty stable, and 1.7 is getting pretty long in the tooth.

-------------------------

Syberyn | 2019-05-24 20:40:21 UTC | #17

Alrighty, thanks for letting me know.

-------------------------

Syberyn | 2019-05-24 21:02:23 UTC | #18

Sorry for doublepost, but uhh how do I compile it for MinGW with code::blocks? Thanks.

-------------------------

weitjong | 2019-05-25 00:48:45 UTC | #19

Use the provided convenient batch file or script for invoking CMake. For your case it is "cmake_codeblocks.bat".

BTW, the release automation seems to be largely intact. CI release build on a few of the platforms failed but that was caused by the CI could not find the old compiler toolchain expected by build script in 1.7.1 tag and nothing to do with the quality of the new tag. This is something preventable in the future. So, yeah, I learnt one or two lessons in this exercise that will make the future releases better.

-------------------------

Syberyn | 2019-05-25 00:48:36 UTC | #20

I don't see that bat in the repo.

-------------------------

weitjong | 2019-05-25 00:49:59 UTC | #21

It is in the "script" directory now in the master branch.

-------------------------

Syberyn | 2019-05-25 01:34:09 UTC | #22

Oh, okay thanks haha.

-------------------------

Syberyn | 2019-05-25 03:49:52 UTC | #23

Thanks everyone, the examples are working as intended.

-------------------------

