Enhex | 2017-01-02 01:06:15 UTC | #1

I have a rigid body character controller player.
I start a server and connect with a client.
The client and the server have a player each.
The client sees the following thing:
When the server player moves, it's rotation snaps and freezes to some angle, and it's location drifts.
After the player stops moving for some time, it's rotation and location get corrected. When it moves again, it goes back to being incorrect.

What is causing it? It seems like when the rigid body is active the node replication gets messed up.

-------------------------

cadaver | 2017-01-02 01:06:17 UTC | #2

Can you post code that you think is relevant? I don't think I've seen this kind of issue in the server-authoritative rigidbody replication examples (SceneReplication, NinjaSnowWar).

One thing that may be throwing things off is the interaction with the SmoothedTransform component, which is automatically created to client nodes; it stores the last received pos/rot from server as something to interpolate towards, instead of applying right away. This is for cases where updates are infrequent or choppy, or the rigidbodies have been set to local so that the client never sees them. I just pushed a change to master that should allow you to simply remove the SmoothedTransform from your client node: after that the pos/rot starts applying to the node & rigidbody directly, without interpolation.

-------------------------

Enhex | 2017-01-02 01:06:18 UTC | #3

Yeah I haven't seen it when I first tried the replication system.
I'm not sure what could've caused it, the rot/loc stuff is pretty simple  - a node with a character controller component. the character controller updates the physics stuff and the transformation gets replicated by the node.

I noticed that in both SceneReplication and NinjaSnowWar the server doesn't have a local player, all the players connect to it as clients.
In my case I didn't create complete separation between the server and client - the hosting server is also a server-side player, and it's the only player that suffer from this problem.

If that's the problem - is there a way to create complete separate server and client from network perspective on the same instance of a game, and connect to the server?
The goal is to start a server and join it without having to start two programs, like most MP games do. It's a really important UX feature.

BTW I switched to my own naive full state transfer network system and the problem doesn't exist there. It might suggest it has nothing to do with the player's state, but something else inside Urho's network system that causes it.

-------------------------

cadaver | 2017-01-02 01:06:18 UTC | #4

Having or not having a local player shouldn't be of consequence. The server and client parts of the networking are logically separate and can be used within the same Urho instance, even though there is just one Network subsystem.

There are two basic ways to implement hosting while playing:

1) On the host there's just the authoritative server scene. The host player is controlled there directly and the view is rendered using this scene.
2) Create 2 scenes on the host. The server scene, which is not rendered, and the client scene, which the host player uses to connect to the server using localhost address. The client scene is rendered. Note that there is just one Urho context and no multithreading going on.

Way 2) consumes more performance and memory but can be easier to implement as connecting to a remote server or connecting to the locally hosted server can use same logic flow.

-------------------------

