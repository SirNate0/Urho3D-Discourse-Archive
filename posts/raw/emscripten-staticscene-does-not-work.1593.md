itisscan | 2017-01-02 01:08:46 UTC | #1

I have succesfully compiled StaticScene.cpp through Emscripten compiler. But when I open StaticScene.html, I get "Exception thrown, see JavaScript console" in Urho3D console I get 

[code][Fri Dec 18 11:17:26 2015] WARNING: Could not get application preferences directory
[Fri Dec 18 11:17:26 2015] INFO: Opened log file StaticScene.log
[Fri Dec 18 11:17:26 2015] INFO: Added resource package Data.pak
[Fri Dec 18 11:17:26 2015] INFO: Added resource package CoreData.pak
[Fri Dec 18 11:17:26 2015] INFO: Set screen mode 1024x768 windowed
[Fri Dec 18 11:17:26 2015] INFO: Initialized input
[Fri Dec 18 11:17:26 2015] INFO: Initialized user interface
[Fri Dec 18 11:17:26 2015] INFO: Initialized renderer
[Fri Dec 18 11:17:26 2015] INFO: Set audio mode 44100 Hz stereo interpolated
[Fri Dec 18 11:17:26 2015] INFO: Initialized engine
-1[/code]

In the result, I get only black screen. 

[url]http://imgur.com/jS2h8YZ[/url]

However, HelloWorld example works fine. I suppose that is something wrong with scene and resource loading. 

I compile example with following command - [code]emcc -I"mypathtoincludefolder" -Wno-invalid-offsetof -ffast-math -m32 -Wno-
warn-absolute-paths -Wno-unknown-warning-option --preload-file CoreData.pak --us
e-preload-cache --preload-file Data.pak --use-preload-cache -s ALLOW_MEMORY_GROW
TH=1 -O2 StaticScene.cpp -o StaticScene.html -l"..\libUrho3D" -lGL -s USE_SDL
=2 -D"URHO3D_STATIC_DEFINE"[/code]

Platform - win32. Also I get next warnings when compilation is done. Maybe that was the reason why example does not work properly.

[code]warning: unresolved symbol: posix_spawn
warning: unresolved symbol: posix_spawn_file_actions_init
warning: unresolved symbol: posix_spawn_file_actions_destroy
warning: unresolved symbol: _ZNK6Urho3D4Node12GetComponentENS_10StringHashEb
warning: unresolved symbol: posix_spawn_file_actions_adddup2[/code]

So, How i can get working  StaticScene example ? Thanks.

-------------------------

weitjong | 2017-01-02 01:08:48 UTC | #2

Why do you need to call "emcc" directly to build instead of calling "make"? Are you not using CMake to configure/generate your project? There are a number of "magic" happen behind the scene in our build system. If you side step that then I am afraid we are not able to support you much. Take for the example the posix_spawn warnings you got, it was caused by missing "NO_POPEN" compiler define. All the compiler flags and defines are automatically configured to target HTML5 when Emscripten compiler toolchain is chosen in our build system.  Perhaps you also need to fire a js debugger in your browser to see what went wrong. A "-1" certainly does not mean any things to us.

-------------------------

