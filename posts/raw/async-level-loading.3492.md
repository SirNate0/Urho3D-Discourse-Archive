Lumak | 2018-04-27 01:46:29 UTC | #1

This pertains to 3D levels, not 2D.

repo: https://github.com/Lumak/Urho3D-AsyncLevelLoad

Below is a simple async level loading/transition vid.

*Replaced video to better demonstrate level loading/off-loading.
https://youtu.be/m8rSFHBdSKA

-------------------------

johnnycable | 2017-08-26 14:17:40 UTC | #2

Not yet started. I guess red lines are tiles/levels to get in as your character moves...
So you cast a limited ray with some radius, get some list of asset and fetch to a background loader?
I'm still not getting if zones are purely visual or are set up into a level subdivision... like
octree/zone/level/tile/character...

-------------------------

monkeyface | 2017-08-26 14:40:54 UTC | #3

What exactly is it loading? Looks like there is already stuff in the green zone before you enter...

-------------------------

Lumak | 2017-08-26 18:08:29 UTC | #4

What you see in the video is a two-level system, meaning you'll have two levels loaded at any given time. A level consists of a large white-ground tile, two load-triggers (green transparent boxes) to load the next and previous level, and misc. render objects. Obviously, you want to make level-loading inconspicuous in a real game but for demo purpose they pop in as you move through triggers.

Here's a pic of a single level:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/2471831fa111514892d9c46d0dde2dee8e901325.jpg[/img]

My current level-loading doesn't load any new resources, and I'm in the process of changing that.

*Replaced the orig video to better demonstrate level loading/off-loading.

-------------------------

johnnycable | 2017-08-26 19:44:06 UTC | #5

That means you load level in a step-by-step fashion? No object pooling?

-------------------------

Lumak | 2017-08-26 20:27:28 UTC | #6

The whole purpose of async loading is to avoid object/resource pooling (have all your assets loaded in memory) and only load levels that you need as the player progresses through the game.

-------------------------

Lumak | 2017-08-26 20:32:39 UTC | #7

Damn, I'm already done with this implementation which also includes the old terrain background loader that I had to dig up. So, collaboration offer is officially over and closing this thread.

Hmm, how do you close a thread.

-------------------------

Modanung | 2017-08-26 20:38:12 UTC | #8

[quote="Lumak, post:7, topic:3492"]
Hmm, how do you close a thread.
[/quote]

_Close topic_ under topic admin actions, the wrench in the top right.

-------------------------

Lumak | 2017-08-26 20:39:54 UTC | #9

ok Thank you. **20 chars**

-------------------------

