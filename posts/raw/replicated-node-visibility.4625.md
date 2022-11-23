extobias | 2018-10-29 17:09:58 UTC | #1

Hi, it's possible to create a replicated node and only show it on certain clients?
Thanks in advance.

-------------------------

Miegamicis | 2018-10-30 07:32:52 UTC | #2

By default this kind of feature is not shipped in with the engine. But you can achieve that by adding custom data to replicated nodes and decide to show/hide the on the client side.

-------------------------

Miegamicis | 2018-10-30 07:34:48 UTC | #3

From the docs:

https://urho3d.github.io/documentation/HEAD/_network.html
**Scene replication**
* A node's [user variables](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_node.html#a4b1a508ba21834d35b46da264e915de3) VariantMap will be automatically replicated on a per-variable basis. This can be useful in transmitting data shared by several components, for example the player's score or health.

-------------------------

extobias | 2018-11-01 22:58:50 UTC | #4

Thanks for your answer
That's a good one, I'm already using node user var. Using this aproach I should have to manage the node and as doc said
"After connecting to a server, the client should not create, update or remove non-local nodes or components on its own. However, to create client-side special effects and such, the client can freely manipulate local nodes."

When I need to remove the node, the client should inform this to the server?
Thank for your response

-------------------------

Miegamicis | 2018-11-02 11:00:26 UTC | #5

I would do something like this:

1. Create replicated node
2. Create my custom replicated component
3. Custom component waits for the specific event from the server and after receiving it creates the StaticModel and other components with the LOCAL state.

In this scenario the base replicated node will still receive position, scale, rotation and other details about it but you could decide who sees it and who doesn't by sending the event only for specific connections.

-------------------------

extobias | 2018-11-02 11:02:48 UTC | #6

That's perfect, thanks

-------------------------

