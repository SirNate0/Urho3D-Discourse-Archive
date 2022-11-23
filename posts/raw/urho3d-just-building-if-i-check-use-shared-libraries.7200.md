killinbassou | 2022-02-23 03:26:41 UTC | #1

I'm using Ubuntu Focal LTS and Urho3D 1.7.1 Source.

CMake (GUI) runs fine, but when I build on CodeBlocks it happens:

```
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_x11dyn.c.o): in function `SDL_X11_LoadSymbols':
SDL_x11dyn.c:(.text+0x94e): undefined reference to `XAllocSizeHints'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x966): undefined reference to `XAllocWMHints'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x974): undefined reference to `XAllocClassHint'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x982): undefined reference to `XAutoRepeatOn'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x990): undefined reference to `XAutoRepeatOff'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x99e): undefined reference to `XChangePointerControl'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x9ac): undefined reference to `XChangeProperty'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x9ba): undefined reference to `XCheckIfEvent'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x9c8): undefined reference to `XClearWindow'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x9d6): undefined reference to `XCloseDisplay'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x9e4): undefined reference to `XConvertSelection'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x9f2): undefined reference to `XCreateBitmapFromData'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa00): undefined reference to `XCreateColormap'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa0e): undefined reference to `XCreatePixmapCursor'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa1c): undefined reference to `XCreateFontCursor'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa2a): undefined reference to `XCreateFontSet'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa38): undefined reference to `XCreateGC'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa46): undefined reference to `XCreateImage'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa54): undefined reference to `XCreateWindow'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa62): undefined reference to `XDefineCursor'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa70): undefined reference to `XDeleteProperty'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa7e): undefined reference to `XDestroyWindow'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa8c): undefined reference to `XDisplayKeycodes'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa9a): undefined reference to `XDrawRectangle'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xaa8): undefined reference to `XDisplayName'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xab6): undefined reference to `XDrawString'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xac4): undefined reference to `XEventsQueued'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xad2): undefined reference to `XFillRectangle'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xae0): undefined reference to `XFilterEvent'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xaee): undefined reference to `XFlush'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xafc): undefined reference to `XFree'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb0a): undefined reference to `XFreeCursor'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb18): undefined reference to `XFreeFontSet'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb26): undefined reference to `XFreeGC'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb34): undefined reference to `XFreeFont'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb42): undefined reference to `XFreeModifiermap'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb50): undefined reference to `XFreePixmap'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb5e): undefined reference to `XFreeStringList'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb6c): undefined reference to `XGetAtomName'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb7a): undefined reference to `XGetInputFocus'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb88): undefined reference to `XGetErrorDatabaseText'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb96): undefined reference to `XGetModifierMapping'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xba4): undefined reference to `XGetPointerControl'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xbb2): undefined reference to `XGetSelectionOwner'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xbc0): undefined reference to `XGetVisualInfo'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xbce): undefined reference to `XGetWindowAttributes'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xbdc): undefined reference to `XGetWindowProperty'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xbea): undefined reference to `XGetWMHints'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xbf8): undefined reference to `XGetWMNormalHints'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xc06): undefined reference to `XIfEvent'
```

It seens it not linking SDL compiled library or -lX11, but if I check on CMake "X11_SHARED" it works and then it goes wrong again with alsa and pulseaudio (same, unchecked, then I need to check them to compile)

sorry for my english

-------------------------

killinbassou | 2022-02-23 03:27:27 UTC | #2

Same for 1.8 downloaded from github "release".

```
/usr/bin/c++  -mtune=generic  -Wno-invalid-offsetof -march=native -msse3 -pthread -fdiagnostics-color=auto -O3 -DNDEBUG   CMakeFiles/RampGenerator.dir/RampGenerator.cpp.o  -o ../../../bin/tool/RampGenerator  ../../../lib/libUrho3D.a -ldl -lm -lrt -lGL 
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_x11dyn.c.o): in function `SDL_X11_LoadSymbols':
SDL_x11dyn.c:(.text+0x96e): undefined reference to `XAllocSizeHints'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x986): undefined reference to `XAllocWMHints'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x994): undefined reference to `XAllocClassHint'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x9a2): undefined reference to `XAutoRepeatOn'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x9b0): undefined reference to `XAutoRepeatOff'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x9be): undefined reference to `XChangePointerControl'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x9cc): undefined reference to `XChangeProperty'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x9da): undefined reference to `XCheckIfEvent'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x9e8): undefined reference to `XClearWindow'
/usr/bin/ld: SDL_x11dyn.c:(.text+0x9f6): undefined reference to `XCloseDisplay'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa04): undefined reference to `XConvertSelection'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa12): undefined reference to `XCreateBitmapFromData'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa20): undefined reference to `XCreateColormap'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa2e): undefined reference to `XCreatePixmapCursor'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa3c): undefined reference to `XCreateFontCursor'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa4a): undefined reference to `XCreateFontSet'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa58): undefined reference to `XCreateGC'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa66): undefined reference to `XCreateImage'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa74): undefined reference to `XCreateWindow'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa82): undefined reference to `XDefineCursor'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa90): undefined reference to `XDeleteProperty'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xa9e): undefined reference to `XDestroyWindow'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xaac): undefined reference to `XDisplayKeycodes'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xaba): undefined reference to `XDrawRectangle'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xac8): undefined reference to `XDisplayName'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xad6): undefined reference to `XDrawString'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xae4): undefined reference to `XEventsQueued'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xaf2): undefined reference to `XFillRectangle'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb00): undefined reference to `XFilterEvent'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb0e): undefined reference to `XFlush'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb1c): undefined reference to `XFree'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb2a): undefined reference to `XFreeCursor'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb38): undefined reference to `XFreeFontSet'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb46): undefined reference to `XFreeGC'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb54): undefined reference to `XFreeFont'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb62): undefined reference to `XFreeModifiermap'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb70): undefined reference to `XFreePixmap'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb7e): undefined reference to `XFreeStringList'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb8c): undefined reference to `XGetAtomName'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xb9a): undefined reference to `XGetInputFocus'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xba8): undefined reference to `XGetErrorDatabaseText'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xbb6): undefined reference to `XGetModifierMapping'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xbc4): undefined reference to `XGetPointerControl'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xbd2): undefined reference to `XGetSelectionOwner'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xbe0): undefined reference to `XGetVisualInfo'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xbee): undefined reference to `XGetWindowAttributes'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xbfc): undefined reference to `XGetWindowProperty'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xc0a): undefined reference to `XGetWMHints'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xc18): undefined reference to `XGetWMNormalHints'
/usr/bin/ld: SDL_x11dyn.c:(.text+0xc26): undefined reference to `XIfEvent'
```

