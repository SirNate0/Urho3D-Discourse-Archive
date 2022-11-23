George1 | 2017-07-27 12:05:47 UTC | #1

Hi guys,
Is the SendEvent occurs in the current Frame or next subsequence frames?

Thanks

-------------------------

Eugene | 2017-07-27 12:50:40 UTC | #2

SendEvent occurs immediately.

-------------------------

George1 | 2017-07-28 03:38:34 UTC | #3

Cool, thanks for the info.


One more question, can I control which components can have variable time step, which component can have continuous time step?

I have made discrete time step in my framework code. But it is not pretty. It would be good to know if the engine already support these internally. As it would likely be more optimised than mine. 

Thanks

-------------------------

Eugene | 2017-07-28 09:23:15 UTC | #4

I know what is _fixed_ and _variable_ time step.
Please explain what's "continuous" and "discrete" time step.

-------------------------

Modanung | 2017-07-28 09:30:53 UTC | #5

I would interpret "continuous" (every frame) as _variable_ and "discrete" as _fixed_.
But technically speaking it all happens at intervals, making all updates discrete by definition.

-------------------------

George1 | 2017-07-28 10:29:32 UTC | #6

Slightly different definition.

Continuous in this case assume very small interval (e.g. every frame), like what the engine is doing right now. Discrete means large interval.

Sorry, I use the incomplete term here. What I mean is discrete random interval, or interval that changes with time and can be controlled by the user between rendering frame.

Thanks

-------------------------

Eugene | 2017-07-28 11:43:30 UTC | #7

If you want to call something with fixed delay you should either accumulate time in Update and manage calls on your own or use physics updates that occur exactly every 1/60 seconds (by default)

-------------------------

