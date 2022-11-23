zakk | 2017-09-20 14:03:30 UTC | #1

Hello,

I want to use Lua with Urho3DPlayer only (just scripting).
I'm using Arch Linux 64 bits, with pre-compilated Urho3D shared libs.


I've written a minimal program for this, but i've some questions about the output of Urho3DPlayer command execution.

Let's see the script for beginning

<code lua>

function Start()
  graphics.windowTitle = "hello world"
  SubscribeToEvent("KeyUp",exit_test)
end

function exit_test(eventType,eventData)
    local key = eventData["Key"]:GetInt()

    --eventType and eventData are userdata
    if key == KEY_ESCAPE then
      engine:Exit();
    end
end
</code>

So it's just a black window with a title, waiting for ESC key to be pressed.

I launch it this way:

Urho3DPlayer helloworld.lua -w -p .

the "-p ." parameter is for avoiding using the Data and CoreData from the sample directory.

So i'm on my own, no data, no resources, just the script.

> [Wed Sep 20 15:52:33 2017] INFO: Opened log file /home/zakk/.local/share/urho3d/logs/helloworld.lua.log
> [Wed Sep 20 15:52:33 2017] INFO: Created 3 worker threads
> [Wed Sep 20 15:52:33 2017] INFO: Added resource path /home/zakk/sources/Urho3D-1.7-Linux-64bit-SHARED/usr/local/bin/
> [Wed Sep 20 15:52:33 2017] INFO: Added resource path /home/zakk/sources/Urho3D-1.7-Linux-64bit-SHARED/usr/local/bin/../share/Urho3D/Resources/Autoload/LargeData/
> [Wed Sep 20 15:52:33 2017] INFO: Set screen mode 1024x768 windowed monitor 0
> [Wed Sep 20 15:52:33 2017] INFO: Initialized input
> [Wed Sep 20 15:52:33 2017] INFO: Initialized user interface
> [Wed Sep 20 15:52:33 2017] ERROR: Could not find resource Textures/Ramp.png
> [Wed Sep 20 15:52:33 2017] ERROR: Could not find resource Textures/Spot.png
> [Wed Sep 20 15:52:33 2017] ERROR: Could not find resource Techniques/NoTexture.xml
> [Wed Sep 20 15:52:33 2017] ERROR: Could not find resource RenderPaths/Forward.xml
> [Wed Sep 20 15:52:33 2017] INFO: Initialized renderer
> [Wed Sep 20 15:52:33 2017] ERROR: Could not initialize audio output
> [Wed Sep 20 15:52:33 2017] INFO: Initialized engine
> [Wed Sep 20 15:52:34 2017] INFO: Loaded Lua script helloworld.lua
> [Wed Sep 20 15:52:34 2017] INFO: Executed Lua script helloworld.lua

But with only this little script, i have a lot of questions !

1) what are those _Added resource path_ , i've specified "-p ." for avoiding this

2) Urho3DPlayer tries to load Textures, a Technique and a RenderPath.
I've looked at _Urho3DPlayer.cpp_ sourcefile, and i guess it comes from the Urho3D engine itself.

What if those files are not present ? Can i put code in the script for avoiding their loading ?
For what i see, it doesn't seem to block script execution, which wait for ESC key press as it should do.

3) What is the error _could not initialize audio output_ ? I don't see it when i run the Lua samples (but couldn't find in the sample where were the sound init).

I think it's all for the moment, but quite a lot for a beginning!

Thank you for reading :)

Zakk.

-------------------------

JTippetts | 2017-09-20 19:16:46 UTC | #2

Using -p allows you to specify the resource directories, which includes the core data as well as your game-specific data. Using -p with no path tells Urho3DPlayer.exe that there are no resource directories, but it doesn't tell it not to try to look for the stuff it needs in CoreData. All the basic ramp textures for lights, the built-in shaders, the default render-path, etc... are found in CoreData. It still needs those to run correctly, you just aren't letting it find them. So it'll _try_ to load them, fail (because they can't be found), and yell at you in the log.

