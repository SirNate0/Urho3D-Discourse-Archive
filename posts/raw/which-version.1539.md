Redgeneral | 2017-01-02 01:08:22 UTC | #1

I am a newbie to this project - I'd like to try out Urho3D on my Raspberry pi Zero, but I am unsure which version of the download to use. I don't know the difference between static and shared, or what the v7a means. Which should I go for?

-------------------------

bukkits | 2017-01-02 01:08:22 UTC | #2

Start by downloading the [url=https://github.com/urho3d/Urho3D/archive/1.5.zip]full Urho3D 1.5 zip file[/url]. This will include both static and shared. Then use cmake, make and gcc to compile Urho3D.

I'm curious to see how it runs, maybe include some screenshots of samples if you get it to work?


EDIT: Static and shared don't matter that much when you're just trying to test things out, and there is an option in cmake to select which one you want. Those come down to development needs and preferences. If you're unsure, static will do just fine.

-------------------------

1vanK | 2017-01-02 01:08:22 UTC | #3

[quote="Redgeneral"]I am a newbie to this project - I'd like to try out Urho3D on my Raspberry pi Zero, but I am unsure which version of the download to use. I don't know the difference between static and shared, or what the v7a means. Which should I go for?[/quote]

shared: exe + dll
static: big size exe

I do not know which extensions are used it Raspberry pi Zero, but I think that the message is clear

-------------------------

Redgeneral | 2017-01-02 01:08:26 UTC | #4

I've ran the demos on my raspberry pi zero and these are my results

Pi zero settings = 1ghz, 512Mb ram, 128Mb reserved for graphics, 1024x768 screen
Urho version: Urho3D-1.5-Raspberry-Pi-SHARED

Note: although programs were launched and interacted with, interaction continued on the desktop. Moving mouse and clicking in program could trigger things on desktop, such as selecting files or launching programs from taskbar- in one demo the web browser was launched.

Note: when taking screenshots of the demos, the screenshot would capture the desktop instead. As a result I resorted to using a camera for screen shots - apologies for wonky / slightly blurred images.


The following were not tested due to no sound device or internet access
14 (Sound effects), 16 (Chat), 29 (sound synthesis)


Warning - demo 23 (Water) stops the pi - no mouse movement or keyboard input (cannot escape), does not progress beyond black screen and mouse even after 1hr of waiting - pi plug had to be pulled to restart the device


The following had geometry issues (all used same person model) but otherwise ran well:
6 (skeletal animation), 13 Ragdolls, 15 (Navigation), 18 (Character demo), 39 (crowd navigation)
[img]http://redgeneral.frogland.co.uk/urho3d/model-problems.jpg[/img]

No mouse - no interaction:
2 (hello gui), 37 (ui Drag), 40 (localization)
[img]http://redgeneral.frogland.co.uk/urho3d/interaction-problems.jpg[/img]

Slow down:
10 Render to texture
11 Physics
12 Physics stress test
17 Scene Replication
20 Huge object count - massive slow down
21 Angle script integration
22 Lua integration
27 urho 2d physics
28 urho 2D physics rope
[img]http://redgeneral.frogland.co.uk/urho3d/slow-down.jpg[/img]

No problems:
1 Hello world
3 sprites
4 static scenes
5 animating scene
7 Billboard
8 Decals
9 Multiple viewports
19 Vehicle demo
24 Urho 2D sprite
25 Urho2D particle
26 Console input
30 light animation
31 material animation
32 urho2D constrains
33 urho2D spriter animation
34 Dynamic geometry
35 signed distance field test
36 urho2d tilemap
38 scene and ui load
41 database demo
[img]http://redgeneral.frogland.co.uk/urho3d/fine-and-dandy.jpg[/img]

My interpretations
- The person model has problems either with the file or with how it is loaded
- physics is a big bottle neck - slows everything down until things come to rest, then it speeds up again
- angel script and lua script slow everything to a crawl
- Render to texture slowdown on pi
- mouse inputs continue to effect desktop / window items when urho is running

It seems a nice engine but due to the problems I don't think its ready for use on the pi

-------------------------

weitjong | 2017-01-02 01:08:26 UTC | #5

The problems are not with the game engine. They are due to samples code and the assets being used. I think you should realize the same samples are being used for the other platforms with higher hardware capabilities. In fact the physics stress test sample will bring some old desktops to their knees as well, let alone RPI. Most the problems that you just described are known problems because we don't write specific samples just for targeting RPI limited capabilities to its max.

Regarding mouse and keyboard input interference with desktop, I am really dumbfounded by this. What desktop are you talking about here? Those USB devices are supposed to be connected to the RPI board itself,  aren't they?

-------------------------

weitjong | 2017-01-02 01:08:26 UTC | #6

I think I have assumed too much. I thought you know already that our RPI port does not rely on X11. You should kill X before running the samples or configure your RPI to boot up in text mode directly.

-------------------------

Redgeneral | 2017-01-02 01:08:26 UTC | #7

By desktop I mean the desktop of the raspberry pi operating system Raspbian - for example I run the decal demo and every time I click to add a decal onto the object by left mouse click, it also clicks stuff on the Raspbian desktop depending on where it thinks the mouse is. So I have found that during the demo the mouse has launched programs, selected files etc. 

I didn't know that the x11 was not required - I will look into killing X and trying again.


I do realise the raspberry pi has far less capabilities, however I was asked for screenshots of how it ran and so I tested each demo to show just that. I pointed out which features are not feasible for the pi (physics, and the lua/angel scripting engines) and which features actually worked. 
The only bugs were the person model, the gui demos, and the strange behaviour regarding the desktop.


I think I should have been clearer with the last sentence of my previous post - the lua scripting was one of the things that drew me to this engine, but as that has problems on the pi, I may just choose to stick to a Windows machine with Urho.

-------------------------

weitjong | 2017-01-02 01:08:26 UTC | #8

Once you have killed X then Urho3D game engine can utilise all the CPU and GPU computing power for its own use, so the performance should be better than your earlier test result. The problem with Jack (naked man) having too many bones for RPI to handle has been asked a few times in the forums. As for Lua or LuaJIT, I was surprised initially myself that they work at all. Again, the problem is with what you want the scripts to do on Pi. The problem is not with the scripting integration itself. I guess one needs to manage the expectation when working with Pi.

-------------------------

