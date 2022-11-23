namic | 2017-01-02 01:05:25 UTC | #1

After a long time working on Unity engine and other proprietary software, i decided to dedicate some time to the Urho3D engine and, maybe, migrate some of my projects to it. However, i wasn't able to find any good books, tutorials or documentation on it.

[ul]
[li]Where i can find good learning material? Also, any good samples to work with?[/li]
[li]Is there any modern book on it that you guys recommend?[/li]
[li]Is PBR part of the rendering workflow?[/li]
[li]Are there any examples of multiplayer games, such as an FPS?[/li]
[li]Are there any examples of basic scene editors or terrain editors, so i can start from there? Just something basic: manipulating objects with gizmos and saving that information in the scene. And then loading ingame.[/li][/ul]

-------------------------

Dave82 | 2017-01-02 01:05:25 UTC | #2

[quote="namic"]After a long time working on Unity engine and other proprietary software, i decided to dedicate some time to the Urho3D engine and, maybe, migrate some of my projects to it. However, i wasn't able to find any good books, tutorials or documentation on it.

[ul]
[li]Where i can find good learning material? Also, any good samples to work with?[/li]
[li]Is there any modern book on it that you guys recommend?[/li]
[li]Is PBR part of the rendering workflow?[/li]
[li]Are there any examples of multiplayer games, such as an FPS?[/li]
[li]Are there any examples of basic scene editors or terrain editors, so i can start from there? Just something basic: manipulating objects with gizmos and saving that information in the scene. And then loading ingame.[/li][/ul][/quote]

Hi IF you are familiar with c++ OOP and component based design then you will get into it in maybe 4-5 days by reading the documentation and the samples. Urho3d has a really clean and simple api although i'm not a big fan of component based programming. 

You can find samples in Urho SDK they cover almost everything you need to get into programming with Urho3d
AFAIK there's no books currently but the documentation is really helpful.There are interesting tutorials/examples on the wiki that shows some tricks and stuff  : [urho3d.wikia.com/wiki/HowTos](http://urho3d.wikia.com/wiki/HowTos)
Urho3d comes with an simple yet advanced scene editor .It is really easy to use. The editors best feature (if we could call it a feature) i like is The interface is really well designed and user friendly. (Some people like messy unintuitive editors where the gui is a bloated garbage and you will spend 3 months to even start the damn thing :smiley: well i hate that  !)

-------------------------

jmiller | 2017-01-02 01:05:25 UTC | #3

Hello and welcome to the forum. :slight_smile:

How I got into Urho3D

Checked out the master/head branch
[code]git clone https://github.com/urho3d/Urho3D.git[/code]

