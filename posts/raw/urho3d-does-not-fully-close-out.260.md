vivienneanthony | 2017-01-02 00:59:12 UTC | #1

Hi,

I downloaded the latest tar file and compiled it. It compiled 100% and installed. A manner .Urho3D directory update and now the editor loads correctly.

The version I downloaded was urho3d-Urho3D-c4b337d

The problem I have with is closing. You can see it in the videos I'm making.  If I run the editor.sh program from the command line Urho3D does not fully exit out. I have to type ctrl-c to exit back to the command line. Is anyone having the same problem? You will see the problem at the end of the video.

Vivienne


Video #2
 [video]http://youtu.be/DLZY1w4Us9s[/video]

-------------------------

friesencr | 2017-01-02 00:59:12 UTC | #2

Looks like you are using a terminal emulator.  Try using the terminal that ships with the os.  That is just my guess.

Also you can collapse every node by checking the all checkbox and clicking collapse.

Also, also I will add a node search after get done with my resource browser after i get done with work crap :slight_smile:

-------------------------

weitjong | 2017-01-02 00:59:12 UTC | #3

In my opinion this should not be caused by the terminal emulator. I use one myself and I don't have this closing issue. Urho applications can be launched from an interactive shell in any type of terminal or even from a debugger within any IDE, the app would not know the difference. 

There could be a bug in the Editor. When closing, it attempts to re-create the configuration directory before saving the editor configuration settings. Under normal circumstances, this approach works for initial run as well as subsequent runs. However, I suspect the function responsible for creating the directory trips over in your case. I notice your homedir is now mounted from a different filesystem. I believe that could be the reason why it fails.

-------------------------

vivienneanthony | 2017-01-02 00:59:13 UTC | #4

[quote="weitjong"]In my opinion this should not be caused by the terminal emulator. I use one myself and I don't have this closing issue. Urho applications can be launched from an interactive shell in any type of terminal or even from a debugger within any IDE, the app would not know the difference. 

There could be a bug in the Editor. When closing, it attempts to re-create the configuration directory before saving the editor configuration settings. Under normal circumstances, this approach works for initial run as well as subsequent runs. However, I suspect the function responsible for creating the directory trips over in your case. I notice your homedir is now mounted from a different filesystem. I believe that could be the reason why it fails.[/quote]


I tried chmod 755 and change ownership vivienne:viveienne in the .Urho3D directory includingrecurvsive folders. The home folder is in the same mounted filesystem as /usr/local/share/Urho3D. I tried Xterm and also Konsole with the same response. I also viewed the .log to see if any exiting logs is done. 

Still the same problem. I'm assuming the exit code is tripping over itself like you mentioned.  I'm assuming if it is trying to recreate both the folder and file again. It's getting stuck specifically on Ubuntu instead of checking if the folder and file already exist. I have not seen the code but that's my only guess. 

Urho3d Bin Folder with the new files
[quote]
vivienne@vivienne-System-Product-Name:/usr/local/share/Urho3D$ cd Bin
vivienne@vivienne-System-Product-Name:/usr/local/share/Urho3D/Bin$ ls -l
-rwxr-xr-x  1 root root 16149906 May 15 11:07 AssetImporter
drwxr-xr-x  7 root root     4096 May 15 11:12 CoreData
drwxr-xr-x 16 root root     4096 May 15 11:12 Data
-rwxr-xr-x  1 root root      140 May 15 10:07 Editor.sh
-rwxr-xr-x  1 root root      698 May 15 10:07 NinjaSnowWar.sh
-rwxr-xr-x  1 root root  1650719 May 15 11:07 OgreImporter
-rwxr-xr-x  1 root root   581233 May 15 11:07 PackageTool
-rwxr-xr-x  1 root root   230116 May 15 11:07 RampGenerator
-rwxr-xr-x  1 root root 15889153 May 15 11:07 ScriptCompiler
-rwxr-xr-x  1 root root      473 May 15 10:07 UpdateDocument.sh
-rwxr-xr-x  1 root root 15905847 May 15 11:04 Urho3DPlayer

