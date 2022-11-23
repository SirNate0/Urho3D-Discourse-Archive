namic | 2017-01-02 01:12:14 UTC | #1

About a year ago, on reddit, i've seen this comment about Urho:

[quote][b]friesencr:[/b]
I am one of the Urho contributers. I am not its primary author but I can try answer any questions anyone has.
Also some interesting features that are ommitted from our feature list is hot resource reloading via filesystem watchers, the new asyncrounous resource loader, and multiplayer scene replication. The entire engine is driven by a robust reflection system which powers the network serialization and binary/xml serializers.[/quote]

Is there any documentation on the multiplayer scene replication?

-------------------------

1vanK | 2017-01-02 01:12:14 UTC | #2

[urho3d.github.io/documentation/H ... twork.html](http://urho3d.github.io/documentation/HEAD/_network.html)

-------------------------

namic | 2017-01-02 01:12:22 UTC | #3

That seems very scarce. Is there any simplistic demo with just primitives moving around, using the engine features, such as interpolation, replication, etc? Sorry for all the questions, but coming from a Q1-based engine (Darkplaces), i'm trying to understand the basic netcode that Urho already provides.

-------------------------

1vanK | 2017-01-02 01:12:23 UTC | #4

[quote="namic"]That seems very scarce. Is there any simplistic demo with just primitives moving around, using the engine features, such as interpolation, replication, etc? Sorry for all the questions, but coming from a Q1-based engine (Darkplaces), i'm trying to understand the basic netcode that Urho already provides.[/quote]

Urho3D\Source\Samples\17_SceneReplication

-------------------------

