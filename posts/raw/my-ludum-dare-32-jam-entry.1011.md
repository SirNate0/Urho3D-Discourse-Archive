Bananaft | 2017-01-02 01:04:48 UTC | #1

[video]http://www.youtube.com/watch?v=32O_mfMpv6g[/video]

I've made this game in three days on recent Ludum Dare jam event. My experience with Urho is still pretty poor, and I decided, that participating in a jam is a good opportunity to learn. I went with script only, because I'm not familiar with C++. It also was my first game jam. I worked in CodeLite with AngelScript autocompletion set up with help of this thread: [groups.google.com/forum/#!topic ... WOOGAdwlEU](https://groups.google.com/forum/#!topic/urho3d/8WOOGAdwlEU)

Download: [url]https://dl.dropboxusercontent.com/u/8845134/ld32/supapowah.zip[/url]
Source, single .as file: [url]http://pastebin.com/4fL39qaC[/url]
LD page: [url]http://ludumdare.com/compo/ludum-dare-32/?action=preview&uid=51412[/url]

Feel free to criticize.

I really enjoyed working on Urho. It performs like a beast. And I figured out a lot of new things in that three days despite the lack of documentation and tutorials for noobs like me. Anyway, here are several things, that I want to clarify:

1) Later in development the Urho3d player started to crash pretty often. There is no particular action, causing it. It should be something in my code, but is there a way to debug a Urho3d player crush (other than building and running it in debug mode)? Is it dumping crash logs somewhere?

2) Is there a way to restart the whole game? I ended up with scene_.RemoveAllChildren(); and then creating everything up again. Is it okay? Or maybe there is something else I have to remove manually?
 
3) Updates. Is there a place where I can find the list of all available update functions, and order in which everything gets updated? 

4) At first, I was happy to find out, that I can read input from any place, like Update() or FixedUpdate() of script objects, but actually, that's doesn't work sometimes, and sometimes depends on FPS. Examples are not constant in the ways, thay handling input, so what is the basic do/ do not?

5) Enabling vsync drops fps to 15.

-------------------------

thebluefish | 2017-01-02 01:04:48 UTC | #2

Nice entry for being done in 3 days! In particular, I like the weapon design, the chaining, and the zombies.

One thing I would suggest for future events is to modify the Urho3D player yourself. There is no reason (Though Game Jams sometimes require you to forsake all reason) to require someone to run GAME.bat. Instead, you can change Urho3D player to match the defaults you expect, and let other players modify those defaults with the command-line switches made available if they want to do their own thing.

1. You can specify the log level of the Urho3D Player with the -log switch:

[quote]
-log <level> Change the log level, valid 'level' values are 'debug', 'info', 'warning', 'error'
[/quote]

You can look at the other switches at [url=http://urho3d.github.io/documentation/HEAD/_running.html]Running Urho3D player application[/url].

These logs should go to a file called URHO3D.log

2. I believe with the Urho3D player, you're doing a good job of "restarting" the game. The alternative would be to recreate the scene entirely. With a C++ game, there would be more available to you, but your solution works fine.

3. You can view the main loop at [url=http://urho3d.github.io/documentation/HEAD/_main_loop.html]Engine initialization and main loop[/url]. Additionally, there are C++ headers for events, such as PhysicsEvents.h, that will give you a more verbose list of what events you can hook. I'm not familiar enough with AngelScript to offer exactly how to translate these, but it will all work.

4. Input is handled during then E_BEGINFRAME update. You can check for Input anytime after this event, and expect it to be consistent across the frame. Therefore there is no real "standard" to check it. You could listen for input events, or check the Input subsystem yourself. It's really up to what works best for you.

5. Damn, son.

You can look through the [url=http://urho3d.github.io/documentation/HEAD/index.html]Urho3D documentation here[/url].  There's a drop-down box at the top-right corner if you're using an older build (Such as 1.32).

-------------------------

sabotage3d | 2017-01-02 01:04:49 UTC | #3

Looks really cool man !

-------------------------

Bananaft | 2017-01-02 01:04:50 UTC | #4

Thank you both for feedback.

[quote="thebluefish"]One thing I would suggest for future events is to modify the Urho3D player yourself. There is no reason (Though Game Jams sometimes require you to forsake all reason) to require someone to run GAME.bat. Instead, you can change Urho3D player to match the defaults you expect, and let other players modify those defaults with the command-line switches made available if they want to do their own thing.
[/quote]

Yeah, that's a shame, indeed. As I said, I'm not very familiar with c++ yet. My only experience is - building Urho. I knew, it's should be easy, but I was afraid to get stuck on this task and lose too much time.

I also thought, would be cool, if Urho3Dplayer would be trying to start some default filename like autoexec.as (.lua), or checking for file to start in some simple text file. Ability to make games without diving into c++ is a nice feature to have.

1. I've enabled log file writing. But there is nothing engine writes right before the crash.
3. That's seems to be exact thing I (over)looked for.

Thank you very much for your answers!

-------------------------

thebluefish | 2017-01-02 01:04:50 UTC | #5

Log file could be in a different location, but I can't seem to locate where the default is. If it crashes before creating the log, then it's having a problem early on. I believe initializing the Engine subsystem is what creates the log file.

-------------------------

Bananaft | 2017-01-02 01:04:50 UTC | #6

[quote="thebluefish"]Log file could be in a different location, but I can't seem to locate where the default is. If it crashes before creating the log, then it's having a problem early on. I believe initializing the Engine subsystem is what creates the log file.[/quote]

It seems like Urho doesn't save logs by default. To enable it you have to add log.Open("game.log"); at the very top of Start().

It crashes midgame, when nothing really particular or intensive is going on.

-------------------------

thebluefish | 2017-01-02 01:04:50 UTC | #7

The log file is created automatically.

It looks like the default location is C:\\Users\\<your username>\\AppData\\Roaming\\urho3d\\logs\\

This is a hidden directory, but you can most directly access it in Windows Explorer by navigating to %appdata%\\urho3d\\logs\\

In the Urho3DPlayer, the related line is:
[code]
// Use the script file name as the base name for the log file
        engineParameters_["LogName"] = filesystem->GetAppPreferencesDir("urho3d", "logs") + GetFileNameAndExtension(scriptFileName_) + ".log";
[/code]

-------------------------

Bananaft | 2017-01-02 01:04:51 UTC | #8

[quote="Sinoid"]That's what the "CommandLine.txt" file in the Data folder does. If you run the player without any arguments it'll load use that file for command instructions.[/quote]

Oh, ok, cool.

Well, doesn't work for me for some reson. (Win7 64, 1.32 release)

-------------------------

rasteron | 2017-01-02 01:04:51 UTC | #9

Looks good! Thanks for sharing.

-------------------------

Bananaft | 2017-01-02 01:04:51 UTC | #10

[quote="Sinoid"]
You should build from source. So much has changed since 1.32
[/quote]

As I mentioned earlier, I've already built Urho from sources, it was stable version however.  The process, indeed, is reasonably easy. I also built your TIFF packer, though I was close to asking you for binary.

So, slowly, but I'm advancing on C++.

Thank you for being helpful.

-------------------------

