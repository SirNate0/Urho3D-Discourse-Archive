Don | 2018-01-20 23:30:23 UTC | #1

I was wondering if, in a server-client system, it is possible to have certain updates trigger only on the server. Global effects, for example, should not be evaluated individually by each client, but rather by just the server. Is there a system in place for doing such a thing?

As a corollary, if I am reading the documentation correctly, physics is evaluated on both the server and client. It says that in order to have it server-side only, you must make all physics components local to the server. Since components themselves cannot be local, is the best solution to make a "physics" node for each object only on the server with no transformations?

Thanks for the guidance.

-------------------------

Eugene | 2018-01-21 12:56:55 UTC | #2

[quote="Don, post:1, topic:3954"]
Since components themselves cannot be local
[/quote]
They can.

[quote="Don, post:1, topic:3954"]
it is possible to have certain updates trigger only on the server. Global effects, for example, should not be evaluated individually by each client, but rather by just the server. Is there a system in place for doing such a thing?
[/quote]
Elaborate, please.

-------------------------

jmiller | 2018-01-21 13:12:25 UTC | #3

Nodes/components created with CreateMode::LOCAL are not network replicated so exist only locally. 'Scene replication': https://urho3d.github.io/documentation/HEAD/_network.html

Here are two of our network programs. They have branches to act as server or client depending on invocation.
  https://github.com/urho3d/Urho3D/blob/master/Source/Samples/17_SceneReplication/SceneReplication.cpp
  https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scripts/NinjaSnowWar.as

Replication including physics is server-authoritative not [url=https://discourse.urho3d.io/t/bi-directional-scene-replication/439/3]bi-directional[/url]. NinjaSnowWar running in client mode does only send Controls to the server, not change physics. But running in server mode, it receives those Controls to drive physics.

-------------------------

Don | 2018-01-21 19:45:07 UTC | #4

After checking the documentation you are both right, components can be local. I forgot that creation of components is a function of Node. Oops.

[quote="jmiller, post:3, topic:3954"]
Here are two of our network programs. They have branches to act as server or client depending on invocation.
[/quote]

Right now the solution I am using is identical to the branching seen in sample 17, where a server connection is tested for. It certainly works, but I was wondering if there was a more elegant way of doing this. Specifically, I was looking for an update event that is sent only on a server. If the way I am doing it is the correct way, I have no problems with this.

[quote="jmiller, post:3, topic:3954"]
Replication including physics is server-authoritative not bi-directional. NinjaSnowWar running in client mode does only send Controls to the server, not change physics. But running in server mode, it receives those Controls to drive physics.
[/quote]

I understand that replication is server authoritative, which would include physics, but based on the profiler it seems that physics is evaluated anyways on the client (and then overwritten). From the documentation on network replication, it is stated:

> To cut down on the needed network bandwidth the physics components can be created as local on the server: in this case the client will not see them at all, and will only interpolate motion based on the node's transform changes. Replicating the actual physics components allows the client to extrapolate using its own physics simulation, and to also perform collision detection, though always non-authoritatively.

It seems that creating all physics objects as local is best for bandwidth, but it would also seem better for CPU performance. In my current project physics is a huge performance concern, so I would love to have this running on the server only. Are there any downsides to this approach? Maybe some sort of physics latency? If not, I'll switch to this.

[quote="Eugene, post:2, topic:3954"]
Elaborate, please.
[/quote]

Gladly. Specifically I have a FixedUpdate() function on a LogicComponent. This update modifies attributes of other Nodes and Components in a non-deterministic way. In order for this to work correctly, the code must only be run on the server, and have the resultant changes replicated to each client to avoid desync. It seems from carnalis' response that the proper way to do this is to check for the existence of a server connection.

Big thanks to both of you for clarifying, and sorry about the wall of text.

-Don

-------------------------

Eugene | 2018-01-30 08:51:05 UTC | #5

[quote="Don, post:4, topic:3954"]
Gladly. Specifically I have a FixedUpdate() function on a LogicComponent. This update modifies attributes of other Nodes and Components in a non-deterministic way. In order for this to work correctly, the code must only be run on the server, and have the resultant changes replicated to each client to avoid desync
[/quote]

Sorry, I forget to answer here.
I'd make two separate scenes/prefabs: one for offline and server, one for client. Only the first scene would have a component with such logic.

Well, in the perfect world I'd make determenistic "events".

-------------------------

