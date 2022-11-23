Enhex | 2018-04-09 19:59:04 UTC | #1

Are scene replication updates sent and received as complete state snapshots, or per node updates?

-------------------------

Miegamicis | 2018-04-09 22:46:32 UTC | #2

Correct me if I'm wrong but I believe that the whole scene is sent upon connecting and after that updates are sent only per node. All the update related events are handled [here](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Network/Connection.cpp#L390)

-------------------------

