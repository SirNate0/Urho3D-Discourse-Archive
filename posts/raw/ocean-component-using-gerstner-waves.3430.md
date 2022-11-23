Gentle22 | 2017-08-07 18:12:55 UTC | #1

Dear Urho3D community,

because this is my first Topic in this forum I am very excited about your feedback. But first I have to say thank to the people that created this great game engine. I stumbled over it when I was looking for an alternative to the Ogre3D engine, which is a little bit outdated, at least from my perspective. When I looked into the source code of the Urho3D engine I was really impressed how clean and easy to understand it is. I really do not understand why so few people are using it, but maybe I can contribute at least a little bit to change that. But now to my project.

As already mentioned in the title, I am working on a component to simulate waves in real time. Similar to what Lumak already did with his FFT Waves, but I decided to use the Gerstner Waves approach. The work is based on this [GPU Gems article](https://developer.nvidia.com/gpugems/GPUGems/gpugems_ch01.html). My first version contains only the mesh transforming stuff and  **no texturing at all**. But enough of the bla, bla now. Here is a video of what is already working.

https://www.youtube.com/watch?v=RtDOIf-QqUE/

**How it works:**
I created a component called Ocean that needs a planar mesh which is used as a water plane. By applying several sine wave calculation to a
the vertices the waves are created. Currently everything is calculated on the CPU. 

By pressing E, the Wave Editor shows up, which allows you to change the basic properties that are used to create waves. To create some variations the basic properties are not taken as they are but are randomized. To avoid visual jumps all waves are faded-in and out. All waves have a lifetime and if a wave dies it is faded out.

**Properties:**
_Waves_ - The amount of active waves at the same time

_Lifetime_ - The time in seconds a wave is active. Randomized between half and double of the basic property.

_Steepness_ - Defines how steep the crest of a wave is (0 - 1). Higher values moves the vertices closer together at the
 top of the wave.

_Length_ - The distance between the crests. It is also randomized between the half and the double of the basic value.

_Amplitude_ - The height of the wave. Because the length is randomized the amplitude needs to hold the same ratio to 
the length as the basic properties.

_Speed_ - How fast a wave moves. Can be randomized with the Speed Variation checkbox.

_Direction_ - Is the direction of movement (x,z). To create some variation in the direction you specify an angle that defines the allowed variation of the direction vector.

_Fading_ - The editor allows to disable the fading but without fading you get jumps in the vertex positions.
_Speed Variation_ - Enable speed variations.

_Set Button_ - Feeds the properties of the Wave Editor to the Wave System. Newly created waves use the new properties. It takes some time to see the change, depending on the set lifetime.

_Reset Button_ - Saves the new properties to the Wave System and erases all active waves from the Wave System to force a creation of new waves. If fading is disabled, this allows to see immediately the final state of the new properties.

The next steps could be something like this:
- Try to create a realistic texturing for the water plane. I think what I achieved until now was like a _walk in the park_ compared to creating a realistic looking water surface :frowning:
- Try to make other objects floating realistically in the water. There is a good but hard to understand article about that topic [Water Interaction Model](http://www.gamasutra.com/view/news/237528/Water_interaction_model_for_boats_in_video_games.php)
- Optimize by moving the calculations to a Vertex Shader. Not sure if it makes too much sense, because I need the height field also for the physics.

I guess that`s it for now. 

Ah one thing left, you find the source code on my [github](https://github.com/Gentle22) account. I have a Urho3D fork with a branch feature/ocean, but also a repository Urho3D-Ocean which contains only the added files and the water plane model.

-------------------------

Gentle22 | 2017-08-07 17:40:38 UTC | #2

I am not able to embed the video in my post, it is only a link. Can someone please tell me how to to it?

Thanks a lot.

-------------------------

Modanung | 2017-08-07 17:53:29 UTC | #3

Looking quite promising!

[Here](https://discourse.urho3d.io/t/fast-fft-ocean-ocean/1949)'s a link to Lumak's Fast FFT Ocean.

-------------------------

Modanung | 2017-08-07 17:46:18 UTC | #4

[quote="Gentle22, post:2, topic:3430"]
I am not able to embed the video in my post, it is only a link. Can someone please tell me how to to it?
[/quote]

Simply placing a url on a line of its own creates a [onebox](https://github.com/discourse/onebox) where possible.

-------------------------

Gentle22 | 2017-08-07 17:47:48 UTC | #5

Hey Modanung,

thanks for your reply. Yes I have seen Lumak`s work, I think I mentioned it in my post. I read about the FFT Waves in the paper of [Tessendorf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.161.9102&rep=rep1&type=pdf) but I couldn't understand the math behind it :frowning: So I decided to use something I am able to understand and tweak to match my desires. ;-)

-------------------------

Modanung | 2017-08-07 17:48:59 UTC | #6

[quote="Gentle22, post:5, topic:3430"]
I think I mentioned it in my post
[/quote]

Right, read over that and went directly for the good stuff. :blush:

-------------------------

slapin | 2017-08-07 19:21:13 UTC | #7

Any plans on including in stock Urho? I'd sell a soul to have high level constructs like this in Urho.

-------------------------

Lumak | 2017-08-07 23:58:39 UTC | #8

This looks awesome! Nice work.

[quote="Gentle22, post:1, topic:3430"]
Try to create a realistic texturing for the water plane. I think what I achieved until now was like a walk in the park compared to creating a realistic looking water surface :frowning:
[/quote]

I hope you can come up with something better than what I got. Writing my water material/shader was my first attempt at learning about shaders and graphics in general and it just looks bad.  

p.s. Can you please add some kind of License in your ocean repo.

-------------------------

Gentle22 | 2017-08-08 09:33:23 UTC | #9

First of all, thanks for the positive feedback.

[quote="slapin, post:7, topic:3430, full:true"]
Any plans on including in stock Urho? I'd sell a soul to have high level constructs like this in Urho.
[/quote]

Sure, this is the long term goal, but I think in its current state it is not very usable. I think at least the following features must be implemented:

* Good looking GSLS/HSLS shaders
* A way to scale the Ocean to any size, similar like it is done in the Terrain Component.
* Some performance optimizations
* Integration into the Urho3D Editor and making it scriptable

Because I am working as  C++ developer in my day job and have a family my spare-time is very limited. So it could take a while to implement all that stuff. But your comments keep my motivation high :slight_smile:

 [quote="Lumak, post:8, topic:3430, full:true"]
This looks awesome! Nice work.

[quote="Gentle22, post:1, topic:3430"]
Try to create a realistic texturing for the water plane. I think what I achieved until now was like a walk in the park compared to creating a realistic looking water surface :frowning:
[/quote]

I hope you can come up with something better than what I got. Writing my water material/shader was my first attempt at learning about shaders and graphics in general and it just looks bad.  

p.s. Can you please add some kind of License in your ocean repo.
[/quote]

MIT license added. 

Maybe you recognized that I copied your style for my Urho3D repositories, but I have a question. My current workflow is to develop on a feature of my Urho3D fork. If the branch reaches a satisfying state, I copy the added/changed files into a new folder and create a new repository containing only the new or changed files. But that means, I have to copy theses files again if I changed something on the feature branch. Do you know of a way to have particular files/folders tracked by two repositories?

Regarding the shaders I have to admit that I am a pretty noob in that area. When I left the video game industry many years ago, shaders have been very new and I had not the opportunity to dive into them very deeply. But you are never too old to learn something new, so let's see what I can do.

-------------------------

johnnycable | 2017-08-08 13:09:01 UTC | #10

Looks very promising! Good work!

-------------------------

Lumak | 2017-08-08 14:28:05 UTC | #11

[quote="Gentle22, post:9, topic:3430"]
Maybe you recognized that I copied your style for my Urho3D repositories
[/quote]
Yes, I think that simplifies how a repo should be built because everyone should know how to build Urho3D samples.

[quote="Gentle22, post:9, topic:3430"]
Do you know of a way to have particular files/folders tracked by two repositories?
[/quote]
There are more git commands you can perform from GitShell such as what you describe.  You can get help on gitshell topics and there are many tutorials on the github site, but I find doing a branch compare/merge/edit is just too much hassle for me, not to mention I'm still some what novice when it comes to git commands. My preferred way is to have my Urho3D repo untouched and download and copy Urho3D master on my local drive to work with to create samples.

[quote="Gentle22, post:9, topic:3430"]
Regarding the shaders I have to admit that I am a pretty noob in that area. When I left the video game industry many years ago, shaders have been very new and I had not the opportunity to dive into them very deeply. But you are never too old to learn something new, so let’s see what I can do.
[/quote]

You'll find that programming shaders are actually quite fun and some what easy once you get into it - but learning new shading technique (not in Urho3D's list) is quite challenging.  I really didn't learn "how to" until I started on my Urho3D Material Effects repo: to date, that repo has the highest commit count, ha. But you should be able to pick it up rather quickly.

-------------------------

najak3d | 2021-12-04 09:48:15 UTC | #12

Hi, I'm blunt and honest.  I love Urho3D and appreciate what all has been done here.  You have done a TON of GREAT WORK.  And are currently our front runner.

This wave generator is "neat" (the math is cool), but the overall result in the "Ocean" sample demo makes Urho3D look "incapable" of a more realistic Ocean presentation.   The one we have now in Samples is cartoonish and lacking.

I'm only critical here because I want to see Urho become a "leading engine", rather than a forgotten one.  I agree that this is a great replacement for OGRE3D.   But the samples, and momentum here are lacking -- and I think don't give proper demonstration of Urho3D capabilities (which is part of the reason it's falling behind, or losing momentum?).

I am assuming that Urho3D is capable of producing a much better wavy-Ocean presentation.   Has *anyone* used Urho yet for more advance outdoor environment rendering?  (e,g, sun, layered fog, god-rays, day/night transitions, large streamed-terrain, with vegetation/tree imposters, streamed terrain, realistic ocean, clouds, etc?)

Right now, we're debating between using Urho3D.NET or devising a new .NET/C# game engine wrapping Open3D.   We want to both pick the winner, and/or help determine "the winner".  We're approaching this mostly from a C#/.NET perspective, because coding in C# is much easier than C++, while still being just as robust, with a usually-negligible performance hit.

===
Ironically, back in 2003, I was the one who ported OGRE3D's Water demo to Axiom3D (the C# port of OGRE), which employed a similar Wave algorithm.  Urho's current "Ocean Sample" is not even as good as the OGRE3D water demo (as it had a reflection and diffraction effect).  I would assume that the current demo could be upgrade with similar effects in URHO3D with a modification to Shader techniques and settings.  (I would assume we could just apply the techniques from "Water" sample to the "Ocean" sample, right?)

BTW -- I'm currently using Urho3D C++ compilation for my testing.   One of my projects uses UrhoSharp, and another now uses Urho.NET (by @elix22 ).    And we're hoping that Urho might be the best choice for our new project  (which is to provide a winning/easy solution for programmers wanting to add 3D rendering to their .NET apps).   (Program-First style audience.)   As of right now, we're debating between Urho.NET (with Avalonia plugin for UI) vs.  starting a new componentized engine wrapping Open3D.   Our aim, is that we provide a solution that makes it onto the Microsoft website as "recommended platform for rendering 3D" (as UrhoSharp *used* to be, before they removed it).

-------------------------

