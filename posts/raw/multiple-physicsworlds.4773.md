mondoshawan | 2018-12-22 21:57:31 UTC | #1

I need to be able to run multiple Scenes in parallel or otherwise have multiple PhysicsWorlds running simultaneously. Is there a way to do this in Urho3D?

-------------------------

Modanung | 2018-12-22 22:46:44 UTC | #2

Yes, you can create a great number of `Scene`s within a `Context` if you like. Each with their own `PhysicsWorld`. I don't think physics worlds like sharing a scene, though.

Does your situation require combining render results from several scenes, or are most of them only there for simulation purposes?

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

mondoshawan | 2018-12-22 23:13:08 UTC | #3

Danke danke! Glad to be welcomed. =o)

My initial experiments corroborate your statement -- PhysicsWorld instances really don't like sharing the same scene. Generated all kinds of weird behaviors as the forces between two simulations were applied on the same objects.

I'm creating my main Scene and a PhysicsWorld to go with it. If I create a second scene and then add a PhysicsWorld, it prevents the first PhysicsWorld from updating:

[code]
{
  auto *secondScene = new Scene(GetContext());
  secondScene->CreateComponent<PhysicsWorld>(LOCAL);
}
[/code]

(Yeah, I know this is a memory leak -- that's fine for this example)

Looks like the pre-physics event is still firing, though.

-------------------------

Sinoid | 2018-12-23 00:25:01 UTC | #4

I don't have any problems running multiple scenes each with an active physics world in my tools. It should work.

-------------------------

mondoshawan | 2018-12-23 01:10:14 UTC | #5

Yeah, it seems to be something relating to what I'm doing with the code. FWIW, using a single program I can run two Scenes with two different PhysicsWorlds perfectly. The problem occurs when I start a server and connect my client via loopback.

I suspect it may be something non-obvious with scene/network replication. I'll have to play with it further.

Thanks for the confirmation that it should work, though -- isolates the problem to just my stuff. =o)

-------------------------

Sinoid | 2018-12-23 01:58:14 UTC | #6

> I suspect it may be something non-obvious with scene/network replication. I’ll have to play with it further.

~~Network replication only manages 1 scene.~~ Edit: nope, I'm wrong.

-------------------------

mondoshawan | 2018-12-24 21:52:07 UTC | #8

Okay, so now that we've figured out how to keep all of the PhysicsWorlds updating (turns out it was a bug in our physics prestep code), I should explain what our ultimate aim is here. Essentially, we'd like two "spaces" -- one with typical Newtonian-style space plane behaviors, and another "interior" physics behavior where we have local gravity "plating" typical to FPS-style behaviors.

The trick here is that if we try to do this using one PhysicsWorld, obviously, if your mass is great enough, the gravity vector will cause the outer volume to move constantly down. To combat this, we'd like to simulate a second PhysicsWorld, one where the outer "hull" of the volume the player is inside effectively has zero mass. IOW, toggle between different PhysicsWorlds as the player moves between them.

It's not exactly clear how to build something like this in Urho3D -- has anyone attempted to do so in the past? If so, what kinds of approaches might work?

We're attempting to do this in a multiplayer/networked environment, so that would be part of the crazy we're running into.

-------------------------

