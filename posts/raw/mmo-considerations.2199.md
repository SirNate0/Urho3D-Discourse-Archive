looka | 2017-01-02 01:13:52 UTC | #1

Hi all,

I was wondering how suitable would Urho3D be for MMO implementation?

From what I read up about Urho3d so far, I was thinking server could be headless, running whole world in one Scene.
It seems that 32bit positioning would be more than enough, and physics and network could work fine with proper networkpriority and octree.
I would also like to keep client thin as possible, delivering content mostly via networked Packages.

But few things worry me.
First, new nodes in and out of scene would have to be sent to every other regardless of network priority? Maybe this is a non issue, as it is a small message, but still it bothers me that all players on one side of the world need to be notified immediately by every new or removed node or player on the other. Any way around this?

Second, more worrisome, I do not want to force all users to get all content packages in the scene, but rather have it sent to them by their proximity, similar to network priority (distance). As I understood it, package must be declared required for a scene and then it gets replicated. Is there a way to send a package only by some arbitrary logic to each client? I guess I can create my own message type and just SendMessage, but it seems shame not to use Packaging features.

Is it a problem for a scene to have tens of thousands of nodes? Or hundreds of player client connections? Network fps could be low 4-5fps, and most replicated nodes and players would always be outside of replicated distance for any player.

Or is there maybe different approach to use multiple scenes on server (e.g. for each player) and then do some manual server side node sync for each? Or maybe create separate scenes on client just for world/content delivery and render both in parallel? 

Other than these few unknowns, I think Urho3d could be perfect for it!  :smiley:

-------------------------

cadaver | 2017-01-02 01:13:52 UTC | #2

Welcome to the forums. 

The networking part has been written as a guess of what may be useful in a server-authoritative multiplayer game. It has been tested by rather small applications, like the NinjaSnowWar example. It's somewhat leaning on the idea of a realtime action game with a small(ish) amount of players.

For MMO use, I recommend to be at least prepared to roll your own networking solution, if necessary. For any performance figures (number of connections / objects and such), I can only say that try to prototype with as little work as possible, to see if the Urho built-in networking is feasible at all.

About the networked resource packages, this system have been written with the idea of a typical small multiplayer game with a map cycle, the idea being that before joining a map, you get the resources it needs. Urho lacks the concept of "pending" or "waiting" resources, which may pose a problem if you are streaming in the content of a continuous world via packages. In case a package download is late, and you would already need the resources by a game object (for example a StaticModel component), you'll just get an error log print as the StaticModel tries to assign non-existing models/materials, and it forgets those assignments, so it will not retry when the resources actually are available.

In the realXtend virtual world application framework, which was first implemented on top of Ogre3D and then later as a minimal Urho port (see [github.com/realXtend/tundra-urho3d](https://github.com/realXtend/tundra-urho3d)) a custom network-aware asset system was written on top of the underlying engine, and only ready assets would be fed to the engine/renderer. It would also implement its own model component (and other necessary components) that would wait for the assets, and only once ready, would create the renderer-side representation(s).

-------------------------

looka | 2017-01-02 01:13:52 UTC | #3

Thank you for the quick reply!

Ok, so if I understood correctly scene replication as it is would not be well suited, as it is designed for whole and complete scene replication.
But I suppose Urho3d::network class with un/reliable messaging can still be used to stream/download any data to any client, so I could just take it from there?
Have everything run in local scenes on both ends and use networking for syncing them best I can.
Scene node replication and packaged files seem also to be built on top of messaging, but both seem tied to the total scene replication, and I would need to sort of reinvent that so that they are not.

Other way about it perhaps would be to try and keep the current scene replication but:
 1) Also handle new/removed scene nodes with distance factor for each client (wiki does say only "for now" it doesn't  :wink: )
 2) Add "pending resources" flag for (replicated) scene nodes with missing resources to skip rendering and request a package (once package has arrived it clears the flag assigns the resources).
(Apparently, there is already possibility to add packages additionally in the scene later, I suppose that faces same possible missing resources problem.)

Question is which one of the two approaches would be better to pursue, adding a support for partial scene replication per client or abandoning it and reinventing it altogether.

-------------------------

cadaver | 2017-01-02 01:13:53 UTC | #4

Yes, the network messaging itself (using the kNet library) is fairly solid, allowing reliable & unreliable messaging, so building on it should be fine at least for starters. I'm not sure what happens with it when you are running a massive number of connections.

-------------------------

looka | 2017-01-02 01:13:54 UTC | #5

I can do some testing later on about maximum client numbers, but as far as I know there is virtually no limit beside the usual memory and bandwidth. But this seems like high-quality problem which is not very likely to happen in real world.

To be honest I don't feel too happy/excited about implementing my own replication and content delivery protocol. Main reason is that I did that once already (in Marmalade) and while it did work out at the end, I am pretty sure Urho3D does networking way better. Same is certainly also true for 3d graphics and physics, which is also part of the reason of why I am migrating. So now, I would really rather focus on game building than on engine building.

So I would like to try and tweak the Connection/Network a bit to fit my needs. This is what I had in mind:

Basically, hold of creating new nodes before they are close enough by putting [url=https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Network/Connection.cpp#L1146]here[/url] something like [url=https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Network/Connection.cpp#L1214-L1222]this[/url].
Every now and then I would do sort of "garbage collector" for far away nodes and remove them from client scene.

As for content delivery, I do not have clear solution yet. Somewhere [url=https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Network/Connection.cpp#L573]here[/url] I could request a missing package (I'm guessing RequestPackage or something similar). If I am understanding correctly, nodes with missing components are still created and synced (position) but without e.g. geometry component not rendered. Upon receiving it I would need just to apply it to the node and they should automagically appear? 

Please let me know if you think this is feasible, or there is a better way. This way we could have worlds huge, clients thin, high number of players and low bandwidth making it great for MMOs. Hopefully. :slight_smile:

-------------------------

cadaver | 2017-01-02 01:13:54 UTC | #6

Your proposals might work, just make sure that if a client has not created a node or component because it's yet being held, you don't try to send updates to it either. This can be tricky because the creations/deletions are ordered, while updates (specifically latest-data updates like position which can overwrite the earlier data or skip updates with no harm done) are not ordered.

Also, note that rendering is much easier to get "right" in a way that is relatively project or genre agnostic, than networking. Meanwhile there are actual MMO engines with quite high price tags.

-------------------------

