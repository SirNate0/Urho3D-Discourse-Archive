nyt0x | 2017-01-02 01:12:34 UTC | #1

Hi!
Sorry if this is a known issue, I quickly check and couldn't find something that would explain my problem.
I got 2 computer with the same kind of setting: Win10/Visual Studio 14.0 
On both I just cloned the repo at latest. Generate a project for Vs14 x64 using Cmake(UI), the only settings I modify from the default config are c++11 and d3d11.

Nothing fency.

First computer everything works like a charm, link build post-build steps, everything.

The other computer however... always get stuck on the same step, starting to generate lua binding: "Generating tolua++ API binding on the fly for Audio"

And I can't really figure out why. I suspected something with the admin rights on win10 but both computer have the same.

Any hint on what I'm doing wrong would be highly appreciated.

-------------------------

TheComet | 2017-01-02 01:12:34 UTC | #2

Can you post a verbose output of the build log? On windows you can use:
[code]cmake -G "NMake Makefiles" ..
nmake VERBOSE=1[/code]

This might reveal more about where exactly it is getting stuck.

-------------------------

nyt0x | 2017-01-02 01:12:34 UTC | #3

Here`s the build output: [url]http://pastebin.com/LNUpkvnR[/url]

Cmake verbose is on.

-------------------------

TheComet | 2017-01-02 01:12:34 UTC | #4

Hm, not very helpful unfortunately.

You could try invoking tulua++ manually from the command line and see if that works. tolua++ should be in the folder [color=#000080]Build\bin\tool\tolua++.exe[/color].

If you look at [color=#000080]Source/Urho3D/CMakeLists.txt:194[/color] you can figure out how it is invoked:
[code]    foreach (API_PKG_FILE ${API_PKG_FILES})
        get_filename_component (NAME ${API_PKG_FILE} NAME)
        string (REGEX REPLACE LuaAPI\\.pkg$ "" DIR ${NAME})
        set (GEN_CPP_FILE LuaScript/generated/${DIR}LuaAPI.cpp)
        list (APPEND GEN_CPP_FILES ${GEN_CPP_FILE})
        file (GLOB PKG_FILES LuaScript/pkgs/${DIR}/*.pkg)
        add_custom_command (OUTPUT ${GEN_CPP_FILE}
            COMMAND ${CMAKE_BINARY_DIR}/bin/tool/tolua++ -E ${CMAKE_PROJECT_NAME} -L ToCppHook.lua -o ${CMAKE_CURRENT_BINARY_DIR}/${GEN_CPP_FILE} ${NAME}
            DEPENDS tolua++ ${API_PKG_FILE} ${PKG_FILES} LuaScript/pkgs/ToCppHook.lua
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/LuaScript/pkgs
            COMMENT "Generating tolua++ API binding on the fly for ${DIR}")
    endforeach ()[/code]

You'll need to CD to WORKING_DIRECTORY [color=#000080]Source/Urho3D/LuaScript/pkgs[/color] then execute something like this (warning, not tested):
[code]../../../../Build/bin/tool/tolua++ -E Urho3D -L ToCppHook.lua -o Build/Source/Urho3D/LuaScript/generated/AudioLuaAPI.cpp Audio[/code]

-------------------------

nyt0x | 2017-01-02 01:12:34 UTC | #5

Ok based on the CMakeLists.txt and your comment I tried to call from a cmd with admin rights the equivalent of the custom command that is supposed to be launch from cmake.
Got the exact same result, the command goes through (by that I mean I don`t get any error) but never return, it just hang in the tolua process forever..

I wonder if I can attach to the tolua process if I build it in debug and see what's going on in there.

I`ll try that eventually.

Thank you by the way.
If you happen to have anything else I could try I'll be glad to hear about it.  :slight_smile:

-------------------------

nyt0x | 2017-01-02 01:12:35 UTC | #6

Oh boy... I think I found the culprit...
On my second computer I don`t have the same antivirus..
Appears that Avast is one little sneaky bast*** I put it on hold for 10 min just so I can try something else and know it's building!
Worst part is it doesn't tell me anything, not a single pop-up, log or anything.
It just try to run a deepscan on the tolua++.exe (because... reasons... you know..) and endup on a softlock..
That also explain why I couldn`t kill the tolua process.

Thank you for your help again, turns out (as I suspected) the problem was on my side.

I guess that post can be mark as resolve.

I feel stupid not thinking about the antivirus right away...

If I can suggest to add a not somewhere on the "How to build" page, just so others don`t run into the same pb. Worst case they'll hopefully find that post.

Anyway thanks again!

Cheers

-------------------------