IMO, you're signing yourself up for some pain by trying to get around providing CoreData. You can omit Data with no problems, but CoreData is pretty important. You can, of course, provide your own CoreData-style directory that provides the ramps for lights, the default render path, etc... But why? I mean, all that work is done for you, why go through the trouble? You can run -headless, and it won't try to load that stuff, but then it won't create a window for you either, since it'll think you just want to run a server with no display.

As for the audio errors: I've run Urho3D on Linux before. Audio errors are kind of part of the game. Some day, somebody will write sane audio handling for Linux and catch it up with the modern world, but that day is not today, probably not tomorrow, and next decade is looking doubtful too. Sound on Linux is _notoriously_ broken in my experience. You might need to dig around in pulseaudio configurations to get it working correctly. For the record, under Linux Mint I never was able to get it working correctly, and I fucked with it for seven months or more before I bought another Windows laptop.

-------------------------

Modanung | 2017-09-20 22:11:33 UTC | #3

[quote="JTippetts, post:2, topic:3582"]
For the record, under Linux Mint I never was able to get it working correctly
[/quote]
I'm on Linux Mint as well and audio has always worked fine for me.
One thing I do have is the occasional frame drop accompanied by jagged audio, but I blame NVidia for that.

-------------------------

JTippetts | 2017-09-20 22:13:01 UTC | #4

I kept getting buffer underrun errors, no matter what pulseaudio configurations I tried.

-------------------------

Modanung | 2017-09-20 22:51:58 UTC | #5

@JTippetts, did the frame rate also severely drop during these buffer underruns? And were you using NVidia drivers? I get this in Nexuiz as well, for instance.

@zakk's audio problem was that the output could not be initialized at all. This seems to indicate a different problem.

-------------------------

JTippetts | 2017-09-20 22:57:54 UTC | #6

@Modanung It was NVidia drivers. Don't remember if the framerate took a hit or not, it's been awhile. 

"This seems to indicate a different problem."

It's always _some_ problem, at least in my experience. I like Linux, but I don't think I've ever had a problem-free install. And sound seems to be one of those repeat offenders.

-------------------------

Modanung | 2017-09-20 23:02:33 UTC | #7

Beats running spyware as an operating system.

-------------------------

JTippetts | 2017-09-20 23:00:50 UTC | #8

You'll get no argument from me on that one. :smiley:

-------------------------

Modanung | 2017-09-21 13:02:56 UTC | #9

:slight_smile:

@JTippetts: Anyway, I don't think the problem we encountered was sound related. Even though one of the symptoms is an audio buffer underrun. My guess is clutter in the render pipeline (caused by proprietary video drivers) blocks the entire process, which then no longer fills up the audio buffer. 
The proprietary NVidia video drivers used to make my system crash hard; random instant power off. So it's gotten a lot better if you ask me. The alternative is using open source drivers with less bugs, but also less performance and features.

-------------------------

Modanung | 2017-09-21 13:18:43 UTC | #10

@zakk: Btw, it can not find `Textures/Ramp.png` (etc.). Meaning the files do not need to be inside a folder named CoreData:
`AnyResourcesFolder/Textures/Ramp.png` will do. So you _could_ simply copy the missing files to save some kB in the final product.

-------------------------

zakk | 2017-09-21 13:28:32 UTC | #11

Thank you for the answers !

I regret to have put the sound on the table, because it wasn't the most important for me :slight_smile:
 
As the officials Urho3d samples are working, it must be something missing (sound initialization code i must have missed in the sample, should be).

@Modanung : yes, i have seen that you don't need _CoreData_ or even _Data folders_.
For the mandatory GLSL shaders (the rest can be skipped, but minimal shaders must be here for something to be drawm), i put them in a _Shaders/GLSL_ subfolder, found by the "_**-p .**_" parameter.

-------------------------

