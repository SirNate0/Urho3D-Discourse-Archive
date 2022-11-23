booneruni | 2017-12-05 23:34:52 UTC | #1

I'm currently trying to get urho working on my Tinkerboard running the official ASUS image of TiinkerOS.

I have tried the rasperry pi .deb's found on the sourceforge as well as a few others and the only ones that do anything after a successful installation are the 1.7 ARM STATIC A9, and ARM SHARED A9. 

I don't actually know if those two have any impactful differences.

They both produce this output (the last line also shows up in a popup box, so it kinda works)

ERROR: Could not create window, root cause: 'Could not initialize EGL'

https://hastebin.com/raw/ehufinugaf --01HelloWorld output

https://github.com/urho3d/Urho3D/blob/master/Source/ThirdParty/SDL/src/video/SDL_egl.c#L272 --line showing me the error

http://m.uploadedit.com/bbtc/1512498083388.txt --strace output

I'd try the experimental arm build process but that's a single paragraph that's clearly written for more intermediate users. I have no idea what half the stuff it refers to, so i can't even attempt to build that just yet. 

But is this issue with the .debs workaroundable do you think?

-------------------------

weitjong | 2017-12-09 04:30:11 UTC | #2

You already off for a good start. RPI prebuilt package should only be used for Raspberry-Pi. Use the ARM package for the rest of the generic ARM board running on Linux kernel or better yet build from source directly. This is because those prebuilt packages are just build artifact from out ARM-CI. The build settings there may or may not matches the ARM processor you have on your board.

If you don’t know how to cross-compile in general, you can search for it using google. Basically you need to tell the build system where is your compiler toolchain is and where is your sysroot (device system root). You can just download the sysroot repo provided by Urho to your host/build system or just connect your device to your host and mount the system root of your device to you host file system (obviously you need Linux host for that). Alternatively, the easier route would be learn how to build Urho from a desktop Linux host. Once you graduate from that then connect a keyboard and monitor to your board (assuming it can do that), boot it up and build Urho directly on the device itself. Slow no doubt. 

As for your problem, I think it means it missed some of the required dependency packages. We have the list documented in our online documentation. Good luck.

-------------------------

booneruni | 2017-12-06 02:11:01 UTC | #3

> where is your compiler toolchain is and where is your sysroot (device system root).

What do you mean by this. I am a novice in the linux side of things so I don't have the context to know what that means exactly. 

Also for reasons that are irrelevant, this is my desktop pc. The Tinkerboard is my daily driver and there's no backup/2nd computer. 

>You can just download the sysroot repo provided by Urho

I've got the source downloaded from git, is it that?

What was all that stuff about little endians on the page listing the experimental arm build process?

-------------------------

booneruni | 2017-12-07 20:24:03 UTC | #4

Excuse the double post, but I've gotten somewhere else with this.

this is the output i get after doing ./cmake_arm.sh and then doing 'make'
https://pastebin.com/te04dfeB

 ./cmake_generic.sh and then 'make' also didn't work. failing at the same point

-------------------------

weitjong | 2017-12-06 11:08:12 UTC | #5

Like I said earlier, if this is your first time doing cross-compiling then do some research on Google first. Come back here again when you have understood what I meant by cross-compiler toolchain and system root. I will wait :slight_smile: .

If you take the easier route though by building directly on the device/board itself then you just have to make sure you have all the prerequisite dependency dev packages installed before starting building anything. Again good luck.

-------------------------

booneruni | 2017-12-06 18:38:56 UTC | #6

I am building it ON my tinkerboard and am still getting the errors in my "excuse the double post" hastebin log. There is no 2nd pc, so there's no need for cross compilation. I'm trying to get this to work ON a tinkerboard FOR a tinkerboard.

-------------------------

jmiller | 2017-12-06 19:03:02 UTC | #7

We had spent some hours looking into this before posting. What I was thinking is that SDL's eglInitialize() was failing on this configuration, and there seems to be some precedent (and in the first result thread, did I see a patch?). https://www.google.com/search?q=eglInitialize+tinkerboard

