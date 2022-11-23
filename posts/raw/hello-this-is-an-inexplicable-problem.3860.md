spwork | 2017-12-17 21:32:53 UTC | #1

Hello, everyone. I am a novice. I want to ask, I compiled a little thing with urho3d, and used release mode, and then generated exe files. There were more than a lot of inexplicable DLL files. I want to ask how to make the DLL files as less as possible.![20171218053035|360x324](upload://c940IO6kpSr5Agoxs8g6ur4AWqc.png)

-------------------------

weitjong | 2017-12-18 04:31:07 UTC | #2

It is not clear where did you list those DLL from? Surely it is not from the Urho build tree because none of our build scripts do that from what I recall.

If you are referring to Urho dependency to some of Windows/VS runtime DLLs then you can try to reconfigure with URHO3D_STATIC_RUNTIME build option. Having said that, I am not quite familiar with VS and not quite sure those you shortlisted are actually one of them. It worths a try.

-------------------------

spwork | 2017-12-18 03:17:56 UTC | #3

It is useful, using URHO3D_STATIC_RUNTIME to generate EXE, and those strange DLL files are no longer existd. Thank you Admin,Urho3D is a good engine, you people doing a great job!

-------------------------

