rku | 2017-01-02 01:13:22 UTC | #1

[github.com/rokups/Urho3D-nuklear-ui](https://github.com/rokups/Urho3D-nuklear-ui)

I made this very minimal [url=https://github.com/vurtun/nuklear/]nuklear[/url] ui (which is much like ImGui, but fully skinnable) integration subsystem. It leverages sdl example of nuklear integration to do all the heavy lifting and thus actual code that bridges two systems is very minimal. All relevant info  required to integrate this code into your project is in README.md in repository. It does not mention but after you add this subsystem you can draw nuklear UI from E_UPDATE event.

@cadaver / @weitjong : think that patch is appropriate enough to be integrated into engine?

Edit: forgot to mention that it is opengl-only for now.

Edit:
[img]https://github.com/rokups/Urho3D-nuklear-ui/raw/master/screenshot.png?raw=true[/img]

2016-07-06 update:
* Patching Urho3D is no longer needed
* Added GetFontAtlas() method
* Added FinalizeFonts() method
* Added nuklear as submodule

-------------------------

weitjong | 2017-01-02 01:13:23 UTC | #2

Thanks for sharing it. About the "tiny" patch you mentioned, I think it should be OK to merge if you send it in as PR individually.

-------------------------

jmiller | 2017-01-02 01:13:23 UTC | #3

Thanks for sharing this, [b]rku[/b] (and nuklear contributors ofc). I'll be checking this out.

And for the patch - I've wanted an SDL raw event dispatch, and maybe other UI implementations can take advantage of it as well.

-------------------------

rasteron | 2017-01-02 01:13:23 UTC | #4

Nice. This would be a great addition if it can be included in the next version.

-------------------------

Modanung | 2017-01-02 01:13:24 UTC | #5

Looks good!

-------------------------

jmiller | 2017-01-02 01:13:24 UTC | #6

I thought I should report my attempt to integrate this with Urho [b]shared[/b] build and [b]mingw-w64[/b] toolchain. If it can save anyone the time I spent even with the help of [b]rokups[/b] (thanks!) that could save a lot of work... or maybe I'm just missing something, like in cmake.

It's not easy to find a GLEW 64-bit shared library (.dll.a). I managed to build it [[b]edit: with 'make glew.lib', but default target had errors[/b]]
It turned out I also needed to 'make extensions' - which I found uses many Unix tools so the quickest method was to use [url=http://msys2.github.io]MSYS2[/url] and install x86_64 gcc, make, python, git, etc.
Maybe GLEW can and will be optional in the future, as suggested in a nuklear Issues thread.

This integration is with SDL2, and I chose to use the includes and link to the library from Urho itself.

But all the time, I am getting these errors:
In function `nk_sdl_device_create()':
src/nuklear_sdl_gl3.h:98: undefined reference to `__imp_glCreateProgram' [and many more like it]

Urho3D passes defines to downstream projects, in this case GLEW_STATIC, but #undef it or removing from the generated makefile does not seem to affect the linking.

Part of my CMakeLists.txt ..
[code]
set(SDL_LIBRARY "/urho/build/Source/ThirdParty/SDL/libSDL.a")

add_definitions(-DGLEW_BUILD -DGLEW_NO_GLU)
set(GLEW_INCLUDE_DIR "glew-2.0.0/include/GL")
set(GLEW_LIBRARY_DIR "glew-2.0.0/lib")
find_path(GLEW_INCLUDE_DIR glew.h
  PATHS ${GLEW_INCLUDE_DIR})
set(GLEW_NAMES libglew32.dll.a glew32)
find_library(GLEW_LIBRARY
  NAMES ${GLEW_NAMES}
  PATHS ${GLEW_LIBRARY_DIR})
find_package(GLEW REQUIRED)
if(GLEW_FOUND)
  list(APPEND INCLUDE_DIRS ${GLEW_INCLUDE_DIR})
  message("Found GLEW library: ${GLEW_LIBRARY}")
else()
  message("---- GLEW NOT FOUND")
endif()
list(APPEND ABSOLUTE_PATH_LIBS ${SDL_LIBRARY} ${GLEW_LIBRARY})
list(APPEND LIBS opengl32 glu32)

setup_main_executable()
[/code]

Good luck!
I have been wanting to shift my main dev platform to Linux for a while..  [b]edit[/b]: and I've done this  :sunglasses:

-------------------------

rasteron | 2017-01-02 01:13:25 UTC | #7

[quote]which I found uses many Unix tools so the quickest method was to use MSYS2 and install x86_64 gcc, make, python, git, etc.
Maybe GLEW can and will be optional in the future, as suggested in a nuklear Issues thread.[/quote]

Did you manage to build with MSYS2 using default without any changes? I recently tried a quick build but failed to set it up properly.

-------------------------

jmiller | 2017-01-02 01:13:25 UTC | #8

[quote="rasteron"][quote]which I found uses many Unix tools so the quickest method was to use MSYS2 and install x86_64 gcc, make, python, git, etc.
Maybe GLEW can and will be optional in the future, as suggested in a nuklear Issues thread.[/quote]

Did you manage to build with MSYS2 using default without any changes? I recently tried a quick build but failed to set it up properly.[/quote]

I did have some troubles building (like missing fprintf?) but eventually got [b]make extensions[/b] to generate extensions (it needs python and a bunch of packages you can find with pacman -Ss stuff), and [b]make glew.lib[/b] to produce libraries (I have updated my OP with this info)... but quite possibly missed something.

edit: FYI, for me it builds fine on Arch.

-------------------------

rku | 2017-01-02 01:13:34 UTC | #9

Since patch for exposing raw SDL events was [url=https://github.com/urho3d/Urho3D/commit/d48c4120a14c6137fd5f3926c1ecc3e86725fad0]merged[/url] i pushed a little [url=https://github.com/rokups/Urho3D-nuklear-ui/commit/7f2b6aea9f0cc2706149388c7e0acd9050cb0d7e]update[/url] making use of those events. Also added nuklear as submodule dependency.

-------------------------

sabotage3d | 2017-01-02 01:13:40 UTC | #10

Would this work with OpenGL ES 2.0? I noticed on Nuklear's github people were having issues porting it properly.

-------------------------

yushli | 2017-01-02 01:13:40 UTC | #11

Also like to know if GLES 2.0 is supported. It would be nice if it is supported. That way it can run on mobiles.

-------------------------

cadaver | 2017-01-02 01:13:40 UTC | #12

For Urho integration via pull request it would be preferable to use the Graphics + Input subsystems, instead of direct SDL & OpenGL operation. I believe everything in the Nuklear device API should be straightforwardly convertible (just a little more work) and the existing UI shaders would likely work as is.

And since immediate UI operation is something that could feasibly be done from script too, script bindings would certainly make sense as well. At which point the work needed starts to add up :slight_smile: So I certainly don't fault you if you just decide to keep it as an external project.

-------------------------

yushli | 2017-01-02 01:13:40 UTC | #13

It looks like Nuklear UI has great potential to become the UI for Urho3D, if it supports GLES 2.0, and integrate well into the system.  @cadaver, will you accept it as the official Urho3D UI if your requirements are met?

-------------------------

sabotage3d | 2017-01-02 01:13:40 UTC | #14

There is an example with GL ES 2.0 but it is a little low level it will need to be implemented properly in Urho3D: [url]https://community.arm.com/message/37674#37674[/url]

-------------------------

cadaver | 2017-01-02 01:13:40 UTC | #15

Nuklear looks good, but it's a tough sell for an immediate mode library to become "the UI" if that means removing the existing UI, and e.g. reimplementing the editor using Nuklear. There are times when a retained mode UI is more pleasant to use. I have nothing against Nuklear as an addition or alternative.

-------------------------

yushli | 2017-01-02 01:13:41 UTC | #16

Of course it doesn't mean to remove the old UI, nor to rewrite the editor. It just means that this new system is developed to the quality standard of Urho3D, integrated into Urho3D's master branch and documented and maintained officially. That way we can be confident to use the new one, knowing it is backed by Urho3d's masters.

-------------------------

sabotage3d | 2017-01-02 01:13:41 UTC | #17

At the moment it looks like a bit of hack and I cannot switch easily between DX11, OpenGL 2.0,3.0 and ES as it is not using Urho's graphics API.

-------------------------

