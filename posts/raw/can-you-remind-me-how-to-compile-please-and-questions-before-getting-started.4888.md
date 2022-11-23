noals | 2019-02-01 15:15:12 UTC | #1

hi,
i have a new project i want to try with urho3D but that do a while i didn't used linux so i'm a bit lost, i forgot how i was compiling before.
i was able to compile urho3D successfully but i don't remember how i was doing for a project.

if i'm not wrong i set the URHO3D_HOME environment variable in the .bashrc file and my project is well set.
-bin
---CoreData
---Data
-CMake
-cmake_generic.sh
-CMakeLists.txt
-main.cpp

my main.cpp is an old one just to get started but i think it should compile fine.
https://pastebin.com/5RzLD9jR

before i was using a little script with : 
"./cmake_generic.sh /home/noals/Bureau/mf1_build -DCMAKE_BUILD_TYPE=Debug"
but i'm missing a step and i don't remember which one ^^;
i know the first step is to tell the compiler all files to compile and then the second step is to compile but dunno, i'm a bit confused.
could you remind me how to compile my little project to get started please ?


while i'm at it, i have a few questions : 
-is there a ide you would recommend to me ? before i was only compiling through the terminal but this project will be bigger i think so i will need an ide to see things clearly. is it hard to configure kdevelop ? i was interested in this one.
-i saw on the feature that there is knet with urho3D, my first step will be network programming and i know there is a tuto about that but is there a problem with knet if i want to compile my project for android later ?
i want to do a mmorpg but i won't need realtime information kinda, i mean i will only use the network engine to communicate with my database (postgresql) and calculate algos like damage calculation when a player fight a mob or stuff like that. any advice for that too ?
(i know a bit about network programming, i started with java and socket programming actually using the knockknock protocole tutorial from oracle but java was just a pain at some point so i'm back with urdho3D ^^)

thx

-------------------------

Modanung | 2019-02-01 17:30:08 UTC | #2

[quote="noals, post:1, topic:4888"]
i’m missing a step and i don’t remember which one ^^
[/quote]
Could it be `make`? :slight_smile:

-------------------------

noals | 2019-02-01 18:03:04 UTC | #3

yes, i think i don't use my little script as i should so the compiler doesn't find the right directory, i'm using windows while answering right now, i will test tomorrow on linux and to tell how it goes. thx for your support. ^^;

-------------------------

Leith | 2019-02-01 22:52:40 UTC | #4

With regards to IDE, there's lots of choices. I'm using the CodeBlocks IDE on both Linux and Windows. It's nice to have a single toolchain across platforms, on the rare occasions that I need to switch over.

-------------------------

weitjong | 2019-02-02 01:32:35 UTC | #5

If you are using a version for casual desktop usage (as opposed to minimal server install) from any Linux distro then most probably you have “rake” already installed. And if so, just do this from the Urho project root to build Urho3D. 

```
$ rake cmake && rake make
```

This will create a build tree at the default location: /path/to/Urho-project-root/build/native. Set the URHO3D_HOME env-var to point to this build tree path and export it. 

Assuming you just getting started with your own new project, create the skeleton project using “scaffolding” task. 

```
$ rake scaffolding dir=/path/to/your-project-root
```

Now, repeat the steps how you build Urho3D lib earlier, but now substitute the project with your own project. That is, in your own project root, do this. 

```
$ rake cmake && rake make
```

And that’s it. Your build tree is in /path/to/your-project-root/build/native naturally. 

Good luck. 

BTW, knet has been replaced with SlikeNet in master branch.

EDIT: the default build tree path between master and 1.7 tag is different, so adjust accordingly.

-------------------------

Modanung | 2019-02-02 16:02:29 UTC | #6

My preferred IDE is QtCreator with [custom wizards](https://discourse.urho3d.io/t/wrench-class-and-project-wizards-for-qtcreator/2076), btw.

-------------------------

noals | 2019-02-02 10:21:39 UTC | #7

hi, thx, well i think i didn't understand how to set my environment variable.
i had to install rake but everything went fine except compilation.
even trying with the varibale set manually like the compiler say, it doesn't work
>:~/Bureau/mf1$ rake cmake URHO3D_HOME=home/noals/Bureau/Urho3D/build/native && rake make

> CMake Deprecation Warning at CMakeLists.txt:9 (cmake_policy):
  The OLD behavior for policy CMP0026 will be removed from a future version
  of CMake.

 >The cmake-policies(7) manual explains that the OLD behaviors of all
  policies are deprecated and that a policy should be set to OLD only under
  specific short-term circumstances.  Projects should be ported to the NEW
  behavior and not rely on setting a policy to OLD.

>CMake Error at CMake/Modules/FindUrho3D.cmake:343 (message):
  Could NOT find compatible Urho3D library in Urho3D SDK installation or
  build tree or in Android library.  Use URHO3D_HOME environment variable or
  build option to specify the location of the non-default SDK installation or
  build tree.
Call Stack (most recent call first):
  CMake/Modules/UrhoCommon.cmake:244 (find_package)
  CMakeLists.txt:23 (include)

>-- Configuring incomplete, errors occurred!
See also "/home/noals/Bureau/mf1/build/native/CMakeFiles/CMakeOutput.log".

and the CMakeOutput.log
https://pastebin.com/dMtXnVtd

i set my variable by adding a line at the end of .bashrc and .profile just in case it override the first one but it doesn't seem to work.
># Setting environment variables
>export URHO3D_HOME="/home/noals/Bureau/Urho3D/build/native"

-------------------------

noals | 2019-02-02 10:22:20 UTC | #8

i guess that's a good idea since i want it to be crossplatform.

-------------------------

weitjong | 2019-02-02 13:23:31 UTC | #9

Have you actually build Urho3D lib successfully. The Urho3D build tree path should contain two subdirs: include/ and lib/. Only then your URHO3D_HOME pointing to there would be accepted. Your error indicates this is not the case.

There are a few ways to set env-var on *nix system. The method that you mentioned in your last comment are equally valid. Just note that setting in bash profile does not take effect immediately in the current session, unless you explicitly “source” the file in the current session.

-------------------------

Leith | 2019-02-02 13:30:05 UTC | #10

These days its ALL about cross platform, and not which platform you develop on.

-------------------------

Leith | 2019-02-02 13:42:49 UTC | #11

On linux, the install process is easier than has been described in my opinion, don't mess around with rake, use cmake-gui to create your build folder - and once you have it, build it using make, and finally, link your app to the static lib

-------------------------

weitjong | 2019-02-02 14:07:20 UTC | #12

Some people like GUI and some don’t. And for those that don’t, we have bash helper scripts to pull it off using CLI. The rake tasks that I mentioned before simply invoke those bash shell scripts. It is also the one being tested in our CI build. Headless, no GUI, and not for faint hearted.

Choose your own poison. The beauty of our build system is, it does not force anyone to use one method or another. Regardless, URHO3D_HOME needs to be set correctly, or “you shall not pass”.

-------------------------

Leith | 2019-02-02 14:11:24 UTC | #13

funny, I didn't set any environmental variables, yet here I am - but I agree its nice to have options - love your work on the build system.

-------------------------

weitjong | 2019-02-02 14:14:00 UTC | #14

Our build system also follows the old *nix convention. Configure (CMake), make, make install. If you do that then the lib is installed to the system default location. So, the downstream project can find it without problem. The drawback of this approach is, only one version of the lib can be installed at any single time. Using URHO3D_HOME, one can use the lib without installing it and the variable can be set to any build tree path you may have. Just set it on the fly before invoking CMake.

-------------------------

Leith | 2019-02-02 14:14:24 UTC | #15

I built the lib in-situ, and link to it directly, its not "installed" in the conventional sense, but yes I see the beauty

-------------------------

weitjong | 2019-02-02 14:15:57 UTC | #16

Like I said there are more than one ways. Some are supported officially and some are don’t.

-------------------------

noals | 2019-02-02 15:53:12 UTC | #17

Yes, i built Urho3D lib successfully, it went to 100% following the tuto https://github.com/urho3d/Urho3D/wiki/Getting-started-in-Linux. I have the include/Urho3D/directories and .h and lib/libUrho3D.a
And each time i changed the path to URHO3D_HOME, i restarted the computer so i don't understand.

edit: and i use linux mint, my installation is pretty clean, i installed it few days ago especially for programming with urho3D

-------------------------

Leith | 2019-02-02 16:12:40 UTC | #18

I use linux mint also, and I am pretty 'new' at linux, despite my 'previous history' - did you upgrade to tara yet? in the update manager thing, look in the Edit menu for upgrade... ok so you dont really need to set up environmental bullshit, if you have built the lib, you just need to link to it in your app - you need to tell your compiler where it is - I use code blocks ide, and for me, this means adjusting the Build Options, going to the Linker settings, and adding the static lib - the pthread thing threw me for a day

-------------------------

Leith | 2019-02-02 16:21:08 UTC | #19

to be specific, maybe a screen shot is better![snapped|506x500](upload://ui3ja7f8lH63jqeNY7hHkooxOeC.png)
crap, my mouse cursor is in the way, but this is in the right direction

-pthread
-ldl
-lGL
-lGLU
-lGLEW

Super happy to work out any issues you have and make it easier for the next guy.

-------------------------

weitjong | 2019-02-02 17:08:49 UTC | #20

Then it must have found an incompatible Urho3D lib there. Make sure your project build options and build configuration are aligned with the Urho3D lib. I am not sure what exactly went wrong with your setup, but one would for sure get the similar error as yours when, says, pointing URHO3D_HOME to a build tree containing a SHARED lib but expecting a STATIC lib, or pointing to 32-bit lib but expecting 64-bit, etc. Don’t overlook the obvious. Double check everything.

BTW, if you get passed the hurdle then you may try this in your own project root: “rake cmake codeblocks” or “rake cmake codelite” or “rake cmake eclipse”. After that, use the respective IDE to build your own project. There is no need to adjust anything manually in the IDE. Instead always make config setting changes in the CMakeLists.txt and use CMake to reconfigure/regenerate the build tree. Any manual config setting changes in the IDE will be lost. Unless you are happy to “eject” from CMake after your initial build tree is successfully created then you could make further changes using the IDE. But note that I will personally not support such approach. In other words, you will be on your own if you follow this path.

-------------------------

noals | 2019-02-02 20:28:23 UTC | #21

Well, before i was compiling without IDE because i like to keep things simple. i like to know what i'm doing so if there is a problem, i can actually fix it ^^; i don't know either what's wrong here.
i tryed to build it with the WIN32 option but i had the same errors trying to compile the generic project, i kinda overlook the cmake for the generic projet, i didn't do it again because if it was set to 32 instead of 64 it should have work fine i think. i'm thinking about erasing everything and redo it again but it's getting confusing again. maybe i should use 2 urho3D directory, one for 32, one for 64, adding the 2 in my environment and try again, dunno. lol

You tell me to not overlook things, when i use cmake . to compile urho3D i have quite a lot of warning, do i really need those to compile urho3D ?

>-- Could NOT find Readline development library (missing: READLINE_LIBRARIES READLINE_INCLUDE_DIRS) 
-- Could NOT find OSS development library (missing: OSS_LIBRARIES) 
-- Could NOT find Jack Audio Connection Kit development library (missing: JACK_LIBRARIES JACK_INCLUDE_DIRS) 
-- Could NOT find PulseAudio development library (missing: PULSEAUDIO_LIBRARIES PULSEAUDIO_INCLUDE_DIRS) 
-- Could NOT find Esound development library (missing: ESOUND_LIBRARIES ESOUND_INCLUDE_DIRS) -- Could NOT find Readline development library (missing: READLINE_LIBRARIES READLINE_INCLUDE_DIRS) 
-- Could NOT find OSS development library (missing: OSS_LIBRARIES) 
-- Could NOT find Jack Audio Connection Kit development library (missing: JACK_LIBRARIES JACK_INCLUDE_DIRS) 
-- Could NOT find PulseAudio development library (missing: PULSEAUDIO_LIBRARIES PULSEAUDIO_INCLUDE_DIRS) 
-- Could NOT find Esound development library (missing: ESOUND_LIBRARIES ESOUND_INCLUDE_DIRS) 
-- Could NOT find aRts development library (missing: ARTS_LIBRARIES ARTS_INCLUDE_DIRS) 
-- Could NOT find NetworkAudioSystem development library (missing: NAS_LIBRARIES NAS_INCLUDE_DIRS) 
-- Could NOT find RoarAudio development library (missing: SNDIO_LIBRARIES SNDIO_INCLUDE_DIRS) 
-- Could NOT find FusionSound development library (missing: FUSIONSOUND_LIBRARIES FUSIONSOUND_INCLUDE_DIRS) (Required is at least version "1.0.0")
-- Could NOT find Secret Rabbit Code (aka libsamplerate) development library (missing: SECRETRABBITCODE_LIBRARIES SECRETRABBITCODE_INCLUDE_DIRS) 
-- Could NOT find Wayland display server (missing: WAYLAND_CLIENT WAYLAND_SCANNER WAYLAND_CURSOR WAYLAND_EGL XKB WAYLAND_INCLUDE_DIRS WAYLAND_CORE_PROTOCOL_DIR WAYLAND_PROTOCOLS_DIR) 
-- Could NOT find Direct Generic Buffer Ma-- Could NOT find Readline development library (missing: READLINE_LIBRARIES READLINE_INCLUDE_DIRS) 
-- Could NOT find OSS development library (missing: OSS_LIBRARIES) 
-- Could NOT find Jack Audio Connection Kit development library (missing: JACK_LIBRARIES JACK_INCLUDE_DIRS) 
-- Could NOT find PulseAudio development library (missing: PULSEAUDIO_LIBRARIES PULSEAUDIO_INCLUDE_DIRS) 
-- Could NOT find Esound development library (missing: ESOUND_LIBRARIES ESOUND_INCLUDE_DIRS) 
-- Could NOT find aRts development library (missing: ARTS_LIBRARIES ARTS_INCLUDE_DIRS) 
-- Could NOT find NetworkAudioSystem development library (missing: NAS_LIBRARIES NAS_INCLUDE_DIRS) 
-- Could NOT find RoarAudio development library (missing: SNDIO_LIBRARIES SNDIO_INCLUDE_DIRS) 
-- Could NOT find FusionSound development library (missing: FUSIONSOUND_LIBRARIES FUSIONSOUND_INCLUDE_DIRS) (Required is at least version "1.0.0")
-- Could NOT find Secret Rabbit Code (aka libsamplerate) development library (missing: SECRETRABBITCODE_LIBRARIES SECRETRABBITCODE_INCLUDE_DIRS) 
-- Could NOT find Wayland display server (missing: WAYLAND_CLIENT WAYLAND_SCANNER WAYLAND_CURSOR WAYLAND_EGL XKB WAYLAND_INCLUDE_DIRS WAYLAND_CORE_PROTOCOL_DIR WAYLAND_PROTOCOLS_DIR) 
-- Could NOT find Direct Generic Buffer Management development library (missing: GBM_LIBRARIES GBM_INCLUDE_DIRS) 
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE)nagement development library (missing: GBM_LIBRARIES GBM_INCLUDE_DIRS) 
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE)
-- Could NOT find aRts development library (missing: ARTS_LIBRARIES ARTS_INCLUDE_DIRS) 
-- Could NOT find NetworkAudioSystem development library (missing: NAS_LIBRARIES NAS_INCLUDE_DIRS) 
-- Could NOT find RoarAudio development library (missing: SNDIO_LIBRARIES SNDIO_INCLUDE_DIRS) 
-- Could NOT find FusionSound development library (missing: FUSIONSOUND_LIBRARIES FUSIONSOUND_INCLUDE_DIRS) (Required is at least version "1.0.0")
-- Could NOT find Secret Rabbit Code (aka libsamplerate) development library (missing: SECRETRABBITCODE_LIBRARIES SECRETRABBITCODE_INCLUDE_DIRS) 
-- Could NOT find Wayland display server (missing: WAYLAND_CLIENT WAYLAND_SCANNER WAYLAND_CURSOR WAYLAND_EGL XKB WAYLAND_INCLUDE_DIRS WAYLAND_CORE_PROTOCOL_DIR WAYLAND_PROTOCOLS_DIR) 
-- Could NOT find Direct Generic Buffer Management development library (missing: GBM_LIBRARIES GBM_INCLUDE_DIRS) 
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE)

