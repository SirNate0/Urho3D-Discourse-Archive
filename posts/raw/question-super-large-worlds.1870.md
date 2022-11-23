HeadClot | 2017-01-02 01:10:57 UTC | #1

Hey everyone,
So I have been digging around in the Urho3d wiki and I happen to stumble upon [url=https://github.com/urho3d/Urho3D/wiki/Super%20Large%20Worlds]this article[/url] about "super large worlds". Basically I am super interested in Super large worlds for my own project later down the line.

Anyway my question -
Are super large worlds akin to space engineers (or otherwise) currently supported by Urho3d at the moment?

Thank you for your time,
HeadClot

-------------------------

cadaver | 2017-01-02 01:10:58 UTC | #2

Urho3D uses 32bit floats for all scene and rendering maths, so you will run into float precision issues.

There is not any inbuilt support code, but you're free to use whatever tricks (like different scaled objects, or "recentering" the scene so that camera is always near origin) in your application code.

-------------------------

HeadClot | 2017-01-02 01:10:58 UTC | #3

[quote="cadaver"]Urho3D uses 32bit floats for all scene and rendering maths, so you will run into float precision issues.

There is not any inbuilt support code, but you're free to use whatever tricks (like different scaled objects, or "recentering" the scene so that camera is always near origin) in your application code.[/quote]

Hey thank you for the reply - It really means allot and thanks for the clarification.

PS. I am super tired right now and If anything comes out weird you know why.

- HeadClot

-------------------------

gawag | 2017-01-02 01:11:02 UTC | #4

The basic idea of the Super Large Worlds as described by the SpaceEngineers guys or as described a bit differently in my article is too avoid floating point precision problems by either recentering or by simulating more or less independent parts of the world in "own worlds" with own center points. These "worlds" can be virtually offseted to feel like one giant world (you could think of invisible loading zones that move the player and other objects to different worlds).

I'm not sure how independent physics worlds can be simulated by Urho as I haven't tried that. Maybe by having multiple Scenes or Physics Worlds or by using Bullet directly?
[urho3d.github.io/documentation/1 ... scene.html](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_scene.html)
[urho3d.github.io/documentation/1 ... world.html](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_physics_world.html)

The other thing is the graphical side: This should be relatively simple by using nodes, dynamically loading and unloading them and moving them to keep the player in the centered "chunk".

-------------------------

Shylon | 2017-01-02 01:11:05 UTC | #5

As an IDEA, I believe to reach the infinite world, we should think differently, or more specifically, REVERSE thinking, suppose we have a 3d platformer, we do not move our character forward (to right), just play its animation, instead we move whole world to left (however for heavy static scene it may cause bad performance), we load (asynch) patches of world when last world was reached to its end, our character is in position 0 0 0, so all calculation should be reversed like other entities move, like a hamester running inside circle but placing world from file.

I do not remember exactly, but OpenGL use this kind of algorithm, it is matrix stuffs, so my be a good mathematics formula solve this problem.

this scenario can apply also to whole open-world with different worlds chunks.

-------------------------

codingmonkey | 2017-01-02 01:11:06 UTC | #6

>so my be a good mathematics formula solve this problem.
To doing rendering objects on far distances, may helps tech called : Reversed Depth Buffer
it' allow draw large world chunks over 50km (I suppose if value = 1.0 is - 1 meter) without Z-buffer issues.
maybe it's may be used by Urho as default general approach. I guess needed do some fix for camera.frustrum checks and so on.

-------------------------

gawag | 2017-01-02 01:11:07 UTC | #7

It's less about depth buffer issues and more about general floating point imprecision with high numbers. Like problems with positions (stuttering) or the physics. There was a thread here with some with planets and the ones at really high positions disappearing depending on the camera position and angle. That looked like floating point imprecision due to him having really high positions.

About moving the world instead of the player: could work but be complicated as other things are moving as well and that relative to a moving world center. This has to be taken into account and makes things way more complicated and slower due to all the additional calculations. Also the physics engine would have to be modified as well.
My idea was kinda similar though and should make this way easier with a similar effect: The world is moved chunk-wise to keep the player always in a position close to the center. Moves would be only done when the player leaves the center chunk. By having every chunk in the same Node, moving this Node should move the whole chunk without problems.

-------------------------

Shylon | 2017-01-02 01:11:07 UTC | #8

Yeh, physics should changed, but I am sure if someone who good at math and have time, would find a way to improve performance or even some of the current physics formula be useless then. there should be a connection somewhere between physics and whole worlds movements.

-------------------------

gawag | 2017-01-02 01:11:07 UTC | #9

[quote="Shylon"]Yeh, physics should changed, but I am sure if someone who good at math and have time, would find a way to improve performance or even some of the current physics formula be useless then. there should be a connection somewhere between physics and whole worlds movements.[/quote]
Yes it should be possible. But I'm quite sure that the necessary calculations are more expensive as with the normal non-moving world or with the "sometimes-moved world" in my idea or as used by SpaceEngineers. The performance loss may be not that high though and may be ok depending on the case.

-------------------------

AReichl | 2017-01-02 01:11:08 UTC | #10

I think we all would appreciate a "build in" mechanism in Urho3D for shifting the world origin
( in every forum of every engine this topic pops up from time to time, and the answer is always
the same: "just do it right" and always without sample or even a piece of code to get started ).

If i remember right, Bullet has a function to reposition the center of the physics world, so maybe
the "connection" between Urho3D and Physics is not THAT complicated.

Ogre for example has a parameter for the camera to keep it in center and move / rotate everything
around it.

-------------------------

cadaver | 2017-01-02 01:11:08 UTC | #11

My opinion is that the engine shouldn't have built-in additional code for taking account a "world offset", because that is a penalty for all coordinate calculations and a memory access strain, whether you need it or not. And it could still be subject to float inaccuracy.

The exact solution depends on how you are structuring the game world. For example, if you have loadable / unloadable world chunks, they would each likely be under their own root nodes. You would move these nodes as the player crosses from one chunk to another.

The lack of concrete source code may be due to people just talking without having actually implemented a large world game, but that should be allowed I think :slight_smile:

-------------------------

AReichl | 2017-01-02 01:11:09 UTC | #12

> My opinion is that the engine shouldn't have built-in additional code for taking account a "world offset" ...
I don't agree, but you are the boss.
This "feature" is not only used in space games/simulations, but even on "medium" sized maps.

> because that is a penalty for all coordinate calculations and a memory access strain ...
Calculations have to be done all the time - that's what a scenegraph is for.
And let's be honest - if i have 97 FPS or "only" 83, who cares? I can be angry about it for some months,
but in that time there are new computers with 5 times the speed.

> whether you need it or not.
It does not ALWAYS have to be active - only when the user WANTS it, and then he will try to implement
something anyway, which will never be as good or elegant as your own solution.

> And it could still be subject to float inaccuracy.
Yes, but around the camera everything looks fine.

Sorry to mention Ogre again, but i got this idea from there. They have an additional function for the
scene manager ( setCameraRelativeRendering(true or false) ) which does exactly that.

-------------------------

1vanK | 2017-01-02 01:11:09 UTC | #13

I agree, it is very useful feature, but personally, I have not the skill to do something like this :)

