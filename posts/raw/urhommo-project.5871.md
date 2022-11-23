dev4fun | 2020-02-06 03:59:47 UTC | #1

Hello everyone,

Today I am releasing my project of develop a MMORPG (small mmo) using Urho3D (Client and server-side) as open source at my GitHub.

You can check the source code right here:
https://github.com/igorsegallafa/UrhoMMO

I dont have much to say for now, it isn't a consolidated project, but I am trying to do my best for make it happens (for this don't be so critical about it plz hehe).

As the most of people here should know, any game engine is very complicated when we r talking about MMORPG. But when we talk of Urho3D, we mostly talking about a big game framework/library (and for me, this is the best part). This way, anything you want to do, liking to code C++ (my case) and some notion of game, it's really possible.

For this, I had to make a branch of Urho3D to make some modifications on some Urho core codes, like Networking (to accept to connect on multiple servers) and some other things. You can check the branch here:
https://github.com/igorsegallafa/Urho3D/tree/urhommo

I hope this could be useful for someone someday, I am developing as hobby, so you guys can not expect too much from me.

Anyway, thanks for ur time,
Urho ftw.

-------------------------

SirNate0 | 2020-02-06 14:07:41 UTC | #2

[quote="dev4fun, post:1, topic:5871"]
to accept to connect on multiple servers
[/quote]

Could you explain this in more detail?

Also, congratulations on the project, I hope it goes well!

-------------------------

dev4fun | 2020-02-06 16:46:10 UTC | #3

On Network subsystem you can connect on only one server. The problem its on the client side, that I needed maintain the connection with multiple servers (Game Server and Master Server). I know that I could create Network instances for each server desired on client, but what I did was change the Network code for allow this multiple connections and handle it normally.

-------------------------

George1 | 2020-02-06 23:06:41 UTC | #4

This is great stuff.  Most MMORPG do this to reduce down time.

-------------------------

