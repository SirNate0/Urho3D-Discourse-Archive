Leith | 2019-01-30 00:24:21 UTC | #1

Hey guys, I'd just like to confirm something about the order of component initialization.
I found that, due to some subtle dependencies in my current project, that after Loading a scene, I would have to do a bit of housekeeping to fix up broken pointers etc. (mainly weak refs to other components).
I figured that the perfect place to do that was in the DelayedStart method.

Can anyone confirm that the virtual DelayedStart method on Logic components is executed in the same order that the components appear in their scene hierarchy? And can I assume that I have an iron-clad guarantee about the order in which components will be processed generally?
I know that Update and FixedUpdate are called at different rates, but what of the order that components receive events?

-------------------------

