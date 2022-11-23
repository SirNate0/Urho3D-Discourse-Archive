Lumak | 2017-01-17 19:03:13 UTC | #1

Just testing out another aspect of the engine - animation and character movement.  This engine is just so good.

vid
https://youtu.be/HE6OWT8OYfs

debugrenderer
https://youtu.be/O7jxIowf6CY

edit: added debugrenderer vid

-------------------------

gawag | 2017-01-02 01:10:46 UTC | #2

Ah that looks cool. Can you share the code for that? I made a platformer with animations but I feel that the animation code is not done properly. Urho's CharacterDemo is using an AnimationController, are you using that too like in that sample?

-------------------------

Lumak | 2017-01-02 01:10:46 UTC | #3

Hmm, it's not so much the code but the animation set that I bought from the unity store. Luckily, the set that I bought had "InPlace" and "RootMotion" sets, and I used the RootMotion set to extract displacement per frame and convert that to velocity.  And yes, I'm using 18_CharacterDemo code with AnimationController.

-------------------------

thebluefish | 2017-01-02 01:10:46 UTC | #4

Mind sharing the set you nabbed? I like the dummy character, and it looks like it has enough animations for me to make use of it without fiddling around with 3DS Max for a few weeks.

-------------------------

gawag | 2017-01-02 01:10:47 UTC | #5

Hasn't the Unity Store License something that you can only use the resources with Unity?

-------------------------

Lumak | 2017-01-02 01:10:47 UTC | #6

[quote="thebluefish"]Mind sharing the set you nabbed? I like the dummy character, and it looks like it has enough animations for me to make use of it without fiddling around with 3DS Max for a few weeks.[/quote]

Unfortunately, the EULA restricts me to pass them around.  Edit -- it says "you can not re-sell my animations, or give them away to someone else, even if you modify them."

[quote="gawag"]Hasn't the Unity Store License something that you can only use the resources with Unity?[/quote]
Good question, but the question is very broad.  I haven't looked at every asset being sold at the Unity Store to know if any one of those are restricted to used with Unity only.  I can tell you that everything that I bought had no restriction to Unity only.  I've also looked at assets from Unity Essentials, made by Unity, and those have no license.  Most asset license that I bought typically read something like: "royalty free, world wide, for any number of games or applications."

If you aren't sure if the license has a restriction to Unity only, you should visit the publisher's site and see.  Kubold for example states in their license:
[quote]4. You can use the animations in any game engine, you are not limited to UE4 or Unity.[/quote]
ref - [url]http://www.kubold.com/?page_id=527[/url]

-------------------------

1vanK | 2017-01-02 01:10:48 UTC | #7

I think, the license prohibits distribute animations separately, but allows as part of a product (otherwise how to sell the game?). Demo is product xD

-------------------------

thebluefish | 2017-01-02 01:10:48 UTC | #8

[quote="Lumak"][quote="thebluefish"]Mind sharing the set you nabbed? I like the dummy character, and it looks like it has enough animations for me to make use of it without fiddling around with 3DS Max for a few weeks.[/quote]

Unfortunately, the EULA restricts me to pass them around.  Edit -- it says "you can not re-sell my animations, or give them away to someone else, even if you modify them."
[/quote]

I meant a link to the set you found :p I assume I can access that asset store from a browser?

-------------------------

gawag | 2017-01-02 01:10:48 UTC | #9

Assets in the Unity Store seem to be either under the default proprietary Unity Store License or one of three free licenses. Custom licenses are not allowed.
Couldn't find anything about not redistributing outside of Unity though. Thought I read that somewhere in their default license.

-------------------------

Lumak | 2017-01-02 01:10:48 UTC | #10

[quote]
I meant a link to the set you found :p I assume I can access that asset store from a browser?[/quote]

Kubold, link in my previous post.  The guy has many assortments of animations.

[quote="gawag"]Assets in the Unity Store seem to be either under the default proprietary Unity Store License or one of three free licenses. Custom licenses are not allowed.
Couldn't find anything about not redistributing outside of Unity though. Thought I read that somewhere in their default license.[/quote]

I didn't know Unity can put a restriction on all assets sold on their store to be used only for Unity game engine. I've never seen that license. No matter, I bought my assets directly from publisher's site.

-------------------------

Lumak | 2017-01-02 01:10:48 UTC | #11

