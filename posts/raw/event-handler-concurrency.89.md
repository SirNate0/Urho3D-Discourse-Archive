Andy51 | 2017-01-02 00:57:54 UTC | #1

Hi again everyone!

Today I was trying to develop some scripted component with FSM inside. Everything went great if not for some strange bug causing FSM to stop, and eventually I found that two of my events are handled concurrently in the script.
I was expecting that events should be handled sequently, queued in the object, but seems like that's not the case. Here's what happening:
Event1 is sent to the script from another entity in FixedUpdate
While Event1 is being handled, a timer method fires from DelayedExecute (initiated from the same script) and throws Event2 to self for FSM input. But it actually seems to be handled concurrently to Event1, producing most unexpected results in FSM.

I am not familiar with internal engine cycle, so does that mean that Update and FixedUpdate run in separate threads?
And how do i solve the concurrency issue in my case?

-------------------------

cadaver | 2017-01-02 00:57:54 UTC | #2

Think of events as immediate function calls, which may be nested. Update() & FixedUpdate() both run in the main thread and there shouldn't be actual concurrency. ScriptInstance's scene update event handling (which is responsible for Update() being called) proceeds in the following order:

- Execute delayed calls whose timer has expired
- Call script object's DelayedStart() method if necessary
- Call script object's Update() method

FixedUpdate() comes after that, along with the physics world simulation steps (on some engine frames there may be none, when rendering FPS is above physics FPS.)

-------------------------

Andy51 | 2017-01-02 00:57:54 UTC | #3

Oh, i just found that i was actually invoking SendEvent from one of the event handlers, that explains the concurrency effect. But i still cannot agree that sending event will interrupt the current flow to process the handler (especially when sending events to self) is expected behavior. I foresee a huge amount of frustration with a newbies like myself over such nested calls and related bugs. This would definitely cause issues in multithreaded setups also.
Anyway, thanks for the quick reply with the newb questions again :slight_smile: Now i have to think of the other way to somehow organize a queue of events to feed to FSM without relying on native events system...

-------------------------

cadaver | 2017-01-02 00:57:54 UTC | #4

Executing the entire engine frame is based on nested events, as is much of the UI functionality. So having script object event handlers not be nested would require a queuing mechanism and make it behave differently than the rest of the engine, which also would be confusing.

Creating your own "game event" system sounds like a solid approach. I think you might be able to use DelayedExecute() with 0 delay, as those are always queued to the next scene update event.

-------------------------

Andy51 | 2017-01-02 00:57:55 UTC | #5

Ok, thank you! My FSM finally works alright. Though i believe it would be great to introduce a convenient timer interface..

-------------------------

