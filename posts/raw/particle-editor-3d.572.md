hdunderscore | 2017-01-02 01:01:26 UTC | #1

I've put together a particle editor (for 3d particles), with help from ChrisMAN.

Available to test here:

[github.com/hdunderscore/Urho3D/ ... icleEditor](https://github.com/hdunderscore/Urho3D/tree/Editor_ParticleEditor)

Known Bugs:
[ul][li]Redo doesn't work for LineEdit values[/li][/ul]

Screenshot:
[img]https://pbs.twimg.com/media/B27k4cqCEAA0uV7.png:large[/img]

-------------------------

cadaver | 2017-01-02 01:01:27 UTC | #2

Looks good!

Too bad it won't get to 1.32, but that version is long overdue and after that we can be more aggressive in taking in new things again.

-------------------------

codingmonkey | 2017-01-02 01:01:27 UTC | #3

well done [b]hd_[/b], this very good and important tool

also, urho3d needs build-in tail generator, with: color ramps fx, fade-out fx... and so on )

-------------------------

hdunderscore | 2017-01-02 01:01:28 UTC | #4

Thanks !

Yeah I still want to add some things to ParticleEffects, eg:
[ul][li] Variations over lifetime[/li]
[li] Emission type: distance mode - emits X particles per Y units travelled[/li]
[li] Particle type: Static Mesh[/li]
[li] Emitter shapes: Cone (base, volume), Static Mesh (vertex, edge, face, volume ?)[/li][/ul]

When stacking up particle emitters onto a single node, I noticed there can be some kind of depth fight/pop. I'm not sure if this is something that needs to be solved on emitter level (eg, having multiple effects on one emitter to share a billboard set, or having a depth bias/priority) or shader level.

codingmonkey - I saw that you have written a tail generator? You could contribute :wink:

-------------------------

codingmonkey | 2017-01-02 01:01:28 UTC | #5

>I saw that you have written a tail generator? You could contribute :wink:
yep, but i don't known what is that - contributor, and how to become him )
and at last my generator is very simple and buggy, everybody can write a similar.

-------------------------

ucupumar | 2017-01-02 01:01:37 UTC | #6

Mesh particles is one of features that I most missed when switched to Urho! 
I hope this project is going well! 

:mrgreen:

-------------------------

hdunderscore | 2017-01-02 01:01:37 UTC | #7

Yeah definitely a useful feature, however it may be a while before I get back to that as I have a few other things I want to work on.

I have fixed the undo/redo issue and submitted a pull request on this. If anyone spots any bugs, let me know !

-------------------------

Mike | 2017-01-02 01:01:37 UTC | #8

For now it works great  :slight_smile:

-------------------------

codingmonkey | 2017-01-02 01:01:37 UTC | #9

good job!)

-------------------------

ucupumar | 2017-01-02 01:01:44 UTC | #10

Thanks hd_! It works great! 

But, imho, the arrow manipulator looks too big and it's blocking the actual particles. 
Can it be changed to grid or something? Or at least, a switch to turn it on or off?

-------------------------

ucupumar | 2017-01-02 01:08:17 UTC | #11

Bumping old thread!  :slight_smile: 

I'm implementing some improvement to particle editor. I've already added pull request [url=https://github.com/urho3d/Urho3D/pull/1060]here[/url]. The changes are:
[ul]
[li]Adding grid with option to hide it[/li]
[li]Gizmo now always visible in the left corner[/li]
[li]Change particle preview viewport camera to behave more predictably[/li][/ul]

Screenshot:
[img]http://i.imgur.com/Kriey2M.png[/img]

-------------------------

codingmonkey | 2017-01-02 01:08:18 UTC | #12

Hi ucupumar, good work!
How did you think, is it possible to add ability with supporting the "baked animation" to current urho's particle emitter ? For faked physic-like curved flows and various effects.

-------------------------

ucupumar | 2017-01-02 01:08:18 UTC | #13

[quote="codingmonkey"]Hi ucupumar, good work!
How did you think, is it possible to add ability with supporting the "baked animation" to current urho's particle emitter ? For faked physic-like curved flows and various effects.[/quote]
Maybe that's possible, but I think direction aligned particles should be implemented first. There are still a lot of limitations of Urho3D particles because of that missing stuff.
Anyway, the pull request is already merged! Yay!  :smiley:

-------------------------

codingmonkey | 2017-01-02 01:08:18 UTC | #14

>direction aligned particles should be implemented first
I think this feature supported from old days - POINT SPRITES HW-feature

-------------------------

1vanK | 2017-01-02 01:08:18 UTC | #15

[quote="codingmonkey"]Hi ucupumar, good work!
How did you think, is it possible to add ability with supporting the "baked animation" to current urho's particle emitter ? For faked physic-like curved flows and various effects.[/quote]

may be good way is realisation emitting of instances of nodes (prefabs) with components (like tail-generator)

for it need 2 component
1) Component-emitter, which will generate (just copy sample) a nodes with initial speed and random direction
2) Component for emitted nodes (self deleting after delay, various effects) + we can use physics (eg sparks can bounce from a floor)

p.s. I can not evaluate the performance of this solution

-------------------------

codingmonkey | 2017-01-02 01:08:19 UTC | #16

>may be good way is realisation emitting of instances of nodes (prefabs) with components (like tail-generator)
no, it's will be very dramatically slowly solution
I think what all simulation may be written into texture1D(?) and then in vertex shader we move points from (vertex buffer) by "baked" positions what readed from this texture. but it's only in theory. 
-actually particles have a life time, how do visual kill of each of them ?
-animation may be long loop, and VB fixed (determined count of particles) in size, in this case I guessing need some how to reuse already killed points in VB. (or its work for exporter: if particle.lifeTime == end then particle = getNewParticleInfo() )

-------------------------

1vanK | 2017-01-02 01:08:19 UTC | #17

[quote="codingmonkey"]actually particles have a life time, how do visual kill of each of them ?[/quote]

animate opacity to 0
animate size/tail length to 0

EDIT: see [post6907.html](http://discourse.urho3d.io/t/particle-trails/1157/3) for visual effect

-------------------------

ucupumar | 2017-01-02 01:09:09 UTC | #18

[quote="codingmonkey"]>direction aligned particles should be implemented first
I think this feature supported from old days - POINT SPRITES HW-feature[/quote]
Hmm, I didn't know about those POINT SPRITES HW feature. 

Anyway, actually I'm doing some experiment about this direction based particles.
And now I can show you some little preview. It's inspired from Unity stretched billboard particles. 
Here is the first screenshot:
[img]http://i.imgur.com/IXCP17G.png[/img]
I'll upload the gif/video soon. Need some tweaking first.  :slight_smile:

-------------------------

Mike | 2017-01-02 01:09:09 UTC | #19

It looks great !  :slight_smile:

-------------------------

