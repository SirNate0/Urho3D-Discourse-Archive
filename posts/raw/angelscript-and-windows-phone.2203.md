NiteLordz | 2017-01-02 01:13:53 UTC | #1

I am trying to get AngelScript supported within the Windows Universal Platform (UWP), and currently, have it working in the x86 and x64 builds, but the ARM build does not work.  I have tried using the various supplied files for ARM within MSVC, but none of them work properly.  I have spoken with Andreas, and going to try to debug the native calling convention to add support.  

With that said, would i be able to use generic calling convention, similar to what Emscripten is using, to get this platform supported in the mean time.

If so, what would need to happen? I have looked inside the angelscript.h file and saw the preprocessor flags for __EMSCRIPTEN__ to enable AS_MAX_PORTABILITY flag, and when i add in an additional flag for Windows Phone, i get a ton of warnings, and then a few error messages.

I was wondering if i needed to disable/enable any other flags anywhere.

-------------------------

cadaver | 2017-01-02 01:13:54 UTC | #2

Add also a new condition for whether Boost includes are added to the build: Source/CMakeLists.txt, around line 62

Not sure if Windows Phone compiler has something special that needs to be observed, but that and the angelscript.h modification were enough to make 64-bit iOS work in addition to Emscripten.

-------------------------

NiteLordz | 2017-01-02 01:13:55 UTC | #3

I almost can say i have the native calling convention working within the W10M platform.  However, the issue i now have is loading of resources.

If i load resources from the c++ side, the resource loads properly. 

However, if i try to load that resource from script side, the file's do not "exist", although i have confirmed they do, by testing from the c++ side.

From the AngelScript implementation, is there anything that you can think of that might cause this?  I have disabled threading, as the W10M device i have is single threaded (not sure if that could be a cause or not anyways).

-------------------------

DavTom | 2017-01-02 01:14:14 UTC | #4

I am facing the same problem to get Urho3D to work in W10M.
Urho3D.lib depends on AngleScript.Lib. I am gethering information here perhaps it may be helpful for others to finish this task.
[url]http://stackoverflow.com/questions/39552696/how-to-compile-angelscript-for-arm-windows-phone-8-w10m[/url]

-------------------------

