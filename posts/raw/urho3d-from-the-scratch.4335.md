techno77 | 2018-06-20 07:20:53 UTC | #1

Hello and thank you for that engine, but...

I can not found any clear instructions how to install Urho3D from the scratch.

I'm new in gamedev and C++, so not exactly understanding how to organize file structure and build the new project. 

YouTube videos are only for version 1.6 and less, so it it not compare with 1.7.

Please help! How my Urho3D folder structure should look like? And how to build Hello world app?

-------------------------

Miegamicis | 2018-06-20 07:38:34 UTC | #2

It really depends. If you are planning on building games using prebuilt binaries, then all you have to do is set up the URHO3D_HOME environment variable and point it to the directory, where you have extracted the engine binaries.
If you plan on compiling project by yourself, get familiar with CMake which makes everything really easy. 

For the ubuntu the stops for building the engine is as following:
```
sudo apt get-update
sudo apt-get install -y libgl1-mesa-dev git cmake g++ libx11-dev
git clone https://github.com/urho3d/Urho3D.git
cd Urho3D
bash cmake_generic.sh build
cd  build
make
```

If everything worked, build/bin and build/lib should contain everything you need and in this case you can point the `URHO3D_HOME` environment variable to point to `Urho3D/build` directory

Regarding the project structure it's really up to you how you would like to structure the project. I would suggest looking at the Urho3DPlayer source code to get up and running.
https://github.com/urho3d/Urho3D/tree/master/Source/Tools/Urho3DPlayer

-------------------------

techno77 | 2018-06-20 07:53:35 UTC | #3

Thank you for reply. 

> It really depends.

This is the biggest problem for beginner. We don't know how to do it best way.


> For the ubuntu the stops for building the engine is as following:

I found the same build instructure for ubuntu or whatever, but I'm on windows. And that's the second problem :)

Is any tutorial of CMAKE build for Windows?

-------------------------

Miegamicis | 2018-06-20 08:08:01 UTC | #4

On Windows it should be much simpler since command line won't be used. Download CMake and Urho3D. Open up CMake, set the source directory to the one, where you've downladed engine source. Set the build directory (where the build files will be stored):

