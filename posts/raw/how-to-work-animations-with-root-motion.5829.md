misc | 2020-01-21 02:30:34 UTC | #1

Was this [root motion patch](https://discourse.urho3d.io/t/root-motion-patch/4464) never merged?

How do you work with animations with root motion? Does urho support it?
For example, godot has something like get_root_motion_transform() which you can use to transform a node.

Thanks.

-------------------------

rku | 2020-01-21 07:43:22 UTC | #2

It wasnt merged because it is just a proof of concept implementation which had unsolved problems. Urho3D has no facilities to work with root motion animations otherwise.

-------------------------

Modanung | 2020-01-21 14:04:02 UTC | #3

[quote="misc, post:1, topic:5829"]
For example, godot has something like get_root_motion_transform() which you can use to transform a node.
[/quote]

`Node`s do have `WorldToLocal` and `LocalToWorld` functions which you could maybe wrap into a convenient `LocalToLocal` operation for your situation that handles whole transforms. This addition might even make a nice pull request, or I could be flabberverbing.

-------------------------

