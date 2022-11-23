vivienneanthony | 2017-01-02 00:59:08 UTC | #1

Hi

I'm having trouble compling the software. I have Ubuntu 64-bit which does not allow 32-bit and 64-bit OpenGl. Do anyone have any suggestions? It sucks a little I'm a finger tip from completely compiling Urho

Vivienne

[quote][  6%] Built target Box2D
[ 23%] Built target Bullet
[ 23%] Built target Civetweb
[ 24%] Built target Detour
[ 29%] Built target FreeType
[ 29%] Built target JO
[ 32%] Built target kNet
[ 32%] Built target LZ4
[ 32%] Built target PugiXml
[ 34%] Built target Recast
[ 47%] Built target SDL
[ 47%] Built target StanHull
[ 47%] Built target STB
[ 51%] Built target AngelScript
[ 51%] Built target GLEW
[ 52%] Built target LibCpuId
[ 79%] Built target Urho3D
Linking CXX executable /media/home2/vivienne/urho3d-Urho3D-59ef932/Bin/Urho3DPlayer
/usr/bin/ld.bfd.real: cannot find -lGL
collect2: ld returned 1 exit status
make[2]: *** [/media/home2/vivienne/urho3d-Urho3D-59ef932/Bin/Urho3DPlayer] Error 1
make[1]: *** [Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all] Error 2
make: *** [all] Error 2
[/quote]

-------------------------

cadaver | 2017-01-02 00:59:08 UTC | #2

You can enable a 64-bit build by giving the command line parameter -DURHO3D_64BIT=1 to CMake.

-------------------------

vivienneanthony | 2017-01-02 00:59:08 UTC | #3

[quote="cadaver"]You can enable a 64-bit build by giving the command line parameter -DURHO3D_64BIT=1 to CMake.[/quote]

It compiled and I did a make install.

Oddly, to run the editor I have to put. I'm not sure if the permissions are correct for it to get the default installed resources location when starting 

sudo ./Urho3DPlayer Scripts/Editor.as

I ran this in the installed bin folder.

Which is located at /usr/local/share/Urho3D/Bin/Data/.

[quote]
vivienne@vivienne-System-Product-Name:/usr/local/bin$ sudo echo $PATH
/usr/lib/lightdm/lightdm:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games[/quote]

-------------------------

vivienneanthony | 2017-01-02 00:59:08 UTC | #4

I added /usr/local/shared/Urho3D/Bin to the path. 

Any suggestions on what next?

-------------------------

friesencr | 2017-01-02 00:59:08 UTC | #5

I can't speak exactly to the intent of the `make install` method.  I believe this was method of installation to make the *nix toolchain (like autoconf) easier to link/compile to and not to run on its own.  However as soon as your run make the Bin folder will contain all of the executables.  You should  be able to run those executables.

-------------------------

vivienneanthony | 2017-01-02 00:59:08 UTC | #6

[quote="friesencr"]I can't speak exactly to the intent of the `make install` method.  I believe this was method of installation to make the *nix toolchain (like autoconf) easier to link/compile to and not to run on its own.  However as soon as your run make the Bin folder will contain all of the executables.  You should  be able to run those executables.[/quote]

Yea. I got it running. I'm just looking for a good tutorial. I made something in Blender and maybe I can port it to Urho3d.