For example:
![image|496x102](upload://u2cmBsDX7qRMdjfNMXPX7AEcO2R.png)
_Note: Screenshots are taken on Ubuntu 16.04_

Then at the bottom of CMake GUI press "Configure", select your prefered compiler, wait for it to finish and then press "Generate". On Windows I usually use Visual Studio so when I generate build files for VS the build directory should contain the Urho3D.sln file which can be used to open complete Visual Studio project for Urho3D. It will also contain sub-project Urho3DPlayer and all the samples.

Let me know if this helps.

-------------------------

jmiller | 2018-06-20 08:16:26 UTC | #5

FWIW, building process on supported platforms
  https://urho3d.github.io/documentation/HEAD/_building.html

-------------------------

Miegamicis | 2018-06-20 09:35:01 UTC | #6

Regarding the code structure I always wanted to make a repo which would contain the skeleton app. So here it is:

https://github.com/ArnisLielturks/Urho3D-Empty-Project

It's very much a WIP but at least is shows one of the ways how the project can be structurized.

-------------------------

techno77 | 2018-06-20 09:38:39 UTC | #7

Oh, yes! Here it is!
Thank you so much, dear Miegamicis!

-------------------------

Miegamicis | 2018-06-20 11:38:33 UTC | #8

If everything worked as expected, the output should be similar to this:
![com-|345x194](upload://uVuEeSuGEaYJQyr4zQLbnpCTxsb.gif)

-------------------------

Miegamicis | 2018-06-21 11:43:21 UTC | #9

I updated the repo with the tutorial and code samples.

-------------------------

smellymumbler | 2018-06-21 12:26:05 UTC | #10

That's really useful, thanks!

-------------------------

Miegamicis | 2018-07-02 14:08:47 UTC | #11

I have added couple of things:
1. `*.as` scripts which are placed in `Data/Mods` folder will be automatically loaded on startup.
2. Config file loading on startup from the `Data/Config/Game.json` file. File contents are available withing the app by using `GetGlobalVar` method
3. Splash screen animations
4. Loading screen animations
5. Basic scene from one of the Urho3D samples
6. Code cleanup and readme file updated to reflect all the changes

Preview from one of the earlier builds which is missing few new things from the list
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/6/6a1342a2dbc258fee7ed43736b266cb1e208779f.gif'>

-------------------------

Miegamicis | 2018-07-06 16:52:33 UTC | #12

Time for another update.

I added bunch of additional features that I think are necessary when starting new project:

* Started writing Wiki to describe all the functions and possibilities - https://github.com/ArnisLielturks/Urho3D-Empty-Project/wiki
* Added configuration file loading/saving functionality with possibility to register addtional config files that should be loaded when creating mods etc. https://github.com/ArnisLielturks/Urho3D-Empty-Project/wiki/Global-configuration

* Window manager which should take care of all application window lifecycle - built in the same way how the levels are handled. Added scoreboard window sample which is handled this way
https://github.com/ArnisLielturks/Urho3D-Empty-Project/wiki/UI-Window-management
* Started creating settings window where you could change audio, graphics and other game related settings
* Added console mod which supports new console command registering and console command handling. https://github.com/ArnisLielturks/Urho3D-Empty-Project/wiki/Console-commands

* A bunch of small fixes and improvements

-------------------------

smellymumbler | 2018-07-06 13:25:49 UTC | #13

That's really useful. I never thought about this stuff before and you made it look very easy. Thanks!

-------------------------

Miegamicis | 2018-07-06 13:45:36 UTC | #14

I've been developing my hobby projects with this engine for the last 3 years so I have coded a lot of components and even more times rewritten them because of how bad they were. This is basically just putting together the "nice" stuff of all my projects and in parallel just thinking about new stuff that I think would be useful for my future projects.

Maybe you have any ideas how this can be improved further? I'm open to any suggestions.

-------------------------

smellymumbler | 2018-07-06 17:59:04 UTC | #15

I think that a sample of graphics/sound settings screen would be crazy. Sliders and stuff. Controlling filtering, shadow quality, etc. Maybe even changing between DX and GL? That's usually very hard to do right. 

Other ideas:

* Input binding screen
* Quake-like cvars and aliases?
* Level setup screen: defining some vars before starting a scene, such as this: https://www.howtogeek.com/wp-content/uploads/2012/12/650x380xfps_trainer.png.pagespeed.gp+jp+jw+pj+js+rj+rp+rw+ri+cp+md.ic.1xsGDHPlhp.jpg

-------------------------

Miegamicis | 2018-07-06 18:24:10 UTC | #16

* Input binding - already in my to-do list, hopefully can be done in the next week or so
* Cvars - this actually is pretty simple to implement by this https://github.com/ArnisLielturks/Urho3D-Empty-Project/wiki/Console-commands
I already did something similar in one of my projects

* Level setup screen - I can take a look at this, maybe implement some sort of map dropdown before starting a level just to show how it could be done

Regarding switching between DX and GL I'm not really sure how it could be implemented, since graphics engine is chosen before building the engine itself.

-------------------------

SirNate0 | 2018-07-06 22:17:35 UTC | #17

I think you could actually configure loading DX or GL if you used a shared library and added some logic to load one version or the other (maybe). It's probably way more work than it's worth, though. If it's a real concern, my vote would be just have multiple executables.

How do you plan on doing a configurable input? And would it support joysticks and keyboard/mouse, or just one?

-------------------------

Miegamicis | 2018-07-07 07:57:50 UTC | #18

Regarding the controller inputs I think that it will be as universal as possible, I will listen to mouse/keyboard/joystick inputs and map them against something so the users themselves can decide on what kind of controller they want to play the game. But let's see how it goes.

-------------------------

smellymumbler | 2018-07-07 14:26:58 UTC | #19

Shadow quality, AA, that's also dependent on compilation options?

-------------------------

Miegamicis | 2018-07-07 17:05:25 UTC | #20

Everything else can be changed on runtime.

-------------------------

Miegamicis | 2018-07-13 18:44:03 UTC | #21

Another update:

* Added INI file reader - https://github.com/carnalis/ConfigManager
Description: https://github.com/ArnisLielturks/Urho3D-Empty-Project/wiki/Global-configuration

* Added Mouse/Keyboard/Joystick input mapping - saving mapped input in INI file
Description: https://github.com/ArnisLielturks/Urho3D-Empty-Project/wiki/Input-binding
![image|413x425](upload://6hYFfwA0Q77BfAzGhNyp73HTVZr.png)
I know, I know, the UI sucks, but it's not a priority for now.

* Mod hot reloading, when you run the game, all the mods which are inserted in Data/Mods subdirectory will be picked up automatically. If you remove it, it will be automatically unloaded.
Description: https://github.com/ArnisLielturks/Urho3D-Empty-Project/wiki/Modding-(AngelScript)

* Pause menu added in in-game level with possibility to resume game, return to menu or exit game
![image|446x272](upload://dvnc8F9hYX23bgQhPo5rR6YmXvA.jpg)

* Ability to move around the in-game level by using the keys that you configured - mouse/keyboard/joystick
Would be cool if someone could test this with different controllers since I have only 1 type of it available.

* Settings view improved a bit, configuration saving is not yet implemented! I guess that will be my next priority

* Started to work on new console just so there would be more place for the actual text
Some inspiration:
![image|345x246](upload://1tklcga7iyQ5pHfbKwM1z79nyFy.jpg)

* Added CVARS
![image|690x78](upload://tzSyzUArokE9ydD1LFu0UsJLCTe.png)
If you enter GlobalVar name directly in console it will output the actual value for it. If you enter new value after the variable name, it will automatically be replaced. It will try to cast it to the same format that it was previously.
More info here: https://github.com/ArnisLielturks/Urho3D-Empty-Project/wiki/Console-commands

If you have any more ideas, please share them!

-------------------------

smellymumbler | 2018-07-13 18:45:37 UTC | #22

Holy crap this is so amazing! :D

-------------------------

smellymumbler | 2018-07-13 18:58:14 UTC | #23

Just throwing random ideas:

* Control for mouse sensitivity, invert X/Y
* Same for joystick (left/right stick sensitivity, invert, etc)
* Field of view, brightness, gamma, for video settings
* Credits screen
* Graphics quality presets (Low, Normal, Good, Ultra, etc) which are just presets of other video configurations (enable aa, etc)
* Dynamic cvar menu: Imagine a "Game" settings tab that allows you to select a list of cvars there to display, so some game settings can be easily tweaked by the player (third/first person, help, etc)

-------------------------

Miegamicis | 2018-07-13 19:04:13 UTC | #24

Thanks for the ideas! :+1:
This should keep me busy for some time.
Added them all to my to-do list

-------------------------

smellymumbler | 2018-07-13 19:05:11 UTC | #25

I don't know if that's what you are looking for, but if you consider network to be a part of your project, then the whole Host Game/Join Game structure results in a lot of work. Done that whole thing for a game I was working on in UDK (i know...) and wow... what a boatload of work!

-------------------------

Miegamicis | 2018-07-13 19:12:05 UTC | #26

I have thought about this, I have pretty good background of the Urho3D networking system and I also have some projects that I can try to use as a base for this, but the only issue is that for those who don't want the networking part of this sample, it should be easibly removable.
I'm on vacation next week, so I guess I will have more time to think about this.

-------------------------

Bluemoon | 2018-07-14 17:13:06 UTC | #27

To be honest this is an awesome work!! Keep it up

-------------------------

smellymumbler | 2018-07-18 22:38:49 UTC | #28

Might not be related at all to what you are aiming for, but having an example for splitscreen multiplayer would be nice (the difficult part is handling 4+ inputs).

-------------------------

SirNate0 | 2018-07-19 03:47:31 UTC | #29

I don't think handling the input should actually be that hard - you just shift from a per-game controller configuration to a per-character/player one (I've also never done it, though). Unless you mean handling more than four players...

-------------------------

Miegamicis | 2018-07-19 10:44:26 UTC | #30

It isn't that difficult, the only problem here is handling all the in-game events for each of the players - seperate GUI's, health, ammo etc.

-------------------------

Miegamicis | 2018-07-23 14:07:14 UTC | #31

I succesfully created small multiplayer (splitscreen) game by using different controllers (joysticks). I'm planning to add this sample to the repo this week. I was kinda suprised that it took <1 hour to create it on top of the `Urho3D-Empty-Project`. Besides that I'm also planning to finish these things:

* Configuration saving

* Audio manager - all the ingame audio lifetime will be handled by this

* Mouse and joystick configuration tabs - sensitivity, inverted controls  etc.

Already finished:

* Graphics settings are applied when you hit `Save` button in the configuration window

* Same for audio. I added few sample sounds so you could test it out

* Credits screen added, new button in the main menu

-------------------------

smellymumbler | 2018-07-24 12:49:16 UTC | #32

That's cool! How many players did you manage to get before affecting FPS?

-------------------------

Miegamicis | 2018-07-24 13:13:38 UTC | #33

I had pretty simple scene so I was not able to test the performance

-------------------------

smellymumbler | 2018-07-30 17:30:40 UTC | #34

I don't know if you still need ideas, but couple more came to my head:

* i18n
* MOTD: fetch content from API call and render
* Framerate cap in graphics settings
* Enable/disable fullscreen
* Quake-style sure you want to quit?

-------------------------

Miegamicis | 2018-07-30 19:23:36 UTC | #35

Awesome!

Best thing about having many things in to-do list is that I can switch from task to task and it doesn't get boring. :)
Also, in the next update I will start a new thread in discoure, so we can continue the conversation there.

-------------------------

ucmRich | 2018-08-01 09:48:28 UTC | #36

@Miegamicis Thank you sooooo much for your work on this!!  It makes it so much easier for me to come back to Urho3D for some games and projects I want to start with this engine :smiley:

I just wish there was a way to get JavaScript officially into Urho3D; I would work JS miracles like I used to do for DX Studio (r.i.p)  :heart_eyes:

-------------------------

smellymumbler | 2018-08-01 13:48:28 UTC | #37

If you want JS, there's https://github.com/AtomicGameEngine/AtomicGameEngine

-------------------------

