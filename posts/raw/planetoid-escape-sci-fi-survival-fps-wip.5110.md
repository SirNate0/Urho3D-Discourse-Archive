QBkGames | 2019-04-21 01:20:43 UTC | #1

After almost 2 years of work, I've finally completed what I think is a playable version of the 3D game, Planetoid Escape (I'm yet to come up with a better name 🙂).
Although only about half of my vision for the game is complete, the survival aspect is mostly implemented and also basic crafting. So, it should be possible to survive long enough to craft enough things to become self sufficient.

Setting
*After your interstellar ship exploded, you have crash landed in an escape pod, on a nearby desert planetoid. To survive you have to find food, oxygen, the planetoid atmosphere not being suitable for you to breathe and energy to power various devices which can assist you in your survival attempt.*

![Screenshot_0010|690x388](upload://xPOE3WBLqohjz7SIjkg4INrClFW.jpeg) 
![Screenshot_0011|690x388](upload://b3CSz4IayyurZmMyt98KGS6YR1K.jpeg) 
![Screenshot_0013|690x388](upload://dPG3LE9pHyUkUT2DlO0JcAa6hNs.jpeg) 

If anyone is interested in giving it a try, it can be downloaded from:
http://www.qbkgames.com/Dev/PlanetoidEscape/

Any feedback is welcome!

-------------------------

GodMan | 2019-04-20 17:03:23 UTC | #2

Looks nice good job.

-------------------------

QBkGames | 2019-04-21 01:15:38 UTC | #3

Thanks. It definitely needs more polish, but for now the focus is on functionality to make sure I have a game first.

-------------------------

QBkGames | 2019-04-21 01:19:08 UTC | #4

My biggest problem right now is actually physics, which for some reason takes a long time to update, even though I only have a handful of dynamic bodies. It seems that the update time is also affected by the number of static bodies (which there are a lot of and I need even more). This does not make sense to me, as I thought having a space partition algorithm (such as an oct-tree) would allow for virtually unlimited objects in the world.

-------------------------

Modanung | 2019-04-21 07:13:05 UTC | #5

Looks nice. Any chances of a Linux version?

Oh, and I know it's just the default sky, but... it seems a bit cloudy for such an arid environment. ;P

-------------------------

QBkGames | 2019-04-21 09:05:57 UTC | #6

The final version will definitely be on Linux. I was going to postpone porting to Linux because I only have limited experience with it (installed it once a few years ago and tried for a few hours) and never actually programmed on it, so I'm guessing a steep learning curve!? Does the game maybe run on WINE (for now)?

BTW, what would be a good Linux distro for game development? I'm thinking PopOS, but I'm open to suggestions. Also what's a good IDE in Linux for someone used to Visual Studio?

The sky is definitely too cloudy :slight_smile:, but it will have to wait for the polish phase (later on). My next step is to get some creatures in so you have something fun to shoot at :grin:.

-------------------------

Leith | 2019-04-21 13:27:57 UTC | #7

I use Linux Mint, and recommend it. You get firefox WHILE it installs, so you can ask questions if you need to. I dual-boot Windows 10, but rarely use it. My dad is 70 odd, he runs Linux Mint too, and when he needs Windows, he runs VirtualBox on Linux, with an old image of Windows 7.
Linux boots fast, and virtual windows on linux boots hell fast. He's happy with the workaround for the few windows apps that won't play nice under Wine.

-------------------------

GodMan | 2019-04-21 17:21:26 UTC | #8

Here are some pre-made skyboxes with previews. http://www.custommapmakers.org/skyboxes.php

-------------------------

Modanung | 2019-04-22 08:58:25 UTC | #9

I also run Linux Mint (with Xfce). For coding C++ I've basically always used QtCreator.
Check out the [LucKey Toolset](https://LucKeyProductions.itch.io) for a list of other open source software I use.

As browser I can recommend [IceCat](https://spyware.neocities.org/articles/icecat.html), btw... and **[sage](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4003706/#!po=1.02041)** as a dietary supplement and mouthwash ingredient. :grin:

-------------------------

Miegamicis | 2019-04-22 14:47:28 UTC | #10

Tested the game, really enjoyed the idea.

Also here are some ideas how to further improve it:

* Sprinting, walking over the map was slow and I felt that this might help a lot. You could maybe decrease energy faster while the player is sprinting
* Intro tutorial - I spent a lot of time at the beggining to understand what I'm supposed to do. After pressing every button I found out that the F1 button opens up a tutorial window which in short explains how the game works
* More bioms - map is large, but most of it is plain desert. Need to spent a lot of time walking around and in most cases I forgot where my pod was.


I was frustrated that I couldn't find any batteries, hoped to find them in the nearest crash sites but without any luck. All the tools that I found had empty batteries so I was unable to collect any materials which I guess are required to build everything.

-------------------------

QBkGames | 2019-04-23 04:28:26 UTC | #11

Thanks a lot for the feedback.

Regarding your points:

* You are actually sprinting :stuck_out_tongue:, you have to hold Shift to walk slow. But, I agree moving is a bit slow (for now), but that's only because the game in incomplete. I have in plan vehicles you can drive (there should actually be a couple or Rovers somewhere on the map which may need repair before you can drive them). I also want to have creatures roaming around which will make your journey more eventful :smile:.
* I am planing to have a hint system in the game, however it's not trivial so I left it for later. There are some hints on the download page which tell you about [F1] and other critical starting info (which will make its way into the hint system eventually).
* There is a device called the Tracker Visor which you equip into your suit and it shows you where your pod is. It should be found either in the container inside the pod or in the nearest debris field, which you find if you walk in a straight line as you exit the pod.

As far as I was able to test the game, there should be batteries (power cells) and everything you need around, but you do have to explore the map quite a bit to find what you need. The game is a bit slow at the moment because there are no creatures to fight so it is more of a puzzle game (figuring out how to survive and use limited resources) than an action game, but I do want to have more action in it.

-------------------------

QBkGames | 2019-04-27 22:38:48 UTC | #12

I've updated to version 0.5.5, which fixes quite a few bugs, and adds an optimisation to reduce the physics update time so that it can now run at 60 fps on my PC. On the downside, the game takes longer to start up, but I think the benefits are worth it.

Also, if you have played the previous version, it is recommended that you start a new game with the new version as the save game file format has been updated. The 'hack' to start a new game is to simply delete the file <i>"Documents\QBk\Planetoid Escape\SaveGame.peg"</i> before running the game.

Any feedback is welcome at any time.

-------------------------

QBkGames | 2019-04-28 03:13:00 UTC | #13

Posted a game play tutorial video.
**Warning:** Potential spoilers for those who like to explore and discover new things on their own.

https://youtu.be/1hs8oRT3mlo

-------------------------

QBkGames | 2019-07-02 09:23:16 UTC | #14

Version 0.6.0 has just been released. It has the following features:
* Assemble vehicles out of individual parts
* More content: new devices and other objects and of course, vehicles and parts
* Major balancing improvements to make progress faster and more satisfying
* Sprinting ability to move faster (as per [Miegamicis] and other people's recommendation)
* Numerous bug fixes and performance improvements

If anyone wants to try it out, the download link is the same:
http://www.qbkgames.com/Dev/PlanetoidEscape/
Please make sure you **read the hints on the download page** before you play.
All feedback welcome.

![Screenshot_Vehicle|690x388](upload://a5ha4nozLSo2hT2fL78h99jwkyN.jpeg)

-------------------------

QBkGames | 2019-07-23 04:37:25 UTC | #15

I've recently discovered that the code that creates the vehicles was not called correctly, therefore there are no vehicles in the level, only the spare parts.
I've now fixed the issue and released version 0.6.2.

You have to start a new game by simply deleting the file *“Documents\QBk\Planetoid Escape\SaveGame.peg”* before running the game, to take advantage of the bug fixes and a few minor extra features added.

-------------------------

QBkGames | 2019-11-21 06:22:29 UTC | #16

Version 0.7 is now released. It features:
* Creatures roaming the landscape and attacking you if you get too close
* More content, and some old content becoming more relevant with the creatures around
* Sleep mechanic
* As usual, numerous bug fixes and performance improvements

If you want to try it out, same [download link](http://www.qbkgames.com/Dev/PlanetoidEscape/), and **read the hints on the download page**!

All feedback welcome, especially constructive criticism (which is the most useful for future improvements).

![Screenshot_Creatures|690x388](upload://laUJw8PSD47quf6zTENESeW0nef.jpeg)

-------------------------

QBkGames | 2019-11-21 06:27:25 UTC | #17

Now that some areas of the game world are densely populated and there are creatures everywhere, I'm also interested in the game performance on mid-low level machines. For people trying out the game, can you please post some statistics, i.e. you machine specs and game performance stats.

You can use F9 in-game to toggle the profiler (hit twice to show all levels) and F5 to take screenshots (saved to "Documents\QBk\Planetoid Escape\Screenshots"). You assistance is greatly appreciated.

-------------------------

Asimov500 | 2019-12-24 10:55:17 UTC | #18

@QBkGames
I tried out the game. The first thing I noticed was that the sound effect of the feet sounded like a horse trotting. Really on sand you wouldn't really hear it that loud. Also the sound effect kept pausing even though I was still moving. I am running it on windows 10.

However I like the idea of the game. eg building stuff to stay alive.
I did like the fact that when he jumped you could tell that the gravity was low as he stayed in the air for a long time. I would have thought that the survival suit would have some kind of radar so that you can find your way back to your craft, like in the game Tau ceti.

I didn't play it long enough, but an interesting thing that could happen is that it could get dark and you would need some kind of light in your suit, and it would obvioiusly drain your energy faster.

I think with some tweaks this could be a good game.

-------------------------

QBkGames | 2019-12-25 02:02:00 UTC | #19

Thanks for the feedback, I really appreciate it.

I also noticed some problems with the sound sometimes, but I'm not yet sure what it is. The quality of the sound effects may not be the best as I picked what I had handy, but will get improved in the polish phase.

If you keep walking in a straight line as you exit your Escape Pod, you find a debris field where you can find all kind of useful equipment, including a Tracker device, which shows the location of your Escape Pod and also a Flashlight, both of which can be equipped into your suit and need a Power Cell (battery) to operate, which gets drained over time and needs recharging. Also the Flashlight can be upgraded to a more powerful model using the Synthesizer, but you need to find the Blueprint for the upgrade.

The game already contains quite a number of devices and appliances you can find or craft that help your survival and act as a level up of sorts, but you do need to wander around a bit to find stuff and the further you go the more advanced equipment you find.

I'm currently working on a hint system to let the player know what to do, as that seems to be the biggest problem with the game at the moment. Although there is a lot of content and functionality in the game, the player does not know how to find and use it.

With a lot of tweaks, I'm hoping it will end up being a good game :).

-------------------------

QBkGames | 2019-12-25 01:59:41 UTC | #20

BTY, if you don't mind me asking, what machine do you have and what is the game performance like on it? F9 toggles the profiler.

-------------------------

Asimov500 | 2019-12-25 02:13:24 UTC | #21

It is hard to make out what the figures mean in the profiler so I have saved a screenshot. I am running this on a laptop but it is quite a powerful laptop as I am a 3D modeller. Lenovo i7 32gb ram quadro 1000 graphics card.

When you jump he stays in the air for a while assuming this is low gravity, but when he walks the steps are small. If you see the moon landing footage you will notice that each step in low gravity is a longer step. So I would expect the steps to move me slow but a further distance if you know what I mean. It takes a very long time to get to where you are going. If you compare this to movement in Unity I think it would be better if it was speeded up a little.

I do like the idea of this though. Would be cool if your capsule was half buried as well and a trail of scorch marks out of the back, something like in Halo.

Here is a screenshot of the profiler. I am not sure what the figures mean.
![performance|509x491](upload://7bLF4HDMSE7lOoiOWHPs37kHWMk.jpeg)

-------------------------

QBkGames | 2019-12-25 04:54:39 UTC | #22

Thanks for the new feedback.

That figure on the profiler means that the ApplyFrameLimit calculation is wrong :stuck_out_tongue:  and as a result, it shows the game running at 5 fps which for your machine is definitely wrong, it must be doing 60 fps without braking a sweat.

You can move faster (sprint) by holding down Shift, also you can move slower by holding down Ctrl (it is useful in some cases). Note that sprinting uses up Energy and Oxygen at a much higher rate, it's really meant to run away from creatures that attack you.
Also, the relatively slow movement over larger distance is to encourage the player to build vehicles which then let you move faster (and carry more stuff).

There is also a build-in manual / "Survival Guide", available using [F1] key in the game, which describe all game mechanics that are currently implemented.

Also, thanks for the suggestion of the half buried capsule and trail, I'll keep it in mind for the polish phase (to be done later on after I'm happy with the game play functionality).

-------------------------

QBkGames | 2020-01-08 22:40:09 UTC | #23

Just released version 0.75, a minor version focused mostly on aesthetics and bug fixes.
Includes: stary sky at night, more glowing things, more particle effects, etc. Also a basic (timer based) hint system.

![Bloom at Night|690x388](upload://9YWKS0eqrz2ss0xQAMAEmlsSQdu.jpeg)

-------------------------

Miegamicis | 2020-01-08 10:17:45 UTC | #24

Are you planning adding the support for Linux?

P.S. I can help you with CI/CD to automate the builds if needed + auto publish windows/linux builds on https://itch.io/

-------------------------

QBkGames | 2020-01-08 22:43:08 UTC | #25

There will definitely be a Linux version, but because of my limited experience with Linux I was going to leave it for later until I've developed the game a bit further.

I appreciate all the help I can get :slight_smile:. What is CI/CD and how would you go about automating builds and auto publish? Thanks.

-------------------------

Miegamicis | 2020-01-09 14:29:51 UTC | #26

CI/CD - Continuous integration/Continious deployment(or delivery).

Don't know what VC tool you use, but if it's Gitlab, here's a sample snippet: https://gitlab.com/luckeyproductions/manawarg/blob/master/.gitlab-ci.yml

It uses Gitlab's built-in CI tools

If you use Github or Bitbucket, send me a PM, will send you out a configuration for CircleCI service since I don't have any open source projects which uses it.

-------------------------

