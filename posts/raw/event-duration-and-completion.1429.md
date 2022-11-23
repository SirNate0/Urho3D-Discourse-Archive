sabotage3d | 2017-01-02 01:07:41 UTC | #1

What is the best practice with Urho3d for tracking duration and completion of an event? Is there a way to access post, pre and during the event?

-------------------------

cadaver | 2017-01-02 01:07:41 UTC | #2

Urho doesn't define such concepts for events. An event is just a one-off mechanism to transmit information, similar to a function call.

Some systems decide to fire separate start/end events, for example physics collision start/end, or button press start/end, but in the context of the event system itself there is no relationship between them, and what you decide to do with them depends completely on your own program logic. For example you could reset a Timer when you get a start event, and check the timer value when you receive the end event.

-------------------------

sabotage3d | 2017-01-02 01:07:41 UTC | #3

Thanks cadaver, I will create my own logic.

-------------------------

