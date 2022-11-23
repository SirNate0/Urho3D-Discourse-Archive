EricDeflandres | 2017-01-02 01:13:40 UTC | #1

IMHO, an important missing sample would be a small peer-to-peer multiplayer game based on CharacterDemo, including a simple C++ or Node.js lobby masterserver with built-in NAT-punchthrough.

That could be a simple game allowing players to choose the blue or red team, and then control walking characters throwing balls at the other players. The last player alive wins the game for his team. Nothing more.

When a player starts the application, he waits to be connected to a lobby. The masterserver decides if he connects him to an incomplete lobby, or creates a new lobby.

The player joins that lobby, and when the lobby is full enough (for instance at least two players in each team), the masterserver decides which player will be the server for the other players, and the game starts. 

If the player which is currently the server for the other players suddenly disconnects during the game, another player in the lobby (i.e. the next in the lobby player list, or the one with the fastest upload speed) transparently becomes the new server for the other players of the lobby, so that the game can go on until one of the teams wins.

The NAT-punchtrough feature could be based on libjingle, or on Keith Johnston's code in Atomic Game Engine.

As simple as this sample game seems, I find very hard to implement it myself, and this sample alone would probably be enough to make Urho3d the best available engine for indie developers like me who want to implement a peer-to-peer multiplayer game...

-------------------------

rku | 2017-01-02 01:13:41 UTC | #2

That sounds like a great idea. Contributions are welcome.

-------------------------

smellymumbler | 2018-10-18 17:27:01 UTC | #3

Here's a good source: https://github.com/ArnisLielturks/Urho3D-NAT-server

IMHO, P2P is ideal for indie development. Not having to worry about an AWS bill every month is just amazing.

-------------------------

Miegamicis | 2018-10-19 10:08:27 UTC | #4

The networking library that the Urho3D currently uses for networking (SlikeNet a.k.a ex RakNet) is pretty powerfull and can actually do these kind of things. I was also planning to create some sort of master server / lobby sample in the future, but I'm not sure when exactly I will do that.

If you look at the library samples you can seen that some of the things that you mentioned are already there, it's just a matter of enabling and tweaking them when building the Urho3D engine itself. https://github.com/SLikeSoft/SLikeNet/tree/master/Samples

Also did a quick googling and found out this sample which shows P2P chat functionality with the same library - https://github.com/antarktikali/raknet-p2p-chat

Note: NAT punchtrough functionality is already supported by the Urho3D engine.

-------------------------

Miegamicis | 2018-10-23 06:21:39 UTC | #5

Took a look around the SlikeNet samples, this one in particular looks like the one that we need: 
https://github.com/SLikeSoft/SLikeNet/blob/master/Samples/ComprehensivePCGame/ComprehensivePCGame.cpp

It shows the master server, lobby, team and P2P functionality with the help of NAT punchtrough.

-------------------------

Miegamicis | 2018-10-25 16:30:10 UTC | #6

Small update on this:

I was able to get the P2P functionality up and running in the Urho3D networking system, only problem with this tho is that the P2P flows differ from the basic Client-Server quite a lot so the code refactoring to support both modes could take some time, probably few weeks or so. On the bright side it all looks really promissing and I hope I will be able to finish this in November.

Feature branch: https://github.com/urho3d/Urho3D/tree/p2p-multiplayer
The code is messy at this point and there might be some memory leaks when connecting/disconnecting between sessions. Also at this stage the code supports only P2P mode, Client-Server mode probably won't work.

-------------------------

Miegamicis | 2018-10-25 19:31:11 UTC | #7

Preview:
https://imgur.com/TASdzCH

Few details about the demo:

1. As a master server I used plain PHP script to parse incoming requests and and save user GUID in the txt file. All the systems periodally make a request to a similar url to retrieve whatever information is  stored in the txt file.  This kind of imitates a real Master server functionality and automates the testing part for me. When someone creates a new session, he basically makes a request to the server to rewrite the txt file content with his/her GUID.

