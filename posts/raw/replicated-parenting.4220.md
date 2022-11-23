Ka-Wiz | 2018-05-05 17:44:22 UTC | #1

In my project, which uses scene replication, I'm noticing some weird teleport artifacts in the client when nodes have their parents changed on the server. I'm pretty sure this is due to the new position data for the objects being in parent space before the new parent data arrives, ie if I change a node's parent on the server and set position to Vector3::ZERO, in the server that node will be centered on its parent, but in the client the node will teleport to world origin, and stay there until the next position update is sent.

I'm curious if I'm correct about why this is happening, and if anyone has encountered this before and has ideas for a workaround!

-------------------------

