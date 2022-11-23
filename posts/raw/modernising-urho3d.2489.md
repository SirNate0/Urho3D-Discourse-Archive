boberfly | 2017-01-02 01:15:46 UTC | #1

Hi all,

I wanted to continue the discussion that was from the Atomic Game Engine announcement page here, roughly from page 9:
[url]http://discourse.urho3d.io/t/atomic-game-engine-mit-urho3d-fork/643/1[/url]

@cadaver It was interesting to see your take on how engines like Unreal/Unity are designed in relation to Urho and mentioned about Naughty Dog's engine. I discovered this the other day as well:
[url]https://github.com/JodiTheTigger/sewing[/url]
Which is basically an implementation of their fibers co-routine thread-pool which uses the assembly from boost to do fast context jumps.

Anyways, if one were to experiment with this way of designing an engine, I'm just trying to gauge how much refactoring one would need to do with Urho3D vs one from scratch (but I'll repeat, as an experiment which would most definitely break existing features like immediate physics steps like you mentioned). You do mention if we didn't have this then it would be easier to multi-thread the engine. You know it best, what other things would be the potential gotchas do you think you would need to know or the best way to start this? In my head, I guess decoupling the renderer so it is isolated from game logic is one step (the proxy approach sounds like what most engines are doing to separate the game logic world/scene from the renderer, same for Stingray/Bitsquid):
[url]http://bitsquid.blogspot.ca/2016/09/state-reflection.html[/url]

I think to be in-line with Vulkan/Direct3D12's command buffer/lists, the refactor to Graphics.h would be to make another object which manages this for draw/state commands so you could have multiple ones running on multiple threads. On older APIs this could be a purely emulated object which never touches the hardware API which caches these as messages/buffers to be deferred & played back on the render or main thread. The potential problems would be for things that need to change vertex buffers would have to be carefully managed, especially things like blend shapes which I think are updated in an immediate fashion before the draw call (arguably a better/modern approach could be used here instead).