-------------------------

cadaver | 2017-01-02 01:11:09 UTC | #14

When you add functionality to the scene nodes which touches the "hot path" (accessing transform matrices) you will already get a performance hit even from accessing and comparing the flag "is the offset enabled or disabled". In which case it could even be better to just calculate it always without checking first. Furthermore, because it's likely the memory access and not the math which causes the greatest perf. hit, it's not something that's much helped by faster processors. That's why you'd want to keep the scene graph and rendering hot path operations as simple as possible.

-------------------------

1vanK | 2017-01-02 01:11:09 UTC | #15

Why calculate the offset often? Just recalculate postions when player goes away from the center at some distance

-------------------------

gawag | 2017-01-02 01:11:10 UTC | #16

[quote="AReichl"]
> My opinion is that the engine shouldn't have built-in additional code for taking account a "world offset" ...
I don't agree, but you are the boss.
This "feature" is not only used in space games/simulations, but even on "medium" sized maps.

> because that is a penalty for all coordinate calculations and a memory access strain ...
Calculations have to be done all the time - that's what a scenegraph is for.
And let's be honest - if i have 97 FPS or "only" 83, who cares? I can be angry about it for some months,
but in that time there are new computers with 5 times the speed.
[/quote]
Is that a joke?
One of the main principles of C++ is: Don't pay for what you don't need. Your thinking created Java and all those idiots saying "yeah modern computer are fast enough". Bullshit! Look at all those slow application, even those who don't calculate anything are slow and memory intense as fuck due to that philosophy. Look at Skype for example, that thing uses like 1GB of RAM, uses constantly ~10% CPU and has to be restart like once a day due to no longer working properly due to all the lag it's generating. And that's just an instant messenger with telephony!

