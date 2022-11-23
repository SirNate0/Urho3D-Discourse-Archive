Modanung | 2017-01-02 01:07:03 UTC | #1

[i][url=https://gnunet.org/]GNUnet[/url] is a framework for secure peer-to-peer networking that does not use any centralized or otherwise trusted services. The framework offers link encryption, peer discovery, resource allocation, communication over many transports (such as tcp, udp, http, https, wlan and bluetooth) and various basic peer-to-peer algorithms for routing, multicast and network size estimation. GNUnet's basic network topology is that of a mesh network.[/i]

For some reason this seems like a perfect solution for gaming to me. Has anyone here heard of GNUnet before and considered this?
I may be talking gibberish.

-------------------------

Enhex | 2017-01-02 01:07:03 UTC | #2

Peer to peer isn't a good solution for games in general.
First of all you increase the data you need to upload & download from once from/to the server to N times from/to every client.
Second, you can't do anything about cheating because every client has authority over the information it sends and none of the other clients is trustable for cheat detection (can false detect).
Third, it makes synchronization much more complex, if not impossible, because there's no authoritative server state to synchronize to.

P2P for games can only work well when you have very few peers, so few that you can count them on one hand.
The only advantage is that the turnaround time between clients is reduced by not having to go through a server.

-------------------------

cadaver | 2017-01-02 01:07:04 UTC | #3

GNUnet is GPL so it cannot be used by Urho.

However the idea of offering either P2P or client-server is good, as long as you understand the ramifications. If we ever were to change the network library then probably the recently open-sourced Raknet would be the best option.

-------------------------

rasteron | 2017-01-02 01:07:04 UTC | #4

[quote="cadaver"]GNUnet is GPL so it cannot be used by Urho.

However the idea of offering either P2P or client-server is good, as long as you understand the ramifications. If we ever were to change the network library then probably the recently open-sourced Raknet would be the best option.[/quote]

I definitely agree. +1 for Raknet

-------------------------

Modanung | 2017-01-02 01:07:14 UTC | #5

Thanks for clarifying.

-------------------------

