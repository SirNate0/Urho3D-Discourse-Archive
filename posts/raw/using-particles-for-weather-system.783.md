rogerdv | 2017-01-02 01:02:51 UTC | #1

Is it possible to simulate rain or snow with the current particle system? How could I do it?

-------------------------

boberfly | 2017-01-02 01:02:51 UTC | #2

Fairly easy, just transform a node with an emitter component randomly in X & Z and make it spawn snow or a rain image that transforms in negative Y, maybe constrain the random min/max to the bounding box of a zone. I did this for my app but it was a locked camera which could dolly with the accelerometer so I only needed to transform the emitter randomly in the X axis only, without a zone.

You may just need to experiment with the particle emitter for awhile:
[url]http://urho3d.github.io/documentation/1.32/_particles.html[/url]
[url]http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_particle_emitter.html[/url]
[url]http://urho3d.github.io/documentation/1.32/_zones.html[/url]

-------------------------

devrich | 2017-01-02 01:02:52 UTC | #3

[quote="rogerdv"]Is it possible to simulate rain or snow with the current particle system? How could I do it?[/quote]

 :ugeek: Ahhh the memories.  This is something I've "sorta" done before in another engine many years ago.

I too need to have a weather particle system of some kind in place for my game idea as well and since everyone has been helping me a Lot I figure i'll try to do something to give back. ( this experience will also help me get more familiar with Urho3D's inner workings like I should do anyway )

I don't know "for sure" if I can do the same thing I did years ago with Urho3D but I've spent the last couple hours looking into it and I am optimistic!  I am therefore going to give it a go and see how far I get.  I'll reply to this topic with any results ( or lack there of ) .

Wish me luck!


@boberfly: Thanks for pointing us in the right direction; I'll start with your suggestions :slight_smile:

-------------------------

