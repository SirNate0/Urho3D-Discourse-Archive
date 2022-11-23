Enhex | 2017-01-02 01:03:50 UTC | #1

Hi,

I would like to suggest adding client to server and server to client file sending API.
I did find this suggestion: [github.com/urho3d/Urho3D/issues/476](https://github.com/urho3d/Urho3D/issues/476) though I think it would be better to have a dedicated API for sending files, just like sending packages.
The thing with packages is that they're overkill for sending single files, adding arbitrary complexity to the task. While using messages to send files is probably simpler, it doesn't clearly express the intention.

It would be nice to have functions like:
SendFile()
BoardcastFile() - server only

A use case for example is something like Counter-Stike's player sprays. The spray's texture will need to be sent from the player to the server and then from the server to the rest of the players (no p2p).
Another use case example is Garry's Mod duplication tools, which let players save things they build and upload them to servers they join.

-------------------------

cadaver | 2017-01-02 01:03:50 UTC | #2

Packages are intended for a collection of resources needed for example by a level, so you're right that they're not the right tool for sending just a single file.

Personally I stand by what I said in the issue and won't be working on this. But I'm not preventing anyone else. I could just see the API getting partially muddled in the areas of "who is allowed to send what", "where it's saved", "how the file is advertised to other clients" and I believe application-specific code can answer those better.

-------------------------

rasteron | 2017-01-02 01:03:51 UTC | #3

I agree with Lasse here. Enhex, this is something specific to a game, genre or type of game. One method can be: Urho3D has Civet Web and HTTP requests so I don't see any problem doing a quick implementation on this feature.

-------------------------

cadaver | 2017-01-02 01:03:51 UTC | #4

For something that's done between the game clients and game server you don't even need to go to civetweb or http requests or anything like that. As long as the file is not ridiculously large (let's say several megabytes) all you need to do is to stuff it into a reliable ordered kNet message and kNet will handle fragmenting it to packets as appropriate. And if it's so large that kNet chokes on it then you can do a manual splitting into several reliable messages.

-------------------------