-------------------------

booneruni | 2017-12-06 22:23:59 UTC | #8

i might be getting different results bc it's redirecting me to the .co.uk, or I just don't know what i'm supposed to be looking for in that first link |:

-------------------------

weitjong | 2017-12-07 01:55:08 UTC | #9

My apology. Sometime my English fails me, expecially before my morning coffee. Now I understood perfectly what you meant by not having 2nd computer. Earlier I thought you wanted to say you have a primary PC (implying Windows) and don’t have another one on Linux for cross-compiling. In which case it should not be a showstopper to learn cross-compiling still. 

Anyway, your errors are compilation error. It looks different than runtime errror pointed out by @jmiller (I could be wrong though). Your compilation errors were more probably caused by missing GL header file. And that’s the reason why I asked you to ensure you have installed all the required dev packages. I could not be more specific here to tell you what exactly is the missing package name because I don’t have that device and I also don’t know whether Asus’s package repository is based on Debian or not.

-------------------------

booneruni | 2017-12-07 02:23:01 UTC | #10

Okay, i've just gone through this list https://urho3d.github.io/documentation/HEAD/_building.html#Building_Prerequisites and double checked, i think there might have been one or two that i missed (or assumed i already had)

I hope it was just a small mistake like that and that it gets past 56% this time

E;

Nope same failure at 56%. it is debian based I think, btw

-------------------------

weitjong | 2017-12-07 04:41:26 UTC | #11

What I found it strange is that your output actually didn’t complain about missing header, but the GL functions that would have been declared by the GL.h. It could be a wrong or incomplete header file is installed in your system (only a wild guess).

-------------------------

booneruni | 2017-12-07 04:59:28 UTC | #12

Are you referring to the output of the example, or output of compiling it?

-------------------------

weitjong | 2017-12-07 05:46:56 UTC | #13

Output from your paste bin. Unless, of course, if you didn’t paste all the errors then it would explain it.

-------------------------

booneruni | 2017-12-07 05:47:12 UTC | #14

From that I take it you didn't see the 2nd paste bin link, the first one has everything that was given. The log from the 2nd pastebin link is the output from my compiling attempt. I ommited logs from the 50-55% steps because those had completed without fail.

-------------------------

weitjong | 2017-12-07 06:11:30 UTC | #15

If so, then it is strange as I first put it. You have the header file and yet your header file didn’t do what it supposed to do.

-------------------------

booneruni | 2017-12-07 06:29:15 UTC | #16

Is that a header file in the source i downloaded? do you think if i get a working one and try compiling that it would get a little bit further along?

-------------------------

weitjong | 2017-12-07 14:10:32 UTC | #17

No, that header file comes from the dev package, not part of Urho source code. Look for it somewhere in your /usr/include or its subdirs. This is normally where dev headers get installed.

-------------------------

booneruni | 2017-12-07 20:53:13 UTC | #18

I've just gone through the prerequisite list again and reinstalled stuff i already had just in case those downloaded wrong. But which header file are you referencing exactly? 

The only thing i can see from the compiler output is a .cpp file: Urho3D/Source/Urho3D/Graphics/OpenGL/OGLGraphics.cpp

Everything you've said sounds reasonable, but I have no idea what to do with any of that information... I'm a novice thrown in at the deep end because of the platform this tinkerboard runs on.

I might have to call it quits soon because this is just infuriating



e:

Here's another log after messing around with some libraries, it failed at 50% instead of 56% so i'm just posting it here in case i need to reference it https://pastebin.com/wSPHnw3K

-------------------------

weitjong | 2017-12-08 00:36:24 UTC | #19

I have already answered that. The name of the problematic header is "GL.h". Compare the content of that file in your host system to Urho prepared ARM sysroot to see if there is anything wrong. I have highlighted one of the line. 

https://github.com/urho3d/armhf-sysroot/blob/master/usr/include/GLES/gl.h#L683

