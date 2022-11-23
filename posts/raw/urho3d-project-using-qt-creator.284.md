brachna | 2017-01-02 00:59:23 UTC | #1

Does anyone here managed to successfully setup Urho3D project using Qt Creator?
I would love the ability to code in Qt Creator, rather than using MSVC 2012, but so far been frustrated in trying to set it up.

I downloaded latest sources from git, build Urho3D itself using generated .sln.
Now that I have a library I would like to build my project using Qt Creator, but can't seem to set it up, seems to heavily rely on CMake.

Sorry, quite a newb to this.

Windows 7 32bit / Qt Creator 3.1.1 / MSVC 2012

-------------------------

friesencr | 2017-01-02 00:59:23 UTC | #2

I did get it to work on several computers, each on different platforms, so I know its posible :slight_smile:  However I have had a rough couple of weeks at work which has erased anything useful from my brain.  I will give it a whirl later from scratch.  For my linux machine I get the feeling I did the default gcc cmake and picked the build folder as my project and it imported cmake configuration in the build folder to set up the project.

-------------------------

Bluemoon | 2017-01-02 00:59:23 UTC | #3

This works for me (mindlessly lifted from the pkgconfig file Urho3D.pc  :smiley: )
NOTE: I'm using MSVC 2010 on an x86 Windows, but i believe with some tweaks it can be adapted to any platform

Add the following to your projects .pro file

[code]

TEMPLATE = app
CONFIG -= console
CONFIG -= app_bundle
CONFIG -= qt

TARGET = #Your Output Name

#This might be an overkill but I just added all of them as I saw them in the pkgconfig file
#it is for a release build with static library linkage and having angelscript enabled
DEFINES += WIN32 _WINDOWS NDEBUG _SECURE_SCL=0 ENABLE_SSE ENABLE_MINIDUMPS;
DEFINES += ENABLE_FILEWATCHER ENABLE_PROFILING ENABLE_LOGGING ENABLE_ANGELSCRIPT 
DEFINES += URHO3D_STATIC_DEFINE _CRT_SECURE_NO_WARNINGS HAVE_STDINT_H


# $(URHO_HOME) should point to your Urho3D installation folder
INCLUDEPATH += $(URHO_HOME)\include $(URHO_HOME)\include\SDL


#If you wish you can add these ones depending on your needs
# INCLUDEPATH += $(URHO_HOME)\include\Bullet $(URHO_HOME)\include\Direct3D9 $(URHO_HOME)\include\kNet


#$(DIRECTX_SDK) = where your directX sdk is installed for Windows and don't forget to replace x86 with x64 for those on x64 systems
LIBS += -L$(URHO_HOME)\lib   -lUrho3D   "$(DIRECTX_SDK) \Lib\x86\d3d9.lib"

#Then these guys, every single one of them seems to be needed on Windows
LIBS += kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib
LIBS += dbghelp.lib imm32.lib version.lib winmm.lib ws2_32.lib


HEADERS += #Your Header

SOURCES += #Your Source File

[/code]

I hope it works for you. When I'm chanced I'll find a way to share a Qt Creator project template for Urho3D I made  :smiley:

-------------------------

brachna | 2017-01-02 00:59:23 UTC | #4

Thanks Bluemoon, now I'm getting closer.

