Eugene | 2017-01-02 01:13:39 UTC | #1

Subj.
I want to use "empty" geometry that will be correctly processed (i.e. skipped) by render systems.

-------------------------

cadaver | 2017-01-02 01:13:39 UTC | #2

Yes, it shouldn't crash or log errors, but you're inducing a waste of time in the render process, since it will actually go to the render queue. More powerful ways to stop rendering is to simply leave a null geometry to the model (assuming it's programmatically created), or set a material with null technique.

-------------------------

Eugene | 2017-01-02 01:13:39 UTC | #3

[quote="cadaver"]Yes, it shouldn't crash or log errors, but you're inducing a waste of time in the render process, since it will actually go to the render queue. More powerful ways to stop rendering is to simply leave a null geometry to the model (assuming it's programmatically created), or set a material with null technique.[/quote]
To create propper switch between proxy billboard and real geometry I need to disable rendering of proxy nearer that switch distance and vise versa.
I thought about using empty geometry with specified LOD distances.
Can I reach my goal without using empty geometries?
Can I trigger some optimization to prevent queuing of such geometries?

PS: Huh, actually I can implement it inside Drawable when prepare batches.

-------------------------

