nergal | 2017-11-17 21:57:29 UTC | #1

Is it possible to somehow control how often the Update function for a logiccomponent is called when registered to listed to update callbacks?

For example if I have a phys-class that handles my physics that I want to update with 30 FPS while the rest should update at 60 FPS?

(or should i handle this manually?)

-------------------------

Eugene | 2017-11-18 10:03:54 UTC | #2

[quote="nergal, post:1, topic:3749"]
(or should i handle this manually?)
[/quote]

Yes, you should add some update throttling or like this.
Beware that once you step aside from pre-render update you have to interpolate manually all values that you compute during fixed update and want to use for rendering.

-------------------------