you also told me about the master branch too for the other networking library, i'm using the release 1.7, is it knet or the other with it ?
is there something i should use to have everything up to date ? im not familiar with those things, maybe it could help me fix the problem. 

@Leith yes, i guess i have tara since i installed recently and it's up to date. thx for the help with codeblock but i better check this problem well, im going for a long project and if i can't even compile manually or don't know why, i'm sure it will be a problem later for me...

-------------------------

I3DB | 2019-02-02 20:42:35 UTC | #22

[quote="noals, post:21, topic:4888"]
i’m using the release 1.7
[/quote]


[The urhosharp team used 1.7 and have a set make scripts](https://github.com/xamarin/urho) that work on nearly any windows platform, or all of them. They didn't do well with networking though.

-------------------------

weitjong | 2019-02-03 02:55:20 UTC | #23

Have you read the online docs. https://urho3d.github.io/documentation/1.7/_building.html? Those output lines you posted above were coming from SDL (and not from Urho specifically). Also why some of the lines keep repeating? Have you modified the build scripts? If you read the doc then you should know that it is ok to build without the non-essential software deps. But for those essential deps, you need to have one chosen and installed. For example for the sound server (essential), you may want to take care the missing PulseAudio, since it does not seem you have others installed. For display server (essential), if you already have X then you can ignore the missing Wayland. Note that SDL supports multiple sound and display servers. But for starter, just go with common combination: PulseAudio + X. 

CMake supports out-of-source build. What it means is that you can have only one project source tree and in theory limitless count of project build trees. You can instruct CMake, either using CMake-GUI, or CLI, or through our helper script or via rake to generate the build tree in an alternative path instead of the default path (specified in the our build script). One build tree for each build config. Never mixing a same build tree for different build config. You will be asking for trouble, if you do.

You will have to decide for your own whether to use release 1.7 or (unreleased) master version for your own project. As any open source projects, master branch may not be stable at time and need help from its users to send PR for bug fixes. Using release tag is stable, in the sense that the code is frozen (with all the bugs baked in too). We also do not provide any back porting fixes.

-------------------------

noals | 2019-02-03 07:44:44 UTC | #24

Yes i read a bit of the doc but it compiled fine with build-essential and a few other packages so i didn't really paid attention. No i didn't modified the build scripts, i wouldn't know how lol
I will go through this more seriously and redo everything again, i'm just surprised it didn't went like on ubuntu years ago. I switched to linux mint because i was able to have sound on this one.. >< and i like the interface better.

About which branch i want to use, i think i better use the unreleased version, at least until 1.8 come out i think. At first, i will spend lot of time with network programming so it will be more a c++ console application than something else. I just know that it will be easier to add graphic and sound later with Urho3D. My project is a bit ambitious but it's also kind of minimalist, i won't need physic for example.

How do i set up my environment for that ?

-------------------------

weitjong | 2019-02-03 09:08:09 UTC | #25

If you plan to use master branch then you may want to try our latest build mechanism using Docker Build Environment (or DBE for short). Check it out. Read the new segment of the docs in the HEAD version of the online doc. The DBE frees you from having to prepare your host/build machine entirely, not even the “build-essential” is required. The only prerequisite is “Docker-CE” must be installed first.

To build Urho3D lib, from Urho3D project root:
```
$ script/dockerized.sh native
```

By default the build tree is generated using rake tasks internally as before, however now it happens inside a docker container. The build tree path by default is “/path/to/Urho3D-project-root/build/native” in your host machine, so it is the same as conventional build. Set the URHO3D_HOME env-var to point to this path and export it. Again, same as before.

To scaffolding new project:
```
$ script/dockerized.sh native rake scaffolding dir=/path/to/your-project-root
```
The only caveat is that this path must be accessible by the docker container.

To build your newly scaffolded project, go to your project root:
```
$ script/dockerized.sh native
```

You can also set the env-var on the fly, like so:
```
$ URHO3D_HOME=“/path/to/Urho3D-project-root/build/native” URHO3D_other-build-option=.... script/dockerized.sh native
```

Good luck.

-------------------------

Leith | 2019-02-03 12:16:46 UTC | #26

I am happy to step you through building urho using cmake-gui if you would like another option - and yes I recommend using the latest version, on git, not the link to 1.7 on the home page

-------------------------

noals | 2019-02-03 15:10:11 UTC | #27

thx, everything worked fine.
i compiled urho3D-master and the generic project that was "scaffolded"

"**Read the new segment of the docs in the HEAD version of the online doc.**"

>WHAT DOESN'T WORK:
> - Networking. Javascript can only use http and websockets protocols and at the moment it's not supported.

what about SlikeNet ? could you give me more info about it ?

@Leith actually i don't use tara, tara is mint 19 and i use tessa that is mint 19.1
i saw it following the tutorial to install docker.
https://agipme.fr/2018/10/installation-de-docker-sur-linux-mint-19.html

i will try to get familiar with the engine as it is, thx a lot for all your help.

-------------------------

weitjong | 2019-02-03 15:31:57 UTC | #28

I am not the maintainer for the networking subsystem, but I don’t think SlikeNet integration in master branch has brought any changes on networking for Web build. Contribution is welcome.

-------------------------

noals | 2019-02-03 15:55:27 UTC | #29

ok thx, i will check it anyway.

-------------------------

Miegamicis | 2019-02-04 07:51:51 UTC | #30

Networking for web platforms are not supported at the moment. We had some discussions  how to implement it with the current networking library to fully support cross-platform functionality, but so far I haven't yet tried to actually achieve that.

-------------------------

noals | 2019-02-04 09:15:09 UTC | #31

Actually, i'm not really interested in web platform, javascript or the kind, i saw "what doesn't work : networking" so i asked, but i really don't know about portability whatsoever. I know it will be a problem to me but i better try to do something instead of caring about it now.

Already i saw that SLikeNet in Urho3D uses UDP and i didn't see anything about TCP so i will try to implement things like that but i'm still a beginner anyway, i will see how it goes.

-------------------------

Leith | 2019-02-04 12:09:05 UTC | #32

AFAIK SlikeNet is the new version of RakNet, which is totally about UDP, so we have this other thing called CivetWeb, which can do basic http stuff, but not https - I could be wrong, I have not yet turned my hand to networking on this engine

EDIT - theres some mention of https in the civetweb master branch

-------------------------

Miegamicis | 2019-02-04 12:33:30 UTC | #33

SLikeNet also has a TCP support.

-------------------------

noals | 2019-02-04 19:54:35 UTC | #34

@Leith @Miegamicis
Yes, i knew it was RakNet, there was also TCP support with it before but even if SLikeNet support it, i didn't see it implemented in urho3D so i will check the engine. 
I suppose SLikeNet is in the libs used to compile urho3D so the TCP classes should be accessible there, or should i recompile and use SlikeNet as an external lib ? i also need to check the doc to do urho3D objects...

For now, i just compiled my main.cpp test, one thing at a time. ^^

-------------------------

Leith | 2019-02-06 05:06:33 UTC | #35

I've been asking all kinds of "stupid" questions for the past couple of weeks, and learned a lot by doing so. I have no idea if SlikeNet's TCP stuff is exposed to Urho or not, it's a fairly recent addition so I would not be shocked to find the current implementation is half-baked. If that is the case, I'm happy to help with anything network-related, and will gladly assist in creating a solution, providing of course that you're happy to share such a solution back to the community, and see it appear in the next public release.

-------------------------

Miegamicis | 2019-02-06 08:03:18 UTC | #36

All the features of the SLikeNet can be easily "opened" to Urho3D engine by changing the CMake file for the library:

https://github.com/urho3d/Urho3D/blob/master/Source/ThirdParty/SLikeNet/CMakeLists.txt#L16-L24

These flags cover all of the SLikeNet features, most of them are disabled at the moment because the engine is not using them. Feel free to change that if needed. As I see, `_RAKNET_SUPPORT_TCPInterface=0` is disabled at the moment, but I did get it to work when I was doing the implementation and testing out different capabilities.

-------------------------

Leith | 2019-02-06 08:35:25 UTC | #37

Thanks, TCP is the backbone of a lot of my networked games, it provides the pipe to talk to the web backend scripts, typically php interface to sql - I can't do without a pipe, and plain http is becoming almost extinct in the face of https and ssl certification ... noteworthy that my university dropped teaching web backend tech in the year after I finished my degree, apparently now they teach game dev, but provide no strong foundation. It makes me sad that those who come behind me will know less and be of less value, but spend the same time and money for the same degree.
I guess what I am pointing out is that it is a lot cheaper and faster to set up a webserver and database and write the interface scripts, than to write a custom server on a custom protocol and find an affordable rackserver host to run the server.

-------------------------

