lebrewer | 2021-10-13 18:56:39 UTC | #1

Is there a cron-like scheduler within the engine? For example, every X frames, execute a callback?

-------------------------

urnenfeld | 2021-10-16 09:18:41 UTC | #2

This is not exactily what you want, But I have solved similar problem with this approach:

https://discourse.urho3d.io/t/solved-send-delayed-or-timed-event-sendevent/6619/10

The solution as it is, is not covering cylic events,  could be added in the proccesing function, by readding them after being triggered...

-------------------------

lebrewer | 2021-10-14 14:12:47 UTC | #3

Oh, that's a very interesting approach. Thanks for the snippet!

-------------------------

urnenfeld | 2021-10-16 09:31:25 UTC | #4

You are welcome! Let me know if you add the cyclic capability, I will surely use it too.

Thinking it over it is simplier: you just need to restart the *time* value after expiration&delivery, instead of removing from the Vector. 

However the approach would need also a method for cancelation.

-------------------------

