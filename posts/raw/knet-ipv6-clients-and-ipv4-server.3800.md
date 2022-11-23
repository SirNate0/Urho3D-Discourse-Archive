projector | 2017-12-05 03:37:48 UTC | #1

I'm aware that kNet+ does not support IPv6. I have a question regarding to connectivity between IPv6 clients and IPv4 server.

In a case I choose to use kNet+(and the networking feature provided by Urho) to develop the game server and client, the game client will connect to the server though the server domain name(not IPv4 address). If a game client is in the network that use only IPv6 addresses, would it be able to connect to the game server?

Any help is appreciated.

-------------------------

Lumak | 2017-12-05 17:52:51 UTC | #2

This might be helpful: https://docs.oracle.com/cd/E19683-01/817-0573/6mgc65bd2/index.html

-------------------------

projector | 2017-12-06 22:15:11 UTC | #3

Thank you. here is the additional information I've found :

https://developer.apple.com/library/content/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/UnderstandingandPreparingfortheIPv6Transition/UnderstandingandPreparingfortheIPv6Transition.html#//apple_ref/doc/uid/TP40010220-CH213-SW1

kNet clients that are in IPv6-only network should be able to communicate with IPv4 server if the kNet API is compatible with IPv6 DNS64/NAT64 translation. Will need to find out if kNet is compatible with IPv6 DNS64/NAT64.

-------------------------

SirNate0 | 2017-12-13 02:29:43 UTC | #4

I've been working on creating a pull-request ready setup integrating RakNet with Urho3D based on JSandusky's earlier work (he basically finished it, or at least got it to what seems to be a working state). Since RakNet does support IPV6 (it seems, though I did have to make a few fixes in the IPV6 specific code, mostly adding/moving some includes, so I don't know how well maintained the feature is), I went ahead and tried adding said support. You can see the code here: [https://github.com/SirNate0/Urho3D/tree/raknet](https://github.com/SirNate0/Urho3D/tree/raknet)
There's still a lot of work to do with it, but it might be easier for you to try this than to mess around with kNet.

-------------------------

projector | 2017-12-13 03:57:58 UTC | #5

Thanks SirNate0, it's great to hear that you are working on integration of Raknet with Urho3D. I will try this.

-------------------------

