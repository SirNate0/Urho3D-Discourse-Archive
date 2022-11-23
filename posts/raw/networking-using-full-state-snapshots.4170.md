Enhex | 2018-04-13 21:25:10 UTC | #1

Currently Urho's scene replication sends individual updates at the node level.

This doesn't combine well with running prediction on the client since the prediction can't start from the same state the server had.

Adding an option to the network system to send updates in complete snapshots, and sending an event when a snapshot is received would solve that problem.

In case anyone needs a quick & dirty solution I implemented something simple that achieves that:
https://github.com/Enhex/Urho3D-State-Snapshot

It doesn't have any optimizations like delta updates, so it's still desirable to provide this feature in Urho.

-------------------------

George1 | 2018-04-14 03:24:42 UTC | #2

The way game server do that is sending a time to client or client sending time to server in it's packet. This prevent speed hacking etc.

-------------------------

Enhex | 2018-04-14 09:51:19 UTC | #3

Do what?

Sending timestamp won't help with prediction.

-------------------------

