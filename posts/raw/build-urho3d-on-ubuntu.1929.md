Sasha7b9o | 2017-01-02 01:11:37 UTC | #1

Hi.
Build Urho3D on Ubuntu, Code::Blocks.
Log:
[code]Linking CXX executable ../../../bin/Urho3DPlayer 
cd /home/sashs7b9/Urho3D/Source/Tools/Urho3DPlayer && /usr/bin/cmake -E cmake_link_script CMakeFiles/Urho3DPlayer.dir/link.txt --verbose=1 
/usr/bin/c++  -Wno-invalid-offsetof -march=native -ffast-math -pthread -g -DDEBUG -D_DEBUG    CMakeFiles/Urho3DPlayer.dir/Urho3DPlayer.cpp.o  -o ../../../bin/Urho3DPlayer -rdynamic ../../../lib/libUrho3D.a -ldl -lm -lGL -ldl -lm -lGL 
/usr/bin/ld: cannot find -lGL 
/usr/bin/ld: cannot find -lGL 
collect2: error: ld returned 1 exit status 
make[2]: *** [bin/Urho3DPlayer] Error 1 
make[1]: *** [Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all] Error 2 
make: *** [all] Error 2 
make[2]: Leaving directory `/home/sashs7b9/Urho3D' 
make[1]: Leaving directory `/home/sashs7b9/Urho3D' 
Process terminated with status 2 (0 minute(s), 7 second(s)) 
2 error(s), 0 warning(s) (0 minute(s), 7 second(s))[/code]

As I understand it, the error in this line from file CMakeFiles/Urho3DPlayer.dir/link.txt --verbose=1 : 
/usr/bin/c++  -Wno-invalid-offsetof -march=native -ffast-math -pthread -g -DDEBUG -D_DEBUG    CMakeFiles/Urho3DPlayer.dir/Urho3DPlayer.cpp.o  -o ../../../bin/Urho3DPlayer -rdynamic ../../../lib/libUrho3D.a -ldl -lm -lGL -ldl -lm -lGL 

Help a newbie in linux.

-------------------------

rasteron | 2017-01-02 01:11:37 UTC | #2

This is an issue that is being asked a lot by Urho3D starters for Linux. I'm assuming you are using 64bit, right? Check my old posts or I'll be back with the link.

Edit: I can only find my old post atm, there's a recent one here asked by another member with an updated solution:
[groups.google.com/forum/#!topic ... NIicGpzHY4](https://groups.google.com/forum/#!topic/urho3d/oNIicGpzHY4)

-------------------------

rku | 2017-01-02 01:11:37 UTC | #3

[code]/usr/bin/ld: cannot find -lGL [/code]
Sounds like development package of libGL is not installed.

-------------------------

weitjong | 2017-01-02 01:11:37 UTC | #4

Yes, it looks like it. Though normally I would not expect that to happen to Ubuntu user because I think Ubuntu will automatically prompt user to install a suitable proprietary graphical driver (kernel module, to be more precise) based on the GPU hardware that it finds. Previously in the "Building prerequisites" for Linux we did mention that Urho3D requires a library implementing the OpenGL API needs to be installed. The text has been removed in the HEAD version because we have now a lot more other information to cover there. The original text was very vague in any case. But I think most users know how to do this without explicitly telling them. It is like asking Windows users (devs) have they install the NVidia/AMD graphic driver for their discrete card.

EDIT: and you should avoid Mesa implementation if possible.
EDIT2: If you need more detail instruction then you need to tell us which GPU do you have.

-------------------------

christianclavet | 2017-01-02 01:11:38 UTC | #5

Hi,
Since you are using Ubuntu try using the command console and input theses and try with CMAKE to see what is missing. You might have to add other libs as you go.

Using this on MINT (a fork of Ubuntu):

[code]sudo apt-get install build-essential
sudo apt-get install libgl
sudo apt-get install libasound2-dev[/code]

As for each of theses lines: (You need the libs for the developer side)
- You need the development header (build-essential)
- You need OpenGL dev lib (libgl1 and libglu1)
- You need a sound dev lib  (libasound2)

Check the output from CMAKE, this is really nice as it will tell you what is missing when it fail to build.
[b]NOTE:[/b] You really [b][u]need to rebuild from sources[/u][/b] using CMAKE. Looking at the output, it look like you took a build somewhere and tryied to compile on your system.
If you havent done a build from source, be sure CMAKE is installed. Then using the command line navigate to the folder of the source then just do a command like this:
[code]cmake_codeblocks ../BUILD[/code]
This will invoke cmake and build from source in a folder named "BUILD" in the parent of the path. Check the messages from CMAKE to see if you got everything. If all work well, then you can take the CMAKE gui and add/change options in want you want to use from URHO, and should be able to compile it.
[b]EDIT: [/b]changed sudo apt- commands to not use the mesa as proposed. APT- should be able to find it.

-------------------------

Sasha7b9o | 2017-01-02 01:11:42 UTC | #6

[b]rasteron[/b], [b]rku[/b], [b]weitjong[/b], [b]christianclavet[/b], thanks for the help.
I put the Ubuntu on a virtual machine. After replacing VMVare on VirtualBox everything everything was decided by itself (or rather, to avoid mistakes during installation).

-------------------------

