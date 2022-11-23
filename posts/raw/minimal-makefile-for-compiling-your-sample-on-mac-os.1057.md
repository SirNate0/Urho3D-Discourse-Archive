DanteZ | 2017-01-02 01:05:07 UTC | #1

I hade some fun last night trying to build Urho3D from source and use statically linked in my project. Sine I am pretty new on Mac OS X and clang for few reasons does not fall in my favourite compilers category (GCC and Linux is in my Hearth forever) :slight_smile:. Hoverer, because I started to use Mac and did not wanted to make dual boot Linux on it (pain....), I needed to sort out the compilation on clang.

I tried to make simple sample project and compile from scratch. After some tinkering around I came up with this, dirty, but simple sample. I hope you find it useful:

---------------------------------------------
SRCTOP=..
BINDIR=$(SRCTOP)/Bin

PROGRAM=my-urho3d-using-program

CXX=clang++

Urho3D_INC_DIRS=-I/Users/<...>/GameDev/Urho3D/build/include/Urho3D
ThirdthParty_INC_DIRS=-I/Users/<...>/GameDev/Urho3D/build/include/Urho3D/ThirdParty
Urho3D_LIB_DIRS=-L/Users/<...>/GameDev/Urho3D/build/lib
ThirdthParty_LIB_DIRS=-L/opt/X11/lib

LIB_DIRS=$(Urho3D_LIB_DIRS) $(ThirdthParty_LIB_DIRS)
LIBS=-lUrho3D -lGL
INCLUDE_DIRS=$(Urho3D_INC_DIRS) $(ThirdthParty_INC_DIRS)

CXX_FLAGS=-std=c++11
FRAMEWORKS=-framework Cocoa -framework IOKit -framework AudioUnit -framework CoreAudio -framework ForceFeedback -framework Carbon

SOURCES= MyApplication.cpp

all:
>-mkdir -p $(BINDIR)
>-$(CXX) $(CXX_FLAGS) $(FRAMEWORKS) $(INCLUDE_DIRS) $(LIB_DIRS) $(LIBS) $(SOURCES) -o $(BINDIR)/$(PROGRAM)

clean:
>-rm $(BINDIR)/$(PROGRAM)

-------------------------

weitjong | 2017-01-02 01:05:07 UTC | #2

Welcome to our forum.

It's nice to see a simple Makefile still works with Urho3D library. I suppose you have defined URHO3D_API somewhere else manually to get it to work. And speaking of compiler defines, there are others you may consider to add them into your build system. A few subsystems (e.g. logging) may not work correctly without its corresponding define set, unless your intention is really to disable them. I would remove /opt/X11/lib from the ThirdParty lib dirs at it does not exist (at least on my Mac VM). And depends on what you actually reference in your own project, you may need other frameworks like CoreServices. You may consult the generated "Urho3D.pc" in the Urho3D build-tree to get the comprehensive list of libs, defines, and flags. The list is just a reference. As I said earlier, simple is nice too.

-------------------------

DanteZ | 2017-01-02 01:05:07 UTC | #3

Thanks fore the reply weitjong :slight_smile:. 
And I take my hat off on Urho3D code. Very nice, clean and easy to understand. I try to write same way and, so when I look at it sometimes it even feels like my own. :smiley:

Regarding Makefile. You are correct, that I don't need /opt/X11/lib, I still feel weird about this framework thing on Mac (though it looks fantastically simple). I actually needed to -framework OpenGL, Instead of trying to link GL like on gcc.

Regarding the logging - nope my intentions is to keep it working and if loging means Urho3d.log file I see in current directory - it works.

Thanks for the tip on Urho3D.pc, I will definitely take a look at it. On URHO3D_API - I don't remember manually defining it anywhere, my environment variables are clean. All I did as addition. I made Data folders:
??? CoreData
??? ??? RenderPaths
??? ??? ??? Forward.xml
??? ??? Techniques
???     ??? NoTexture.xml
??? Data
??? Textures
??? ??? Ramp.png
??? ??? Spot.png


The reasons why I choose Makefile over cmake and suggested practices are simple:
- I am stubborn institutionalised high frequency server developer for nix* platforms :smiley:. And my IDE is shell and VIM. My build system normally is Makefiles, automake, autoconf etc. I want to feel all the linkages and dependencies and keep write my code in VIM.

I am newbie in OpenGL, as hobbist I went through OpenGL, Ogre, Unity, Marmalade etc. And stopped on Urho3D, probably because I see familiar excellent code, great potential and access to all levels from Scene Management systems to OpenGL. Great job! However - since I am newbie I might quite possibly do something wrong here.

Here is actually working Makefile for simple running project:

-----------------------------------------------------
SRCTOP=..
BINDIR=$(SRCTOP)/Bin

PROGRAM=my-urho3d-spike

CXX=clang++

ROOT_DIR=<../Users/...>

Urho3D_INC_DIRS=-I$(ROOT_DIR)/Urho3D/build/include/Urho3D
ThirdthParty_INC_DIRS=-I$(ROOT_DIR)/Urho3D/build/include/Urho3D/ThirdParty
Urho3D_LIB_DIRS=-L/$(ROOT_DIR)/Urho3D/build/lib

LIB_DIRS=$(Urho3D_LIB_DIRS)
LIBS=-lUrho3D
INCLUDE_DIRS=$(Urho3D_INC_DIRS) $(ThirdthParty_INC_DIRS)

CXX_FLAGS=-std=c++11

FRAMEWORKS=-framework Cocoa -framework IOKit -framework AudioUnit -framework CoreAudio -framework ForceFeedback -framework Carbon -framework OpenGL -framework CoreServices

SOURCES=MyApplication.cpp

all:
>-mkdir -p $(BINDIR)
>-$(CXX) $(CXX_FLAGS) $(FRAMEWORKS) $(DEFINES) $(INCLUDE_DIRS) $(LIB_DIRS) $(LIBS) $(SOURCES) -o $(BINDIR)/$(PROGRAM)

clean:
>-rm $(BINDIR)/$(PROGRAM)

----------------------------------------------

Tried it, built it, looks like working. I will start to add cameras, some teapot meshes for further test. But it looks like it might work very well. :slight_smile:

-------------------------

weitjong | 2017-01-02 01:05:07 UTC | #4

When you start to include more of Urho API header files, sooner or later you know what I meant. Either you have copied Urho3D.h from somewhere to your project source or you have the URHO3D_API manually defined,  you will get build error otherwise. 

On the logging,  I meant to say the logging entry from your own app. The logging macros are no-op without the corresponding define.

And I thought all this while I am the only Linux geek here using terminal as IDE and Vim as editor. Welcome indeed.

-------------------------

DanteZ | 2017-01-02 01:05:07 UTC | #5

Yep. Urho3D.h is included in main .cpp. And know comes to my mind, I remember I did that exactly because of URHO3D_API. Sorry totally forgot about it :smiley:.

-------------------------

bmcorser | 2017-01-02 01:09:26 UTC | #6

Anyone who makes it this far down the post might be interested in [topic1740.html](http://discourse.urho3d.io/t/building-samples-on-mac-os-x-el-capitan/1675/1) (it's a Makefile for building the sample applications on OS X)

-------------------------