vivienne@vivienne-System-Product-Name:~$ ls -al .Urho3D
total 36
drwxr-xr-x   3 vivienne vivienne  4096 May 15 11:24 .
drwxr-xr-x 134 vivienne vivienne 20480 May 15 11:21 ..
drwxr-xr-x   2 vivienne vivienne  4096 May 18 09:37 Editor
-rwxr-xr-x   1 vivienne vivienne   908 May 18 09:41 Urho3D.log
vivienne@vivienne-System-Product-Name:~$ 

[/quote]

-------------------------

vivienneanthony | 2017-01-02 00:59:13 UTC | #5

[quote="friesencr"]Looks like you are using a terminal emulator.  Try using the terminal that ships with the os.  That is just my guess.

Also you can collapse every node by checking the all checkbox and clicking collapse. 

Also, also I will add a node search after get done with my resource browser after i get done with work crap :slight_smile:[/quote]

Cool!

Point A - Tried. Still same problem using Xterm and Konsole

Point B - Got that.

Point C - Cool. If I have any ideas of the Editor UI. I'll mention it. The only thing I can think of is making the windows and menu bar a different color background instead of black with some opacity to it.  Still the search or highlight by keyword would be a nice Editor update in the hierarchy list.

Thanks.

-------------------------

weitjong | 2017-01-02 00:59:13 UTC | #6

Can you post the output of these commands:

[code]$ df -h /home/vivienne
$ df -h /media/home2/vivienne
$ lsblk
[/code]

If you think this is irrelevant then just ignore me.

-------------------------

vivienneanthony | 2017-01-02 00:59:13 UTC | #7

[quote="weitjong"]Can you post the output of these commands:

[code]$ df -h /home/vivienne
$ df -h /media/home2/vivienne
$ lsblk
[/code]

If you think this is irrelevant then just ignore me.[/quote]

Here is the output.

[quote]vivienne@vivienne-System-Product-Name:/media/home2/vivienne/programs/blender/blends/existence$ df -h /home/vivienne
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdb1        55G   39G   14G  75% /
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/programs/blender/blends/existence$ df -h /media/home2/vivienne
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       985G  235G  701G  26% /media/home2
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/programs/blender/blends/existence$ lsblkNAME   MAJ:MIN RM    SIZE RO TYPE MOUNTPOINT
sda      8:0    0    1.4T  0 disk 
??sda1   8:1    0 1000.5G  0 part /media/home2
sdb      8:16   0   59.6G  0 disk 
??sdb1   8:17   0   55.7G  0 part /
??sdb2   8:18   0      1K  0 part 
??sdb5   8:21   0    3.9G  0 part [SWAP]
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/programs/blender/blends/existence$ 
[/quote]

It's definitely not space.

-------------------------

weitjong | 2017-01-02 00:59:13 UTC | #8

Which of the two is your homedir?

[code]$ echo $HOME[/code]
And which of the two has the .Urho3D directory created?

-------------------------

vivienneanthony | 2017-01-02 00:59:13 UTC | #9

[quote="weitjong"]Which of the two is your homedir?

[code]$ echo $HOME[/code]
And which of the two has the .Urho3D directory created?[/quote]

[quote]vivienne@vivienne-System-Product-Name:~$ echo $HOME
/home/vivienne
vivienne@vivienne-System-Product-Name:~$ 
[/quote]

-------------------------

weitjong | 2017-01-02 00:59:13 UTC | #10

Since you did not answer the second question, I assume the answer is the same as the first. In which case, it is a dead end for me. I am still curios though, why your shell prompt sometimes show you are in /home and on the other times you are in /media/home2? That's what mislead me as if you are dealing with two filesystems here. Or you have actually two user accounts which go to these two places? Anyway, I have tried to help. May be others could help to continue from here. 

As a last resort, perhaps you could try to delete the .Urho3D directory and let it to be recreated again. It's a long but desperate shot  :smiley: .

-------------------------

vivienneanthony | 2017-01-02 00:59:14 UTC | #11

[quote="weitjong"]Since you did not answer the second question, I assume the answer is the same as the first. In which case, it is a dead end for me. I am still curios though, why your shell prompt sometimes show you are in /home and on the other times you are in /media/home2? That's what mislead me as if you are dealing with two filesystems here. Or you have actually two user accounts which go to these two places? Anyway, I have tried to help. May be others could help to continue from here. 

