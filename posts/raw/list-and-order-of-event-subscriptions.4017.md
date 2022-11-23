burgreen | 2018-02-14 20:59:24 UTC | #1

I am trying to run Urho3d in headless mode.

It is crashing during the SendEvent(E_POSTUPDATE, eventData) in Engine::Update().

Besides doing a global search on subscriptions involving E_POSTUPDATE (which I did do), is there a way to discover the complete list and order of subscriptions invoked by a E_POSTUPDATE signal?

I am trying to locate where the crash is occurring. 

Thanks.

-------------------------

Eugene | 2018-02-14 21:27:07 UTC | #2

[quote="burgreen, post:1, topic:4017"]
is there a way to discover the complete list and order of subscriptions invoked by a E_POSTUPDATE signal
[/quote]

Exactly this:

[quote="burgreen, post:1, topic:4017"]
Besides doing a global search on subscriptions involving E_POSTUPDATE (which I did do)
[/quote]

And all inner calls of e.g. `LogicComponent`s

Do you have STR/stack/dump of the crash?

-------------------------

burgreen | 2018-02-14 21:29:46 UTC | #3

In Object::SendEvent(), I can dump receiver->GetTypeName().

This gives me what I am after.

-------------------------

Eugene | 2018-02-14 22:30:05 UTC | #4

Please report the crash or send PR with fix when you find the root cause.

-------------------------

burgreen | 2018-02-14 23:00:17 UTC | #5

It was traced back to a third party add-on component that I had included, which had a postupdate subscription buried in it. There was no issue on the Urho3d side.

-------------------------

Eugene | 2018-02-15 08:43:36 UTC | #6

Great, thanks for follow-up.

-------------------------

