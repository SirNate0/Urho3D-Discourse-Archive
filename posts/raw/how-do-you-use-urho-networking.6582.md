Eugene | 2020-11-29 09:24:54 UTC | #1

I'm not asking how to use Urho networking in general.
I'm curious how you used Urho networking in your games in practice.

What API do you use? Do you use low-level messaging? Do you use remote events? Do you use scene replication? Please link the game if possible: it's important for the context.

I know only one multiplayer game made with Urho and they used 100% custom networing solution.

-------------------------

Modanung | 2020-11-29 10:12:45 UTC | #2

Networking - like UI - is low on my list of priorities for any project: It starts with a concept, from which graphics and gameplay grow together iteratively. Both networking and UI require most parts of a game to be somewhat set in stone. I've done some experiments, and what Urho provides seems to suffice for in-game purposes. However, *properly* testing its functionality is tricky without collaboration. [spoiler]Since I am only a single player.[/spoiler]

One thing that seems crucial yet not included with the engine is some form of matchmaking. Nobody wants to paste IPs around. And although I understand this to be somewhat out of scope for an _engine_, it may be one of the reasons people use non-Urho solutions that _do_ come with this functionality. In my view however, these often seem somewhat bloated and dependent on centralized services. Someday I hope to use a database hosted on the LucKey Productions website to connect players through  in-game lobbies.

I've also fantasized about having some protocol definition(s) that could associate links with games. These could then be sent or posted as a form of invitation. Something like magnet links for games.

-------------------------

Modanung | 2020-11-29 13:07:38 UTC | #3

It might also be nice to have something in-house akin to Steam/Battle.Net that could be used to browse/install available games (including prototypes), find other players, chat and start/share matches.
And not be [spyware](https://spyware.neocities.org/articles/steam.html) of course, or provide any, for that matter. It might even come with the possibility of scheduling/announcing matches on a public [calendar](https://gitlab.com/Modanung/ChronoCal). This could also be used for continuously adding new coop chapters on a regular basis, instead of thinking in terms of expansion packs.

-------------------------

Modanung | 2020-11-29 13:09:41 UTC | #4

I see how core devs like to focus on the engine, but it helps to *understand* we're inside an ecosystem.
Without a setting, you're just running isolated experiments, which - rightfully - *avoids* complex relations.

-------------------------

JSandusky | 2020-12-01 03:39:43 UTC | #6

So nobody actually read the prompt.

---

I mostly used the lower level stuff, down to just interacting with CivetWeb itself for websockets and HTTP. HTTP for embedded debug-server, web-sockets for angelscript debugging.

In a prototype that did use networking I also mostly relied on remote-events aside from the default replication. I really didn't care for the `Controls`, it was needlessly limited and didn't bring anything for how limited it was (such as prediction or state tracking) - even for a prototype I ended up expanding that into something very very fat and then having to widdle it down before sending it off.

Only 1 game (that is probably being played right now) I've made in Urho actually used networking, but it was done just before the SLikeNet move (it was the reason I did the initial RakNet work because kNet didn't have the guts needed for LAN discovery and adding it was going to be hell) and that also used mostly remote-events but `controls` were less of a problem because it was targeted onto older generic Sega-based racing hardware for the Cape-verde arcade market. So it was really a LAN game as there was a hub machine with the local router and the other machines are plugged into that. So networking wasn't much of a hassle there since latency was almost a total non-issue.

IMO, the controls stuff is messed up. It doesn't make sense given that Urho3D doesn't really do much of anything fantastic regarding state. It's not saving state, it's not rollback capable, it's just ... *meh - here's this packet of generic data where we decided some info is sort of important, have at it bro!* Just make it a generic VariantMap then and add some basic delta capabilities to VariantMap.

-------------------------

