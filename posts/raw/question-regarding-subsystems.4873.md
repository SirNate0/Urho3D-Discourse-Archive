Leith | 2019-01-28 05:49:18 UTC | #1

Can someone please define for me exactly what a Subsystem is, and what requirements it has, other than deriving from Object, and being a Singleton? What makes Subsystems different to Components (which require a factory, and so are not singleton), and maybe show me an example use-case?
In my uni days, a subsystem was a container for components of the same type, and provided base logic to deal with components of that type. I am not exactly certain how subsystems work in Urho3D - is it just a replacement for static stuff? How does a subsystem object behave differently once registered, other than that we can query for its pointer? How is this different or more efficient than using static singletons?

-------------------------

Modanung | 2019-01-28 08:46:20 UTC | #2

I believe a subsystem is simply an `Object` registered as such, after which all `Object`s can reach it.

-------------------------

Leith | 2019-01-29 03:30:17 UTC | #3

That was pretty much the answer that I had expected.. thank you !! :)

-------------------------

