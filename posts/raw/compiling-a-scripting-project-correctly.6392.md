evolgames | 2020-09-15 19:31:59 UTC | #1

What's the procedure for packaging/compiling a scripting project?
On all my Urho projects I've done the following:

* lua scripting
* project is run via urho3dplayer binary (which reads CommandLine.txt for the main.lua file)
* people on windows just run urho3dplayer.exe (renamed game.exe)
* data folder is accessible, along with scripts
* everthing works fine
Here's an [example](https://evolgames.itch.io/polysporia-ii).

I recently got a new pc and did a clean linux install. I followed [this](https://github.com/urho3d/Urho3D/wiki/Getting-started-in-Linux) short guide and built urho with the lua flag. The binaries are there and work fine.

What I've been doing works (or seems to). I have a template that I use and like other engines/frameworks with lua, I type away and run Urho3DPlayer anytime I want. However, I want to distribute my projects the right way. What is the correct procedure here? The binary samples still require the Data folder, but neither of the script folders. So what are they exactly? Are they just urho3dplayer files that *don't* read commandline.txt? Or do they have certain files embedded in them? Is there C++ code compiled in those samples?

I'm using Geany to edit my scripts. Because I've never needed to compile I have no idea how to set that up. Is there a guide anywhere for angelscript project distribution that I can read over? I found a wizard for codeblocks (which I don't use) but it looked to be for windows. I should have some terminal commands to do, correct? Or, is it okay to distribute a project like I am? Am I supposed to be creating make files to build my project with only the necessary files? Currently, I've just been stripping things down in a copied project folder, which has a Data folder etc and everything it needs to run all in a zip archive. I mean it works as a weird standalone thing, but I want to learn the proper way for lua and angelscript projects. I feel like I'm wildly off from what I should be doing.

-------------------------

SirNate0 | 2020-09-15 22:42:19 UTC | #2

The binary samples are all compiled c++ code. The lua/AS samples are scripts that the compiled c++ code that produced the Urho3DPlayer runs.

Possibly there is a way to embed all the files in the executable, but I'm pretty sure it's common for programs to have resources/config files/etc. beyond just an executable, so the zip file approach is probably fine.

To the best of my knowledge, Angel Script is probably too small to have any "proper" way of distributing things. Lua may have a more standard approach, but you require the Urho3D library with lua (built into the player or as a separate shared library depending on your build settings), so the zip file approach is probably still best.

I'm certainly no expert on distribution, so others may have more insightful answers, but what I said above is my understanding of it.

-------------------------

evolgames | 2020-09-15 23:27:34 UTC | #3

Ah okay that makes a lot of sense. I haven't used Windows in forever, but I think there's a way to make portable the entire folder as an .exe with a batch file or something.
But yeah most people find it intuitive enough. They unzip, see some stuff and a Game.exe and they can figure it out from there.

There is the issue of code protection, not that *I* care. It'd definitely be more convenient for modding to be able to edit an easily accessible script. But I know some people making proprietary software would have more of an incentive to "hide" code. And by that I mean just make it less easy to access or figure out. I tried compiling my lua scripts once but for some reason Urho3DPlayer didn't like that and refused to run them.

I guess if it works it works.

-------------------------

