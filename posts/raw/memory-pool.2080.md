sabotage3d | 2017-01-02 01:12:53 UTC | #1

Hi guys,
Have anyone implemented a memory pool for Urho3D? What would be the best way to approach this?

-------------------------

hdunderscore | 2017-01-02 01:13:07 UTC | #2

Although I haven't used them, Urho has Allocator class which might be used for that.

In one project where I had many projectiles firing, I made a simple Vector<Projectile> pool, that gave a notable performance improvement.

-------------------------

sabotage3d | 2017-01-02 01:13:07 UTC | #3

Ah cool I didn't know about that. Can it be used to create a pool for Urho3D's smart pointers and containers?

-------------------------

Modanung | 2017-01-02 01:13:08 UTC | #4

[quote="sabotage3d"]Ah cool I didn't know about that. Can it be used to create a pool for Urho3D's smart pointers and containers?[/quote]
Yes, heXon's [url=https://github.com/LucKeyProductions/heXon/blob/master/spawnmaster.h]SpawnMaster[/url] does object pooling too. Basically using a single template function.

-------------------------