As a last resort, perhaps you could try to delete the .Urho3D directory and let it to be recreated again. It's a long but desperate shot  :smiley: .[/quote]

The home folder is the default folde /home/vivienne.

I have a separate drive with a home partition whish is /media/home2/viviennee. It's just the name of it. The actual home is /home/vivienne where the .Urho3D is created.

I have tons of data and programs on /media/home2/viviennee which I run constantly including builds. From compiled libraries, executables, and also wine/x86 based software that creates a .folder in /home/vivienne. I really don't think it's the computer or Ubuntu but the process closing out Urho3D.

-------------------------

weitjong | 2017-01-02 00:59:15 UTC | #12

[quote="vivienneanthony"]I really don't think it's the computer or Ubuntu but the process closing out Urho3D.[/quote]

Yes, I have suspected that much since the beginning that there could be a bug in the Editor. But we need to know exactly what is the root cause of your issue before we can fix it. As you already aware, others don't have this particular issue.

-------------------------

vivienneanthony | 2017-01-02 00:59:17 UTC | #13

[quote="weitjong"][quote="vivienneanthony"]I really don't think it's the computer or Ubuntu but the process closing out Urho3D.[/quote]

Yes, I have suspected that much since the beginning that there could be a bug in the Editor. But we need to know exactly what is the root cause of your issue before we can fix it. As you already aware, others don't have this particular issue.[/quote]

If you need any other console output, I'll be happy to make it.  Since it's a weird bug on specific computers I am guessing.

-------------------------

weitjong | 2017-01-02 00:59:19 UTC | #14

I think I have fixed the problem. Please kindly use the latest revision in the master branch to test.

-------------------------

vivienneanthony | 2017-01-02 00:59:19 UTC | #15

[quote="weitjong"]I think I have fixed the problem. Please kindly use the latest revision in the master branch to test.[/quote]

I'll test it out. No luck.

-------------------------

vivienneanthony | 2017-01-02 00:59:19 UTC | #16

[quote="weitjong"]I think I have fixed the problem. Please kindly use the latest revision in the master branch to test.[/quote]

I'm not sure if this means anything. When compiling the samples I noticed.

[quote]
[ 60%] Building CXX object Engine/CMakeFiles/Urho3D.dir/IO/File.cpp.o                               
/media/home2/vivienne/Urho3D-master/Source/Engine/IO/File.cpp: In member function ?virtual unsigned int Urho3D::File::Read(void*, unsigned int)?:
/media/home2/vivienne/Urho3D-master/Source/Engine/IO/File.cpp:298:84: warning: ignoring return value of ?size_t fread(void*, size_t, size_t, FILE*)?, declared with attribute warn_unused_result [-Wunused-result]
/media/home2/vivienne/Urho3D-master/Source/Engine/IO/File.cpp:311:73: warning: ignoring return value of ?size_t fread(void*, size_t, size_t, FILE*)?, declared with attribute warn_unused_result [-Wunused-result]
[ 60%] Building CXX object Engine/CMakeFiles/Urho3D.dir/IO/FileSystem.cpp.o
/media/home2/vivienne/Urho3D-master/Source/Engine/IO/FileSystem.cpp: In member function ?Urho3D::String Urho3D::FileSystem::GetProgramDir() const?:
/media/home2/vivienne/Urho3D-master/Source/Engine/IO/FileSystem.cpp:663:48: warning: ignoring return value of ?ssize_t readlink(const char*, char*, size_t)?, declared with attribute warn_unused_result [-Wunused-result]
/media/home2/vivienne/Urho3D-master/Source/Engine/IO/FileSystem.cpp: In member function ?Urho3D::String Urho3D::FileSystem::GetCurrentDir() const?:
/media/home2/vivienne/Urho3D-master/Source/Engine/IO/FileSystem.cpp:502:27: warning: ignoring return value of ?char* getcwd(char*, size_t)?, declared with attribute warn_unused_result [-Wunused-result]
[/quote]

-------------------------

weitjong | 2017-01-02 00:59:19 UTC | #17