I don't know how big the FPS impact would be but you want all the performance you can get. Look at those VR devices that require >= 90 FPS with more than FullHD. The stuff they can render with that FPS boundary is years behind compared to normal games that are happy with 40 FPS on 1080p or 30 FPS on 720p often still used on the current consoles like the PS4.

The only thing possible close to your idea would be to introduce a new build flag that adds this feature via #ifdef's so that it doesn't slow down users who don't use it. But it's still to restricted as it only fixes rendering issues and not also the other issues that a chunk based approach would fix.

[quote="AReichl"]
> And it could still be subject to float inaccuracy.
Yes, but around the camera everything looks fine.

Sorry to mention Ogre again, but i got this idea from there. They have an additional function for the
scene manager ( setCameraRelativeRendering(true or false) ) which does exactly that.[/quote]

It's not just about rendering but also about other calculations like physics calculations. Image a ball rolling through a room 10km away from the player. Oh it clipped through the floor! So bad!
Or walking NPCs who clip through stuff and get stuck or whatever. Or general movement error even without physics. 

[quote="1vanK"]Why calculate the offset often? Just recalculate postions when player goes away from the center at some distance[/quote]

That's exactly the chunk based approach already mentioned and that can be easily done on your own without slowing everyone down. Connect to one of the update events, check if the player is still close enough to the center or if your chunks have to be moved so that the player is again close to the center. Chunks further away are unloaded and if necessary calculated independently like in some parallel world with it's own center as the SpaceEngineers guys seem to be doing.

I think it's not really worth the additional maintenance cost seeing that it is a mediocre solution anyway. Unless I'm missing something.

See the Space Engineers article if you haven't: [blog.marekrosa.org/2014/12/space ... ds_17.html](http://blog.marekrosa.org/2014/12/space-engineers-super-large-worlds_17.html)
That's a multiplayer, physical based, spaceship and -station building game with harvestable asteroid and planets that can also be digged into. Think of objects lying in you base on the moon, you fly to a different planet many miles away (I think they are typically a few hundred miles apart) and the objects should better not jump around and clip into machines due to imprecision.

Also the solution is quite custom anyway. Some may get away with completely unloading stuff far away. Others may have to keep calculating stuff like machines processing stuff or plants growing. Others may have to keep actual physic running or want to have screens that show stuff happening in places super far away.

-------------------------

Enhex | 2017-01-02 01:11:10 UTC | #17

@AReichl: It's a feature only useful with very specific applications, and has a significant overhead. It doesn't belong to the core of the engine, it's a higher level system which needs to be built on top of it.
It may be possible to implement it as an external addon library.

-------------------------

1vanK | 2017-01-02 01:11:10 UTC | #18

