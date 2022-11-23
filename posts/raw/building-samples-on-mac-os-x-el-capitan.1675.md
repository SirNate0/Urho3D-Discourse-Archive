bmcorser | 2017-01-02 01:09:26 UTC | #1

I was interested in building some of the sample apps, but being fairly clueless on The Ways Of Compilers asked on the IRC channel (#urho3d on freenode) where valera_rozuvan was kind enough to point me to this post [topic1088.html](http://discourse.urho3d.io/t/minimal-makefile-for-compiling-your-sample-on-mac-os/1057/1) which helped a lot.

With a few tweaks, we managed to get the following together, which should compile samples on OS X:
[code]

SAMPLE_NAME=<name of sample (without .cpp)>
URHO3D_BASEDIR=/Users/<you>/<path/<to>/Urho3D

CXX=clang++

Urho3D_INC_DIRS=-I$(URHO3D_BASEDIR)/build/include
Urho3D_Samples_DIR=-I../
ThirdthParty_INC_DIRS=-I$(URHO3D_BASEDIR)/build/include/Urho3D/ThirdParty
Urho3D_LIB_DIRS=-L$(URHO3D_BASEDIR)/build/lib
ThirdthParty_LIB_DIRS=-L/opt/X11/lib

LIB_DIRS=$(Urho3D_LIB_DIRS) $(ThirdthParty_LIB_DIRS)
LIBS=-lUrho3D
INCLUDE_DIRS=$(Urho3D_INC_DIRS) $(ThirdthParty_INC_DIRS) $(Urho3D_Samples_DIR)

CXX_FLAGS=-stdlib=libc++
FRAMEWORKS=-framework Cocoa -framework IOKit -framework AudioUnit -framework CoreAudio -framework ForceFeedback -framework Carbon -framework OpenGL

SOURCES=$(SAMPLE_NAME).cpp

all:
	$(CXX) $(CXX_FLAGS) $(FRAMEWORKS) $(INCLUDE_DIRS) $(LIB_DIRS) $(LIBS) $(SOURCES) -o $(SAMPLE_NAME)

clean:
	rm $(SAMPLE_NAME)
[/code]

-------------------------

weitjong | 2017-01-02 01:09:26 UTC | #2

That's cool. However, the subject of your post gives the impression that we need different Makefile template for El Capitan which it really doesn't. There are still a few things missing in the template. Once your sample app goes a bit more complex then you will realize it.

For me, the easiest way to get an up-to-date Makefile is to let CMake generates it. Assuming the URHO3D_HOME is already being set correctly in the host system pointing to a natively built Urho3D build tree, then do this.

[code]
cd /path/to/your/Urho3D/project/root/where/Rakefile/resided && rake scaffolding dir=/tmp/MySample
cd /tmp/MySample && rake cmake build_tree=.
[/code]
By default our build system should use Makefile generator, so the last command above should give a generated Makefile in the /tmp/MySample directory. If the auto-generated Makefile contains too much things for you then you can find the crux of the configuration in these two files: flags.make and link.txt found in /tmp/MySamples/CMakeFiles/Main.dir directory. You should see that information more or less available in the generated Urho3D.pc file (configuration file for pkg-config) as well. So, another sane approach is to use hand-crafted Makefile calling pkg-config tool internally to get all the details.

Now I am not saying what has been configured by our build system with the CMake is 100% correct (it is still under active development), but I can safely say using this approach you will get an up-to-date settings always. As we constantly improving our build system, the configuration you see today might get change later.

-------------------------

bmcorser | 2017-01-02 01:09:27 UTC | #3

That's great, ty weitjong. Now I have my project dir separate from the Urho3D sources :+1:

-------------------------