I was *finally* able to reproduce the closing issue on my Fedora system with the previous revision. After the fix, it works now on my system. So, I thought it should fix yours as well. Just to be sure, I am referring to the fix committed in revision [github.com/urho3d/Urho3D/commit ... e9e3572597](https://github.com/urho3d/Urho3D/commit/96295b4923f48aed21cce07f8cd5c1e9e3572597).

The build warnings seem normal to me.

-------------------------

vivienneanthony | 2017-01-02 00:59:20 UTC | #18

[quote="weitjong"]I was *finally* able to reproduce the closing issue on my Fedora system with the previous revision. After the fix, it works now on my system. So, I thought it should fix yours as well. Just to be sure, I am referring to fix committed in revision [github.com/urho3d/Urho3D/commit ... e9e3572597](https://github.com/urho3d/Urho3D/commit/96295b4923f48aed21cce07f8cd5c1e9e3572597).

The build warnings seem normal to me.[/quote]

It didn't so I leave it as a looming Ubuntu/Debian bug. I will focus on actually coding a app with a start screen.

-------------------------

rasteron | 2017-01-02 00:59:20 UTC | #19

Hi guys, just to help out: I'm also using a Linux VM and a clean system as well and I don't have any closing out problems (terminal and windowed) with the version prior to the latest build. Vivienne, my guess is it might have something to do with your scene, graphic driver or how you have setup/build Urho3D.

Anyways, as you said you don't really need to worry about it for now as this is really a small thing. :slight_smile:

cheers.

-------------------------

vivienneanthony | 2017-01-02 00:59:20 UTC | #20

[quote="rasteron"]Hi guys, just to help out: I'm also using a Linux VM and a clean system as well and I don't have any closing out problems (terminal and windowed) with the version prior to the latest build. Vivienne, my guess is it might have something to do with your scene, graphic driver or how you have setup/build Urho3D.

Anyways, as you said you don't really need to worry about it for now as this is really a small thing. :slight_smile:

cheers.[/quote]

I'm not sure. I completely did it the normal way. The samples work so I'm not certain if it's that. It occurs even if it's a new scene with nothing in it and pretty much the driver is used for Blender and online gaming. I'm assuming its something with the save configuration. That's all I know.

-------------------------

weitjong | 2017-01-02 00:59:20 UTC | #21

I manage to figure out how to reproduce the issue after I followed almost exactly what OP has done. Install Urho3D to a local filesystem as root. As such all the executables are now owned by root but with execute permission for others. OP then invokes the executable in the /usr/local/share/Urho3D/Bin as a normal user. For me, I could only reproduce the closing issue when this is done when the current working directory is not writeable by user. If I invoke in my homedir then no issue. The revision prior to the fix attempts to create a log file in current working directory which fails in the former case. After the fix, all the executables shipped by Urho3D project creates log file in ~/.local/share/urho3d/logs (in Linux platform) regardless of current working directory. Other platforms get their different preferences path assigned by SDL. Previously I was also troubled by having the logs scattering all over the place, so this fix also scratches my own itch.

I agree that we should move on. I just hope that we will not hear a huge sigh or comment from OP regarding this again in his next video blog :slight_smile:.

-------------------------

vivienneanthony | 2017-01-02 00:59:20 UTC | #22

[quote="weitjong"]I manage to figure out how to reproduce the issue after I followed almost exactly what OP has done. Install Urho3D to a local filesystem as root. As such all the executables are now owned by root but with execute permission for others. OP then invokes the executable in the /usr/local/share/Urho3D/Bin as a normal user. For me, I could only reproduce the closing issue when this is done when the current working directory is not writeable by user. If I invoke in my homedir then no issue. The revision prior to the fix attempts to create a log file in current working directory which fails in the former case. After the fix, all the executables shipped by Urho3D project creates log file in ~/.local/share/urho3d/logs (in Linux platform) regardless of current working directory. Other platforms get their different preferences path assigned by SDL. Previously I was also troubled by having the logs scattering all over the place, so this fix also scratches my own itch.

I agree that we should move on. I just hope that we will not hear a huge sigh or comment from OP regarding this again in his next video blog :slight_smile:.[/quote]

Lol. Don't worry. No sighs. It just be a looming issue  that might pop up if another person have the same problem. Until then it's a dead subject. I am glad it did help fix that little nag of having log files all over the place.

I probably sigh because I want to do a almost huge world terrain map seamless using the libnoise library with exportable world terrain. That's a totally different subject.

-------------------------