Having the renderer proxy separation, perhaps the data-oriented stuff could be applied here as this is where the tight loops would be run for things like frustum culling and such, so the 'fat' entity/component system which is scattered in memory might not be such a big deal in terms of cache-coherency for gameplay stuff (you could always nest a new component which is cache coherent for what you want to do, like a crowd system or particles as a workaround, I've seen this done by making a custom 'shape' in Maya for a crowd system). The other bottleneck I could think of is how bones for animated skeletons are a part of these 'fat' nodes, so my other experiment was to use ozz-animation for this task, however you would lose flexibility here like setting ragdoll collision boxes on bones for one, or just implement them differently.

The other thing was I was taking a look at how PhysX lets you implement its tasks to run in your own threadpool by using their interface:
[url]http://docs.nvidia.com/gameworks/content/gameworkslibrary/physx/guide/Manual/Threading.html[/url]
And Bullet recently got patches to re-implement its threading ability for v2.x:
[url]https://github.com/bulletphysics/bullet3/pull/390[/url]

I'd love to work on some experiments here, but being pragmatic I know my job will prevent me doing this so I am time poor. Having a focus through a discussion is important, apologies if there is already a thread about this. This post is already quite long, but I thought I'd just put down my thoughts on things. Cheers!

-------------------------

boberfly | 2017-01-02 01:15:46 UTC | #2

Link to ozz-animation:
[url]https://github.com/guillaumeblanc/ozz-animation[/url]

An interesting looking abstraction of the modern graphics APIs, which uses std::function to record commands on the OpenGL side into a vector to be played back later (as a fallback the other APIs don't do this, I think in practice if you're not doing the AZDO stuff in OpenGL then it probably won't be very fast):
[url]https://github.com/ronsaldo/abstract-gpu[/url]

-------------------------

artgolf1000 | 2017-01-02 01:15:46 UTC | #3

Urho3D is becoming mature today, I like the pure c++ solution, it give me largest freedom to control everything.

But mature means that the architecture is difficult to change, developers usually give up if the modification affects a lot.

I think it not bad to keep the engine's architecture as a pure c++ solution.

I am also impressed by those pure Javascript 3D engines, they use WebGL and HTML5 to present everything, maybe that's the future.

-------------------------

cadaver | 2017-01-04 11:30:00 UTC | #4

I don't have a lot of additional insight to this; the big but kind of nebulous inefficiency I've uncovered seems to be the large amount of data traversed during rendering (cache misses), which ties into Drawable & Node being fat. So preferably you'd have some lightweight structures for culling (e.g. just world AABBs), and something else for lighting and other render preparation processes. Urho's scene rendering processing is quite complex, as light and zone interactions need to be checked, and this often involves collecting things into vectors (ie. drawable's light list, light's drawable list). If the rendering didn't need this, like being pure deferred or 3D-light grid like Doom, then a lot of time would be saved.

As for game logic and such, it's hard to think without having concrete usecases. I don't unfortunately have any personal large projects using Urho going on, but of course you could do various synthetic torture cases, like just getting a lot of objects doing something (either physics, or other logic.)

What artgolf1000 writes is very true. Urho is mature in the sense that it has its way of doing things, and also quality / ease-of-use expectations are fairly high due to its history, which makes changing it in a large way challenging or undesirable. This is kind of unfortunate for its continued development. 

I also personally am unlikely to commit self-destructive amounts of time to large-scale changes any more, but I'm totally open for forks, or even (like I've written before elsewhere) being replaced as the lead if someone has energy to spare and wants to become Urho's version of dark_sylinc completely overhauling Ogre for 2.x :)

-------------------------

boberfly | 2017-01-04 18:29:05 UTC | #5

Cheers for the reply cadaver & artgolf1000!

Yeah very much understood that these are too destructive of changes for sure, it was me just putting thoughts onto a page. Maybe a fork makes more sense and would be a lot easier to deal with, or maybe set up something like Turso3D for a test-bed for experimentation first.

I think the whole maintaining backwards-compatibility for Ogre having 2 namespaces feels like OpenGL-level horrid and I'm all about the less code the better, so a fork/experimental branch-off sounds more appealing right now. Looking at Godot 3.0 too, it feels like ES3.0 is the baseline and then the plan is to later get an ES2.0 to work around this with fallbacks rather than getting all the graphics APIs to behave like DX9-era.

About Doom's rendering, yeah I've been thinking along these lines of doing clustered forward hybrid, which seems to work very well with VR as well, and UE4 decided to do this as well, except I think compute shaders fill in the grid with light look-ups rather than the CPU, but this might clash with async stuff if you were to pipeline other stuff there so that might be why Doom does it on the CPU.

And about gameplay, yeah the traditional ECS lends itself with DOD cache-coherency well, but you lose API-friendly flexibility compared with fat node entities with fat components that currently exist. I'm thinking the least path of resistance is to maybe get the component internal data into some struct manager which is grabbed using an ID handle rather than a pointer, maybe a base class which has a generic POD/Vector with a custom struct layout that all components have their own subclass of, and grab a handle from it so that this 'manager' class is in charge of lifetime and can do things like snazzy swap-deletes like the Bitsquid/Stingray articles suggest. This 'manager' class would also need to do batch update loops, maybe this is where you make the meat of the logic work in a 'job' type way anyways. Not all components need to work this way perhaps....

-------------------------

boberfly | 2017-01-04 19:37:56 UTC | #6

Huh, actually under Navigation the design of having a CrowdManager + CrowdAgent component systems have a cool way of doing DOD. Very much like I was talking about with the custom Maya crowd system which used a Maya shape to define the agents...

-------------------------

cadaver | 2017-01-04 19:52:36 UTC | #7

Bullet's dynamics world (encapsulated in PhysicsWorld) is sort of a system / manager too. Though the underlying Bullet rigidbodies are less DOD and more in the direction of traditional "fat" objects.

-------------------------

vivichrist | 2018-06-30 05:08:58 UTC | #8

I have some code for clustered shading that I could donate. I created this code for a fourth year graphics paper. however it works on the cpu side of things and according to many white papers on the subject this is the way to go for integrating the 'thousands of lights' approach.

-------------------------

franck22000 | 2018-06-30 07:43:52 UTC | #9

Hello Vivichrist, I am very interested by this, do you have a github repository somewhere for that ?
Is it working with deferred shading or only forward shading ?

-------------------------

vivichrist | 2018-07-05 10:40:03 UTC | #10

It was to replicate the work in "Clustered Deferred and Forward Shading
[Ola Olsson, Markus Billeter, and Ulf Assarsson]." It is on bitbucket (private) but I can zip it up and Share it here I guess. The code can be adapted to either forward or deferred as noted in the white paper, the code is just an implementation of a quick algorithm to create the arrays for uploading to video memory as textures. It worked well but I never analysed it for memory leaks and such. There are array classes for accumulating the 3D Texture for cluster lookup etc. and lib dependences of GLM. This was intended to be used with Unity as managed C++ rendering code but instead I just mangled it into a hacked version of the Standard Shader.

-------------------------

franck22000 | 2018-06-30 09:53:09 UTC | #11

Would be nice if you could share a zip here yes :)

-------------------------

vivichrist | 2018-06-30 10:27:13 UTC | #12

I'll have to tidy it up a bit.

-------------------------

vivichrist | 2018-07-05 07:29:20 UTC | #13

here is the cpu side code:
https://www.dropbox.com/s/2smxacibe7nngxg/LightAssignment.7z?dl=0

The only files worth looking at are the LightAssignment and Array3D/4D classes

-------------------------

vivichrist | 2018-07-05 07:36:46 UTC | #14

So basically the two arrays that are produced should be uploaded to GPU ram as texture1D's (or the indexing array can be a 3D texture) every frame and used for pixel->lights lookup.

-------------------------

vivichrist | 2018-07-05 08:25:48 UTC | #15

Although on a different tack I think the idea of Tiled Light Trees [Yuriy O’Donnell, Electronic Arts Matthäus G. Chajdas, AMD] is better/easier to implement in some ways. Requires binary search implementation within a shader.

-------------------------

vivichrist | 2018-07-05 08:31:56 UTC | #16

lightListIndex getCluster( in float4 vpos )
{
    float4 suv = vpos;
    suv.xy /= _ScreenParams.xy;
    float depth = SAMPLE_DEPTH_TEXTURE_PROJ(_CameraDepthTexture, UNITY_PROJ_COORD(suv));
    depth = Linear01Depth(suv.zw);
    return _Clusters[(int)((_ScreenParams.x - vpos.x) / _TileSize) * _Cellsy * _Cellsz
    					 + (int)((_ScreenParams.y - vpos.y) / _TileSize) * _Cellsz
    					 + (int)(depth * (float)(_Cellsz))];
}

-------------------------

vivichrist | 2018-07-08 12:22:53 UTC | #17

actually it requires a depth first search ordered list with skip references

-------------------------

