dev4fun | 2018-02-03 21:25:59 UTC | #1

Hey, Im doing my server side and client side using Urho3D, but in the middleway, I got a problem.. I will separate server side on two servers, Login Server and Game Server. This way, game will need to have two networks, one to connect with Login Server, and other to connect with Game Server.

The problem its: Looking for the Urho3D samples, I see that use **GetSubsystem<Network>()** to retrieve Network pointer, and this way I can connect in just one server. It isnt that I want.

Solution would create two Networks objects, but how to do this? Im asking because of I dont know how the events would work this way...

Thanks.

-------------------------

Eugene | 2018-02-03 21:33:49 UTC | #2

Try to use `Connection` object directly for Login Server.
Never tried it on my own tho.

-------------------------

dev4fun | 2018-02-03 21:35:39 UTC | #3

[quote="Eugene, post:2, topic:3984"]
Connection
[/quote]


Hmm maybe. Do u know if I can create new **SharedPtr**'s of Network?

-------------------------

Eugene | 2018-02-03 22:20:07 UTC | #4

Well, theoretically you _can_, with some code tweaking... Doesn't mean that this would work good. Doesn't mean that you _need_ it at all. Probably not. `Network` provides high-level scene replication, so it is both Game Server and "Game Client". You cannot have two of them w/o running into troubles. Don't need it in almost 100% of use cases.

-------------------------

dev4fun | 2018-02-03 22:22:38 UTC | #5

Got it. I was checking Urho3D::Network class, and I believe that will be easy to make a modification on this to works how I want.

-------------------------

dev4fun | 2018-02-03 23:33:42 UTC | #6

Hahaha I got some problems when I tried to do this, dont know why, but I dont have a good knowledge on Urho3D yet.

If someone have interest to do this, Im looking for on this topic:
https://discourse.urho3d.io/t/paid-mod-on-network/3985

-------------------------

Eugene | 2018-02-04 08:30:51 UTC | #7

Are there any problems that don’t allow you to just create multiple connections?

-------------------------

dev4fun | 2018-02-04 21:47:02 UTC | #8

Solved! I'll be testing the code for now and if all works good I release on forum for everyone.

Thanks for your help.

-------------------------