Plus this:

`/../../../Urho3D-1.8/build/include/Urho3D/ThirdParty/PugiXml/pugixml.hpp|672|note: declared here|`

Gcc version 9.3.0
Cmake version 3.16.3
CodeBlocks version 20.03

I've a look on ubuntu packages and there are static libraries on libx11-dev

Anyone can help me?

-------------------------

SirNate0 | 2022-02-23 02:39:35 UTC | #3

Hello, and welcome to the forum! Where is this "use SHARED libraries" option? Is it something in CodeBlocks? And is this in building Urho or is it in building your application using Urho? What are you trying to do in using it? Are you just trying to build Urho as a shared library, or are you trying something else?

Also, if you wrap the code/console output in triple backticks, it won't have the messed up formatting, and also won't replace `..` with .., etc.

E.g.
```
    ```
    Your Code/Output Here. 
    Without the indentation, I just it to show the backticks for you.
    ```
```
If you select it and hit the `</>` icon it should add the backticks for you.

-------------------------

killinbassou | 2022-02-23 03:43:14 UTC | #4

[quote="SirNate0, post:3, topic:7200"]
welcome to the forum!
[/quote]

Thanks!

[quote="SirNate0, post:3, topic:7200"]
Where is this “use SHARED libraries” option?
[/quote]

"Use SHARED libraries" It's a way I made up of saying to "disable SHARED library options" on Cmake-GUI

Take a look:

![Screenshot_20220223_003443|690x224](upload://39em2ML4vtz8gEURDvct4XQyv6k.png)

Print shows opening Urho3D source with CMake GUI by the first time, then I uncheck all this options.
And yes, on the bottom I even tried to change the library locations from .so to .a library

[quote="SirNate0, post:3, topic:7200"]
Is it something in CodeBlocks?
[/quote]

No.

[quote="SirNate0, post:3, topic:7200"]
And is this in building Urho or is it in building your application using Urho?
[/quote]

Build Urho.

[quote="SirNate0, post:3, topic:7200"]
What are you trying to do in using it?
[/quote]

Build Urho3D, learn samples, how everything works (build samples from source, build using urho3d static library),etc

[quote="SirNate0, post:3, topic:7200"]
Are you just trying to build Urho as a shared library, or are you trying something else?
[/quote]

Just build Urho3D and its samples and tools

[quote="SirNate0, post:3, topic:7200"]
Also, if you wrap the code/console output in triple backticks, it won’t have the messed up formatting, and also won’t replace `..` with …, etc.

E.g.

```
    ```
    Your Code/Output Here. 
    Without the indentation, I just it to show the backticks for you.
    ```
```

If you select it and hit the `</>` icon it should add the backticks for you.
[/quote]

Edited

-------------------------

SirNate0 | 2022-02-23 03:59:19 UTC | #5

[quote="killinbassou, post:4, topic:7200"]
“Use SHARED libraries” It’s a way I made up of saying to “disable SHARED library options” on Cmake-GUI

Take a look:

![Screenshot_20220223_003443](upload://39em2ML4vtz8gEURDvct4XQyv6k)
[/quote]
I see now. 

[quote="killinbassou, post:4, topic:7200"]
Print shows opening Urho3D source with CMake GUI by the first time, **then I uncheck all this options.**
[/quote]
Why are you unchecking them? I'm not saying you can't, but my philosophy is to leave all the defaults except those I have a reason to change. 

That said, it's possible changing some of them may break things (you've encountered that, after all). In this case, I think at least some, maybe all, of those `*_SHARED` options are generated by the SDL build script. For example, the ALSA_SHARED option is from 
```
Source/ThirdParty/SDL/CMakeLists.txt:dep_option(ALSA_SHARED         "Dynamically load ALSA audio support" ON ALSA OFF)
```

-------------------------

killinbassou | 2022-02-23 04:21:21 UTC | #6

[quote="SirNate0, post:5, topic:7200"]
Why are you unchecking them?
[/quote]

:confused: 
Well... I wanna to build a static library. If I let any dynamic library how it'll merge statically the libs to build urho3d.a (static)? Sorry if I'm wrong.

How Urho3D handles with it?

[quote="SirNate0, post:5, topic:7200"]
In this case, I think at least some, maybe all, of those `*_SHARED` options are generated by the SDL build script. For example, the ALSA_SHARED option is from
[/quote]

Yeah.... disable ALSA_SHARED make it fail too by SDL

-------------------------

SirNate0 | 2022-02-23 04:47:44 UTC | #7

Leave those *_SHARED options with the default settings. They're system libraries, basically. ALSA for sound, X11 is the display, etc. Your end user will have those installed and configured on his system for it to work anyways, so you want those to be linked dynamically so the correct version is chosen. Even if you got it to use a static library for those it would probably fail on the user's system. The build system will package what is reasonable into the static library (e.g. Bullet Physics) and will link dynamically the things that make sense for that (e.g. OpenGL). Just select the STATIC library type for Urho, which I think is the default.

-------------------------

weitjong | 2022-02-23 15:54:13 UTC | #8

It is unfortunate that CMake does not have namespace concept for the variables. In the CMake-gui you see all the configurable variables from Urho3D as well as the underlying libraries like SDL. You are advised not to modify those from SDL, unless you are very sure what you are doing. Toggling the variable for URHO3D is safe during initial build tree configuration/generation though. Read the docs on what they do (we call that "build options" in our docs). Our build scripts then will based on those build options to configure the rest for you automatically. So, basically just toggle URHO3D_XXX ones and click "configure" and then click "generate".

As for the how SDL uses SHARED library internally. It may be different for one target platform to the next. However, I can tell you this, on Linux platform we would pretty much like everything to be shared. For sure you don't want to link those GPL stuff statically in your own binary. Even on Windows platform, we still use those DLL from the WinSDK, don't we? So, it is not much different.

-------------------------

