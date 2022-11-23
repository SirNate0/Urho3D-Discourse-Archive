THEMIKEBERG | 2017-01-02 01:10:36 UTC | #1

[img]http://i.imgur.com/sC7lBWu.png[/img]
Disclaimer: I'm very new to C++ and fairly new to programming in general. I was playing around with C# for a while in Unity and then I found Urho and I'm quite in love with it this is how I feel like teaching myself to program it's fun.

The only thing I can think of is the scale I have this model set to.

[code]		planetNode_ = scene_->CreateChild("Earth");
		planetNode_->SetPosition(Vector3(0.0f, 0.0f, 149570000.0f));
		planetNode_->SetScale(12742.0f);
		StaticModel* earth = planetNode_->CreateComponent<StaticModel>();
		earth->SetModel(cache->GetResource<Model>("Models/Sphere.mdl"));[/code]

My last project in Unity created star systems on runtime through procedural generation based in 2D which was fun however I want to take this to 3D at the moment it's not to scale by a long shot I also have no idea if what I'm attempting at this scale is possible but I'd like to see what I can do with it. Right now I'm just trying to familiarize my self with Urho and how it works. 

Anyone care to point me in the right direction?

-------------------------

gawag | 2017-01-02 01:10:36 UTC | #2

Does that also happen at positions closer to 0?
Does the model have multiple layer?
It could be that the floating point gets imprecise enough at such a high position value so that faces close to each other start "jumping" and z-fighting. Solution would be to not have faces so close to each other and use textures, or have smaller position values.
You could also use a trick to keep stuff close to you always at low position values to avoid floating point issues. I just started writing down an idea I had on how to do that: [github.com/urho3d/Urho3D/wiki/S ... rge-Worlds](https://github.com/urho3d/Urho3D/wiki/Super-Large-Worlds)

-------------------------

THEMIKEBERG | 2017-01-02 01:10:36 UTC | #3

[quote="gawag"]Does that also happen at positions closer to 0?
Does the model have multiple layer?
It could be that the floating point gets imprecise enough at such a high position value so that faces close to each other start "jumping" and z-fighting. Solution would be to not have faces so close to each other and use textures, or have smaller position values.
You could also use a trick to keep stuff close to you always at low position values to avoid floating point issues. I just started writing down an idea I had on how to do that: [github.com/urho3d/Urho3D/wiki/S ... rge-Worlds](https://github.com/urho3d/Urho3D/wiki/Super-Large-Worlds)[/quote]

It seems to happen to everything yes.
No multiple layers that I know of it's just the Sphere.mdl file provided.
I'll check out your link, thank you!

-------------------------

gawag | 2017-01-02 01:10:36 UTC | #4

Have you tried moving the object to 0,0,0 (or close too)? Same flickering?

Also a note to the text I wrote: you could keep the player/camera and stuff around it close to 0,0,0 and have object far away (sun, other planet) have high coordinates. The chunk based system may not really help in your case but the basic idea of keeping coordinates of close stuff low to avoid floating point issues should help.

No layers? Hm... Are the normals correct? Can't really tell without seeing the model in an editor and only by that screenshot, can you provide the Blender file if there is one?

-------------------------

THEMIKEBERG | 2017-01-02 01:10:36 UTC | #5

[quote="gawag"]Have you tried moving the object to 0,0,0 (or close too)? Same flickering?

Also a note to the text I wrote: you could keep the player/camera and stuff around it close to 0,0,0 and have object far away (sun, other planet) have high coordinates. The chunk based system may not really help in your case but the basic idea of keeping coordinates of close stuff low to avoid floating point issues should help.

No layers? Hm... Are the normals correct? Can't really tell without seeing the model in an editor, can you provide the Blender file if there is one?[/quote]

You should already have it, it comes with Urho3D source. "Sphere.mdl"
[url=https://www.dropbox.com/s/lqtyqc5h26sd5m9/Sphere.mdl?dl=0]Download it here[/url]

As for it flickering close to 0,0,0 I have no idea anymore. Something has changed and I can no longer see anything. I think it has to do with the zone I setup. I still don't fully understand how to implement a zone that lets the camera see very far. 
[code]  Node* zoneNode = scene_->CreateChild("Zone");
    Zone* zone = zoneNode->CreateComponent<Zone>();
    zone->SetBoundingBox(BoundingBox(-16910.0f, 16910.0f));
    zone->SetAmbientColor(Color(0.1f, 0.1f, 0.1f));
    zone->SetFogColor(Color(0.0f, 0.0f, 0.0f));
    zone->SetFogStart(-16910.0f);
    zone->SetFogEnd(16910.0f);
[/code]

Thanks for your help it's greatly appreciated.

EDIT/ No it does not happen to objects close to 0,0,0.

Would this be a cause of float inperfections? If I cout my vector3 floats to setpercision(1) would that possibly help?

EDIT// ^ That did not help.
EDIT/// Alright So I've rebuilt this in the same manner I did before, I have recorded a short video showing what is happening.
[video]https://www.youtube.com/watch?v=RVvqY-BZvwo[/video]

This happens when I turn the camera with the mouse, it's hard to tell but if I move the mouse along the horizontal axis while looking at it from the direction you see the "planets" from the second planet and up to the last disappear until I move my mouse towards the light. I'm not sure if this is a lighting issue or an issue with my Zone. Either or I'm having a good jolly amount of fun with it.

Planet 2 sits at Vector3(2500000.0f, 0, 0) it counts up by 1000000 for each planet, with the tenth planet sitting at Vector3(10500000.0f, 0, 0).

-------------------------

gawag | 2017-01-02 01:10:36 UTC | #6

Oh it's the shipped Sphere.mdl, shouldn't be a model issue then.

I just tested the zones out. At first I thought the bounding box size being too small to cover your whole scene could cause issues but I made my zone super small and nothing changed. Then i completely removed the zone and nothing changed, so it doesn't seem to be a issue with the zone. Maybe the zones are just to set the fog and the nearest zone is picked for setting the fog values. You could remove that zone part too (for testing or if you don't need fog or whatever else zones offer).

[quote]EDIT/ No it does not happen to objects close to 0,0,0.
Would this be a cause of float inperfections?[/quote]
Seems like it. I'm still a bit surprised. The sphere looks fine outline and shape wise but the screenshot looks like z-ordering issues (z-fighting). The graphics card seems to be rendering parts of the backside of the sphere in front of the front. Could be a bug but also just a result of the high values that can't really be fixed.
I couldn't really see that issue in the video. In the video it seems like planets for away from the sun (0,0,0 I guess) are not always displayed depending on camera position and orientation. Could be the same issue with z-ordering due to floating point imprecision, the distance values may be ending up behind the camera and therefore no visible sphere.
Does it help scaling the whole scene down and using lower values?

[quote]
If I cout my vector3 floats to setpercision(1) would that possibly help?[/quote]
Do you mean std::cout? Setting the precision does only change the output format when using std::cout to output numbers. Doesn't help.

BTW: I have a space skybox which I used in an Urho project and you may want to use it or something like that as well:
[github.com/damu/Urho-Sample-Pla ... /stars.png](https://github.com/damu/Urho-Sample-Platformer/blob/master/bin/Data/Textures/stars.png)
[github.com/damu/Urho-Sample-Pla ... _space.xml](https://github.com/damu/Urho-Sample-Platformer/blob/master/bin/Data/Textures/skybox_space.xml)

[code]
        Node* skyNode=globals::instance()->scene->CreateChild("Sky");
        skyNode->SetScale(50000.0f);
        Skybox* skybox=skyNode->CreateComponent<Skybox>();
        skybox->SetModel(globals::instance()->cache->GetResource<Model>("Models/Box.mdl"));
        skybox->SetMaterial(globals::instance()->cache->GetResource<Material>("Materials/skybox_space.xml"));
[/code]
Skybox is a special model that is moved with the camera and always behind everything else. The scale doesn't really matter.

Looks like this in that project: [youtube.com/watch?v=6BmD0r6Mb0Q](https://www.youtube.com/watch?v=6BmD0r6Mb0Q) (I don't remember the asteroid material looking that blurry... maybe I should improve that...)
There are some post-processing effect active like fake HDR and bloom which make the stars way bigger and brighter.

-------------------------

THEMIKEBERG | 2017-01-02 01:10:36 UTC | #7

[quote="gawag"]Oh it's the shipped Sphere.mdl, shouldn't be a model issue then.

I just tested the zones out. At first I thought the bounding box size being too small to cover your whole scene could cause issues but I made my zone super small and nothing changed. Then i completely removed the zone and nothing changed, so it doesn't seem to be a issue with the zone. Maybe the zones are just to set the fog and the nearest zone is picked for setting the fog values. You could remove that zone part too (for testing or if you don't need fog or whatever else zones offer).

[quote]EDIT/ No it does not happen to objects close to 0,0,0.
Would this be a cause of float inperfections?[/quote]
Seems like it. I'm still a bit surprised. The sphere looks fine outline and shape wise but the screenshot looks like z-ordering issues (z-fighting). The graphics card seems to be rendering parts of the backside of the sphere in front of the front. Could be a bug but also just a result of the high values that can't really be fixed.
I couldn't really see that issue in the video. In the video it seems like planets for away from the sun (0,0,0 I guess) are not always displayed depending on camera position and orientation. Could be the same issue with z-ordering due to floating point imprecision, the distance values may be ending up behind the camera and therefore no visible sphere.
Does it help scaling the whole scene down and using lower values?

[quote]
If I cout my vector3 floats to setpercision(1) would that possibly help?[/quote]
Do you mean std::cout? Setting the precision does only change the output format when using std::cout to output numbers. Doesn't help.

BTW: I have a space skybox which I used in an Urho project and you may want to use it or something like that as well:
[github.com/damu/Urho-Sample-Pla ... /stars.png](https://github.com/damu/Urho-Sample-Platformer/blob/master/bin/Data/Textures/stars.png)
[github.com/damu/Urho-Sample-Pla ... _space.xml](https://github.com/damu/Urho-Sample-Platformer/blob/master/bin/Data/Textures/skybox_space.xml)

[code]
        Node* skyNode=globals::instance()->scene->CreateChild("Sky");
        skyNode->SetScale(50000.0f);
        Skybox* skybox=skyNode->CreateComponent<Skybox>();
        skybox->SetModel(globals::instance()->cache->GetResource<Model>("Models/Box.mdl"));
        skybox->SetMaterial(globals::instance()->cache->GetResource<Material>("Materials/skybox_space.xml"));
[/code]
Skybox is a special model that is moved with the camera and always behind everything else. The scale doesn't really matter.

Looks like this in that project: [youtube.com/watch?v=6BmD0r6Mb0Q](https://www.youtube.com/watch?v=6BmD0r6Mb0Q) (I don't remember the asteroid material looking that blurry... maybe I should improve that...)
There are some post-processing effect active like fake HDR and bloom which make the stars way bigger and brighter.[/quote]

It's all good just means I'll need to drop the scale and sacrifice more detailed ships. Thanks for the skybox I'll give it a try!

At the moment the goal is to generate star systems with procedural generation with at least a maximum of 12 planets, I'm glad I wont be bothering with elliptical orbit like my last project. Unless I decide to make this into a 3D 4X game... Probably not. 

I appreciate the help gawag!

-------------------------

gawag | 2017-01-02 01:10:36 UTC | #8

[quote]It's all good just means I'll need to drop the scale and sacrifice more detailed ships. [/quote]
Nah. I meant scaling the planets down to like 0.001 of their current size and reduce the distance accordingly to keep the same dimensions but in lower values.

But another thing that came to my mind: Try changing the near and far clipping distance that may greatly help you and fix the z-order issues:
[code]
//Camera* camera=cameraNode_->CreateComponent<Camera>();  // somewhere the camera is being created
camera->SetFarClip(50000000);
camera->SetNearClip(100);
[/code]
Play around with the values so that everything you want visible is visible and nothing is so close to the camera that it disappears. The range between the values should be as small as possible to avoid z-fighting.

You're welcome!

That project sounds quite interesting. Is it just a testing project? Hobby? School? Commercial?

If you also want to make ships and space stations and possible walk around on those you may actually need some kind of trick to keep the values around the player/camera low to stay precise. That system that Space Engineers uses or the one I described in the article may be relevant depending on what you want to do. Could be tricky.

Edit: Forgot to link the material to the space skybox: [github.com/damu/Urho-Sample-Pla ... Skybox.xml](https://github.com/damu/Urho-Sample-Platformer/blob/master/bin/Data/Materials/Skybox.xml)

-------------------------

hdunderscore | 2017-01-02 01:10:36 UTC | #9

My first guess was floating precision error. In large scale games (even when position is only >10,000), other solutions are used especially if you are using the physics engine. World tiling is one way, another simple solution you can try is to have all planets in one node and more the universe instead of the camera so that the positions are always near to zero.

-------------------------

THEMIKEBERG | 2017-01-02 01:10:37 UTC | #10

[quote="gawag"]That project sounds quite interesting. Is it just a testing project? Hobby? School? Commercial?

If you also want to make ships and space stations and possible walk around on those you may actually need some kind of trick to keep the values around the player/camera low to stay precise. That system that Space Engineers uses or the one I described in the article may be relevant depending on what you want to do. Could be tricky.[/quote]

It was a hobby prototype that turned into an actual game prototype. The point was to get a general understanding of how "Procedural Generation" could work, my project went through a fairly simple process for generating a star system:

[code]
Single Star, or Binary?
If Single, determine mass, classification, and temperature.
If Binary Determine Aphelion and Perihelion, then mass, classifications, and temperatures.
Have Barycentre get and sum masses of central star(s).
Determine amount of planets and planets with satellites (moons).
On generation of each individual planet check if in Goldilocks zone, run random range for if intelligent life.
If intelligent life = true, generate colony, determine life form technological advancement.
If technological advancement = true, generate a minimum of one "man made" satellite orbiting barycentre.
On generation of each individual planet outside determine classification of planet (from "Hot gas Giant" to "cold rock" and everything in between).
Determine resource types and amount available per planet.
After planet generation, determine if asteroid belt = true, if true generate asteroid belt (each asteroid was it's own "gameobject") determine aphelion and perihelion of asteroid belt.
Generate "Alien structure" as farthest orbiting body of star system. Alien Structure was the only means of transport from star system to star system. Has ability to transport whole fleets of space ships.
[/code]

I didn't get too far into actual game play as the point was to determine a proper pipeline for system generation. After that was achieved I set my sights on a more toned back version of the generator within a 3D environment mostly not accounting for actual orbit because it doesn't make sense gameplay wise when orbiting bodies appear to be standing still to the human eye. There is still a lot of work to do on the pipeline like understanding the use of perlin noise to create textures on runtime. As well as other graphical additions that I did not account for in the 2D version. I also need to gain a grasp of XML as a means to properly save/load generated star systems. To me XML is really exciting as it can give me saved data per system generated to help improve the pipeline. :smiley:

At the moment I've thought of a method for "Large object LOD" this would be for objects greater than X Km's long like Planets and Super structures. It involves transitioning from a scene with small objects to a scene with a bigger more detailed objects the closer you get to the object in question. (Detailed objects would always be at 0,0,0 of the scene transition) It's going to be difficult to implement as my understanding of C++ syntax is weak. However I think I'm up for the task. (I'm not going to attempt planetary landing, procedural generation of that level is too high of a scope, just being able to get close to a planet and it looking massive on screen is the goal) I hope to use world tiling for believable distances for the smaller/less detailed planet objects and super structures giving the illusion that the player has just traveled a great distance. 

[quote="hd_"]My first guess was floating precision error. In large scale games (even when position is only >10,000), other solutions are used especially if you are using the physics engine. World tiling is one way, another simple solution you can try is to have all planets in one node and more the universe instead of the camera so that the positions are always near to zero.[/quote]

Indeed this does seem to be the case, which is fine because from my first initial test this only seems to have an effect on objects that are sitting at any position greater than 1500000.0 if this holds true then it is good news for my "Large Object LOD" idea. 

All in all a better understanding of Urho3D and C++ syntax is in order, I believe that I'll obtain that simply through trial and error like I did with C#, it helps that a lot of things within Urho and C++ are in a sense similar to C# and Unity. I am hoping it helps with the learning process.

EDIT/ Just had a thought that my Large object LOD idea and world tiling could possibly be implemented in the exact same way via "world tiling" right now the plan of attack is the scour the examples and docs to see if I can figure out how to load Node's from XML files then see if I can make world tiling happen.

Thanks guys!

-------------------------

gawag | 2017-01-02 01:10:37 UTC | #11

Sounds interesting.

About noise: there's a library called libnoise that may be useful: [libnoise.sourceforge.net/](http://libnoise.sourceforge.net/)
I used that library many years ago to generate heightmaps.
Are you sure you want to generate textures at each startup? Would really slow down startup.
Or just at the first?
You could also just pre-generate textures. I experimented with these to generate seamless textures: [urho3d.wikia.com/wiki/Creating_T ... extureEdit](http://urho3d.wikia.com/wiki/Creating_Textures_with_NeoTextureEdit)

About XML: I wrote about reading quite a while ago: [urho3d.wikia.com/wiki/XML](http://urho3d.wikia.com/wiki/XML) Never tried writing but should be easy as well.
Urho3D has also the feature of loading and saving scenes. I've never used that though and using XML more directly could be better in your case anyway.

[quote]All in all a better understanding of Urho3D and C++ syntax is in order, I believe that I'll obtain that simply through trial and error like I did with C#, it helps that a lot of things within Urho and C++ are in a sense similar to C# and Unity. I am hoping it helps with the learning process.[/quote]
Could you write things down where you were stuck or that you find weird or difficult? I'm always interesting in difficulties regarding Urho and C++ (or programming in general). Also we are working on adding learning material to Urho and such "beginner difficulties" or "slowdowns" would be really helpful. Also I find Urho to be sometimes weird to use and I'm sure I'm not the only one.

Edit: Oh have you tried changing the near and far clip distance? Could help.

-------------------------

Enhex | 2017-01-02 01:10:37 UTC | #12

[quote="hd_"]another simple solution you can try is to have all planets in one node and more the universe instead of the camera so that the positions are always near to zero.[/quote]
You'd still have precision problems with the node itself.

-------------------------