2. All applications join the same session, each participant knows everything about other participants and the one who is in the session the longest becomes the host. There's a small button at the bottom left corner which resets the timer for the application and when it's pressed, someone else becomes a host

3. When the host quits the application, all the peers in the network get the timeout message (by default after 10s) and elect a new host

4. I created a small sphere object which position and linear velocity is changed each frame for the peer who acts as a host, for others the same sphere is affected by the physics engine just so you and I can see the actual effects of being the host.

> Edit: Sorry for the framerate!

-------------------------

smellymumbler | 2018-10-25 23:13:54 UTC | #8

Holy crap, you work fast! That's quite cool. Dying to test it on my router and check the latency.

-------------------------

Miegamicis | 2018-10-26 07:32:22 UTC | #9

Not really that fast, this took me 3 days to get to this point. A lot of trial and error along the way. Still a lot of things that I haven't yet implemented. On the bright side I really enjoy working on this.

-------------------------

Miegamicis | 2018-11-07 19:07:11 UTC | #10

Another update:

Got the sample similar to 17_SceneReplication to work in P2P mode. Besides that also updated the networking to support both modes - p2p and server-client mode. Did quite a lot of small fixes regarding the new networking mode but at the moment it seems stable enough for others to try this out.

Things that I still have to implement:
Lobby mechanisms (all peers agree when they can start the game)
Enable/Disable mid-game joins for the p2p mode
Correct scene load state between peers, just like in regular server-client mode

https://imgur.com/a/GYihgxM

-------------------------

Miegamicis | 2018-11-20 18:52:20 UTC | #11

It's been a while since my last update. In this time I was able to update/add few things:

* Ready event added which gives opportunity for each peer know about other peer readiness
* Mid game joins can now be disabled using `Network::SetAllowedConnections` method.
* Additional networking events added
* P2P and Server-Client mode  switch fixed, bugs fixed relating to the Server-Client mode
* Lobby mechanisms added which are supported by the upgraded Master server:
Code: https://github.com/ArnisLielturks/Master-server
Docker image: https://hub.docker.com/r/arnislielturks/master-server/

  `Search for session` button triggers call to Master server to get the first open session (session, where all the peers are still in lobby). If no open sessions are found, new session will be created and information about it will be posted every 1 second by the host system. If other peer takes over as a host, previous session information will be deleted and new session information will be posted by the new peer. All the sessions which have not been updated in the Master server for 10 seconds will be automatically deleted.


Small demo:
https://youtu.be/7qPPjEHar30

Things in my to-do list:
* AS integrations + sample
* Lua integrations + sample
* Code refactoring so I could finally create a PR


Not sure what to do with the demo that I've got so far. It seems quite big to be included in the engine itself. I' m thinking of creating seperate repo with detailed information how to set everything up.

-------------------------

smellymumbler | 2018-11-20 19:56:59 UTC | #12

It's amazing how smooth this works. :heart_eyes:

-------------------------

Miegamicis | 2018-11-21 09:21:13 UTC | #13

Well it's my local machine haven't yet tested this between multiple systems. But there should not be any difference from the basic Client-Server mode. I could provide compiled binaries so we could all test it without building it + I could use them on seperate machines more easily.

-------------------------

Miegamicis | 2019-11-25 10:37:57 UTC | #14

A while ago decided to split up my PR https://github.com/urho3d/Urho3D/pull/2400 into multiple projects, since the sample in the PR was too advanced and required additional services to be set up. Don't get me wrong, the PR still contains the sample, but a much simpler one.

The advanced P2P sample was moved to this repo: https://github.com/ArnisLielturks/Urho3D-P2P-Multiplayer

Required services for the advanced sample can be set up with the help of Terraform, all required scripts are here - https://github.com/ArnisLielturks/Urho3D-P2P-Multiplayer-Services
Services will be hosted on Digital Ocean with the smallest droplet possible (5$/month) but it should be more than enough to test it out and even host smaller project to production (HTTPS is not set up at the moment). 

If you have any questions or concerns about it, let me know!

-------------------------