Started building per documentation and reading on more topics
[urho3d.github.io/documentation/HEAD/index.html](http://urho3d.github.io/documentation/HEAD/index.html)
[urho3d.github.io/documentation/HEAD/pages.html](http://urho3d.github.io/documentation/HEAD/pages.html)

Browsed the samples, which are written in both C++ and AngelScript (similar to C++). Like the rest of the code, they're very clean and well-commented.

FPS: NinjaSnowWar is a functional multiplayer FPS written in a few files of AngelScript.

PBR: hd_ contributed some physically based shaders you may want to check out.
[topic921.html](http://discourse.urho3d.io/t/shaders/899/1)

-------------------------

GoogleBot42 | 2017-01-02 01:05:25 UTC | #4

Hey there!   :slight_smile:   These will help you to understand the engine's structure, how to compile, etc.

[url]http://urho3d.github.io/documentation/1.4/index.html[/url]

If you want to script in lua or angelscript you will want to pay particular attention to the "Urho3D Player" If you want to go the C++ route you will want to use Urho3D as an external library. Note that if you choose to code in angelscript you will not be able to target HTML5 because how angelscript works and how Urho3D exposes it api to angelscript.

Be sure to check out the samples as well you can learn a lot from them! (There are 39 samples in total.)  See here: [url]http://urho3d.github.io/documentation/1.4/_examples.html[/url]

The urho3D wiki that was posted before is nice because anyone can contribute but it currently doesn't have much content.  As you work through learning Urho3D and you have time it would great if you added some content there! :wink:

This forum is very active and (I think) is very friendly.  One of the biggest advantages of Urho3D is that is has a highly motivated development team.  Bugs are often fixed the same day.  Features are constantly being added.  For example, just over the last few months DirectX11 and OpenGL 3 renderers were created and are in the latest Urho3D release v1.4   Also DetourCrowd and webgl/HTML5 via emscripten support was added as well!  Here are the web demos: [url]http://urho3d.github.io/HTML5-samples.html[/url]

I hope that helps!  :wink:

-------------------------

TikariSakari | 2017-01-02 01:05:25 UTC | #5

[quote="GoogleBot42"]
This forum is very active and (I think) is very friendly.  One of the biggest advantages of Urho3D is that is has a highly motivated development team.  Bugs are often fixed the same day.  Features are constantly being added.  For example, just over the last few months DirectX11 and OpenGL 3 renderers were created and are in the latest Urho3D release v1.4   Also DetourCrowd and webgl/HTML5 via emscripten support was added as well!  Here are the web demos: [url]http://urho3d.github.io/HTML5-samples.html[/url]
[/quote]

Hey thanks, I was actually looking for these samples some time ago, but couldn't find them anywhere in the documentation. Most likely I just missed it. Now that I checked, google seems to find the link pretty fast though by just googling: "Urho3D html5". 

I was kind of expecting the link to be in either first page, which could easily give people impression what Urho is about when entering the page, or under Document -> Examples, but it is not in there either.

-------------------------

GoogleBot42 | 2017-01-02 01:05:25 UTC | #6

It sort of is on the first page... There is a blue box with the text "site navigation" click it and a drop down box comes up.  Press "pages" and you are taken [url=http://urho3d.github.io/pages.html]here[/url].  Then html5 samples is in the list of links...

-------------------------

XGundam05 | 2017-01-02 01:05:31 UTC | #7

Didn't want to start a similar thread when one already existed:

I'm trying to use Urho as an external library and setting everything up to develop for the Pi 2. But something just isn't clicking. I've never used CMake, and my last experience with traditional make files was a single quarter class ~7 years ago. All my development (asides from then) has been in windows. Specifically in C# during the past 5 years of my job doing line-of-business and full-stack web stuff.

It could just be residual frustration from trying to get Linux to dual boot on my Win 8.1 laptop (it won't, but that's another matter), but the documentation on using it as a library is about as clear as mud to me right now. Between that, setting up the cross-compile toolchain, and never having even heard of CMake before this, I just feel lost. Any guidance is appreciated. [i]Maybe things will look different in the morning after I get some sleep.[/i]

-------------------------

weitjong | 2017-01-02 01:05:32 UTC | #8

I only have Pi but it should not be of any differences with Pi 2. I would strongly suggest you to also install Ruby and Rake into your host system. I am assuming you will be doing cross-compiling build for RPI on a Linux host system. Building Urho3D library on Pi device itself is even more easier to do, but it just take longer time to complete due to Pi slow CPU processor speed.

[ol]
[li] Setting up all the pre-requisite software.
- Clone the RPI cross-compiler toolchain from [github.com/raspberrypi/tools](https://github.com/raspberrypi/tools). Set RPI_PREFIX environment variable accordingly. Note this is not just a path to the tool directory. The variable must also contain the prefix string. So, it should be set to something like this: /path/to/raspi-tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian/bin/arm-linux-gnueabihf
- Clone the RPI sysroot from [github.com/urho3d/rpi-sysroot](https://github.com/urho3d/rpi-sysroot). Set RPI_SYSROOT environment variable to where you have cloned the sysroot.

[/li]
[li] Building Urho3D library. Assuming you have already cloned Urho3D. Go to that cloned directory and from the Urho3D project root, execute below commands.
[code]rake cmake rpi && rake make rpi[/code]
[/li]
[li] Using Urho3D library. First you need to create a skeleton project structure. So, execute below command still in the Urho3D project root. You may replace ~/myproject to /path/to/anywhere/you/like/for/your/new/project.
[code]rake scaffolding dir=~/myproject
export URHO3D_HOME=$(cd ../rpi-Build; pwd)[/code]
Once this is done, go to that new project directory and from your own project root this time, execute below commands. If you already have your own *.cpp and *.h source files that you want to use in the build, now it is a good time to use them to replace the place holder source files (Urho3DPlayer.cpp and Urho3DPlayer.h) in the project root.
[code]rake cmake rpi && rake make rpi[/code][/li][/ol]

Simple. No? The truth is, I could as easily just substitute 'rpi' in all the above commands with 'mingw', 'android', 'ios', or even 'emscripten' to target the respective platform.

-------------------------

GoogleBot42 | 2017-01-02 01:05:32 UTC | #9

weitjong explained the easiest way I know. :slight_smile:  I would try that and see where it gets you.

If you are dependent on an IDE you may have trouble getting one to run nicely on the raspberry pi particularly because of how little memory it has how slow its processor is.  Thus, I doubt that you will be able to run any IDE nicely that is written in Java.  From my experience these use a lot more CPU power and several times more memory than similar IDE's.  Some IDE's written in C/C++ might work.  I use qt creator and opening a small project uses about 170 MB of RAM (Not bad considering that the raspberry pi 2 has 2GB of RAM total IMO but of course much of that memory already called for just to run the OS, X server, etc.).  There are a lot of other IDE's written in C++ too.

If you want something more lightweight (but looking awesome :stuck_out_tongue:) I suggest sublime text.  It is a commercial text editor (not a full IDE but in some ways similar) but there is no obligation to pay for it if you don't want to.

But then there is also a simple text editor with syntax highlighting.



I know this is off-topic but you said you couldn't get linux working in a dual boot environment with windows 8?  I definitely understand.  Secureboot is a HUGE pain.  What linux were you trying to install?  I have installed ubuntu on my brother's comp (he wasn't enough of a linux guy for arch linux which is my OS of choice :wink:) in a dual boot situation with windows 8.  It was a pain to get it working but I got it working eventually. (If you are new to linux I highly recommend that you install ubuntu or some other OS that has an auto installer because installing the OS yourself can be very scary if you don't know what you are doing because of the windows OS you don't want to hurt or delete.)

First, where did you get stuck? Again, what were you trying to install?  Did you disable secure boot?  (To disable it completely you will need to disable it in the control panel and in BIOS. You may need to set an administrator/supervisor password in BIOS to be allowed to disable secure boot).

I don't know how smart ubuntu's auto auto installer is with setting up the partitions to install linux and shrink windows 8 but I can tell you that 4 years ago when I first started with linux (now my main OS) I had installed ubuntu and its auto partitioning tool is very smart but that was with windows 7 and some things have changed since then.  If worst comes to worst you may have to partition it yourself.  There are a lot of youtube videos to help with that I think.

Finally, when ubuntu (or whatever you pick) is installed be sure to go into BIOS and change the boot order to boot the "device" called "ubuntu" first instead of windows 8.  Don't worry you will still be able to boot windows 8 (assuming you disabled secure boot correctly) in a prompt that comes up right after booting "ubuntu".  This prompt is known as grub.  It is a mini-os only a few megabytes large that serves as a boot loader for linux and --if you have multiple os's-- a place where you can choose between os's.

I hope that helps.   :slight_smile:

-------------------------

weitjong | 2017-01-02 01:05:32 UTC | #10

I forgot to mention earlier in my post that there is a build option "URHO3D_SCP_TO_TARGET" where you can use to set up an automatic SCP between your host system and the target Raspberry Pi device. Obviously for this to work both your host system and Pi must be on a same local network, and that you have enabled the sshd daemon on Pi, and you have setup the SSH digital keys and authorized_keys. If you don't know what I am talking about then it is fine also. Just use an USB flash drive to transfer the files over  :wink: .

About the dual booting thing. I have not tried that on a laptop. I have only done that on my full tower rig. Now I have a triple boot setup even (Fedora Linux, Mac OS X, and Win7) on a single 120 GB SSD. I have only one advice. Have a backup contingency plan. When I started to learn dual booting years ago on my old workstation rig, I had multiple Hard Disk at my disposal, so I have a luxury to try to install each OS on a different disk without have to worry about the partition resizing or about the risk of overriding the boot manager. On a laptop I can imagine it will be a daunting task for beginner. Good luck.

-------------------------

XGundam05 | 2017-01-02 01:05:32 UTC | #11

Thanks for all the help [i](this is officially the nicest forum I've been on besides r/monsterhunter and the MF0 Hangar)[/i] :slight_smile: I will attempt the rake method. I think I was mostly getting hung up on trying to understand the intricacies of cmake without actually diving into it.

As to the dual boot issue, I wasn't getting the installer to recognize my windows partition. It kept complaining about the hibernation file, and the MBR portion of the partition table was oversized for some reason. Fixed the partition table using gdisk, but then windows threw a tizzy and I had to repair it. After that, the hibernation file was gone, and the partition table was fixed, so I was able to install Ubuntu (15.04)...but the "repair" left my user profile corrupted in windows.

From there, I made a new user and backed up my user-specific files...but, having had a bourbon barrel stout in hand, I forgot to move the files from the desktop of the temporary profile. I lost 200GB of stuff because of my arrogance and stupidity in not backing up my stuff -.-

So, having nothing to lose, I'm now running Ubuntu as my sole operating system. Ran it for a good while in college many years ago when I had a rather nasty BSOD and no windows disk handy :wink:

I don't plan on using an IDE at the moment (I really need to learn cmake), and my current poison of choice is Atom.

-------------------------

GoogleBot42 | 2017-01-02 01:05:32 UTC | #12

[quote="XGundam05"]As to the dual boot issue, I wasn't getting the installer to recognize my windows partition. It kept complaining about the hibernation file, and the MBR portion of the partition table was oversized for some reason. Fixed the partition table using gdisk, but then windows threw a tizzy and I had to repair it. After that, the hibernation file was gone, and the partition table was fixed, so I was able to install Ubuntu (15.04)...but the "repair" left my user profile corrupted in windows.

From there, I made a new user and backed up my user-specific files...but, having had a bourbon barrel stout in hand, I forgot to move the files from the desktop of the temporary profile. I lost 200GB of stuff because of my arrogance and stupidity in not backing up my stuff -.-[/quote]

 :frowning:  That is quite a horror story.  I hope that you didn't lose anything critical.  (About the hibernation I now remember that windows 8 uses a hybrid sleep that hibernates just the core os for faster startup times and it ideally should be disabled for dual booting.)

I was fortunate because my computer came with windows 7 so even though I didn't know what I was doing I was ok. Again sorry to hear about you unfortunate experience. :\

[quote="XGundam05"]Ran it for a good while in college many years ago when I had a rather nasty BSOD and no windows disk handy [/quote]

That's good to hear!  I was afraid you might abandon linux just because of installation issues (I love linux and try to promote it. :stuck_out_tongue:). (That must have been one nasty BSOD...  :confused:)

[quote="XGundam05"]I don't plan on using an IDE at the moment (I really need to learn cmake), and my current poison of choice is Atom.[/quote]

Poison.   :laughing:  That is so true.  I have become interested in atom myself.  It is not as lightweight as sublime text but sublime's unregistered popup drives me crazy. :stuck_out_tongue:  When I use an IDE I sometimes feel like I am using a crutch.

-------------------------

weitjong | 2017-01-02 01:05:33 UTC | #13

One more thing. When doing an RPI cross-compiling build, our build system has no way to detect automatically whether the targeted Pi device is a Pi 1 or Pi 2. When doing an RPI native build, only then it can reliable detect this and set the default build option correctly. So, for the cross-compiling build targeting Pi 2, you would want to add this build option "RPI_ABI=armeabi-v7a" manually in order to produce better binaries suitable for your Pi 2. Check the build option page for more detail.

-------------------------

XGundam05 | 2017-01-02 01:05:39 UTC | #14

Just wanted to say thanks :smiley: CMake and the Urho3D build process are a thing of beauty. Now off to learn the engine (if I had any unclaimed vacation days, I'd take a few off just for that...this is a fun looking engine) and make a pair of trigger sticks :slight_smile:

Seriously though, thanks :slight_smile:

-------------------------

