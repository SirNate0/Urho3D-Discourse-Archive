WangKai | 2017-09-15 05:56:33 UTC | #1

A dumb question: how can I register extra handler while keeping the original one there.
When I `SubscribeToEvent` the old one will be removed, that's the problem.
This is useful e.g. when we want to add some behavior for UIElement.

Thanks.

-------------------------

weitjong | 2017-09-16 06:10:56 UTC | #2

I think this is intentional based on the comment in the Object::SubscribeToEvent() method. You have to ask Lasse why the old event handler is being removed first, but I could imagine it is done for performance reason. I think you can work around it by registering your own event handler which works like an internal event dispatcher. And then subsequently you can then register one or more "behavioral action" or whatever you want to call it to your own internal dispatcher that keeps all the registered actions.

-------------------------

cadaver | 2017-09-18 08:08:15 UTC | #3

The limit of one handler per receiver + event type is just to simplify the housekeeping related to it, and making unsubscription (especially in script, where you don't have access to the actual C++ handler object) straightforward. You could modify the engine with multiple handler support if you wanted. But yes, I too would recommend an internal dispatcher.

-------------------------

WangKai | 2017-09-17 02:26:06 UTC | #4

Thank you guys for the response :yum:

I can understand. If we have multiple handlers, we can listen from script side to events which have already been handled by C++. By this approach, we can "extend" / "modified" some objects' default behaviors though sounds like hack. I will try other ways before I modify the C++ code.

Cheers!

-------------------------

