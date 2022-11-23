rku | 2019-05-23 13:20:02 UTC | #1

Urho3D UI editor written on top of AtomicGameEngine and imgui. Enjoy.

![](upload://ofVAjk3SzGP0oHd19xQhYfP7HmD.png)

P.S. Remember to clone like `git clone --recursive https://github.com/rokups/UrhoUIEditor.git`

-------------------------

Lumak | 2017-08-11 18:01:46 UTC | #2

Thanks, Rku. I will definitely look at this.  But I'm wondering, why did you choose Imgui over Nuklear when you've invested time in porting Nuklear.  

Currently, there's a PR for Nuklear by fire on Urho3D, and he's done great amount of work but I also wondered why the core members are choosing that pull request over Imgui (can't remember if there was actually a PR) from year earlier.

-------------------------

johnnycable | 2017-08-11 18:22:57 UTC | #3

cloned, but I'm not expert with atomic. How I should run your example?
And most important, how do I port it to Urho?

-------------------------

rku | 2017-08-11 19:22:30 UTC | #4

@Lumak we decided that imgui makes most sense for Atomic so I did integration work and am using it now. One of main arguments was rich ecosystem. I also can say I find imgui easier to work with after some practice. Never had any cryptic crashes either. Nuklear is easier to crash in my experience.

@johnnycable it is a cmake project with all dependencies. You just do recursive clone and build as any other cmake project. You do not even need to port it to urho. Just edit your UI and use it in urho3d as it will be 100% compatible.

-------------------------

Lumak | 2017-08-11 19:44:28 UTC | #5

[quote="rku, post:4, topic:3440"]
we decided that imgui makes most sense for Atomic so I did integration work and am using it now. One of main arguments was rich ecosystem. I also can say I find imgui easier to work with after some practice. Never had any cryptic crashes either. Nuklear is easier to crash in my experience.
[/quote]
I evaluated Nuklear PR some time ago, and while fire has done an awesome job with the integration, I wasn't sure if I wanted to use that UI for my personal projects.  Then I remembered 
https://discourse.urho3d.io/t/external-imgui-integration/1815

and also found it "easier to work with after some practice."

Thanks for clarifying what I suspected about Nuklear's stability. My guess was that since Imgui is more widely used, it must gone through many iterations and bug fixes to make it very stable compared to Nuklear.

-------------------------

rku | 2017-08-11 21:05:36 UTC | #6

If you need you can adapt my Atomic imgui integration code: https://github.com/rokups/AtomicImGUI

-------------------------

johnnycable | 2017-08-12 14:55:51 UTC | #7

git clone --recursive https://github.com/rokups/UrhoUIEditor.git
mkdir build
cd build
cmake ..
make

/Users/max/Developer/Library/UrhoUIEditor/src/main.cpp:543:50: error: implicit instantiation of undefined template 'std::__1::array<char, 4096>'
/Users/max/Developer/Library/UrhoUIEditor/src/main.cpp:543:66: error: implicit instantiation of undefined template 'std::__1::array<char, 4096>'
/Users/max/Developer/Library/UrhoUIEditor/src/main.cpp:545:39: error: implicit instantiation of undefined template 'std::__1::array<char, 4096>'
/Users/max/Developer/Library/UrhoUIEditor/src/main.cpp:546:31: error: implicit instantiation of undefined template 'std::__1::array<char, 4096>'
/Users/max/Developer/Library/UrhoUIEditor/dep/AtomicGameEngine/Source/Atomic/../Atomic/Graphics/../Scene/../Container/HashMap.h:78:11: error: implicit instantiation of undefined template 'std::__1::array<char, 4096>'
/Users/max/Developer/Library/UrhoUIEditor/dep/AtomicGameEngine/Source/Atomic/../Atomic/Graphics/../Scene/../Container/HashMap.h:232:23: error: assigning to 'Atomic::HashNodeBase *' from incompatible type 'Atomic::HashMap<Atomic::String, std::__1::array<char, 4096> >::Node *'
/Users/max/Developer/Library/UrhoUIEditor/dep/AtomicGameEngine/Source/Atomic/../Atomic/Graphics/../Scene/../Container/HashMap.h:122:13: error: no matching constructor for initialization of 'Atomic::HashIteratorBase'
/Users/max/Developer/Library/UrhoUIEditor/dep/AtomicGameEngine/Source/Atomic/../Atomic/Graphics/../Scene/../Container/HashMap.h:604:29: error: no matching conversion for functional-style cast from 'Atomic::HashMap<Atomic::String, std::__1::array<char, 4096> >::Node *' to 'Atomic::HashMap<Atomic::String, std::__1::array<char, 4096> >::Iterator'
/Users/max/Developer/Library/UrhoUIEditor/dep/AtomicGameEngine/Source/Atomic/../Atomic/Graphics/../Scene/../Container/HashMap.h:328:36: error: implicit instantiation of undefined template 'std::__1::array<char, 4096>'
5 warnings and 9 errors generated.

OsX 10.12.6, XCode 8.3

-------------------------

rku | 2017-08-12 15:46:34 UTC | #8

Hmm i myself am not having any issues crosscompiling for osx, though its using make, not xcode.

Could you try adding `#include <array>` to `UrhoUIEditor/src/main.cpp` and `UrhoUIEditor/dep/AtomicGameEngine/Source/Atomic/Container/HashMap.h` at the top and see if it solves errors?

-------------------------

artgolf1000 | 2017-08-18 02:52:39 UTC | #9

After add "#include \<array\>" to UrhoUIEditor/src/main.cpp, the compile errors disappeared, but it generate lots of link error:
Undefined symbols for architecture x86_64:
  "_AudioObjectAddPropertyListener", referenced from:
      _COREAUDIO_Init in libSDL.a(SDL_coreaudio.m.o)
      _prepare_audioqueue in libSDL.a(SDL_coreaudio.m.o)
  "_AudioObjectGetPropertyData", referenced from:
      _prepare_device in libSDL.a(SDL_coreaudio.m.o)
      _prepare_audioqueue in libSDL.a(SDL_coreaudio.m.o)
      _device_unplugged in libSDL.a(SDL_coreaudio.m.o)
      _build_device_list in libSDL.a(SDL_coreaudio.m.o)
  "_AudioObjectGetPropertyDataSize", referenced from:
      ...
  "_objc_setProperty_nonatomic", referenced from:
      -[MacFileWatcher setPathName:] in libAtomic.a(MacFileWatcher.mm.o)
      -[MacFileWatcher setChanges:] in libAtomic.a(MacFileWatcher.mm.o)
  "_objc_sync_enter", referenced from:
      -[MacFileWatcher readChanges] in libAtomic.a(MacFileWatcher.mm.o)
      -[MacFileWatcher addChange:] in libAtomic.a(MacFileWatcher.mm.o)
      _ScheduleContextUpdates in libSDL.a(SDL_cocoawindow.m.o)
      -[SDLOpenGLContext setWindow:] in libSDL.a(SDL_cocoaopengl.m.o)
  "_objc_sync_exit", referenced from:
      -[MacFileWatcher readChanges] in libAtomic.a(MacFileWatcher.mm.o)
      -[MacFileWatcher addChange:] in libAtomic.a(MacFileWatcher.mm.o)
      _ScheduleContextUpdates in libSDL.a(SDL_cocoawindow.m.o)
      -[SDLOpenGLContext setWindow:] in libSDL.a(SDL_cocoaopengl.m.o)
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [bin/UIEditor] Error 1
make[1]: *** [src/CMakeFiles/UIEditor.dir/all] Error 2
make: *** [all] Error 2

-------------------------

rku | 2017-08-18 09:48:40 UTC | #10

Looks like some things fail to link. Since i do not have a Mac i am not of much help. However if you figure it out please do tell!

-------------------------

TheComet | 2017-08-20 00:36:10 UTC | #11

Just compiled this now. The window is too large for my screen and I cannot resize it to anything lower. My screen is 1280x1024.

-------------------------

johnnycable | 2017-09-01 13:14:24 UTC | #12

Compiled on Ubuntu. Editor fires up, but I cannot input numbers into those rightmost fields...

-------------------------

rku | 2017-09-01 13:37:31 UTC | #13

@TheComet it is 3D application after all. You can change resolution in code the same way initial resolution is set for Urho3D applications.

@johnnycable you got it working, awesome! To change numbers click and drag. Yes, it is not a most polished thing and expect bugs too ;)

Edit: ctrl+click to enter values to those fields.

-------------------------

rku | 2017-09-04 13:11:44 UTC | #14

Just letting you know that style editing is now working.

How to:

1. Open style file like `Urho3D/bin/Data/UI/DefaultStyle.xml`
2. Open UI file like `Urho3D/bin/Data/UI/EditorColorWheel.xml`
3. Save attribute values to style file from attribute menu (button between attribute name and value)

Opening style file separately is necessary because UI files do not point to style file.


In near future i hope to add UI for selecting rects in UI texture. This is by far most tedious part when tuning UI file.

-------------------------

