trillian | 2020-03-17 08:31:32 UTC | #1

Hi all,

since about 3 years I'm working on a game server with Urho3D as the client's game engine. Slowly it is taking some shape, although if you ask me how much is done, I would say 1% :laughing:.

But recently I made it possible to change skills with the client and suddenly it feels a bit more complete :star_struck: see https://devtube.dev-wiki.de/videos/watch/a6c82c9d-aebe-4097-8019-3f186b7330aa

GitHub: https://github.com/stievie/ABx
GameDev.net blog: https://www.gamedev.net/projects/1587-abx
Some videos: https://devtube.dev-wiki.de/video-channels/trill_channel/videos

All the best and stay healthy.
Stefan

-------------------------

Modanung | 2020-03-18 00:06:11 UTC | #2

Are you looking for people to test that Trojan toiletpaper? Or is it too soon? :slightly_smiling_face: 

Following the instructions in the readme I run into the following compilation error:
```
In file included from ../Include/kaguya/state.hpp:17,
                 from ../Include/kaguya/kaguya.hpp:11,
                 from ../abserv/abserv/stdafx.h:86:
../Include/kaguya/lua_ref_table.hpp: In static member function ‘static kaguya::lua_type_traits<std::array<_Tp, _Nm> >::get_type kaguya::lua_type_traits<std::array<_Tp, _Nm> >::get(lua_State*, int) [with T = float; long unsigned int S = 3]’:
../Include/kaguya/lua_ref_table.hpp:380:12: error: ‘res’ may be used uninitialized in this function [-Werror=maybe-uninitialized]
     return res;
```

-------------------------

trillian | 2020-03-18 05:10:39 UTC | #3

I was just very happy that the Skills work the way they work now, and I wanted to share it. I'm not yet sure what to do with the toilet paper :grinning:.

I found the maybe-uninitialized warning of GCC a bit unreliable, but I didn't get it yet in the kaguya library (the Lua binding the server uses). However, I added now -Wno-maybe-uninitialized to abserv.make.

-------------------------

Modanung | 2020-03-18 10:06:31 UTC | #4

I've always wanted to TP the colloseum. :stuck_out_tongue_winking_eye:

-------------------------

Modanung | 2020-03-18 10:53:22 UTC | #5

I tried copying `config.xml` into `Bin/` and `Bin/config/`, but in both cases I still get:
```
Required argument 'host' is missing
Required argument 'port' is missing

Type `dbgclient -h` for help.
```
When running `./dbgclient -host stievie.mooo.com -p 2748` I see this:

![dbgclient|690x386](upload://d8Gdf0sSzIsH2S0CQkVihS5VPcu.png) 
Which disappears when I resize the terminal window.

-------------------------

trillian | 2020-03-18 11:14:38 UTC | #6

You try to connect to the wrong host, change 
```
  <parameter name="LoginHost" type="string" value="stievie.mooo.com" />
```
`stievie.mooo.com` to the host your are running the server, e.g. `localhost`
in config.xml.

This config file should be in `abclient/bin`, it is to tell the game client where to connect to. Only the game client (`abclient/bin/fw`) needs it.

And you seem to use the debug client, which connects to the server and shows some internal states. I wrote this client for debugging the AI.

You may want to run `./fw` in `abclient/bin` instead, which is the game client.

Good luck Stefan

P.S. Yeah the debug client does not react when the size of the terminal changes.

-------------------------

Ka-Wiz | 2020-04-18 04:49:53 UTC | #7

hey there! i'm a fan of ancient greece and guild wars so this project really caught my eye lol

it's awesome that you've been working on it so long and i'm looking forward to the finished product, but i won't hold my breath of course, no pressure lol. looks great so far, putting together different skill builds was the best part of GW and it's cool seeing it in yours!

-------------------------

trillian | 2020-04-18 07:32:35 UTC | #8

Thank you, I appreciate to hear that there would be interest in such a game :heart_eyes:.

I guess someone must pickup the torch, if nobody else does it. GW had so many great ideas, and after so long time there is still nothing that compares to it. It would be a shame if that would be lost some day.

-------------------------

Ka-Wiz | 2020-04-18 21:05:58 UTC | #9

i'm curious, what made you pick ancient greece? the mythology?

-------------------------

trillian | 2020-04-19 06:23:27 UTC | #10

One day I realized that I need a setting for the game. I'm not a story writer and I'm not good at it, so I thought I could pick something existing. I think there are several reasons why this setting is a good pick:
* I didn't want to make another medieval RGP. I think there are not many ancient RPGs, most are located in the Tolkien universe
* It is not copyrightable
* It has a rich mythology

-------------------------