-------------------------

booneruni | 2017-12-08 01:34:15 UTC | #20

What do you mean by 'to urho prepared arm sysroot'?

also I found these files;
>linaro@linaro-alip:~$ sudo find / -name "gl.h"
>/usr/include/GL/gl.h
>/usr/include/GLES/gl.h

 And the GLES one has this

> GL_API void GL_APIENTRY glGetBufferParameteriv (GLenum target, GLenum pname, GLint *params);
> GL_API void GL_APIENTRY glGetClipPlanex (GLenum pname, GLfixed eqn[4]);
> GL_API void GL_APIENTRY glGenBuffers (GLsizei n, GLuint *buffers);
> GL_API void GL_APIENTRY glGenTextures (GLsizei n, GLuint *textures);
> GL_API GLenum GL_APIENTRY glGetError (void);
> GL_API void GL_APIENTRY glGetFixedv (GLenum pname, GLfixed *params);
> GL_API void GL_APIENTRY glGetIntegerv (GLenum pname, GLint *params);
> GL_API void GL_APIENTRY glGetLightxv (GLenum light, GLenum pname, GLfixed *params);
> GL_API void GL_APIENTRY glGetMaterialxv (GLenum face, GLenum pname, GLfixed *params);
> GL_API void GL_APIENTRY glGetPointerv (GLenum pname, GLvoid **params);
> GL_API const GLubyte * GL_APIENTRY glGetString (GLenum name);
> GL_API void GL_APIENTRY glGetTexEnviv (GLenum env, GLenum pname, GLint *params);
> GL_API void GL_APIENTRY glGetTexEnvxv (GLenum env, GLenum pname, GLfixed *params);
> GL_API void GL_APIENTRY glGetTexParameteriv (GLenum target, GLenum pname, GLint *params);
> GL_API void GL_APIENTRY glGetTexParameterxv (GLenum target, GLenum pname, GLfixed *params);
> GL_API void GL_APIENTRY glHint (GLenum target, GLenum mode);
> GL_API GLboolean GL_APIENTRY glIsBuffer (GLuint buffer);
> GL_API GLboolean GL_APIENTRY glIsEnabled (GLenum cap);
> GL_API GLboolean GL_APIENTRY glIsTexture (GLuint texture);
> GL_API void GL_APIENTRY glLightModelx (GLenum pname, GLfixed param);
> GL_API void GL_APIENTRY glLightModelxv (GLenum pname, const GLfixed *params);

That's the same spread of lines as the embed preview on your link. Again, I don't understand what I'm supposed to be looking for. There's nothing standing out and i fear I may be a bit out of my depth because it's not obvious nor intuitive for me. 

So sorry if the answer is right in front of me, I'm just a little bit blind in experience

-------------------------

weitjong | 2017-12-08 01:54:37 UTC | #21

We prepare sysroot for each target platform needed by our CI cross-compiling build in the GitHub repositories. Don’t worry too much about it if you don’t understand it (for now). I only mentioned it so you can have something to compare with.

[quote="booneruni, post:20, topic:3822"]
linaro@linaro-alip:~$ sudo find / -name “gl.h”

/usr/include/GL/gl.h

/usr/include/GLES/gl.h
[/quote]

First of all, `sudo` is not a “cure all” command. You should only use it sparingly when it is absolutely necessary. You don’t need it in the above command, if you limit the search to “/usr/include”. Also, you should not search the root in the manner you have done because the search would not only include virtual files in the /proc but also may span to multiple disks even networked one if they are mounted to your filesystem at the time.

Finally, I think the problem may be the “/usr/include/GL/GL.h”. It should not be there and the compiler may use that file instead of the one in the GLES subdir. Try to remove the offending file and see if you make any progress. If it does then try to remove the wrong package which has caused that offending header to be installed in the first place. That should clean up everything automatically for you.

HTH

-------------------------

booneruni | 2017-12-08 02:14:15 UTC | #22

