jonathan | 2017-10-08 23:38:14 UTC | #1

Hey,

Trying to build Urho3d 1.7 as a buildroot package. My target is an ARM Tegra K1 processor. Here is the `urho.mk` file which defines a cmake package in buildroot.

```
URHO_VERSION = 1.7
URHO_SOURCE = $(URHO_VERSION).tar.gz
URHO_SITE = https://github.com/urho3d/Urho3D/archive
URHO_INSTALL_STAGING = YES
URHO_INSTALL_TARGET = YES
URHO_CONF_OPTS = \
	-DURHO3D_ANGELSCRIPT=0 \
	-DURHO3D_LUA=0 \
	-DARM_PREFIX=$(HOST_DIR)/usr/bin/arm-buildroot-linux-gnueabihf- \
	-DARM_SYSROOT=$(TARGET_DIR) \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DURHO3D_IK=0 \
	-DURHO3D_NETWORK=0 \
	-DURHO3D_PHYSICS=0 \
	-DURHO3D_NAVIGATION=0 \
	-DURHO3D_URHO2D=0 \
	-DURHO3D_WEBP=0 \
	-DURHO3D_WEBP=SHARED

$(eval $(cmake-package))
```
The build gets to 93% and errors. Looking back through the output there are two main problems with linking. The first is with pugi.

```bash
XMLElement.cpp:(.text+0x20): undefined reference to 'pugi::xpath_node::attribute() const'
XMLElement.cpp:(.text+0x2c): undefined reference to 'pugi::xml_attribute::operator void (*)(pugi::xml_attribute***)() const'
XMLElement.cpp:(.text+0x36): undefined reference to 'pugi::xpath_node::attribute() const'
XMLElement.cpp:(.text+0x44): undefined reference to 'pugi::xml_attribute::set_value(char const*)'
```

In fact, every call to pugi is an undefined reference. The second is with SDL, same deal.

```
OGLGraphics.cpp:(.text+0x274c): undefined reference to `SDL_GetNumVideoDisplays'
OGLGraphics.cpp:(.text+0x2806): undefined reference to `SDL_GetDesktopDisplayMode'
OGLGraphics.cpp:(.text+0x2858): undefined reference to `SDL_GL_SetAttribute'
OGLGraphics.cpp:(.text+0x2860): undefined reference to `SDL_GL_SetAttribute'
OGLGraphics.cpp:(.text+0x2868): undefined reference to `SDL_GL_SetAttribute'
OGLGraphics.cpp:(.text+0x2874): undefined reference to `SDL_GL_SetAttribute'
OGLGraphics.cpp:(.text+0x287c): undefined reference to `SDL_GL_SetAttribute'
OGLGraphics.cpp:(.text+0x2884): undefined reference to `SDL_GetDisplayBounds'
```

Searching through the built files I found these libraries already build as shared libraries

```
~/v/buildroot (master|…) $ find output/build/urho-1.7/ -name '*.so'
output/build/urho-1.7/Source/ThirdParty/FreeType/libFreeType.so
output/build/urho-1.7/Source/ThirdParty/StanHull/libStanHull.so
output/build/urho-1.7/Source/ThirdParty/SDL/libSDL.so
output/build/urho-1.7/Source/ThirdParty/PugiXml/libPugiXml.so
output/build/urho-1.7/Source/ThirdParty/JO/libJO.so
output/build/urho-1.7/Source/ThirdParty/Assimp/libAssimp.so
output/build/urho-1.7/Source/ThirdParty/LZ4/libLZ4.so
output/build/urho-1.7/Source/ThirdParty/WebP/libWebP.so
```

So my question is why aren't the paths to these third party libraries part of the library search path when I build and configure.

Thanks!

-------------------------

weitjong | 2017-10-09 02:00:33 UTC | #2

Your setup does not seem right to me. If you use our provided build system then you should find that we configure all our third-parties to be built as STATIC library.

-------------------------

jonathan | 2017-10-09 12:24:09 UTC | #3

Ok I'll try that. Though, I thought the .sh files were just thin wrappers around a single cmake command:

```
cmake -E make_directory "$BUILD" && cmake -E chdir "$BUILD" cmake $OPTS $@ "$SOURCE" && post_cmake
```

This is essentially what buildroot is doing. Anyway, I'll update when I have those results.

-------------------------

weitjong | 2017-10-09 13:27:44 UTC | #4

It appears as though somewhere you might have accidentally reset the CMake to its default where it prefers SHARED to STATIC library. In our build script we have intentionally switch this so that STATIC is used by default unless explicitly stated otherwise. I cannot say how/where did that happen in your setup. If you have setup everything correctly then the Urho3D library (regardless of whether it is a STATIC or SHARED) should contain all the symbols from the 3rd-party libraries. That answers your question of why we don't need to include library search path for the 3rd-party libraries. All the symbols are already statically linked (SHARED `libUrho3D.so`) or archived into (STATIC `libUrho3D.a`), respectively.

-------------------------