Found this in "Asset Store Terms of Service and EULA."
[quote]Unless you have been specifically permitted to do so in a separate agreement with Unity and except as permitted under the Unity-EULA, you agree that you will not reproduce, duplicate, copy, sell, trade or resell any Asset that you have acquired from the Unity Asset Store for any purpose.[/quote]

So the Unity Essential assets can not be distributed.  Good to know, but I haven't used that anyway.

-------------------------

gawag | 2017-01-02 01:10:48 UTC | #12

[quote="Lumak"]
[quote="gawag"]Assets in the Unity Store seem to be either under the default proprietary Unity Store License or one of three free licenses. Custom licenses are not allowed.
Couldn't find anything about not redistributing outside of Unity though. Thought I read that somewhere in their default license.[/quote]

I didn't know Unity can put a restriction on all assets sold on their store to be used only for Unity game engine. I've never seen that license. No matter, I bought my assets directly from publisher's site.[/quote]

Of course they can't change the copyright but they can disallow certain license terms of stuff published on their site. As it seems they only allow one of four licenses to choose from when publishing stuff on the store.

-------------------------

Lumak | 2017-01-02 01:10:48 UTC | #13

I'm still not convinced that Unity restricts all assets sold on their store to be used only with Unity game engine.

I read the "Unity Asset Store Terms of Service and EULA" again and can't find where it states that.  What I found was this phrase:
[quote]2.2
Licensor grants to the END-USER a non-exclusive, worldwide, and perpetual license to the Asset to integrate Assets only as incorporated and embedded components of electronic games and interactive media and distribute such electronic game and interactive media. Except for game services software development kits (?Services SDKs?), END-USERS may modify Assets. END-USER may otherwise not reproduce, distribute, sublicense, rent, lease or lend the Assets. It is emphasized that the END-USERS shall not be entitled to distribute or transfer in any way (including, without, limitation by way of sublicense) the Assets in any other way than as integrated components of electronic games and interactive media. Without limitation of the foregoing it is emphasized that END-USER shall not be entitled to share the costs related to purchasing an Asset and then let any third party that has contributed to such purchase use such Asset (forum pooling).[/quote]

The first sentence:
[b][quote]... integrate Assets only as incorporated and embedded components of electronic games and interactive media and distribute such electronic game and interactive media[/quote][/b]

It doesn't specify that the electronic games have to be made with Unity game engine.  And I only see one EULA, not four.  Maybe someone can point to where this restriction is cited.

-------------------------

gawag | 2017-01-02 01:10:49 UTC | #14

[quote="Lumak"]I'm still not convinced that Unity restricts all assets sold on their store to be used only with Unity game engine.

I read the "Unity Asset Store Terms of Service and EULA" again and can't find where it states that.  What I found was this phrase:
...
[/quote]
As I already said I couldn't find that either. Maybe they changed that or I misunderstood something.

[quote]
The first sentence:
[b][quote]... integrate Assets only as incorporated and embedded components of electronic games and interactive media and distribute such electronic game and interactive media[/quote][/b]

