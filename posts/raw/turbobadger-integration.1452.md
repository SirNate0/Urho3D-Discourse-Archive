Lumak | 2017-01-02 01:07:48 UTC | #1

[url]http://urho3d.prophpbb.com/topic1512.html[/url]

Details:
-window build, not tested on other platforms
-mouse/key input, no touch
-the turbobadger library is included as Thirdparty/TurboBadger and builds with Urho3D.lib, however, since there's no dependency or modification to Urho3D source, this folder can be moved to Tools build folder and wouldn't be an issue.
-the demo is fully functional. all previous issues are fixed.

File list:
-Source/Thirdparty/TurboBadger - turbobadger lib files
-Source/Samples/54_TurboBadger - source code that runs turbobadger
-bin/Data/TB - data, including demo data

Issues:
-none

Configuration:
-turbobadger font types: TBBF(default), FreeType, and STB. The TBBF font was the default for the demo, but this can be easily changed in tb_config.h.  I've not tested other fonts.

What's next?
- not sure what to do with this, but I thought someone else might be interested in this type of stuff.

edit1: updated issues, corrected source paths
edit final: all issues fixed.
edit: added a link to my merge with the Urho3D-master.

-------------------------

Lumak | 2017-01-02 01:07:48 UTC | #2

In all fairness, memory leak could be attributed to something that I'm doing or not doing. I stepped through TurboBadger glfw demo for windows and copied and pasted lot of what was in the demo, but I could've missed something.

edit: fixed.

-------------------------

Lumak | 2017-01-02 01:07:50 UTC | #3

Memory leak issue fixed.  It was my doing, and it's embarrassing to admit that I forgotten Urho3d's delete process.  And I also pushed a lot of clean up code yesterday as well, so what's on the master is good to go.

edit: upper case inputs still remaining.

-------------------------

Lumak | 2017-01-02 01:07:50 UTC | #4

All fixed and checked in.

-------------------------

Hevedy | 2017-01-02 01:07:50 UTC | #5

To compile that on Urho3D or include in the project what is the way ? is that included?

Edit:

*Added the line 65 add_sample_subdirectory (54_TurboBadger) in Source/Samples/CMakeLists.txt to include the sample.
*Added the line 108 add_subdirectory (ThirdParty/TurboBadger) in Source/CMakeLists.txt to include the TurboBadger lib.

This are errors: ?
The line UIDrag.h 40 should be URHO3D_OBJECT( UIDrag ); and no OBJECT( UIDrag ); ?
The line TBWrapper.h 51 should be URHO3D_OBJECT( TUIRendererBatcher ); and no OBJECT( TUIRendererBatcher ) ?
HANDLER to URHO3D_HANDLER

Anyway after change that i got 6 errors
Error	8	error C2208: 'Urho3D::Application' : no members defined using this type 54_turbobadger\UIDrag.h	40	1	54_TurboBadger
Error	3	error C1903: unable to recover from previous error(s); stopping compilation	54_turbobadger\TBWrapper.h	51	1	54_TurboBadger


*I using the master version but with the 1.4 adding only that changes to the CMakeList.txt give me too errors with the generated files.

41>Urho3D-1.4\Build\bin\54_TurboBadger.exe : fatal error LNK1120: 195 unresolved externals

-------------------------

Lumak | 2017-01-02 01:07:51 UTC | #6

Sorry to hear you're having problems building this.  I posted your build problem with the master branch here - [url]http://discourse.urho3d.io/t/turbobadger-full-integration/1457/2[/url].

Can you tell me what some of the 195 unresolved externals are when linking it with 1.4?

-------------------------

Hevedy | 2017-01-02 01:07:52 UTC | #7

[quote="Lumak"]Sorry to hear you're having problems building this.  I posted your build problem with the master branch here - [url]http://discourse.urho3d.io/t/turbobadger-full-integration/1457/2[/url].

Can you tell me what some of the 195 unresolved externals are when linking it with 1.4?[/quote]

Not sure but all the obj libs from Turbobadger give me error at compile the sample.

-------------------------

Lumak | 2017-01-02 01:07:52 UTC | #8

Hmm, not much to go on.  You might try creating a new sandbox and see if that works.

-------------------------

Lumak | 2017-01-02 01:07:52 UTC | #9

Try my merged branch of Urho3D-master - [url]https://github.com/Lumak/Urho3D[/url], flags -DURHO3D_SAMPLES=1 -DURHO3D_TB_DEMO=1

-------------------------

Hevedy | 2017-01-02 01:07:53 UTC | #10

[quote="Lumak"]Try my merged branch of Urho3D-master - [url]https://github.com/Lumak/Urho3D[/url], flags -DURHO3D_SAMPLES=1 -DURHO3D_TB_DEMO=1[/quote]

Yeah thanks, tomorrow i go to try that, thanks you!

-------------------------

Hevedy | 2017-01-02 01:07:55 UTC | #11

[quote="Lumak"]Try my merged branch of Urho3D-master - [url]https://github.com/Lumak/Urho3D[/url], flags -DURHO3D_SAMPLES=1 -DURHO3D_TB_DEMO=1[/quote]

Well compiling you repo work without problems but at open the demo only have a brown background ?
*After include the flag -DURHO3D_TB_DEMO=1 now all works, thanks you!

-------------------------

Lumak | 2017-01-02 01:07:56 UTC | #12

ok, cool.

-------------------------

Dave82 | 2017-01-02 01:08:02 UTC | #13

Wow awesome work Lumak ! Didn't have time to test it yet but it looks beautiful ! I like Urho's UI but this really needed , i hope the UI will be replaced in the Editor. A beautiful gui would attract more users.

10/10

-------------------------

