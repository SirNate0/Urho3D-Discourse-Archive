huminzheng | 2021-06-28 11:14:15 UTC | #1

Hi，guys
When I use the httpRequest,there is some build error. How could I to handle this problem ? Thanks !

error: undefined symbol: *ZN6Urho3D7Network15MakeHttpRequestERKNS_6StringES3_RKNS_6VectorIS1_EES3* (referenced by top-level compiled C/C++ code)
warning: Link with `-s LLD_REPORT_UNDEFINED` to get more information on undefined symbols
warning: To disable errors for undefined symbols use `-s ERROR_ON_UNDEFINED_SYMBOLS=0`
warning: _ *ZN6Urho3D7Network15MakeHttpRequestERKNS_6StringES3_RKNS_6VectorIS1_EES3* may need to be added to EXPORTED_FUNCTIONS if it arrives from a system library
error: undefined symbol: _ZNK6Urho3D11HttpRequest16GetAvailableSizeEv (referenced by top-level compiled C/C++ code)
warning: __ZNK6Urho3D11HttpRequest16GetAvailableSizeEv may need to be added to EXPORTED_FUNCTIONS if it arrives from a system library
error: undefined symbol: _ZNK6Urho3D11HttpRequest8GetStateEv (referenced by top-level compiled C/C++ code)
warning: __ZNK6Urho3D11HttpRequest8GetStateEv may need to be added to EXPORTED_FUNCTIONS if it arrives from a system library
Error: Aborting compilation due to previous errors
em++: error: ‘D:/emsdk/node/14.15.5_64bit/bin/node.exe D:\emsdk\upstream\emscripten\src\compiler.js C:\Users\pc\AppData\Local\Temp\tmppgqrv48i.txt’ failed (1)
mingw32-make[2]: *** [Source\Samples\00_Aphro3DWeb\CMakeFiles\00_Aphro3DWeb.dir\build.make:1060: bin/00_Aphro3DWeb.html] Error 1
mingw32-make[1]: *** [CMakeFiles\Makefile2:1234: Source/Samples/00_Aphro3DWeb/CMakeFiles/00_Aphro3DWeb.dir/all] Error 2
mingw32-make: *** [makefile:165: all] Error 2

-------------------------

JTippetts1 | 2021-06-28 22:52:45 UTC | #2

As mentioned in the other thread, URHO3D_NETWORK is not currently supported for web builds. @Miegamicis is looking into possibly resurrecting his in-progress branch to add support using WebSockets, but has indicated it would still take a bit of work to complete a PR.

-------------------------

