TheTophatDemon | 2020-01-07 21:11:05 UTC | #1

Last year, I finished a project using Urho3D, a game called [War Priest](https://discourse.urho3d.io/t/war-priest-is-finally-here/5483).
I had said that I would write about my experience of creating the game using Urho3D.

I primarily relied on C++ and custom components, and I occasionally used AngelCode scripting for cutscenes and prototyping. I built level geometry by hand in blender and then placed placeholder entities in the scene editor for the game code to replace later. Making the levels was by far the most time-consuming process, and I often found it frustrating to fiddle around with individual vertices and faces, and to try and make good-looking textures that could tile well. If I were to do it over again, I would probably have tried to find a way to use a Quake editor, like TrenchBroom, or to make it tile-based.

When this project first got underway, I was expecting to finish it in one Summer. However, it ended up taking me multiple years due to a packed school schedule and changing home life. Though I enjoyed the game itself, during the long development cycle, I often felt impatient to finish it so that I could work on new ideas. This regrettably led me to ignore seeking help from the forum and reporting bugs that I found with the engine and editor, because I did not want to halt my progress to wait on replies or recreate bugs in new projects (so that people wouldn't have to compile the entire game themselves).

**Particular aspects of Urho3D**

*Performance* - I was very impressed by how well the game ran. The graphics were simple, sure, but I was very used to running into performance problems early on with such graphics using other engines. It could handle a screen full of particle emitting projectiles and animated enemies while keeping a silky smooth 60FPS (and often 200FPS). I made simple optimizations, like AI LOD, but I do believe that what Urho3D does under the hood has had a significant contribution to the game's overall performance. However, in debug mode, the game would sometimes slow to a crawl when there was a lot of physics stuff going on.

*Entity Component System* - ECS was pretty new to me when I started the project, and I quickly fell in love with it. I found it especially useful for special effects and prototyping. I found that Urho3D's implementation was a bit awkward, however. Having to register every custom component and to use weird macros was inconvenient, but I suppose it was necessary in order to make things work with the Scripting engine. For creating custom components and syncing them with the scripting engine, I found the documentation to be vague and incomplete, and I ended up mostly mimicking example code. I also didn't like how I couldn't seem to have my own constructor parameters for custom components.

*Scene Editor* - The scene editor was quite a nice feature. Being able to mess with all of the engine's features, run scripts to perform automated editing tasks, and edit materials and effects in real time, really streamlined the process of learning the engine and making levels. However, I also ran into annoying bugs pretty much every time I used it. Just to name a few: 
-Every time I opened the editor, I would not be able to edit any text fields until I tabbed out of it and refocused the window.
-The editor would sometimes crash when loading one scene after having a different one open, for no apparent reason.
-When saving a UI layout, certain Text nodes would not have their sizes saved, causing them to collapse into nothingness when the layout was opened again.
I was also disappointed that I couldn't drag UI elements to move them. It made repositioning them a pain in the neck.

*Compiling* - I almost always have trouble compiling other peoples' C++ projects, especially when something like CMake is involved. Though the engine was very large and incorporated many libraries, I was able to use CMake to generate projects without that much fuss. This may be a perk of the engine's design, or just due to me having more experience.

*Physics* - Physics engines are always difficult to work with, so it seems. Though Urho3D's Bullet implementation got the job done well enough, I still ran into problems with my character controllers often. There was plenty of random jittering, clipping through walls, and missed collision events that I had to hack around. The causes here are complex. It could be something wrong with Bullet, or the implementation of Bullet, or how I set the velocities of my actors directly in order to have full control of their movement, or how each game map was just one big triangle mesh. I have since seen better implementations of kinematic character controllers, but they seem to rely on using Bullet directly, which is less than ideal. Nevertheless, I think being able to have a precise and reliable character controller is quite important for most games, and a lot of engines I've used don't seem to have very elegant solutions for that.

*Blender Exporter* - The blender exporter made the asset pipeline a lot more convenient and worked reliably, though I noticed that it would mess up per-face vertex coloring. It would be quite nice to have it updated for Blender 2.8 (within the next 5 years, at least)!

*Graphics Pipeline* - This engine has a unique way of rendering that is very flexible. Though it was a little hard to wrap my head around, and made for a bunch of .xml files, it allowed me to avoid a lot of redundant shader code and allowed me to make quick changes to how the game looked. Quite nice!

*Profiler* - Having an in-built profiler was quite the luxury, and now I want one in all of my projects!
I did find it a little hard to read, though. There's quite a bit of text, and it changed often, so I often had to take screenshots to really see what was going on. I generally found that the physics engine and raycasting took the most processing power. Have a look!

![performance_robelocks|690x388, 100%](upload://4Ms4DNQHFvPwZ13R60l606NyDOl.png) 

That's pretty much all I have to say about that. Though I've made quite a few criticisms, I think that Urho3D is a pretty good engine overall. I had spent a lot of time trying out different engines (that weren't immensely popular like Unity), but I would always run into some missing or broken feature that would impede my project, but Urho3D is quite feature complete.

As for the game itself, I am satisfied with how it turned out, even though it is rather short for my liking. Next time I get into such a large project, though, I will need to make sure I'm really invested into the idea and put more time into planning the code-base, and finding more streamlined content creation pipelines.

-------------------------

suppagam | 2020-01-07 22:18:37 UTC | #2

Urho's performance is the most important feature of the engine. It's impressive how well it handles anything you throw at it. The PBR implementation is the only slow thing, so as long as you stick to the standard rendering path, everything is smooth and fast. 

I'm working on a Doom-like with a huge amount of monsters and the engine doesn't even flinch. It's a wonderful piece of architecture.

-------------------------

QBkGames | 2020-01-08 01:24:38 UTC | #3

Another advantage of Urho is that the code base is not overwhelmingly huge (like Unreal or others), so a solo developer stands a change of looking at it, understanding enough to be able to modify and customize it if necessary.

-------------------------

Sinoid | 2020-01-08 01:28:35 UTC | #4

[quote="TheTophatDemon, post:1, topic:5809"]
I generally found that the physics engine and raycasting took the most processing power. Have a look!
[/quote]

**Tip**: in Bullet there's [little difference between a raycast and a swept sphere cast](https://pybullet.org/Bullet/phpBB3/viewtopic.php?t=3716). They both work off the same old-school `extents+radius` traces like Quake. So if the volume of a sphere is more meaningful than an infinitely narrow ray it's little extra cost (just whatever API cruft).

Doing lots of raycasts when one convex-cast will suffice is a silly thing you see too often.

[quote="TheTophatDemon, post:1, topic:5809"]
Nevertheless, I think being able to have a precise and reliable character controller is quite important for most games, and a lot of engines I’ve used don’t seem to have very elegant solutions for that.
[/quote]

It's *"hiding in plain sight"* since you can handle character locomotion almost identically to a Quake clone (well, everyone uses the same general approach) with sweep queries. Only the trace changes to accommodate Bullet's queries.

Never thought of it as something missing. Is it really that needed?

-------------------------

Modanung | 2020-01-08 15:57:48 UTC | #5

Concerning the editor, I'll repeat @cadaver's words once again...
 [quote="cadaver, post:2, topic:2407"]
My view is that the existing editor is somewhere halfway between a complex script API usage example, and a production-usable editor. [...] Probably the ideal would be, if you wanted to improve the user experience at the same time, would be to use an actual native UI toolkit in the editor and rewrite it in C++. [...] Perhaps the editor could be another library, which adds functionality into Urho base.
[/quote]
[ManaWarg](https://discourse.urho3d.io/t/manawarg/5403) started inspired by those words, but needs work (or has room to apply your vision to, is another way to look at it).
https://luckeyproductions.itch.io/manawarg

-------------------------

GodMan | 2020-01-11 17:33:00 UTC | #6

What do you use to handle ai pathfinding? Do you use the built in navigation mesh options? Just Curious how others handle this.

-------------------------

