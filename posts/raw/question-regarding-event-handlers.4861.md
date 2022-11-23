Leith | 2019-01-25 00:42:49 UTC | #1


I have noticed that if I have two Components attached to the same Node, and both have subscribed to receive the same event (in my case its E_NODECOLLISION), only one of the components receives the event.

Is this intentional, or is it a bug in the physics collision event dispatcher?
My concern is that if collision events are being intercepted by a component near the top of the node hierarchy, that they won't be able to reach components on nodes further down the tree - I know for a fact it is a problem for two components on the same node, but I am not yet sure if this issue runs deeper.

For example, if we have a large collision hull around our character, and a ragdoll of collision hulls deeper in the same node hierarchy, each with a component subscribing for collision events, I worry that collision events may not propagate to those components.

-------------------------

Virgo | 2019-01-25 02:01:18 UTC | #2

I dont know how event system works in urho3d, but i guess you can only connect an event to exactly one handler of same type.

if you have two handlers `Game::Handler()` and `Game::Handler2()`, you can only connect to one of them, if you try to do with another one, the previous one will be removed?
but you can still connect the same event to other types of handler, like a lambda or `Sample::Handler()`?

-------------------------

Leith | 2019-01-25 02:59:44 UTC | #3

OK I think I've worked out what I was doing wrong.
The Object base class, which implements eventing, does a check for whether same event is registered to same receiver object (called sender, for some strange reason).

I was using OnSetNode( node ) to hook my event up, and passing the event sender object as 'node'. What I needed to do was pass 'this' instead, so that my sender object was unique.

Basically, the two classes were both attempting to register for the same event, using the same receiver object, and that is a no-no.

It was worth looking into, now I understand the eventing system a lot better.

-------------------------

lezak | 2019-01-25 14:07:08 UTC | #4

Sender is an object that sends event, receiver is an object that is subscribed to to this event (so there is no "strange reason" for incorrect naming). 
Events are being send to all objects subscribed to this event by this sender (there's also option to subscribe to event without providing sender) and there is no mecanics for "intercepting" events, so two components on one node can react to the same event. If it's not working for You, it means there is propably something wrong with Your setup.

-------------------------

