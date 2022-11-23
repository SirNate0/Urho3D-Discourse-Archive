Enhex | 2017-08-21 11:41:20 UTC | #1

Hi,

I'm working on a CSP system for Urho3D. The system is pretty simple:
- send complete networked state snapshot with last input ID received
- read it and re-applying all the inputs since the last ID received

The problem is that I'm getting a stutter. It happens when snapshots of the moving player are received and a bit after that.

Here's a video of the problem, using 1000ms latency:
https://www.youtube.com/watch?v=fho73G7ywPU

With no latency the problem doesn't exist.
With 100ms it barely happens and when it does it's barely noticeable.

anyone got any idea what could cause it?
Could it be the network attributes' previous state?
Could it have anything to do with the smooth transform component?

-------------------------

GoogleBot42 | 2017-01-02 01:04:12 UTC | #2

Hmmm I think it would help others help you if you posted some code... Although it does seem that the problem happens when you change your velocity.

-------------------------

Enhex | 2017-01-02 01:04:12 UTC | #3

[quote="GoogleBot42"]Hmmm I think it would help others help you if you posted some code... Although it does seem that the problem happens when you change your velocity.[/quote]

I've uploaded the Subsystem to Github:
[github.com/Enhex/Urho3D-CSP-Attempt](https://github.com/Enhex/Urho3D-CSP-Attempt)
Note that it isn't refined or anything. Also note that I wrote it using some stdlib and stdlib style.

Actually in order to simplify re-applying inputs I'm changing position instead of velocity, so no physical simulation time is required (which is another whole level of problem).
Considering we have the same fixed time step on both sides (1/60), we should have the same result.

Also inputs are re-applied instantly after the state snapshot is read on the client side.

EDIT:
Something I just noticed is ApplyAttributes(), could it be somewhat related?

-------------------------

cadaver | 2017-01-02 01:04:13 UTC | #4

Check the SmoothedTransform component, which is created to networked client nodes and whose purpose is to smoothly lerp the current transform toward the last value received from server. It may be interfering, so you may need to add a way to turn it off when predicting the character on the client.

-------------------------

Enhex | 2017-01-02 01:04:14 UTC | #5

[quote="cadaver"]Check the SmoothedTransform component, which is created to networked client nodes and whose purpose is to smoothly lerp the current transform toward the last value received from server. It may be interfering, so you may need to add a way to turn it off when predicting the character on the client.[/quote]

I tried removing SmoothedTransform but it didn't help. Is there anything else that could get in the way?

-------------------------

Enhex | 2017-01-02 01:04:15 UTC | #6

After doing a bit more testing with higher latency it appears that the problem is a jump between the received state and the predicted state.
The prediction happens immediately after the received state is read, so why does the received state gets rendered?
Are events threaded, so it's possible that the scene is being rendered before the prediction takes place?

-------------------------

GoogleBot42 | 2017-01-02 01:04:16 UTC | #7

[quote="Enhex"]After doing a bit more testing with higher latency it appears that the problem is a jump between the received state and the predicted state.
The prediction happens immediately after the received state is read, so why does the received state gets rendered?
Are events threaded, so it's possible that the scene is being rendered before the prediction takes place?[/quote]

One second after you change direction/speed the jumps would be expected I think...  It seems that may be the source of your problems... doesn't the problem happen if you move in a constant direction and speed?

-------------------------

cadaver | 2017-01-02 01:04:16 UTC | #8

There is no threading, the sequence on each frame is always:

Update network (read packets, apply attributes)
Update scene (includes physics update)
Render

If you have rigidbodies, note that Bullet is also doing its own interpolation. I recommend debugging through a frame and setting a breakpoint on functions that modify Node transform (Node::SetPosition, SetRotation, SetTransform etc.) so that you see exactly what is being changed and when.

-------------------------

Enhex | 2017-01-02 01:04:16 UTC | #9

tried lowering the physics FPS to 5, and there's a noticeable mismatch between the number of inputs sent to the number of inputs processed by the server.
So the CSP buffers more inputs than it should in this case.
Basically Urho was sending inputs at 30 fps while applying them at 60 fps, which caused to buffer more input than the server actually applies.

The solution is custom input sending message that doesn't wait for Urho's Network system to be sent. Then send and process inputs at the same rate. And it works!

I built the system on top of Urho and it lives alongside Urho's Network system. Well since I don't have access to the connection's sendMode_/position_/rotation_ I couldn't include setting net priority with the custom input message.

I'd love to see Urho having client side prediction because network system without CSP is like a car without wheels (unless you're making LAN/non-real-time MP game, which are rather rare use cases).
My CSP system uses much simpler networking, sending a complete state snapshot of the CSP nodes in a single message. No create/update/remove node/component, no delta/latest.
The client can deduce which nodes are new and which needs to be removed like this:
[img]http://i.imgur.com/hvld64c.png?1[/img]

Of course that means it doesn't scale well with increased number of nodes & components, but it's enough to only use it on player controlled objects since it can work alongside urho's network system, so it should be fine.
(tho ideally everything should be client side predicted)

-------------------------

thebluefish | 2017-01-02 01:04:16 UTC | #10

You would be surprised how cheap those updated can be made. There's no reason this couldn't be done in such a way that an entire scene is client-side-predicted with little overhead. Of course, that all depends on who wants to dedicate that kind of time :p

-------------------------

cadaver | 2017-01-02 01:04:16 UTC | #11

It's great that you found a solution that worked for you.

