evolgames | 2022-05-12 22:06:15 UTC | #1

I've been following this tutorial/module instrcutions for using steam's p2p servers with a godot game and was wondering if this would work with urho. It uses their api and lets you create a lobby, invite friends via steam, and connect for multiplayer without much other nonsense. No natpunchthrough, paying for servers, or anything else like that.

Has anyone used steamworks api with urho? It should be possible right? Just curious.

https://www.youtube.com/watch?v=si50G3S1XGU
https://gramps.github.io/GodotSteam/howto-module.html

-------------------------

JSandusky | 2022-05-13 03:49:55 UTC | #2

Yes. It's doable. The NAT stuff is dealt with by Steam Relay where you communicate via SteamID or fake-ips (provided from the Steam API). Might want to ping @Enhex as it's possible he's poked his head there.

Lobbies and the rest are technically a separate thing that interacts with networking and UI. Urho3D has nothing in place that you need replace for it so it's ground-up work. Lobbies have never existed as far as it is concerned, so roll your own thing.

The Urho3D networking code is amongst the easiest to overhaul in the codebase for any change because aside from just changing types around here and there porting it is just overhauling a few functions, the Connection class, and the message-loop (lots more of course, but the bulk of the work is there). kNet -> old RakNet took a few days to proof of function (@SirNate0 iirc carried the work forward to SLikeNet and probably invested more time than that ensuring function). The data-ghosting, interpolation, and the like remains the same regardless of what communication API you use.

It gets harder if you need these features for non-Steam builds. You need to provide an intermediate authentication server to access Steam APIs to dish out tokens so your network traffic can cross steam relays.

-------------------------

Enhex | 2022-05-13 10:10:40 UTC | #3

Steamworks is basically a C++ library and Urho being a library itself makes it very easy to integrate it.

https://partner.steamgames.com/doc/sdk/api

-------------------------

evolgames | 2022-05-14 22:02:38 UTC | #4

You know what, I found this:
https://2dengine.com/?p=sworks

Since I use Lua scripting for Urho this should work. I'll give it a try. It would basically set me up as far as I got with GodotSteam.

-------------------------

