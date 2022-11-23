Leith | 2019-06-10 07:27:10 UTC | #1

Has anyone attempted to do anything more interesting than simple skybox?
SkyDome?
SkySphere?
Procedural blending?

I was just curious to ask if I can save myself the effort, before throwing myself into a more advanced skybox shader.

-------------------------

George1 | 2019-06-10 10:30:51 UTC | #2

I remember saw a procedural sky component a few years ago on this board.  It actual done very well. Hopefully you can locate it and revive that.

https://discourse.urho3d.io/t/procsky-component/1168

https://github.com/jforjustin/ProcSky

-------------------------

Leith | 2019-06-10 10:36:58 UTC | #3

Thanks! I've done this stuff before on other engines, but this will save me time, no doubt.
Happy to hand back the result as a PR for a companion component to SkyBox

That actually brings up a separate point for me.
The component oriented approach, including the loose event system, was meant to help us to decouple our code.
But in practice, some components always need each other to be there.
This would be a companion, it would require at least one skybox component to exist.

-------------------------

fnadalt | 2019-06-10 13:02:45 UTC | #4

Take a look at this I made... I borrowed the skybox technique from somewhere that should be written somewhere within the project tree, or I could look it up again.
https://github.com/fnadalt/World

-------------------------

johnnycable | 2019-06-10 14:37:17 UTC | #5

This one seems very cool

https://discourse.urho3d.io/t/precomputed-atmospheric-scattering/2897

-------------------------

QBkGames | 2019-06-11 05:29:26 UTC | #6

I'm also interested in some skybox with independent moving cloud layer and moving sun. However I'm more interested in a lightweight shader that looks good enough rather than something very realistic and sophisticated (and expensive to render).

-------------------------

Leith | 2019-06-11 08:00:10 UTC | #7

I agree, and have some ideas / previous experience in producing a high quality look at low cost.
What I don't have is much hands-on experience with Urho's rendering pipe.

-------------------------