I deleted that file, i'm going to `make clean` and then `make` to see if that does the trick.


It didn't do the trick.. It failed at 11% now instead of its highest of 58%

[ 11%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11clipboard.c.o
In file included from /home/linaro/dev/urho/Urho3D/Source/ThirdParty/SDL/src/video/x11/SDL_x11opengl.h:28:0,
                 from /home/linaro/dev/urho/Urho3D/Source/ThirdParty/SDL/src/video/x11/SDL_x11video.h:69,
                 from /home/linaro/dev/urho/Urho3D/Source/ThirdParty/SDL/src/video/x11/SDL_x11clipboard.c:28:
/usr/include/GL/glx.h:32:19: fatal error: GL/gl.h: No such file or directory
 #include <GL/gl.h>
                   ^
compilation terminated.
Source/ThirdParty/SDL/CMakeFiles/SDL.dir/build.make:2150: recipe for target 'Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11clipboard.c.o' failed
make[2]: *** [Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/x11/SDL_x11clipboard.c.o] Error 1
CMakeFiles/Makefile2:447: recipe for target 'Source/ThirdParty/SDL/CMakeFiles/SDL.dir/all' failed
make[1]: *** [Source/ThirdParty/SDL/CMakeFiles/SDL.dir/all] Error 2
Makefile:149: recipe for target 'all' failed
make: *** [all] Error 2


Also about the find command, I didn't know where to look for that file on my system so i just used that to find it. And it screamed at me about permission denied on the first try without it so i sudo'd to get a clean output without an aids as piss stream of permission denied logs. i generally try things without it first.

do you know how i might be able to trace which package installed the /include/GL/ bits, or will i just have to guess?

-------------------------

weitjong | 2017-12-08 02:50:47 UTC | #23

Forgot to mention you have to regenerate the build tree from scratch. Use cmake_arm.sh to generate a fresh one as you have done before. Make sure in the output it only turns on VIDEO_OPENGLES_V1/2 but not VIDEO_OPENGL. If it still does that then you can also manual override to force it to false by passing “-D VIDEO_OPENGL=0” when you call the shell script.

That’s a good sign btw, because your errors now is no longer strange to me.

As for the clean up, read the man pages of apt-cache or something. There should be an option of the command for this sort of things. Google is also your good friend. I hope you don’t mind I only pointing the direction but not the solution. Besides, I also don’t have Debian system in front of me now.

-------------------------

booneruni | 2017-12-08 03:35:48 UTC | #24

[quote="weitjong, post:23, topic:3822"]
./cmake_arm.sh -D VIDEO_OPENGL=0
[/quote]
I ran this and retried compiling and it got to 58% again after much anticipation.

https://pastebin.com/jEwaUCEL

-------------------------

weitjong | 2017-12-08 03:40:16 UTC | #25

But did you regenerate the build tree from scratch as told? Nuke the build tree first, start from a clean sheet.

-------------------------

booneruni | 2017-12-08 03:40:50 UTC | #26

do you mean `make clean` if so yeah i did, if not then i'm not sure what to delete/run

-------------------------

weitjong | 2017-12-08 03:51:27 UTC | #27

No. I meant you have to ‘rm’ the whole build tree. And the whole output from CMake after you call the shell script.

-------------------------

booneruni | 2017-12-08 03:52:27 UTC | #28

Is that the "bin" directory? I'm not exactly sure what to rm

-------------------------

weitjong | 2017-12-08 03:53:17 UTC | #29

The whole directory where you ran the “make” command from all this while.

-------------------------

booneruni | 2017-12-08 03:55:19 UTC | #30

Just to be sure (since I'm on a capped internet connection and redownloading the entire thing if it wasn't needed would be a pain), the entire  directory here?

>linaro@linaro-alip:~/dev/urho/Urho3D$ ls
Android                  cmake_android.bat     cmake_install.cmake
CMake                    cmake_android.sh      cmake_ios.sh
CMakeCache.txt           cmake_arm.sh          cmake_mingw.bat
CMakeFiles               cmake_clean.bat       cmake_mingw.sh
CMakeLists.txt           cmake_clean.sh        cmake_ninja.bat
CPackConfig.cmake        cmake_codeblocks.bat  cmake_ninja.sh
CPackSourceConfig.cmake  cmake_codeblocks.sh   cmake_rpi.sh
Docs                     cmake_codelite.bat    cmake_tvos.sh
LICENSE                  cmake_codelite.sh     cmake_vs2015.bat
Makefile                 cmake_eclipse.sh      cmake_vs2017.bat
README.md                cmake_emscripten.bat  cmake_xcode.sh
Rakefile                 cmake_emscripten.sh   include
Source                   cmake_generic.bat     lib
SourceAssets             cmake_generic.sh
?

-------------------------

weitjong | 2017-12-08 04:22:51 UTC | #31

It seems your build tree is non out-of-source. If so, then you can’t easily do what I told you to do. You may able to just call cmake_clean.sh first before cmake_arm.sh, but I cannot guarantee you how clean that would get you.

P.s. In future, remember to use out-of-source build tree.

-------------------------

booneruni | 2017-12-08 17:48:16 UTC | #32

After some back and forth with someone on IRC we've gotten it to ~90% and this last one gets to some of the samples, it looks like

https://pastebin.com/QXrPuX02 89% --most recent

https://pastebin.com/7DcQ8gCa 91%

making it with this "make -j 4 VERBOSE=1"

and doing the cmake stuff with 
"
./cmake_arm.sh build -D VIDEO_OPENGL=0 -D CMAKE_CXX_FLAGS="-E -g3" -D URHO3D_WEBP=0 -D URHO3D_TOOLS=0
"

-------------------------

booneruni | 2017-12-08 21:33:07 UTC | #33

Okay i've gotten some more information; I'm starting by wiping the build tree using `rm build -r ` and then doing the following 

`./cmake_arm.sh build -D VIDEO_OPENGL=0 -D URHO3D_LIB_TYPE=SHARED -D CMAKE_BUILD_TYPE=Debug -D URHO3D_PCH=0 /usr/include/GLES/ -D CMAKE_CXX_FLAGS="-E -g3"`

gets me this output https://hastebin.com/titehorumi.sql

and then

`cd build && make -j 4 -k VERBOSE=1`

gets me this;

https://cdn.discordapp.com/attachments/308880718044463105/388805054330830849/out.txt

sorry for the awkward link, it hit the limit of every paste site i tried.

-------------------------

weitjong | 2017-12-09 02:27:48 UTC | #34

I spotted a few errors in parameters you pass to CMake as well errors in the CMake output. I don't think the "-E" compiler flag should be used at all here because it simply tells GCC to do nothing except preprocessing the compilation unit. While on the other hand, "-g3" would instruct it to produce the object file with most verbose debugging information. That's also not what you actually need at this juncture. Also that you have pass the option to use Debug build config which in turn will emit "-g" flags. Depending on the order of the flags, the last one win out. I suggest you to not passing flags externally unless you are sure what you are doing. 

I would also leave URHO3D_PCH to its default ON state for any GCC-derivative compiler toolchain. It is a good thing to have (speeding up subsequent build time). Btw, setting up "ccache" (see the online doc) will give an even massive reduction on build time. That is exactly what you need building on an ARM board directly.

The reference to a GLES header path in the parameter actually does nothing also, IMHO. And finally I believe the "-DVIDEO_OPENGL=0" is the only one makes the difference here. For the benefit of other readers, that option is only needed because OP has wrongly installed a dev package in his system. This manual override is a temporary measure until that offending package has been removed. Normally our build system should automatically configure this option to OFF when targeting generic ARM platform.

-------------------------

booneruni | 2017-12-09 02:27:47 UTC | #35

Okay so now i will run `./cmake_arm.sh build -D VIDEO_OPENGL=0 -D URHO3D` since the rest doesn't seem to do much
It gave this output
https://hastebin.com/ificijojoz.sql

and then I got this output https://cdn.discordapp.com/attachments/308880718044463105/388878957514194944/out.txt

from `make -j 4 -k VERBOSE=1`

-------------------------

weitjong | 2017-12-09 02:51:04 UTC | #36

Back to square one. It will be easier for me if I have the board myself and be able to probe it directly. Anyway, can you show the output of this command:

    echo |cc -E -dM - |grep -E '__arm__|__aarch64__'

-------------------------

booneruni | 2017-12-09 02:59:58 UTC | #37

 ` #define __arm__ 1`

-------------------------

weitjong | 2017-12-09 03:46:17 UTC | #38

Good. Then based on the code in this line below then the compiler should use the "GLES2/gl2.h" header file (only today I am responding to you with my primay system in front of me).

https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/OpenGL/OGLGraphicsImpl.h#L36

In Urho prepared sysroot for our CI build, we have something like this.

https://github.com/urho3d/armhf-sysroot/blob/master/usr/include/GLES2/gl2.h#L448

So, do the same comparison as you have done before in your system root to see whether the content of your "/usr/include/GLES2/gl2.h" looks any fishy or not.

-------------------------

booneruni | 2017-12-09 03:55:49 UTC | #39

I only have /inlcude/GLES/, not GLES2. and i don't have gl2.h, just gl.h and some others.

But on line 683 of /usr/include/GLES/gl.h I have `GL_API const GLubyte * GL_APIENTRY glGetString (GLenum name);`

This is the first I'm seeing of GLES2, so this looks promising

-------------------------

booneruni | 2017-12-09 05:14:08 UTC | #40

Okay I just put a whole lot of stuff (including GLES2) into my includes and I'm getting this output at the end of the make https://hastebin.com/ijemuzilid.js

-------------------------

weitjong | 2017-12-09 05:45:47 UTC | #41

May I ask how did you "put a whole lot of stuff"? You should have hunted down the right dev package in your package repository. After installing it, it should then not just only providing you the development headers but also the the development library to link against too. If you just "tinker" your root file system then you might just cause irreparable damage to it. However, it explains a lot the strangeness I see so far :smile:  .

-------------------------

booneruni | 2017-12-09 05:50:51 UTC | #42

This is the first haphazard tinkering i've done relax.. Nothing is either clear or working so far so I'm trying things in leu of many other options. I moved things over from the armhf-sysroot-master repo after conference with someone on the irc trying to figure this out

It shouldn't explain anything because the only fiddling i've done so far was at your request (deleting another gl.h)

-------------------------

jmiller | 2017-12-09 06:13:23 UTC | #43

..and a good bit of that on my advice when I missed some things. :coffee::coffee::coffee::coffee:

-------------------------

weitjong | 2017-12-09 06:40:47 UTC | #44

I just quickly did an ARM build from scratch using the build environment I already setup (cross-compiler is also a Linaro one like yours, with ccache to speed boost, etc). And it went through uneventfully. 

    $ time (rm -rf ../arm-Build && rake cmake arm && rake make arm)
```
 real	0m36.871s
 user	1m34.970s
 sys	0m25.248s
```

It was fast not because of my host system but more thanks to ccache. So, there you have it. It proves there is nothing wrong with our code base or the buildsystem. Since the start I said the problem is with your setup does not have all the prerequisite dev packages installed. Unfortunately though I cannot give you the exact list of the packages as I have not used Tinkerboard before and I have no idea what its package repository is based from. If your claim is correct that it is based on Debian then you might try this list:

```
$ sudo apt-get install libgles{1,2}-mesa-dev libx11-dev libxcursor-dev libxext-dev libxi-dev libxinerama-dev libxrandr-dev libxrender-dev libxss-dev libxxf86vm-dev libasound2-dev libpulse-dev libdbus-1-dev libreadline6-dev libudev-dev
```

I am not responsible if it does more harm than good. I am just taking a shot in the dark here.

-------------------------

