jzpekarek | 2020-06-08 03:49:25 UTC | #1

I have been trying to build Urho3D 1.8 alpha, but I get the error below, and I have no idea how to move forward, so wanted to check if anyone else might have some ideas on how to fix this. If I do a ALL_BUILD, I get many of these errors, if I just try to build Urho3D for a single configuration, I get one of the errors as shown below.

1>C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(231,5): error MSB6006: "cmd.exe" exited with code -1073741521.

-------------------------

George1 | 2020-06-08 09:11:30 UTC | #2

Just use cmake gui to build.  Search for other thread on cmake gui.

-------------------------

jzpekarek | 2020-06-09 02:12:02 UTC | #3

I think I figured it out, I downloaded Visual Studio 2017, and it seems to work, so maybe the 1.8 alpha hasn't been tested with VS 2019. The only issue I had were a few linker errors that I was able to fix by adding SetupApi.lib to the linker input.

-------------------------

George1 | 2020-06-09 03:04:03 UTC | #4

Download from github?
I think built using vs2019 should works fine.  I used the full vs2019 on windows 10.

-------------------------

GoldenThumbs | 2020-06-09 05:52:06 UTC | #5

Master is v1.8 alpha right? If so it built just fine with Visual Studio 2019 today.

-------------------------