Urho itself has to be a bit wary so that it doesn't come to include a networking model that doesn't scale well to begin with. Whole scene prediction could be interesting, but it basically means that on every server update, the client has to rewind and instantly simulate physics with a timestep that's equal to the latency. This may be extreme, because even the normal physics timestep from frame to frame can be punishing on the client CPU in a complex scene.

For things that are lacking in the existing Urho network interface, I suggest modifying the classes like you need, and making a pull request.

-------------------------

Enhex | 2017-01-02 01:04:16 UTC | #12

Well yeah that depends on the scale of the game, but if you look at a lot of multiplayer games which are real time and use physics engines, like shooters for examples, they don't have a lot of physical objects or things that need to be CSP'd. Quake, Counter-Strike, MOBA games, and pretty much every multiplayer game I can think of. Heck some of them don't even use physics engines (or only for client side effects). The point is that it isn't a new problem, and all mutliplayer games deal with it.
Another way around re-running the whole simulation is to have kinematic body for the player with custom movement, so you can reapply inputs only on the player object.
Or maybe your game doesn't even use rigid bodies for the players, or at all (e.g. real time strategy games).
For things which don't need to be predicted accurately you could have complete client side simulation. And it goes on...

The problem with implementing CSP with the existing Network system is that you need a complete state snapshot. For example you can't use delta updates on the predicted state, because the predicted state might be wrong and the whole point of sending the state is to correct it (If you're 100% deterministic you don't need to send anything for the most part, deterministic lockstep).
A possible way around it is to maintain two states, CSP state and replication state. the replication state gets replicated as it does in Urho but does not affect the scene, just sits in the background so the CSP can copy it each frame and perform a prediction on it, and the CSP state will be the one used by the scene. As long as Urho's network updates create complete, or maybe at least near complete snapshots of the server state, the client will be able to predict it accurately enough.
If you want to give this approach a try that would be great if it works, it will enjoy Urho's already existing network efficiency, and won't change the API that much, probably just adding PREDICTED to LOCAL and REPLICATED.
(For now I spent way more time than planned on the CSP thing and I need to move on with my project, so I'm not going to try it)

The most important thing to keep in mind is that it's better to have something that doesn't scale well than something that doesn't work at all. It's nice and dandy to have a car that uses 90% less fuel but if it doesn't have wheels it won't get anywhere.
Without client side prediction real time games over the internet aren't an option, and that's a much much smaller possibility space than games that can handle the overhead. CSP is essential.

Well I hope it helped to convince you that CSP is a must, and if it didn't try to think about multiplayer games you know and ask two questions:
Are they playable over the internet without CSP?
Can they handle the overhead of CSP?

-------------------------

cadaver | 2017-01-02 01:04:16 UTC | #13

It is frankly unnecessary to argue for the importance of client-side prediction, because it is a given for certain types of games. The real question is how it can be achieved without sacrificing the generic usability of the networking subsystem, and in the presence of a physics simulation. In extreme cases throwing away Urho's inbuilt networking completely could be a very valid solution. As is picking another engine that *does* have CSP already built in. It's probably not what you want to hear, though :slight_smile: but remember that Urho is a voluntarily maintained project and the best course of action to make sure it proceeds in the direction you want, is to actually put in the time and contribute, instead of writing on the forums of what it *should* have.

What could be added quite easily would be user-assignable hooks or events to the reception of server->client network updates, which would allow the client to maintain the necessary state for prediction, and apply the updates selectively. Also, adding a minimal timestamp (8bit) to the updates, that corresponds to the last client->server input update the server has seen.

-------------------------

GoogleBot42 | 2017-01-02 01:04:16 UTC | #14

Hey Enhex could you post the source code?  It might be helpful to others and I would like to see how you did it as I will need to do it sooner or later.  :slight_smile:

-------------------------

Enhex | 2017-01-02 01:04:17 UTC | #15

[b]@cadaver[/b]
Well I did spend about 2 weeks (lost track already) attempting to make a CSP system on top of Urho3D, so it's not like I'm all talk no walk.
The first attempt was to apply prediction on the state after it got replicated, which is almost the same approach as you suggest, but it didn't work (possibly I did something wrong).
The second attempt was to remove as many unknown factors as possible in order to be able to know exactly what's going on by implementing a custom straight forward network system, without modifying Urho3D so it can be an "addon" that won't conflict when updating the engine to newer versions. And I almost gave up on it and indeed thought about picking an engine that already have proper multiplayer or implement authoritative client-side objects but at the last moment I figured what went wrong, and gladly I don't have to go with the lesser alternatives.
These two weeks were mainly debugging hell.

I'm offering to contribute my work to be adopted by the engine, and I try to point out that it's better to start with a useful naively implemented and inefficient system than a nearly useless efficient system, and heck they don't even conflict. I also offered a way to have a more efficient CSP system based on the existing replication code by having two states, but that requires modifying Urho and if it doesn't get in I'll just have to deal with merge conflicts when updating, and I already offer a system which doesn't conflict.


[b]@GoogleBot42[/b]
As you requested I made a repo on Github with some instructions:
[github.com/Enhex/Urho3D-CSP](https://github.com/Enhex/Urho3D-CSP)

I'll also post it on the code exchange.

-------------------------

cadaver | 2017-01-02 01:04:17 UTC | #16

The changes I wrote about are now in. Server attribute updates can be redirected to events on the client on a per-attribute basis.

Beware, this breaks protocol due to the additional 8-bit timestamp in the updates.

-------------------------