It doesn't specify that the electronic games have to be made with Unity game engine.  And I only see one EULA, not four.  Maybe someone can point to where this restriction is cited.[/quote]
The part with the four available licenses is in the store submission guidelines linked from [unity3d.com/asset-store/sell-assets](http://unity3d.com/asset-store/sell-assets):
[unity3d.com/asset-store/sell-ass ... guidelines](http://unity3d.com/asset-store/sell-assets/submission-guidelines)
Under 6.2:
[quote]6.2 Licensing your Content
For the sake of consistency, all Asset Store offerings are covered by a license we have created. Please have a look at the End User License Agreement to be sure you are comfortable with it. If you are offering your content for free, you have the further option of selecting one of three free-licenses, which override the basics of our commercial license. Please do not include your own license terms in your offering.[/quote]

-------------------------

Lumak | 2017-01-02 01:10:49 UTC | #15

Ok, thanks for the links. The submission guidelines 6.2 refers back to "Asset Store Terms of Service and EULA."  It's clear to me that there's no restriction about having to use Unity game engine for 3rd party assets. 
I wonder if, rather, doubt Unity will offer 3rd parties an exclusive license to restrict the assets to be only used by their engine/platform.

-------------------------

Lumak | 2017-01-02 01:10:49 UTC | #16

Let me cover how I incorporate the RootMotion in my character demo.  It's a very simple process.

Using the jump animation as an example, I extracted the Hips/Pelvis node key frames from RootMotion, which is this:
[code]
Jump animation AnimationKeyFrame - total frames = 17
frame= 0, t=0.0333, pos(0, 0, 0)
frame= 1, t=0.0666, pos(0, 0.0957, 0.3708)
frame= 2, t=0.1000, pos(0, 0.2871, 0.6140)
frame= 3, t=0.1333, pos(0, 0.4306, 0.7775)
frame= 4, t=0.1666, pos(0, 0.5941, 0.9131)
frame= 5, t=0.2000, pos(0, 0.7297, 1.0328)
frame= 6, t=0.2333, pos(0, 0.8533, 1.1484)
frame= 7, t=0.2666, pos(0, 0.9251, 1.2521)
frame= 8, t=0.3000, pos(0, 0.9530, 1.3877)
frame= 9, t=0.3333, pos(0, 0.9650, 1.5113)
frame=10, t=0.3666, pos(0, 0.9490, 1.6229)
frame=11, t=0.4000, pos(0, 0.9171, 1.7505)
frame=12, t=0.4333, pos(0, 0.8533, 1.8781)
frame=13, t=0.4666, pos(0, 0.7656, 2.0337)
frame=14, t=0.5000, pos(0, 0.5742, 2.2091)
frame=15, t=0.5333, pos(0, 0.3150, 2.3726)
frame=16, t=0.5666, pos(0, 0.0837, 2.5241)
[/code]

Secondly, keep track of curPos and prevPos each frame using a similar method found in [b]void AnimationState::ApplyTrackFullWeight()[/b] 
and acquire deltaPos = curPos - prevPos;  

Orient the deltaPos in character orientation:     
Vector3 vDisplacement = body->GetRotation() * deltaPos;
Knowing vDisplacement and timeStep, calculate linearVelocity = vDisplacement * (1.0f/timeStep); and just call rigidbody->SetLinearVelocity();

I also turn off gravity during the jump motion to get an exact match of the animation (the animation already accounts for gravity).

-------------------------

gawag | 2017-01-02 01:10:50 UTC | #17

[quote="Lumak"]Let me cover how I incorporate the RootMotion in my character demo.  It's a very simple process.

Using the jump animation as an example, I extracted the Hips/Pelvis node key frames from RootMotion, which is this:
...
[/quote]
So you are moving the bones manually and not with the normal system with the .ani files? Or are you converting that somehow?

[quote="Lumak"]I also turn off gravity during the jump motion to get an exact match of the animation (the animation already accounts for gravity).[/quote]
The character changes it's position in the animation? That should yield problems when using physics. You would have to offset the physical player shape somehow to match the animation offsetted model.

-------------------------

Lumak | 2017-01-02 01:10:50 UTC | #18

> So you are moving the bones manually and not with the normal system with the .ani files? Or are you converting that somehow?
Yes, you move the rigidbody with linear velocity.  So the body and the character will be in sync.  If you play the rootmotion in the game, the animation character will out of sync with the body.

>The character changes it's position in the animation? That should yield problems when using physics. You would have to offset the physical player shape somehow to match the animation offsetted model.
The character's position changes by matching rigidbody's position, as mentioned above. Manipulating rigidbody's linear velocity is similar to applying ApplyImpulse(), the character will naturally follow the body in the system. I turn off/on the gravity using an animation trigger file.

One caveat to implementing this displacement mover is you'll need to smooth out the camera.  I'm still working on tweaking mine.

-------------------------

Lumak | 2017-01-17 19:03:37 UTC | #19

Created a video with physic debugrenderer turned on.

T-pose
[img]http://i.imgur.com/jH9Lbwh.png?1[/img]

vid
https://youtu.be/O7jxIowf6CY

-------------------------

magic.lixin | 2017-01-02 01:10:51 UTC | #20

the best way is extracting the motion of root bone offline and the store the motion vector in animation resource, my way is modifying the animation in script after the animation is loaded.
  the difficult part is animation with rotation or root motion bone is pelvis(the bone has the motion is no the root bone but with local rotation and position)

-------------------------

Lumak | 2017-01-02 01:10:52 UTC | #21

[quote="magic.lixin"]the best way is extracting the motion of root bone offline and the store the motion vector in animation resource, my way is modifying the animation in script after the animation is loaded.
  the difficult part is animation with rotation or root motion bone is pelvis(the bone has the motion is no the root bone but with local rotation and position)[/quote]

I actually do something different than how I describe others can do this w/o having the need for Maya (currently using Maya 2016 LT), and I place a Displacement joint in my animation and the information is exported and embedded in an .ani file.
I can imagine it'll be difficult to duplicate the animation movement if there's rotation involved.  But from the looks of your animation sample videos (Cat Woman/Batman), I think you did an awesome job with that.

-------------------------

magic.lixin | 2017-01-02 01:10:54 UTC | #22

[quote="Lumak"][quote="magic.lixin"]the best way is extracting the motion of root bone offline and the store the motion vector in animation resource, my way is modifying the animation in script after the animation is loaded.
  the difficult part is animation with rotation or root motion bone is pelvis(the bone has the motion is no the root bone but with local rotation and position)[/quote]

I actually do something different than how I describe others can do this w/o having the need for Maya (currently using Maya 2016 LT), and I place a Displacement joint in my animation and the information is exported and embedded in an .ani file.
I can imagine it'll be difficult to duplicate the animation movement if there's rotation involved.  But from the looks of your animation sample videos (Cat Woman/Batman), I think you did an awesome job with that.[/quote]

 a special joint is a clever way of doing this kind of thing, I can imagine that even animation triggers can be stored in this way without making any urho3d specific exporter but just with normal FBX exporter. 
 since all the animations are stolen from the batman arkham games, and there are tons of crazy animations, I don`t want to modify the original data one by one, so just made a batch way in script after all the animations are loaded, the extracted part code are also learned from the RootMotionComputer.cs from unity site.

-------------------------

Enhex | 2017-01-02 01:11:08 UTC | #23

About the Unity Asset Store license:
[unity3d.com/legal/as_terms](https://unity3d.com/legal/as_terms)
Under "ASSET STORE END USER LICENSE AGREEMENT", 2.3 there are 2 restrictions which are annoying:
1. The license is valid only for 1 physical location. If you need it for several offices or working with people online it would mean each place need to buy a license.
2. It requires all computers that use the assets to have appropriate Unity license.

Theoretically you can use assets from the Unity Asset Store, but you'll have to have Unity licenses.

The best option is to try to check the seller's profile to see if they have their own website and find if they sell on other stores with sane licenses.
After going over the licenses of many stores I recommend CGTrader for 3D models, they have nonsense-free license.
For other resources there's market.envato.com, but their 3D store license is 1 use license so I don't recommend it, but their sound/video/graphics have unlimited use license.

-------------------------

gawag | 2017-01-02 01:11:08 UTC | #24

[quote="Enhex"]About the Unity Asset Store license:
[unity3d.com/legal/as_terms](https://unity3d.com/legal/as_terms)
Under "ASSET STORE END USER LICENSE AGREEMENT", 2.3 there are 2 restrictions which are annoying:
1. The license is valid only for 1 physical location. If you need it for several offices or working with people online it would mean each place need to buy a license.
2. It requires all computers that use the assets to have appropriate Unity license.

Theoretically you can use assets from the Unity Asset Store, but you'll have to have Unity licenses.

The best option is to try to check the seller's profile to see if they have their own website and find if they sell on other stores with sane licenses.
After going over the licenses of many stores I recommend CGTrader for 3D models, they have nonsense-free license.
For other resources there's market.envato.com, but their 3D store license is 1 use license so I don't recommend it, but their sound/video/graphics have unlimited use license.[/quote]
Ah that may have been the thing I found.

Other model sources (free!) I just copied from the old Unofficial Urho Wiki:
     [blendswap.com/](http://www.blendswap.com/)
    [matrep.parastudios.de/index.php](http://matrep.parastudios.de/index.php) Collection of Blender materials.
    [blenderartists.org/forum/showthr ... al-Library](http://blenderartists.org/forum/showthread.php?91585-treatkor-s-Junky-Material-Library) Small material library.
    [archive3d.net/](http://archive3d.net/)
    [cgtrader.com/free-3d-models](http://www.cgtrader.com/free-3d-models)
    [turbosquid.com/Search/3D-Models/free](http://www.turbosquid.com/Search/3D-Models/free)
    [artist-3d.com/](http://artist-3d.com/)

-------------------------

Shylon | 2017-01-02 01:11:09 UTC | #25

Very Nice works, keep it up, the last 4 jumps was really funny and nice :slight_smile:

-------------------------

