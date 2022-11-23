Leith | 2019-05-26 04:58:06 UTC | #1


The Object::SubscribeToEvent method is public.
Normally, we call it in the context of "this" class, but because it is public, in theory, it can be called on any valid object instance pointer, by any caller, while the actual handler for the event can be also, in ANY class that supports event handling, and by receiver instance.

This implies, in theory, that we can do some funky things with event redirection.
Am I correct, or way off track?

-------------------------

QBkGames | 2019-05-28 00:50:15 UTC | #2

Though my experience with the engine is still limited, as far as I could gather, I think you are correct, the event system is very flexible, any Object derived class can raise any event and can subscribe to any event (allowing you to do "funky things" :) ).

-------------------------

Leith | 2019-05-28 13:03:12 UTC | #3

In theory, any object can subscribe any other object as listener, and delegate the handling of the event to some other instance of some other class - this is very wide open to abuse, I love it!
Not only can we do this, but we can do it any time. Wonderful!

-------------------------

