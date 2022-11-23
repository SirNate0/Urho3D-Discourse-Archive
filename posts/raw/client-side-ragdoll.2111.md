rasteron | 2017-01-02 01:13:09 UTC | #1

I thought this was already tackled before but I cannot find any example or reference to check out. Last time I remembered the server handles the scenes and scripts?

-------------------------

jmiller | 2017-01-02 01:13:10 UTC | #2

Maybe try Node::Clone(CreateMode::LOCAL) ?

I thought I remembered some post on this, but did not find..
[google.com/search?q=ragdoll ... ophpbb.com](https://www.google.com/search?q=ragdoll+site%3Aurho3d.prophpbb.com)

-------------------------

Modanung | 2017-01-02 01:13:10 UTC | #3

[url=http://discourse.urho3d.io/t/ragdoll-replication/1989/1]Ragdoll replication[/url] topic.

-------------------------

rasteron | 2017-01-02 01:13:10 UTC | #4

Thanks guys. For some reason node.Clone(LOCAL) does not do anything, I'm not sure about REPLICATED but I would assume that will replicate all the physics involved. It should be just updating the physics locally and with obviously slighlty or different results on each client.

I think I'm missing a few more steps and btw I'm using NSW as an example to test it out.

-------------------------

cadaver | 2017-01-02 01:13:11 UTC | #5

Looking at the engine code there shouldn't be anything wrong with calling Clone() with LOCAL createmode. However obviously you need to call it on the client because it never gets replicated otherwise. At the same time the original replicated character should be hidden (disabled) from both rendering and physics. I believe you can do that on the client too, and in fact it can be necessary to do so since otherwise there could be a timing problem, if the server hides/destroys the original, but the client hadn't cloned it yet.

The server will probably continue to send updates for the "real" dead character but these shouldn't account for much bandwidth.

Alternative to Clone() is to send a custom message or remote event to the client that contains all necessary data for the ragdoll, ie. the initial positions of all bones.

-------------------------

rasteron | 2017-01-02 01:13:12 UTC | #6

[quote="cadaver"]Looking at the engine code there shouldn't be anything wrong with calling Clone() with LOCAL createmode. However obviously you need to call it on the client because it never gets replicated otherwise. At the same time the original replicated character should be hidden (disabled) from both rendering and physics. I believe you can do that on the client too, and in fact it can be necessary to do so since otherwise there could be a timing problem, if the server hides/destroys the original, but the client hadn't cloned it yet.

The server will probably continue to send updates for the "real" dead character but these shouldn't account for much bandwidth.

Alternative to Clone() is to send a custom message or remote event to the client that contains all necessary data for the ragdoll, ie. the initial positions of all bones.[/quote]

Thanks Lasse. :slight_smile: I seem to notice that almost all functions in the NSW code are handled by the server, except for the scoring part. Can you give more tips on how to properly do this with local clone and SnowWar?

-------------------------

cadaver | 2017-01-02 01:13:12 UTC | #7

You could also have a replicated ScriptObject in the characters which will also do client logic. Now the ninjas have only local script objects which essentially limits them to server only. Won't go into more detail now, I recommend experimenting.

-------------------------

rasteron | 2017-01-02 01:13:16 UTC | #8

Ok thanks for the tip! I would definitely need to experiment more.

-------------------------

