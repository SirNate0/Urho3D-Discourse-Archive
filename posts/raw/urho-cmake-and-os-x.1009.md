Pellucas | 2017-01-02 01:04:46 UTC | #1

Hi all. I'm trying to generate the xcode project with cmake but I get some error. Here is a snapshot:

[img]http://i.imgur.com/v609i5R.jpg[/img]


[b]I'm using this package:[/b]
Urho3D-1.32.655-OSX-64bit-STATIC-snapshot



[b]OS[/b]: Mac OS X 10.8.5

 :question:

-------------------------

weitjong | 2017-01-02 01:04:47 UTC | #2

Use the source tarball or better yet clone it directly from our GitHub repo to build the library yourself. However, if you really want to, you can use the binary package as you have downloaded for using the library as SDK by following the instructions in [url]http://urho3d.github.io/documentation/HEAD/_using_library.html[/url] documentation page. Naturally, you only use the latter when you already have your own C++ project with your own source code ready.

-------------------------

Pellucas | 2017-01-02 01:04:47 UTC | #3

Thank you weitjong.
I copied the includes, lib and pkgconfig to the /usr/local folders, but I have no idea how to use the pkgconfig with an IDE. I tried to create a project with Qt Creator and this is my [b].pro[/b] file:
[code]
TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += \
    InitGame.cpp

include(deployment.pri)
qtcAddDeployment()


macx: LIBS += -L$$PWD/../../../../../../usr/local/lib/Urho3D/ -lUrho3D

INCLUDEPATH += $$PWD/../../../../../../usr/local/include/Urho3D
DEPENDPATH += $$PWD/../../../../../../usr/local/include/Urho3D

macx: PRE_TARGETDEPS += $$PWD/../../../../../../usr/local/lib/Urho3D/libUrho3D.a

HEADERS += \
    InitGame.h

#unix: CONFIG += link_pkgconfig
#unix: PKGCONFIG += Urho3D
[/code]

I get too much error from header files of the engine, this is the first one:
[code]/usr/local/include/Urho3D/Container/RefCounted.h:53: error: variable has incomplete type 'class URHO3D_API'
class URHO3D_API RefCounted
                 ^[/code]


Otherwise, if I uncomment the two last lines of the [b].pro[/b] file, I get the following message and I can't build my project:
[code]Project ERROR: Urho3D development package not found[/code]
but the file "Urho3D.pc" is in the correct location(/usr/local/lib/pkgconfig/).

It's so frustrating... LOL
any idea?

-------------------------

weitjong | 2017-01-02 01:04:47 UTC | #4

I am actually seriously not sure how to help you because I have no idea what you are trying to do  :laughing: . The "pkgconfig" is not a native tool in Mac OS X. So, you have to use Mac "homebrew" to install it first. But if you are willing to setup "homebrew" to work with your Mac OS X then you might as well ask homebrew to install "cmake" and use that instead. If want the easiest way, use "cmake" rather than "pkgconfig".

If you use binary package then you can extract it anywhere in your filesystem. There is no need to manually move the pieces to /usr/local like you have done. Read the [urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html) page carefully again, especially on the usage of URHO3D_HOME environment variable. You need it to be set to point to where you have extracted the binary package.

If you have to use Qt IDE on a Mac OS X (really?) then you need to set it up to generate project file using CMake, which should give you "makefile" instead of *.pro. You are on your own if you insist on using Qt own project file. In summary, Urho3D uses CMake extensively. When you are not using CMake in anyway to configure/generate the project file then you will find yourself to have a hard time.

-------------------------

