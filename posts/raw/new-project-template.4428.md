Miegamicis | 2018-08-01 06:53:07 UTC | #1

I will continue the post started here: https://discourse.urho3d.io/t/urho3d-from-the-scratch/4335/36

A while ago I decided to start this repo: https://github.com/ArnisLielturks/Urho3D-Empty-Project
The main idea is to create some sort of template for any project that I might start in the future using Urho3D engine.It should contain all the basic functionality that is needed for almost every project - configuration file reading/saving, level management (switching between scenes etc.), UI window management, control mapping to allow players to set up the controls themselves, modding - adding new scripts to the game that engine picks up automatically and many other things.

It's been more than a week since my last update, so here are the things that I was able to do in this time:

* Replaced Urho3D UI with Nuklear UI (https://github.com/rokups/Urho3D-nuklear-ui)
I have ported almost all of the existing views to Nuklear. Previously console could be opened by pressing F1, now it's replaced with the NuklearUI console which can be opened by pressing F4. It still is missing some nice features but it's usable.

* Added spltiscreen sample which currently supports up to 4 players. To launch it just start the game. Additional players can be added either by adding new controllers before the game or while in it, it will adjust the viewport count automatically.

* Settings window now contains joystick and mouse settings. Everything that you are able to change in the settings window will also be saved in the `Data/Config/config.cfg` file. 
All the settings (including mapped control keys) will be saved in the same file

* Fixed a lot of different bugs related to new Subsystems like WindowManager, LevelManager. It should be a lot more stable now

* I added CircleCI as a continuous integration tool to help testing out my changes on multiple platforms (currently Windows[MinGW] and Linux[GCC]). Config file for the build system can be found here: https://github.com/ArnisLielturks/Urho3D-Empty-Project/blob/master/.circleci/config.yml
Config file actually is pretty readable for someone who want to build the project themselves since it contains all of the bash commands to do that.
CircleCI uses docker container which was built with the following repo: https://github.com/ArnisLielturks/Urho3D-Docker-Container

@smellymumbler already gave some good ideas that I could add in the future and if you have any ideas how this can be improved even further, share them!

-------------------------

smellymumbler | 2018-08-01 13:47:23 UTC | #2

Curious: Why the move to Nuklear? Is it faster? Does it have a better architecture?

-------------------------

ucmRich | 2018-08-02 01:10:50 UTC | #3

Wow you're doing great, many thanks! keep it up please :smiley:

-------------------------

Miegamicis | 2018-08-02 06:36:06 UTC | #4

I always thought that it looks kinda unpolished, it does it's job good, but when you wan't something a bit more different you end up rewriting the engine UI code just for this particular case. And of course you have to maintain it yourself when new engine version comes out. That's why I started looking at other solutions. I looked at couple GUI libraries and ended up with Nuklear just because it was very easy to set up, thanks to rokups repo: https://github.com/rokups/Urho3D-nuklear-ui

Nuklear is not faster than Urho's built in UI system, but it is much more powerful since it contains a lot of components already. Main difference in the architecture is that Urho uses event system to deal with UI interaction, Nuklear is not. At first I thought that it's a bad thing but in the end I ended up writing less code and it was more readable.

-------------------------

Miegamicis | 2018-12-12 19:19:17 UTC | #5

Update:

Had second thought in the past months regarding the Nuklear implementation. Stumbled upon a problem with Nuklear and CI which kinda broke the MinGW build process. I was feeling lazy and couldn't figure out how to fix it and decided to move back to Urho3D UI system. 
Besides moving back to Urho3D UI I've added a lot of small improvements like - 
* in-game settings menu, 
* control mapping updates, 
* config file saving structure, 
* multiline achievement texts, 
* additional video settings added.
* LUA script mods are now supported

All the things that are planned for future are available here: https://github.com/ArnisLielturks/Urho3D-Empty-Project/wiki

Let me know if there is something else that you'd like to see in this repo.

-------------------------

smellymumbler | 2018-12-13 01:39:23 UTC | #6

Whoa! Huge wave of amazing updates. Glad to know you opted for Urho's UI instead! It makes for a perfect project, specially if in the future people consider adding this to the main repo. 

Thanks a lot for your effort, dude. This is pure awesome.

-------------------------

Miegamicis | 2018-12-13 09:45:52 UTC | #7

Not sure if this will ever be merged in the main repo since the sample is quite large but the good thing about this is that it gives me ideas how to further improve the engine. Also I'm happy if  others might find this useful.

I myself will probably take this sample app for a spin for the upcomming game jam - GGJ.

-------------------------

Miegamicis | 2019-02-14 09:39:21 UTC | #8

It's been a while since the last update, here's what I've got so far:

* Achievements can now be registered via events
* Achievement progress is now automatically tracked/saved/loaded and there are option in the settings menu to clear achievement progress
* Achievement window was updated to reflect all registered events and their progress
* Joystick key mapping is updated to support multiple joystick types
* Camera FOV can now be changed via settings menu
* Background scene loading via SceneManager, Loading screen reflects the status of the scene manager - https://github.com/ArnisLielturks/Urho3D-Project-Template/blob/master/Source/Levels/Loading.cpp#L35
* Audio manager was updated for easier scene node sound management
* Splash screen now supports multiple images, each of them will be showed in seperate Splash screen https://github.com/ArnisLielturks/Urho3D-Project-Template/blob/master/Source/Levels/Splash.cpp#L69-L72
* Translations are now supported - at the moment there are LV and EN translations, it can be changed via settings window
* Sample gamemode added via help of mods, it supports splitscreen mode, just plug in up to 4 joysticks and test it out - https://github.com/ArnisLielturks/Urho3D-Project-Template/blob/master/bin/Data/Mods/GameMode.as
* Scoreboard window updated, it now reflect player scores with the help of global events and variables which are easily accessible via mods
* DebugHud now displays additional values about the current game state - active level, achievement count, controller count, mod count etc.

What I'm planning to do next:

* Mod library application - web app with the list of all available mods, don't want to bloat this repository with too many mods + I just wanted to do that and there is no one who can forbid me to do that
* Compile this sample for the Android devices
* Seperate control mapping for each controller
* Maybe add networking sample? This will require additional stuff for the engine itself - multiple control sending to server for 1 client connection.
* Does anyone know how I could achieve the brightness, gamma changing for the video? Do I need to create shaders to achieve that? I wan't to add these options in the settings window.

-------------------------

Modanung | 2019-02-14 20:35:59 UTC | #9

[quote="Miegamicis, post:8, topic:4428"]
Does anyone know how I could achieve the brightness, gamma changing for the video? Do I need to create shaders to achieve that?
[/quote]

There is gamma and color correction post-processing render paths included with the engine in `bin/Data/PostProcess/`.

-------------------------

smellymumbler | 2019-02-14 20:35:37 UTC | #10

Holy crap that's a lot of stuff. This is one of the most exciting community projects I've ever seen. You should definitely setup a patreon so we can buy you a few beers.

-------------------------

Miegamicis | 2019-02-14 21:07:10 UTC | #11

Oh, right! Totally forgot about that.

-------------------------

Miegamicis | 2019-02-14 21:13:14 UTC | #12

Thanks! I have big plans for it in the future but at the moment I'm just doing it because it's fun and interesting.

-------------------------

Miegamicis | 2019-02-28 16:48:47 UTC | #13

Small update:

* Spent few days creating automated builds using TravisCI and CircleCI 
* Created project site to test out the build mechanisms and artifact upload -  https://mods.frameskippers.com/view_mod/3 . The archives which are uploaded there contain both - Linux and Windows executables with all the assets. Grab the latest build and test it out. You can easily map these builds with the Github to follow up with the progress.

* added Gamma settings in the video tab - probably will add the PR to the master branch with the changes to allow dynamic gamma changing at runtime.

-------------------------

Miegamicis | 2019-03-14 08:04:45 UTC | #14

Another update:

* Got the Android builds fully working with the sample, check the http://mods.frameskippers.com/ there are windows, linux and Android binaries available.
It still have to do some tweaking with the CI how the Android app actually gets built, for now it's a bit chaotic but at least the app ir runnable on the Android devices.
Also I haven't yet finished the control management for Android devices, but it's one of the next things in my to-do list. I'm planning to use this: https://github.com/Lumak/Urho3D-Joystick
Hope that it will result in the PR in the end since the default engine UI controls are horrible.

* I implemented so called "Loading Steps" which allows to hook up your own methods when the loading screen appears, it will move forward only if all of the loading steps have finished. It uses simple ACK mechanism to check for "inactive" loading steps and move forward with the next step if no ACK message was received for a certain amount of time. For the full example see the mod: https://github.com/ArnisLielturks/Urho3D-Project-Template/blob/master/bin/Data/Mods/LoadStepImitator.as

-------------------------

smellymumbler | 2019-03-14 18:20:03 UTC | #15

Pardon my ignorance, but what would be the point of those steps? So I can multithread loading of assets? Load levels in one thread, textures in another, sounds in another?

-------------------------

Miegamicis | 2019-03-14 18:45:49 UTC | #16

Pretty much everything you want. It's main idea is to indicate in the GUI what exactly is happening and to indicate how much there is left to load to start the actual game.

-------------------------

Pencheff | 2019-03-14 20:47:22 UTC | #17

I love your idea, thank you for sharing your work. Adding my thoughts on the UI, you can ignore my comments if you disagree.

The integrated UI from Urho3D seems flexible enough to do everything a game needs, it just needs some work on top. I just made this "Options subsystem" using Urho3D UI:
![urho3d_integrated_ui|690x404](upload://vksUf5peRIAO8YucLTf6k3jdRnb.png)

Controls are navigatable (using arrow keys) and can be customized using the Urho3D editor. There are 
bunch of controls on top of the standard UI controls like UIBoolOption, UIMultiOption, UISliderOption, UIEditOption. With some trivial work, more controls and dialogs could be added.
I can share the code when I'm done with it.

-------------------------

Miegamicis | 2019-03-15 07:49:13 UTC | #18

Looks really good. I would like to try it out and maybe implement it in this sample.

-------------------------

Pencheff | 2019-03-15 14:43:11 UTC | #19

https://gist.github.com/PredatorMF/8dbf6b1772d5afdf6699ee31057beb12

This is my WIP version without code from my project. It only needs the 2 cpp files added to the project and registering object factories at engine start:
[code] 
  UITemplateElement::RegisterObject(context_);
  UIOption::RegisterObject(context_);
  UIBoolOption::RegisterObject(context_);
  UIMultiOption::RegisterObject(context_);
[/code]

I'm still working on it, trying to make controls as simple as possible and still usable on any device - PC/Tablet/Phone

-------------------------

Modanung | 2019-03-15 15:22:07 UTC | #20

I'm thinking it would be cool (and even more N00B-friendly) if this were to be implemented as wizards like:
https://discourse.urho3d.io/t/wrench-class-and-project-wizards-for-qtcreator/2076
...and:
https://discourse.urho3d.io/t/urho3d-codeblocks-wizard/1379

-------------------------

Pencheff | 2019-03-26 13:44:55 UTC | #21

I've created a GraphicsSettings sample dialog here:
https://github.com/PredatorMF/Urho3D/tree/SetModeTest/Source/Samples/54_GraphicsMode

The components are in ui_option.h/cpp files. There is BoolOption, MultiOption, SliderOption and TabsPanel. These are usable from C++ code and the editor. The demo looks like this:

![graphics-settings|641x500](upload://pIp2Tjvwzgkxo8njkeAO3G3y4Nq.png) ![video-settings|641x500](upload://ngbgFuwC9V8uKxpBDL2yPvEfdJf.png) 

Feel free to modify and use as you like.

-------------------------

smellymumbler | 2019-03-26 13:49:10 UTC | #22

Very useful sample. Dealing with monitor/resolution stuff sucks.

-------------------------

Miegamicis | 2019-03-28 09:54:08 UTC | #23

Thanks! Will try to impement this when I have a chance.

-------------------------

suppagam | 2019-07-18 01:38:55 UTC | #24

I started using this to learn more about the engine and it helped me a lot. Reading through your code is a very interesting way to learn the engine and not very confusing. Thanks for the readable code! :D

-------------------------

Miegamicis | 2019-08-22 15:13:38 UTC | #25

Been taking a long break from this project but few days ago decided to continue working on it. Here's what I've done so far:

* Completed the work on Android app 2 way communication. Next thing in the list for this is to try implement some sort of ad platform, cause that's what everyone is implementing these days anyway
* CI updates for faster building + build artifact upload
* A lot of small updates to the sample gamemode and the GUI
* Map selection window to allow loading 2 different maps
* Now there's a background scene for the main menu
* Credits screen refactored to allow more precise start/end time detection
* Removed Urho3DAll.h includes in all the project and done some cleanup for it

If you wan't to try it out, here's the build artifacts from CI:
Linux: https://303-138001494-gh.circle-artifacts.com/0/build.zip
Windows: https://304-138001494-gh.circle-artifacts.com/0/build.zip
Android: https://302-138001494-gh.circle-artifacts.com/0/launcher-app-armeabi-v7a-debug.apk

And here's few screens of it:
![Screenshot%20from%202019-08-22%2018-11-01|643x500,50%](upload://jA8Z7x51SXKobPzfUh5woTfyxn4.jpeg) ![Screenshot%20from%202019-08-22%2018-11-36|643x500,50%](upload://bS1dzYpErhyGMdV0BQvlnRtm1Ij.png) ![Screenshot%20from%202019-08-22%2018-12-16|643x500,50%](upload://qeGfGCMhHAK5M53w6rY1VpiBhxI.png)

-------------------------

suppagam | 2019-08-22 19:47:18 UTC | #26

What is the 2 way communication? Pardon my ignorance. :(

-------------------------

Miegamicis | 2019-08-22 19:48:13 UTC | #27

Passing events from c++ to java and vice versa.

-------------------------

glitch-method | 2019-08-30 06:50:40 UTC | #28

this is really great stuff, thanks! :smiley:

are you planning to stick with the urho ui then? 

i'm just scratching the surface of game dev yet, but i'm curious about immediate mode and had my eye on nuklear (in particular it looked flexible for hud/journal/inventory type info), what sort of mess does it make? the performance overhead seemed pretty minimal, but i'm too noob to know if it would count as negligible.

-------------------------

Miegamicis | 2019-08-30 09:18:47 UTC | #29

This project was intended as a starting point for any Urho3D game so it made sense to use the inbuilt UI system. I liked working with Nuklear, but didn't wanted to maintain it's integration on all platforms that Urho3D supports. But honestly speaking I think that Urho3D UI system is more flexible, you just have to learn it a bit + now it supports custom shaders which should allow to add cool effects to it. The default skin might look a bit oldschool, but you can heavily modify it to look more modern.

-------------------------

Modanung | 2019-08-30 10:35:30 UTC | #30

4 posts were split to a new topic: [SVG support for UI](/t/svg-support-for-ui/5532)

-------------------------

Miegamicis | 2020-02-06 20:12:51 UTC | #31

Did a lot of updates to the sample lately, it starts to seem that my template project becomes my sandbox for testing out stuff, but I try to keep it as universal as possible, here's the list of stuff that I added or removed:

* introduced perlin-noise terrain generation as part of sample (implemented  https://github.com/Reputeless/PerlinNoise)
* A lot of cleanup of the code to make the actual playable scene as empty as possible
* Implemented the @Pencheff 's settings window, very pleased how it works and looks
* Splitscreen supports up to 8 views just for the heck of it:
![image|690x389](upload://paoMnNFfd9fG0HBZkWP3dZwIAhj.jpeg)  
* Configuration file is now a bit more organized

If you wan't to check it out, please do: https://github.com/ArnisLielturks/Urho3D-Project-Template

-------------------------

Modanung | 2020-02-06 19:16:57 UTC | #32

Awesome interesting stuff! I will be sure to give it another spin in the near future.

-------------------------

lebrewer | 2020-02-06 22:47:06 UTC | #33

This has to be one of the most useful projects I have ever seen in the community. It's useful for a wide variety of projects, from small Ludum Dare prototypes, to full blown projects. Also, very polished. Congratulations, and thank you for the effort @Miegamicis.

 That splitscreen support is awesome too. I wonder if you are working on a kart game?

-------------------------

George1 | 2020-02-06 23:01:10 UTC | #34

All action and no talk.  You are the man of the week :slight_smile:

-------------------------

Miegamicis | 2020-02-06 23:15:21 UTC | #35

No real game behind it. I'm just getting ready for a hackaton I guess. The code quality might not be the best, cause I added quite few community components and didn't tried to update each of it's code to match the projects just because of the future updates that might come from them.

-------------------------

Miegamicis | 2020-02-06 23:19:04 UTC | #36

Can't take all the credit for it. A lot of guys here helped to shape it. :+1:

-------------------------

Pencheff | 2020-02-07 21:47:53 UTC | #37

Just tried it, had some fun jumping around pushing crates :D I had linker error on Visual Studio 2019, unresolved external symbol to SetupDiEnumDeviceInfo, fixed with a 
[code]
target_link_libraries(${TARGET_NAME} Setupapi.lib)
[/code]

-------------------------

Miegamicis | 2020-02-07 22:04:56 UTC | #38

Hi, thanks for the feedback. I ditched VS a while ago and haven't build it on Windows since then. CI takes care of that for me. I noticed that your settings window used some sdl stuff directly, was that intentional? Could it be related to this issue? Anyways I guess we can add the cmake flag to fix this issue for now.

-------------------------

Miegamicis | 2020-02-07 22:07:13 UTC | #39

BTW my favourite part of this sample for now is the ability to plug in joystick while you're playing the level, it should automatically add splitscreen support and spawn the new player on map. Sadly it works only on Windows.

-------------------------

Miegamicis | 2020-02-07 22:27:25 UTC | #40

There's actually a huge list of things that I would like to add to this project, to name a few:

• automatic build publishing to itch.io
• joystick key mapping for each connected controller
• mobile UI controls, for now the gyroscope is used for movement...
• networking support - probably only as a LUA or AS mod for easy removal but haven't yet decided anything
• improved UI design and possibly animations
• miscellaneous settings which would allow adding new configurable values to the settings window using only event system
• and many more

Let me know if there's something else that you might find useful.

-------------------------

Pencheff | 2020-02-07 23:27:32 UTC | #41

The error was related to joystick code and hid.lib, I can give you exact details later. I'm using static Urho3D build so that's probably why the error happens. In my code I'm only using SDL functions already provided by the library in Urho like getting monitor count and monitor resolutions.

-------------------------

CatPawns | 2020-03-28 00:05:12 UTC | #42

Hello am testing the project and this shows in the console 
WARNING: Unknown attribute rotationSpeed in XML data.

-------------------------

Miegamicis | 2020-03-28 07:20:10 UTC | #43

Rather small issue but should be fixed now.

-------------------------

urnenfeld | 2020-12-03 22:57:46 UTC | #44

So when I joined [here](https://discourse.urho3d.io/t/introduction-and-guidance-questions-for-starting-project/4871/13), I started working in a game, which basically was(and even still is) an *extension* of the 10_RenderToTexture example... But it has reached a point where it deserves something more.

Integrating that newbie exercise into **this template**, may have required a bit of time(3/4 weeks with ~1h/day dedication). But the Scene & Level Managing together with the Preferences included in this template(among other things I have not yet discovered) will pay for sure the time invested.

https://www.youtube.com/watch?v=bfE9cNe7Svw

Thanks @Miegamicis!

-------------------------