[youtube.com/watch?v=UWaMXP5 ... 7uTgUBQjaw](https://www.youtube.com/watch?v=UWaMXP5pGak&list=UUTObP1VzcIglm7uTgUBQjaw)

-------------------------

friesencr | 2017-01-02 00:59:08 UTC | #7

I would start by exporting an fbx of your blender scene.  Then in the editor go to the import scene command and select your fbx.  The scene import doesn't really have much in the way of finesse but it should get you going.  The import scene will make separate models/textures for every object in blender.  If you end up using the import scene more you will have to come up with a way of organizing the objects in your blend files that works well for you.

-------------------------

weitjong | 2017-01-02 00:59:08 UTC | #8

[quote="vivienneanthony"]Oddly, to run the editor I have to put. I'm not sure if the permissions are correct for it to get the default installed resources location when starting 

sudo ./Urho3DPlayer Scripts/Editor.as
[/quote]

You should not need to run it using sudo command. In fact, I think it is rather dangerous to do so, considering Urho Editor has an interactive console which could then be used to run any command with root privilege.

Check what is the original Urho3DPlayer file permission and ownership in the Urho3D build tree (URHO3D_PROJECT_ROOT/Bin) and compare that with what has been installed in /usr/local/share/Urho3D/Bin. For my case, I get 775 (owned by me) and 755 (owned by root), respectively. The execute bits are set in either case for "owner", "group", and "others" classes, so it should allow normal user (any user) to execute it.

Check what are your user's and root's umask settings. For my case, they are 0002 and 0022, respectively. Make sure your setting does not mask out the "others" class, like 0007 or something like that. Hope this help.

-------------------------

vivienneanthony | 2017-01-02 00:59:09 UTC | #9

I did a ls -l. This is what I got. I don't think the permissions are correct.

[quote]vivienne@vivienne-System-Product-Name:/usr/local/share/Urho3D$ ls -l
total 20
drwxr-xr-x 5 root root 4096 May 13 13:20 Bin
drwx------ 4 root root 4096 May 13 13:11 CMake
drwxrwxr-x 2 root root 4096 May 13 13:11 Docs
drwxr-xr-x 2 root root 4096 May 13 13:11 Scripts
drwxr-xr-x 3 root root 4096 May 13 13:11 templates
lrwxrwxrwx 1 root root   21 May 13 13:41 Urho3d -> /usr/local/bin/Urho3d
vivienne@vivienne-System-Product-Name:/usr/local/share/Urho3D$ cd Bin
vivienne@vivienne-System-Product-Name:/usr/local/share/Urho3D/Bin$ ls -l
total 49172
-rwxr-xr-x  1 root root 16149654 May 13 13:11 AssetImporter
drwx------  7 root root     4096 May 13 13:21 CoreData
drwx------ 16 root root     4096 May 13 13:21 Data
-rwxr-xr-x  1 root root      140 May  8 04:46 Editor.sh
-rwxr-xr-x  1 root root      698 May  8 04:46 NinjaSnowWar.sh
-rwxr-xr-x  1 root root  1646554 May 13 13:11 OgreImporter
-rwxr-xr-x  1 root root   581233 May 13 13:11 PackageTool
-rwxr-xr-x  1 root root   230116 May 13 13:11 RampGenerator
-rwxr-xr-x  1 root root 15845665 May 13 13:11 ScriptCompiler
drwxr-xr-x  2 root root     4096 May 13 13:18 Scripts
-rwxr-xr-x  1 root root      473 May  8 04:46 UpdateDocument.sh
-rw-r--r--  1 root root      853 May 14 11:39 Urho3D.log
-rwxr-xr-x  1 root root 15862359 May 13 13:11 Urho3DPlayer
vivienne@vivienne-System-Product-Name:/usr/local/share/Urho3D/Bin$ 

vivienne@vivienne-System-Product-Name:/usr/local/share/Urho3D/Bin$ cd Data
bash: cd: Data: Permission denied
[/quote]

-------------------------

weitjong | 2017-01-02 00:59:09 UTC | #10

The file permission for some directories seem wrong. They should not be 700. They are wrong in the installation destination. Have you checked also the file permissions in the project root directory? Also can you post the output of "umask" command as your user account and as root user account.

-------------------------

vivienneanthony | 2017-01-02 00:59:09 UTC | #11

This is what I have so far. I'm not sure how to gett the root umask on ubuntu.
[quote]
[b]vivienne@vivienne-System-Product-Name:/usr/local/share$ umask[/b]
0002
vivienne@vivienne-System-Product-Name:/usr/local/share$

vivienne@vivienne-System-Product-Name:/usr/local/share$ ls -l 
total 56
drwxr-xr-x  2 root root  4096 Apr 25 20:22 applications
drwxrwsr-x  2 root staff 4096 Oct 12  2011 ca-certificates
drwxr-xr-x 10 root root  4096 Feb  7  2013 CEGUI
drwxr-xr-x 11 root root  4096 Aug 12  2013 cegui-0
drwxr-xr-x  2 root root  4096 Feb  7  2013 CELayoutEditor
drwxrwsr-x  3 root staff 4096 Feb 25 13:53 emacs
drwxr-xr-x  3 root root  4096 Feb 26 02:09 ffmpeg
drwxrwsr-x 13 root staff 4096 Feb 28 15:12 fonts
drwxr-xr-x  5 root root  4096 Feb 26 01:41 man
drwxr-xr-x  2 root root  4096 Apr 25 20:22 pixmaps
drwxrwsr-x  7 root staff 4096 Oct 12  2011 sgml
drwxrwsr-x  2 root staff 4096 Aug 11  2013 texmf
drwxr-xr-x  7 root root  4096 May 14 12:17 Urho3D
drwxrwsr-x  6 root staff 4096 Oct 12  2011 xml
vivienne@vivienne-System-Product-Name:/usr/local/share$ ls -l Urho3D
total 20
drwxr-xr-x 5 root root 4096 May 13 13:20 Bin
drwx------ 4 root root 4096 May 13 13:11 CMake
drwxrwxr-x 2 root root 4096 May 13 13:11 Docs
drwxr-xr-x 2 root root 4096 May 13 13:11 Scripts
drwxr-xr-x 3 root root 4096 May 13 13:11 templates[/quote]

Ubuntu Umasking
[askubuntu.com/questions/44542/wh ... es-it-work](http://askubuntu.com/questions/44542/what-is-umask-and-how-does-it-work)

-------------------------

vivienneanthony | 2017-01-02 00:59:09 UTC | #12

[quote="weitjong"]The file permission for some directories seem wrong. They should not be 700. They are wrong in the installation destination. Have you checked also the file permissions in the project root directory? Also can you post the output of "umask" command as your user account and as root user account.[/quote]

So, I did a chmod 755 on the CoreData, Data, and I think Scripts folder. I can it  now from a command line but I get this error when closing

[quote][Wed May 14 23:27:26 2014] ERROR: Failed to create directory /home/vivienne/.Urho3D/Editor/
[Wed May 14 23:27:26 2014] ERROR: Could not open file /home/vivienne/.Urho3D/Editor/Config.xml
[/quote]

-------------------------

weitjong | 2017-01-02 00:59:10 UTC | #13

I think this has becomes off-topic. For your latter problem, check the file permission of the destination directory or the file that gave the error.

-------------------------

weitjong | 2017-01-02 00:59:10 UTC | #14

There is now a new 1.31 source package without the file permission error. I suggest you to download and test this source package. I assume you downloaded the earlier source package from SourceForge because that's the only place where I find to have wrong file permissions. Before re-installing, you may want to first undo the previous installation manually as root user.

-------------------------

vivienneanthony | 2017-01-02 00:59:10 UTC | #15

[quote="weitjong"]There is now a new 1.31 source package without the file permission error. I suggest you to download and test this source package. I assume you downloaded the earlier source package from SourceForge because that's the only place where I find to have wrong file permissions. Before re-installing, you may want to first undo the previous installation manually as root user.[/quote]

The new 1.31 source packaged compiled much better with the better permission. As for the latter problem, I had to manually go back and change  the owner of the .Urho3D folder.

For some reason after closing the editor in the console I have to hit Control-C which I might think it's a bug. It's not fully closing out.

I donwloaded the latest .tar from the main website.

-------------------------

vivienneanthony | 2017-01-02 00:59:12 UTC | #16

[quote="friesencr"]I would start by exporting an fbx of your blender scene.  Then in the editor go to the import scene command and select your fbx.  The scene import doesn't really have much in the way of finesse but it should get you going.  The import scene will make separate models/textures for every object in blender.  If you end up using the import scene more you will have to come up with a way of organizing the objects in your blend files that works well for you.[/quote]

I was  able to convert  the basic building  room, corridors, and junction into a Urho3D scene. I'm not sure how to do the interface part creation in the Editor. It doesn't seem clear to me and I will have to play with the editor even if it's just to a simple screen with a Play and Exit button. I have to figure out creating a environment  like sky and water.

Also, I'm assuming to create a standalone. I have to build a program in C++ basic game code then link it to Urho3D as it being the SDK.

I'm still clueless why I have to now press Ctrl-C to fully close the program in a console.

-------------------------

