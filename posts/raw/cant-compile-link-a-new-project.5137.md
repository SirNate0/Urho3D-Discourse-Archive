entretoize | 2019-05-03 06:18:34 UTC | #1

Hello, I followed the getting started guide, unzipped the github master, created the project with cmake, launched the solution in Visual Studio and compiled the samples.
All samples work, but now I want to create my own project outside of the Urho3d folder.

I created a new project, added the orho3D include folder to my include folder list, and added the urho3d.lib to my project.
But when I compile, i get the folloing error (and many others...)
`LNK2019	unresolved external symbol "public: __thiscall Urho3D::StringHash::StringHash(char const *)" (??0StringHash@Urho3D@@QAE@PBD@Z) referenced in function "void __cdecl Urho3D::DragDropFinish::dynamic initializer for 'P_ACCEPT''(void)" (??__EP_ACCEPT@DragDropFinish@Urho3D@@YAXXZ)`

StringHash is defined in StringHash.cpp, but must I add all cpp files to my project ?
Sorry for the newbie question, I used several sdk in the past but here I don't understand.

Thanks

-------------------------

ab4daa | 2019-05-02 10:04:27 UTC | #2

Hi, 
I suppose you are using C++?
[Here](https://urho3d.github.io/documentation/HEAD/_using_library.html) is the guide to setup a project with cmake.

-------------------------

entretoize | 2019-05-02 11:45:00 UTC | #3

So I can't just compile with CMake a lib to use for windows builds with all the stuff inside ?

-------------------------

weitjong | 2019-05-02 14:00:35 UTC | #4

In theory you can, if you already know Urho3D well enough. One can use the pkg-config to setup a working build without using CMake even. That’s the hint to you. In the pkg-config *.pc file there is enough information on how to configure compiler flags, compiler defines, and header and lib search paths, if you should decide to roll one your own.

-------------------------

QBkGames | 2019-05-03 03:28:47 UTC | #5

Also note that the debug build uses: **Urho3D_d.lib**.

Also check out the Urho3D wiki, especially the first section "Getting started":
https://github.com/urho3d/Urho3D/wiki

-------------------------

entretoize | 2019-05-03 06:14:24 UTC | #6

I understood that I need to use pkg-config but on the Doc they say I need to set PKG_CONFIG_PATH to my pkgconfig file but I don't find this file ...

-------------------------

weitjong | 2019-05-03 08:55:17 UTC | #7

The path should point to where the `Urho3D.pc` is located. This file is auto-generated when the library is built. So it could be in your build tree if you haven’t installed the SDK.

-------------------------

entretoize | 2019-05-03 12:09:28 UTC | #8

OK, thanks I will try that...

-------------------------

