CE184 | 2020-12-31 03:52:57 UTC | #1

I found a similar discussion but links are broken and no conclusion [there](https://discourse.urho3d.io/t/question-about-ragdolls/795/3?u=ce184), and I checked bulletphysics user manual page for constraint, did not find any useful information to interpret the SetAxis() and SetOtherAxis().


In the 13 example, we have head, spione, pelvis bones are all set as box and has the same axis as the world space.
```
CreateRagdollBone("Bip01_Pelvis", SHAPE_BOX, Vector3(0.3f, 0.2f, 0.25f), Vector3(0.0f, 0.0f, 0.0f),
            Quaternion(0.0f, 0.0f, 0.0f));
CreateRagdollBone("Bip01_Spine1", SHAPE_BOX, Vector3(0.35f, 0.2f, 0.3f), Vector3(0.15f, 0.0f, 0.0f),
            Quaternion(0.0f, 0.0f, 0.0f));
CreateRagdollBone("Bip01_Head", SHAPE_BOX, Vector3(0.2f, 0.2f, 0.2f), Vector3(0.1f, 0.0f, 0.0f),
            Quaternion(0.0f, 0.0f, 0.0f));
```
Then we have the constraint:
```
CreateRagdollConstraint("Bip01_Spine1", "Bip01_Pelvis", CONSTRAINT_HINGE, Vector3::FORWARD, Vector3::FORWARD,
            Vector2(45.0f, 0.0f), Vector2(-10.0f, 0.0f));
CreateRagdollConstraint("Bip01_Head", "Bip01_Spine1", CONSTRAINT_CONETWIST, Vector3::LEFT, Vector3::LEFT,
            Vector2(0.0f, 30.0f), Vector2::ZERO);
```

What does it meaning for ```FORWARD``` as both axis for pelvis-spine hinge constraint? Does it mean the hinge axis where both part rotate around? It does not look like to me.

What does it mean for the ```LEFT``` axis between head and spine? Is that the twist axis as mentioned in [this page](http://docs.autodesk.com/3DSMAX/12/ENU/3ds%20Max%202010%20Tutorials/files/WSf742dab04106313315bef0fb112a19e466a-7fd5.htm)? Does not look right to me neither, since twist axis sounds like Y::UP axis for me.

Also, what are those low/high limits? I could guess two angles for the rest 2 axis, but which is for which?
The comment says 'Interpretation is constraint type specific' which is obvious and not very helpful. It'd be good to expand that more, e.g. for hinge, 1st angle is for what, 2nd angle is for what; for conetwist, blablabla...

There is very limited documentation about ragdoll and it's very frustrating to debug it time after time.

-------------------------

evolgames | 2020-12-31 06:38:32 UTC | #2

I had the same issue with ragdolls. I'll check my notes because I might have wrote those down (as far as the low and high limits and what they correspond to).
I assume you've turned on physics debug in the renderer? It helps for the joints, specifically to see how cone twists are oriented.

-------------------------

CE184 | 2020-12-31 06:52:03 UTC | #3

Yep, that debug rendering is the only thing I can rely on debugging, but still lots of trial & errors.
Good to know you have some notes, maybe you could help to update the docs/comments in code if those notes are helpful?

-------------------------

evolgames | 2020-12-31 07:02:05 UTC | #4

Yeah it's definitely annoying guessing. It may be intuitive to others but it wasn't to me. And the way the joints are set up with all the possible inputs of low highs, axis, connections, limits, etc makes it challenging to figure out what is doing what. It's been a while, so I'll take a look, but I think some values in the Vector3s will do nothing, too.
Good idea. Even just a blurb of text in the ragdoll sample or the wiki would be very useful for someone looking at it for the first time. Cause otherwise they have to do the exact same trial and error.

-------------------------

Modanung | 2020-12-31 17:53:04 UTC | #5

https://gitlab.com/luckeyproductions/tools/dolly

-------------------------

CE184 | 2021-01-04 19:16:15 UTC | #6

It depends on Dry and I somehow failed to build that, will try it later. I wonder if there is  one based on Urho3D directly.

-------------------------

Modanung | 2021-01-06 14:02:23 UTC | #7

[quote="CE184, post:6, topic:6645"]
[...] I somehow failed to build that [...]
[/quote]

What OS? :desktop_computer:

-------------------------

CE184 | 2021-01-07 02:54:06 UTC | #8

mac latest os
```
ld: weak import of symbol '___darwin_check_fd_set_overflow' not supported because of option: -no_weak_imports for architecture x86_64
```
I haven't taken a closer look, probably small enough to fix on my own.

But, what is the main difference between Dry and Urho3D? bare bone means only basic features?

-------------------------

Modanung | 2021-01-07 12:19:38 UTC | #9

So far bare bones means no Direct3D or Lua.
Also keeping tools/editors in separate repositories and no Mixamo models (`ozom` branch still).

Other changes include some increased consistency and convenience in the API: Enabled VectorN IntVectorN arithmetic with automatic conversion to float vectors, renamed smart pointers' `Null()` to `IsNull()` and `String`'s `Empty()` to `IsEmpty()`.

Furthermore it's hosted on GitLab - as part of something [bigger](https://luckeyproductions.nl/) - and has an official [chatroom](https://matrix.to/#/#dry:matrix.org). This also means it can be co-developed with the games that rely on it, and modified as things come up in the game development process... such as a [blockmap](https://gitlab.com/luckeyproductions/dry/-/tree/blockmaps/Source/Dry/BlockMap) format (like tiles but 3D).

-------------------------

