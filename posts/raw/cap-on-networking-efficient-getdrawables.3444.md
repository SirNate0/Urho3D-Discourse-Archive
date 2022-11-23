Don | 2017-08-14 01:32:26 UTC | #1

I was working on a Server-Client application with a large amount of nodes. Occasionally, the client would connect but would just have a black screen with no explanation.

I investigated further and noticed that with more than 10K nodes, the server stops transferring any more nodes past 20K or so. This then led to the error. Any idea why this would be happening?

The other issue one encounters when using lots of nodes is a very high octree culling time per frame (Usually upwards of 5 ms). Since 90% of the nodes in my scene are not rendered at the same time, is there any way to make this function more efficient?

Thanks for the help.

Regards,
Don

-------------------------

Eugene | 2017-08-14 16:21:49 UTC | #2

[quote="Don, post:1, topic:3444"]
I investigated further and noticed that with more than 10K nodes, the server stops transferring any more nodes past 20K or so. This then led to the error. Any idea why this would be happening?
[/quote]

Have you tried to debug it?
If you have minimal sample, I can investigate it.

[quote="Don, post:1, topic:3444"]
The other issue one encounters when using lots of nodes is a very high octree culling time per frame (Usually upwards of 5 ms)
[/quote]
`20_HugeObjectCount` has 62500 objects. Do you have the same performance problem here?

-------------------------

Don | 2017-08-23 18:03:29 UTC | #3

I finally got the chance to look into this a bit and I think I found what is causing the issue. As the client connects to a scene with a large number of replicated nodes, the server quickly processes all the nodes and generates update messages. These messages are then given to kNet, which has a cap on it's internal message buffer. If the buffer is already full, then kNet simply drops the message. Therefore, the client never receives the last X nodes.

The problem that leads to is; what is the best approach to fixing it? Any help is appreciated.

About the culling optimization, the performance is just as bad on HugeObjectCount. I just found out about StaticModelGroups, and that is exactly what I was looking for.

-------------------------

Eugene | 2017-08-23 18:13:11 UTC | #4

Please explain what scene do you have and why do you need so much replicated nodes.
Then, if you really need it, try to somehow load scene part-by-part, I don't know... Where does kNet drop messages?

-------------------------

Don | 2017-08-23 18:20:43 UTC | #5

Well right now I am simply testing with 17_SceneReplication sample with extra floor tiles as replicated nodes. (I wanted to make sure it wasn't my code causing some issue).

> Then, if you really need it, try to somehow load scene part-by-part

I'll look into possibilities for this.

> Where does kNet drop messages?

In MessageConnection::EndAndQueueMessages()

    if (!outboundAcceptQueue.Insert(msg))
	{
		if (msg->reliable) // For nonreliable messages it is not critical if we can't enqueue the message. Just discard it.
		{
			///\todo Is it possible to check beforehand if this criteria is avoided, or if we are doomed?
			KNET_LOG(LogVerbose, "Critical: Failed to add new reliable message to outboundAcceptQueue! Queue was full. Discarding the message!");
			assert(false);
		}
		FreeMessage(msg);
		return;
	}

-------------------------

Eugene | 2017-08-23 18:36:44 UTC | #6

Then...
1) You always can tweak the limit to ensure that all your nodes are passed;
2) Urho is balancing between performance and flexibility, it's impossible to get both. If you stuck in performance, you should re-design the scene and lower the capacities.
3) If Urho moves to RakNet, the issue may disappear.

-------------------------

cadaver | 2017-08-23 20:44:53 UTC | #7

Yes, certainly the out-of-the-box networking is not going to work with 20K objects without some kind of culling / interest management added. Which is likely to be application-specific. Typical approach would be to load the static scene from file or generate it procedurally on both server and client, and ensure the actual amount of network replicated objects is manageable (eg. a typical multiplayer game with some player cap, like 64)

-------------------------

Don | 2017-08-23 21:29:10 UTC | #8

That makes sense, as this is definitely an unusual case. I noticed that the network system has a resource package support. Would it be reasonable to procedurally generate the scene server-side, write it to file, add as a package requirement for the (mostly empty) replicated scene, then load it as local on the client?

-------------------------

TheComet | 2017-08-23 21:39:16 UTC | #9

In the game I'm currently developing I also have a situation where I need to send large 2D tile maps (100x100). They way I'm doing it is I have created a separate class called "MapState" which can serialise the tile data to binary. I then have a custom protocol where I dump the entire map and send it to the client, and from that point only send delta updates.

MapState itself does not create any scene nodes, it merely stores tile data. There is a second class called "Map" which clients can create in there scene. It has a method "CreateFromState()", which will take the MapState object and generate local nodes in the scene for each tile.

You may want to also try a similar method. I've found the map is synchronised much, much faster if you send it all in one large chunk rather than sending individual nodes.

-------------------------

cadaver | 2017-08-24 16:10:53 UTC | #10

The package transfer system, especially for dynamically created files, has not been tested much, so your success may vary. Another option could be just stuffing the scene into a custom message or few. If I remember right kNet could tolerate even rather large individual messages.

-------------------------

Don | 2017-08-24 18:11:21 UTC | #11

Thanks for the info! I think I'll at least look into using the package download system, and if that doesn't work out, I'll move to custom messages as you and @TheComet have suggested.

-------------------------

Don | 2017-10-14 08:08:17 UTC | #12

Just an update here after testing. For anyone else who's looking into using a system like this, the aforementioned method does work.

-------------------------