Gawag, is there a pause/freeze in Space Engineers, when chunks of world is loading? Or loading happens in another thread? As far as I know in Urho possible to modify scene only in main thread

-------------------------

1vanK | 2017-01-02 01:11:10 UTC | #19

Or we need some method for rendering two scenes as a whole when camera around of scene border

-------------------------

1vanK | 2017-01-02 01:11:10 UTC | #20

By the way Unity has function [docs.unity3d.com/ScriptReference ... Async.html](http://docs.unity3d.com/ScriptReference/Application.LoadLevelAdditiveAsync.html)

EDIT: In unreal [docs.unrealengine.com/latest/INT ... Streaming/](http://docs.unrealengine.com/latest/INT/Engine/LevelStreaming/)

-------------------------

gawag | 2017-01-02 01:11:11 UTC | #21

[quote="1vanK"]Gawag, is there a pause/freeze in Space Engineers, when chunks of world is loading? Or loading happens in another thread? As far as I know in Urho possible to modify scene only in main thread[/quote]
Usually there is no pause. Sometimes it's running quite slow because of it's high hardware requirements or bad optimization. Also the most performance issues happen when digging (modifying the voxel terrain like planets or asteroids). There is also a performance issue when flying through an asteroid field with a high speed as it has to constantly create procedural created asteroid but the reason should be more the random mesh generation as the resource loading.

[quote="1vanK"]
Or we need some method for rendering two scenes as a whole when camera around of scene border
[/quote]
Do you mean to display the current chunk and another, neighboring chunk that is in another scene? Not sure if something like that would work without problems. My idea is to load multiple chunks around the player to display them into the normal/active scene and unload them when they get further away or moving them to an own scene to continue calculating them. Not sure if such a scene move is even possible directly in Urho3D or if multiple scenes are even possible.

Urho has also the feature of loading resources in the background: [urho3d.github.io/documentation/1 ... ff8b18557b](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_resource_cache.html#a4a1ea3663dbe8bbc8c0c4cff8b18557b)
There should better not be a performance issue with adding stuff to the scene and removing it. I had freezes in Urho before but only when loading resources (normally, not in the background) that had not been loaded before. I resolved that by loading all resources when starting the game or loading a level and not loading a resource the first time when a model is actually placed in the scene during playing. I never experienced a performance problem when adding and removing stuff that was already in the cache. But I also did never have giant scenes and maybe that depends on several factors.

-------------------------

cadaver | 2017-01-02 01:11:12 UTC | #22

Instantiating a chunk of world can be a bit tricky performance-wise. All actual scene modification indeed is allowed only in the main thread. The principle of the Scene::Instantiate operations is that they complete synchronously so that the scene never has half-finished stuff around. On the other hand there's Scene::LoadAsync family of functions which can take several frames and signal you when done, but they disable scene update and rendering for the duration, so they're only meant for traditional load screens.

You should, however, be able to use Scene::LoadAsync from the scene chunk prefab using the mode LOAD_RESOURCES_ONLY. This fires off background threaded load requests to ResourceCache, but doesn't interfere with scene update or change anything in the scene yet. You need to do this in advance of loading the scene chunk (how much advance, the engine really can't tell you.)

Then, when you're actually ready to load the scene chunk in, call Scene::Instantiate and if all resources are loaded, it should be fairly fast. Though things like setting all attribute values, creating physics rigidbodies etc. can still induce some frametime delay.

-------------------------

AReichl | 2017-01-02 01:11:12 UTC | #23

> It's a feature only useful with very specific applications, and has a significant overhead. It doesn't belong to the core of the engine, it's a higher level system which needs to be built on top of it. It may be possible to implement it as an external addon library.

Ok ok - agreed.

-------------------------

Shylon | 2017-01-02 01:11:12 UTC | #24

yeh this feature should not be as a core in Urho3d, however level streaming might be very useful. this idea should apply for a game like RALLY in A real big country, hours and horse of driving :slight_smile:.

-------------------------

