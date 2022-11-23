lebrewer | 2020-03-18 02:56:48 UTC | #1

So far, I've been using Urho as a dependency on my machine. I did the standard `make && make install` and everything works well on my both Fedora and Manjaro setups. However, now that I'm ready to package my project and make it more mature, I wanted to add Urho as an external dependency to my build, so contributors can just clone my repo and run CMake and call it a day. This will be much better for Mac and Windows contributors too.

Unfortunately, I can't get `ExternalProject_Add` to work with Urho. It fails to find paths and I can't compile it as a static dependency. I also tried with a git submodule and `add_subdirectory`, but had the same errors. I suspect the problem lies within the Urho standard CMakeLists.txt.

Has anyone tried to do anything similar?

-------------------------

WangKai | 2020-03-18 07:05:59 UTC | #2

Here is the test in which I use Urho3D as a static library, currently works on Windows - 
https://discourse.urho3d.io/t/android-project-template/5967/2

Edit: Reference document - https://urho3d.github.io/documentation/1.7.1/_using_library.html
you should also need to set URHO3D_HOME -
>When searching in a non-default SDK installation or when searching in any Urho3D project build tree then the actual location need to be provided via URHO3D_HOME environment variable (set in the host system) or URHO3D_HOME build option (set using -D at command line or in cmake-gui). That is, use the URHO3D_HOME to hint the build system to locate the library.

Last not least, you also need to copy/mklink CMake folder from Urho3D to the folder of your project.

-------------------------

lebrewer | 2020-03-18 19:29:21 UTC | #3

I'm confused. Followed your link, where I found a message from you:

> The whole Gradle + CMake + Android Studio for NDK thing is horrible. Weekend ends now, still no progress.

Were you able to make it work? If so, how?

-------------------------

WangKai | 2020-03-19 00:01:00 UTC | #4

It's working on Windows, but not on Android.

-------------------------

Pencheff | 2020-03-19 00:30:55 UTC | #5

You can use the Android NDK to generate standalone toolchain for your target arch and build Urho3D as static with the toolchain. You can do that for every arch you want to target (aarch64 and armeabi-v7a for example) and use those libraries in both windows and linux with Android Studio. That's what I do in my project and its automated, so once I had it done its quite easy now.

Here's a snippet of how I build it using ExternalProject_Add:
[code]
if (ANDROID)
  set(URHO3D_CMAKE_FLAGS
    -DANDROID_PLATFORM=android-${ANDROID_API_LEVEL}
    -DCMAKE_TOOLCHAIN_FILE=${CMAKE_TOOLCHAIN_FILE}
    -DANDROID=${ANDROID}
    -DANDROID_NDK=$ENV{ANDROID_NDK}
    -DTOOLCHAIN_ROOT=${TOOLCHAIN_ROOT}
    -DANDROID_STL=${ANDROID_STL}
    -DCMAKE_AR=${CMAKE_AR}
    -DURHO3D_WEBP=OFF # TODO: needs cpu-features.h
  )
  file(MAKE_DIRECTORY ${platform_spec_path}/urho3d/src/urho3d-build/assets)
elseif (ANDROID OR URHO3D_ARM)
  set(URHO3D_CMAKE_FLAGS
    -DURHO3D_TOOLS=OFF
  )
endif()

ExternalProject_Add(ext-urho3d
  SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src/external/urho3d
  PREFIX urho3d
  UPDATE_COMMAND ""
  PATCH_COMMAND ${PATCHER} urho3d
  CMAKE_ARGS
    -DCMAKE_INSTALL_PREFIX=${platform_spec_path}
    -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
    -DURHO3D_SAMPLES=FALSE
    -DURHO3D_C++11=TRUE
    -DURHO3D_DEPLOYMENT_TARGET=generic
    # TODO: Causes error, PackageTool tries to create file in assets/ folder which doesn't exist
    #-DURHO3D_PACKAGING=TRUE
    ${URHO3D_CMAKE_FLAGS}
)

[/code]

-------------------------

WangKai | 2020-03-19 08:24:15 UTC | #6

Hi Pencheff,

I wonder what does "use the Android NDK to generate standalone toolchain" really mean? 
Could you please modify my HelloWorld project a little bit to show the way you work out on Android?

https://discourse.urho3d.io/t/android-project-template/5967/12?u=wangkai

-------------------------