Now the problem is that I had to download Urho3D-1.31.1-Windows-STATIC-snapshot.zip (that's SDK right?) and use it instead.
Is there a way one can build such installation from source in order to always be up to date?
Because, for example, the library I made is build with URHO3D_OPENGL define, but downloaded installation keeps looking for d3d9.lib,
so I don't have options with it.

---

Nevermind, build installation, but now I'm getting compilation error: LNK1104: cannot open file 'Files\Urho3D\lib.obj'.
Not sure why it looks for such file. I added library in my .pro file:
if( CONFIG( debug, debug|release ) ): LIBS += -L$(URHO3D_HOME)\lib -lUrho3D
else: LIBS += -L$(URHO3D_HOME)\lib -lUrho3D_d

-------------------------

AGreatFish | 2017-01-02 00:59:23 UTC | #5

I am building both Urho3D as well as my own project using QtCreator (on Linux, that is).

QtCreator does have Git as well as CMake integration, therefore the IDE itself is rather easy to use if you manage to set up your project properly.

Using QtCreator you can easily clone Urho3D master and pull the latest changes using the GUI (Import Project -> Git Repository Clone).
To open Urho3D as a project in QtCreator, simply open the CMakeLists.txt in the source directory as a project (because QtCreator supports CMake projects), no need to set up a Qt Project :wink: 

To set up my own project, I used this as a guideline: [urho3d.github.io/documentation/a00004.html](http://urho3d.github.io/documentation/a00004.html)
It's important to make sure you have set the URHO3D_HOME environment variable correctly before compiling.

You can open this CMakeLists.txt in QtCreator as well and stuff should work  :smiley:

Edit:
You can also use the CMake GUI to configure the CMake project more easily before you open it in QtCreator.

-------------------------

brachna | 2017-01-02 00:59:24 UTC | #6

Sure, I actually did download git sources using QtCreator.
Building Urho3D itself is not a problem, I can just use CMake + MSVC for that also.
The goal for me is to set up project pro file that just includes static library and headers, no CMake. Should work, but getting strange error.
If that doesn't work out, I'll try setup described in documentation.

URHO3D_HOME seems to be set correctly, since QtCreator finds installation headers.

---

So it was indeed a silly env var problem. Headers were found without problems, but linking didn't like spaces in path it seems.
Now another strange problem occurred: LNK1104: cannot open file ' \Lib\x86\d3d9.lib'.
Is this file necessary? I build Urho3D with URHO3D_OPENGL define, I don't plan to use Direct3D.

-------------------------

Bluemoon | 2017-01-02 00:59:24 UTC | #7

[quote="brachna"]
So it was indeed a silly env var problem. Headers were found without problems, but linking didn't like spaces in path it seems.
Now another strange problem occurred: LNK1104: cannot open file ' \Lib\x86\d3d9.lib'.
Is this file necessary? I build Urho3D with URHO3D_OPENGL define, I don't plan to use Direct3D.[/quote]

Most likely you still have the directX lib listed as part of the libraries in your .pro's LIBS, simply removing it from the entry should get the job done

-------------------------

brachna | 2017-01-02 00:59:25 UTC | #8

Turns out I just forgot to update project with qmake...

It all works now. Thanks everyone, especially Bluemoon.

Updated template for build with OpenGL.

[code]
TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

TARGET = #Your Output Name

#This might be an overkill but I just added all of them as I saw them in the pkgconfig file
#it is for a release build with static library linkage and having angelscript enabled
DEFINES += WIN32 _WINDOWS NDEBUG _SECURE_SCL=0 ENABLE_SSE ENABLE_MINIDUMPS;
DEFINES += ENABLE_FILEWATCHER ENABLE_PROFILING ENABLE_LOGGING ENABLE_ANGELSCRIPT 
DEFINES += URHO3D_STATIC_DEFINE _CRT_SECURE_NO_WARNINGS HAVE_STDINT_H
# For build with OpenGL
DEFINES += URHO3D_OPENGL

# $(URHO_HOME) should point to your Urho3D installation folder
INCLUDEPATH += $(URHO_HOME)\include $(URHO_HOME)\include\SDL

#If you wish you can add these ones depending on your needs
# INCLUDEPATH += $(URHO_HOME)\include\Bullet $(URHO_HOME)\include\kNet
#For build with Direct3D
#$(URHO_HOME)\include\Direct3D9

# Env var pointing to builded Urho3D installation's library
LIBS += -L$(URHO3D_HOME)\lib

if( CONFIG( debug, debug|release ) ): LIBS += -lUrho3D_d
else: LIBS += -lUrho3D

# For build with Direct3D
#$(DIRECTX_SDK) = where your directX sdk is installed for Windows and don't forget to replace x86 with x64 for those on x64 systems
#LIBS += "$(DIRECTX_SDK)\Lib\x86\d3d9.lib"

#Then these guys, every single one of them seems to be needed on Windows
LIBS += kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib
LIBS += dbghelp.lib imm32.lib version.lib winmm.lib ws2_32.lib
# For build with OpenGL
LIBS += opengl32.lib

HEADERS += #Your Header

SOURCES += #Your Source File
[/code]

-------------------------

sirop | 2017-10-27 19:31:23 UTC | #9

[quote="brachna, post:8, topic:284"]
CONFIG += console
[/quote]

is not the same as
`CONFIG -= console` in Bluemoon's post above.

I can compile only with `CONFIG -= console` (MSVC2015).

So why   `CONFIG += console` in your case?

Is it because of `URHO3D_WIN32_CONSOLE:BOOL=OFF/ON` cmake option of the Urho3d build?

-------------------------

sirop | 2017-10-28 12:24:48 UTC | #10

BTW, I noticed using the example of https://github.com/urho3d/Urho3D/wiki/First-Project that ` ENABLE_LOGGING` only enables logging for the Urho3d lib but not for the source code to be compiled .
I do not know why.

However when using the CMake approach the verbose output says:

> cl   /TP -DURHO3D_ANGELSCRIPT -DURHO3D_IK -DURHO3D_LOGGING -DURHO3D_MINIDUMPS -DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSICS -DURHO3D_PROFILING -DURHO3D_THREADING -DURHO3D_URHO2D -DURHO3D_WEBP -D_CRT_SECURE_NO_WARNINGS -ID:\Urho3D\Build\include -ID:\Urho3D\Build\include\Urho3D\ThirdParty -ID:\Urho3D\Build\include\Urho3D\ThirdParty\Bullet /DWIN32 /D_WINDOWS /W3 /GR /EHsc /MP /MD /O2 /Ob2 /DNDEBUG  /fp:fast /Zi /GS- /D _SECURE_SCL=0 /FoCMakeFiles\FirstProject.dir\main.cpp.obj /FdCMakeFiles\FirstProject.dir\ /FS -c "D:\QtProjects\Urho3d\FirstProject - Kopie\main.cpp"

And then substituting `ENABLE_LOGGING` with `URHO3D_LOGGING` in Qt Project file  does indeed enable logging also for _main.cpp_ of FirstProject.

Do not know if the same change for other options will have any noticeable effect.

-------------------------

weitjong | 2017-10-28 14:08:36 UTC | #11

That's the problem when you are reading from a wiki page that is not being well maintained. Not sure where you read it but those `ENABLE_LOGGING` and other `ENABLE_*` build options were renamed to `URHO3D_*` like about 4 years ago already. As for the `URHO3D_LOGGING` build option, it is intentionally not baked into `Urho3D.h` header file, so you have to pass it once when you generate the build tree for the Urho3D library and then another time when you generate the build tree for your own project. I do not use Qt, so not sure how far off I am. HTH anyway.

-------------------------

sirop | 2017-10-29 02:24:18 UTC | #12

In the discussion above there was a hint about Urho3D.pc .

Nowadays it reads:

> Cflags: /DURHO3D_ANGELSCRIPT /DURHO3D_FILEWATCHER /DURHO3D_IK /DURHO3D_LOGGING /DURHO3D_MINIDUMPS /DURHO3D_NAVIGATION /DURHO3D_NETWORK /DURHO3D_PHYSICS /DURHO3D_PROFILING

This means for me: change all `ENABLE*`  to `URHO3D*` in the Qt Project file.

-------------------------

