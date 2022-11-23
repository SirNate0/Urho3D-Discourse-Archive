fnadalt | 2018-08-20 01:39:33 UTC | #1

Hello. I've been playing around with scene replication. After I start the server, I Remove() some replicated node. After that, I start a client connection, but the node I had removed shows up there. From the server side, I removed the node by: Node@ node = scene.GetChild("x"); node.Remove() (World.as:173). 

Docs say: * When a client is assigned to a scene, the client will first remove all existing replicated scene nodes from the scene, to prepare for receiving objects from the server. This means that for example a client's camera should be created into a local node, otherwise it will be removed when connecting.

I thought the client would remove the replicated node, so then it wouldn't load it from a server scene where it was removed first!

Help!

"World" project:
https://drive.google.com/open?id=1chko8MpacAUgmSWMnhY0dTEI18wkmxX_

-------------------------

Miegamicis | 2018-08-20 15:59:23 UTC | #2

Hi!

I was able to run your samples and indeed saw this issue. This does look like a valid bug in the networking flow. Could you create new issue on github? I will take a look at this.

-------------------------

fnadalt | 2018-08-20 12:53:52 UTC | #3

Does not happen with displacements made BEFORE client connection, or other stuff done AFTER. Haven't tried anything else so far

-------------------------

Miegamicis | 2018-08-20 16:27:08 UTC | #4

I think I managed to trace down the problem.
Could you please test it against this branch: https://github.com/urho3d/Urho3D/tree/network-replication-fix ?

-------------------------

Modanung | 2018-08-20 22:40:50 UTC | #5

Isn't `Scene::Clear(bool, bool)` what you're looking for?

-------------------------

Modanung | 2018-08-22 08:20:09 UTC | #6

Which would mean **will** must be replaced by **should**.
[quote]
...the client _should_ first remove all existing replicated scene nodes from the scene, to prepare for receiving objects from the server.
[/quote]

-------------------------

Miegamicis | 2018-08-22 08:49:57 UTC | #7

But replicated node/component means that it should be handled by the server only. In the described scenario this is not the case and I don't think that it should be done manually.
When server creates scene on the fly and sends it to clients, client connection will automatically remove all replicated nodes from the scene that was assigned to connection: https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Network/Connection.cpp#L1530

This issue appears only for the server scenes which are loaded from the files, filename is also passed to the clients and they try to load the same scene from their local filesystem. I guess someone just forgot to clear the scene afterwards so that's what I did in the fix.

-------------------------

Modanung | 2018-08-22 12:28:06 UTC | #8

I remain doubtful because I somehow think there might be cases imaginable where this generalisation could be unwanted. But my experience on the subject (so far) is insufficient to make this judgement. :face_with_raised_eyebrow:

-------------------------

Miegamicis | 2018-08-22 12:51:21 UTC | #9

I also think that there may be cases where this behavior is unwanted. But I would still say that this fix is needed just because the scene on the `Connection` class should be handled the same way no mater if it's created on the fly or loaded from the file.

-------------------------

fnadalt | 2018-08-22 16:35:17 UTC | #10

Scene::Clear(bool, bool) did the trick. Replicated nodes should be deleted open client connection, within the client scene, in order to make sure deleted replicated nodes on server are not present. That was my case. If there's a better approach... By the way, when a made an experiment in NinjaSnowWar, by adding a replicated box and removing it before any clients connect, it worked. In my app it didn't. The reason was that Octree component in the Ninja app was local, and in mine replicated, so something happened that the client viewport went black. I fixed that by manually changing the ids of that component to be local. The editor doesn't allow edit the id.

-------------------------

Miegamicis | 2018-08-23 06:30:03 UTC | #11

Did you manage to test out with the fix provided? https://github.com/urho3d/Urho3D/tree/network-replication-fix

Just so I know if I can close the ticket

-------------------------

fnadalt | 2018-08-23 10:54:21 UTC | #12

Yes, my comment is based on having tested the fix. Scene::Clear removes al replicated nodes. The Editor inits with the Scen node and its main components (octree ...), as replicated and cannot be modified within the Editor. So they are removed too. Manually editing the scene xml to make them local fixed that and works fine.

-------------------------

