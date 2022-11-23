cirosantilli-china | 2018-01-25 00:31:17 UTC | #1

It would be less verbose if I could do just:

```
otherNode->SendEvent("eventName");
```

but still be able to access `otherNode` on the handler.

Is there a way?

-------------------------

SirNate0 | 2018-01-27 17:38:25 UTC | #2

Pretty sure it's available from the Context (`GetEventSender()`, I think, though I'm not at my computer now to check).

-------------------------

cirosantilli-china | 2018-01-27 17:39:06 UTC | #3

Thanks Nate. The method is on `Object`, and so present in almost all classes that will handle events.

-------------------------

