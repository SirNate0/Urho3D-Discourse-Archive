Kai | 2017-01-02 00:59:17 UTC | #1

Hi,

I come from OGRE since I find performance limits in my game.
I had search a 3D engine replacement for my game engine and I seen often good things about Urho3D in forums.
So I made a simple benchmark with OGRE, Horde3D and Urho3D : Urho3D has just incredible performance !
Since Urho3D is inspired by OGRE, it's very easy to change, the API is the same.
I feel like the high level render engine of Urho3D it's an OGRE clean version so things learned with OGRE are not lost.

First impression with Urho3D :
-Awesone performance !
-API is very clean.
-The code is very well written.
-All is very documented.

A big thanks to Urho3D team !

-------------------------

Bluemoon | 2017-01-02 00:59:18 UTC | #2

Coming from Ogre as well... 

I got the source for Urho3d a couple of weeks back and, to be honest, from the size of the source ( as compared to other sources I've built) I really didn't think it was worth laying a hand on.
 
But just yesterday night (22-05-2014) after going through series of frustration trying to integrate AngelScript to a game project I was working on, I realised Urho had AngelScript integration. Well, I decided to give it a try and Urho3d built 100% without a single error (has really been long I had such an experience), and even running the samples impressed me the more.

I've really invested alot of time and energy in Ogre for my project, but I don't mind taking a bite out of Urho3d, it might just be what I need.

Thanks to all involved and keep it up.

-------------------------

carlomaker | 2017-01-02 00:59:18 UTC | #3

[quote="Bluemoon"]Coming from Ogre as well... 

I got the source for Urho3d a couple of weeks back and, to be honest, from the size of the source ( as compared to other sources I've built) I really didn't think it was worth laying a hand on.
 
But just yesterday night (22-05-2014) after going through series of frustration trying to integrate AngelScript to a game project I was working on, I realised Urho had AngelScript integration. Well, I decided to give it a try and Urho3d built 100% without a single error (has really been long I had such an experience), and even running the samples impressed me the more.

I've really invested alot of time and energy in Ogre for my project, but I don't mind taking a bite out of Urho3d, it might just be what I need.

Thanks to all involved and keep it up.[/quote]

You are welcome :wink:,  i came from Ogre3d too , 
I'm curious, could I know what kind of test, and the difference that you've encountered.

-------------------------

cadaver | 2017-01-02 00:59:19 UTC | #4

[quote="Bluemoon"]I got the source for Urho3d a couple of weeks back and, to be honest, from the size of the source ( as compared to other sources I've built) I really didn't think it was worth laying a hand on.[/quote]
Just curious, did you think it was too small, or too large? :slight_smile:

And to the OP: Welcome! It's great to hear that you've had a positive experience with Urho3D so far.

-------------------------

Bluemoon | 2017-01-02 00:59:19 UTC | #5

[quote="cadaver"]
Just curious, did you think it was too small, or too large? :slight_smile:
[/quote]

I thought it was way too small... My bad I guess :slight_smile:, it turned out size doesn't necessarily matter

-------------------------

Hevedy | 2017-01-02 00:59:19 UTC | #6

This need the render features from ogre (gi, ao...)
But yes the Urho3D performance is good, but no idea how much change that with more shaders in use.

-------------------------

cadaver | 2017-01-02 00:59:21 UTC | #7

If you have a small object count and run heavy shaders then performance in both engines should be equivalent, as it's only the GPU doing most of the work. With higher object / drawcall count Ogre will spend a lot of time setting OpenGL / D3D state redundantly, and in those situations Urho should fare better. This can be partially mitigated in Ogre when you remember to use the instanced entity classes, but doesn't help if you want to render a lot of objects that aren't identical copies.

That said, Ogre has its advantages in the flexibility department, as you get various hooks and listeners into the rendering process, which in Urho would require directly modifying the high-level rendering code.

-------------------------

