Kanfor | 2017-01-02 01:09:30 UTC | #1

Hi everyone.
I'm new in Linux but i need implement Urho3D. I would like make a new empty project and compile it whit Codeblocks or other IDE.
I can make only the samples :frowning:

How can I make an empty project in a very easy way?

I'm not expert in Cmake.
Thanks you a lot! :wink:

-------------------------

valera_rozuvan | 2017-01-02 01:09:30 UTC | #2

Hi! Check out my sample project at [github.com/valera-rozuvan/urho3 ... s-in-shade](https://github.com/valera-rozuvan/urho3d-demos/tree/master/rotating-cubes-in-shade) . It includes just one *.cpp file and a Makefile. You can use it with any IDE. If you have any further questions, don't hesitate to ask = )

Also, check out this topic: [topic1748.html](http://discourse.urho3d.io/t/my-urho3d-demos/1683/1) .

-------------------------

Kanfor | 2017-01-02 01:09:30 UTC | #3

:astonished:  OOHHH!!!

This exactly I need  :stuck_out_tongue:

Thank you very much!
---------------------------------
 :neutral_face:  Not work.

How can I import the project in a IDE?
Codeblocks can't find the libraries like #include <Urho3D/Core/CoreEvents.h>

-------------------------

Kanfor | 2017-01-02 01:09:30 UTC | #4

Hi again.

I think the problem is in the makefile.

URHO3D_INCLUDE_DIR=$(URHO_DIR)/build/include

I don't have /build/include folder in my Urho3D-1.5 folder.

I think is necessary make other action before, like build the library, am i right?

-------------------------

valera_rozuvan | 2017-01-02 01:09:31 UTC | #5

[quote="Kanfor"]I think is necessary make other action before, like build the library, am i right?[/quote]

I have updated the Makefile, and added instructions. Please check again [github.com/valera-rozuvan/urho3 ... s-in-shade](https://github.com/valera-rozuvan/urho3d-demos/tree/master/rotating-cubes-in-shade) .

-------------------------

Kanfor | 2017-01-02 01:09:31 UTC | #6

Great!
 :smiley: 

Thanks again!  :wink:

------------------------

Now I don't have error. I made the libraries (I think) and now they are in the PATH of Linux.

The problem now is when I BUILD the project.

In file included from /usr/local/include/Urho3D/Input/Input.h:29:0,
                 from sampleApp.cpp:4:
/usr/local/include/Urho3D/Input/InputEvents.h:27:30: fatal error: SDL/SDL_joystick.h: not exist

-------------------------

valera_rozuvan | 2017-01-02 01:09:31 UTC | #7

It might be because you don't have several necessary SDL packages installed on your system. Try installing:

[ul]
[li]libsdl-image1.2[/li]
[li]libsdl1.2debian[/li]
[li]libsdl2-2.0-0[/li]
[li]libsdl2-dev[/li][/ul]

What Linux distribution are you using, [b]Kanfor[/b]?

-------------------------

valera_rozuvan | 2017-01-02 01:09:31 UTC | #8

Also, [b]Kanfor[/b], please read carefully the page [urho3d.github.io/documentation/1 ... lding.html](http://urho3d.github.io/documentation/1.5/_building.html) . It describes in detail the prerequisites (what libraries must be installed on your system) for building Urho3D.

-------------------------

weitjong | 2017-01-02 01:09:31 UTC | #9

[quote="valera_rozuvan"]It might be because you don't have several necessary SDL packages installed on your system. Try installing:

[ul]
[li]libsdl-image1.2[/li]
[li]libsdl1.2debian[/li]
[li]libsdl2-2.0-0[/li]
[li]libsdl2-dev[/li][/ul]

What Linux distribution are you using, [b]Kanfor[/b]?[/quote]

Urho3D project does not depend on SDL packages because it has included SDL source files as one of its internal 3rd-party libraries. All the SDL symbols can be found in both the Urho3D static library and Urho3D shared library, so downstream projects simply just need to "link" against the Urho3D library. For using Urho3D v1.5 as external library in your project, reference this documentation page instead. [urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html). There are subtle changes in between them already.

-------------------------

valera_rozuvan | 2017-01-02 01:09:31 UTC | #10

Anyways, my proposed sample project can be built using the instructions I provided. Please see a screencast I made that demonstrates this:

[video]https://www.youtube.com/watch?v=cBhw8qL840o[/video]

-------------------------

Kanfor | 2017-01-02 01:09:31 UTC | #11

WOW!  :astonished: 
Thanks for your time.

The game compile perfectly, but when I start with /sampleApp I have this error:

[color=#FF0000]error while loading shared libraries: libUrho3D.so.0: cannot open shared object file: No such file or directory[/color]

 :unamused: 

I did everything as shown in the video.

-------------------------------

NOW WORKS!!!!!!!

You must add this in command line:

export LD_LIBRARY_PATH=<your folder of Urho3D>/build/lib:$LD_LIBRARY_PATH

-------------------------

valera_rozuvan | 2017-01-02 01:09:32 UTC | #12

You have to make sure that the [b]*.so[/b] file is discoverable. First, check that in the folder [b]~/projects/Urho3D-1.5/build/lib[/b] you have:

[code]valera@valera-HP-ENVY-17-Notebook-PC:~/projects/Urho3D-1.5/build/lib$ ls -a -h -l 
total 22M
drwxrwxr-x 2 valera valera   24 Jan 21 09:15 .
drwxrwxr-x 8 valera valera 4.0K Jan 21 09:11 ..
lrwxrwxrwx 1 valera valera   14 Jan 21 09:15 libUrho3D.so -> libUrho3D.so.0
lrwxrwxrwx 1 valera valera   20 Jan 21 09:15 libUrho3D.so.0 -> libUrho3D.so.0.0.171
-rwxrwxr-x 1 valera valera  22M Jan 21 09:15 libUrho3D.so.0.0.171[/code]

Then create the file [b]/etc/ld.so.conf.d/urho3d.conf[/b], and add the following line to it:

[code]/home/valera/projects/Urho3D-1.5/build/lib[/code]

Then run the command:

[code]sudo ldconfig[/code]

Of course, modify the paths according to your setup.

PS: In the video I also do these steps. Maybe you didn't notice them?

-------------------------

Kanfor | 2017-01-02 01:09:32 UTC | #13

Thank you very much!

 :smiley: 
[b][color=#00BF80]All works right now![/color][/b]

By the way. If you use Netbeans, if you have an error when tun the project, you must add the lib
in [color=#0000FF]propierties/Run/Environment[/color]

There add:
Like name: LD_LIBRARY_PATH
Like value: $LD_LIBRARY_PATH:<your Urho3D folder>/build/lib

 :wink:

-------------------------

weitjong | 2017-01-02 01:09:32 UTC | #14

When linking with Urho3D as shared library, you have to pass the linker flags to set up the "rpath" correctly. Something like this: -Wl,-rpath,/home/weitjong/ClionProjects/urho3d/native-Build/lib:::
Adjust the path accordingly naturally. When done properly then the binary should be able to find the lib without using the LD_LIBRARY_PATH or messing the global ldconfig. If you plan to install the Urho3D library (and your binary) to another location after building it then you need to readjust the rpath entries once again. Below is the ldd output of the sample binary which I built in one place and then move it to /tmp, see that it still able to find the libUrho3D.so.0 correctly despite of that and of course I can also run the binary in /tmp just fine (with -pp for setting the resource prefix path).

[code][weitjong@igloo tmp]$ ldd 01_HelloWorld 
	linux-vdso.so.1 (0x00007ffc351c0000)
	libUrho3D.so.0 => /home/weitjong/ClionProjects/urho3d/native-Build/lib/libUrho3D.so.0 (0x00007f41dfb1b000)
	libdl.so.2 => /lib64/libdl.so.2 (0x00007f41df8e4000)
	librt.so.1 => /lib64/librt.so.1 (0x00007f41df6dc000)
	libGL.so.1 => /usr/lib64/nvidia/libGL.so.1 (0x00007f41df3a8000)
	libm.so.6 => /lib64/libm.so.6 (0x00007f41df0a5000)
	libstdc++.so.6 => /lib64/libstdc++.so.6 (0x00007f41ded23000)
	libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007f41deb0c000)
	libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f41de8ee000)
	libc.so.6 => /lib64/libc.so.6 (0x00007f41de52d000)
	/lib64/ld-linux-x86-64.so.2 (0x0000558951546000)
	libnvidia-tls.so.358.16 => /usr/lib64/nvidia/tls/libnvidia-tls.so.358.16 (0x00007f41de329000)
	libnvidia-glcore.so.358.16 => /usr/lib64/nvidia/libnvidia-glcore.so.358.16 (0x00007f41dc6c7000)
	libX11.so.6 => /lib64/libX11.so.6 (0x00007f41dc387000)
	libXext.so.6 => /lib64/libXext.so.6 (0x00007f41dc175000)
	libxcb.so.1 => /lib64/libxcb.so.1 (0x00007f41dbf52000)
	libXau.so.6 => /lib64/libXau.so.6 (0x00007f41dbd4e000)[/code]

-------------------------

Kanfor | 2017-01-02 01:09:32 UTC | #15

Hi, Weitjong.

What I must add in makefile to not need LD_LIBRARY_PATH?

Thanks!

-------------------------

weitjong | 2017-01-02 01:09:32 UTC | #16

I have already mentioned how to do that in my previous comment. Use the "rpath" linker flag.

-------------------------

