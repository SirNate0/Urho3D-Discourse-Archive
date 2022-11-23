slapin | 2017-05-23 18:53:48 UTC | #1

Hi, all!

How would you implement "closest visible item" query for NPC in Urho?

-------------------------

Modanung | 2017-05-25 12:20:26 UTC | #2

Wrote [this](https://github.com/LucKeyProductions/OGTatt/blob/master/mastercontrol.h#L111-L153) for [OG Tatt](https://github.com/LucKeyProductions/OGTatt):
```
template <class T> T* GetNearestInstanceOf(Vector3 location)
{
    T* nearest{ nullptr };
    float nearestDistance{ M_INFINITY };

    PODVector<T*> components{};
    world.scene->GetDerivedComponents<T>(components, true);

    for (T* c : components) {

        Node* node{ static_cast<Component*>(c)->GetNode() };
        float distance{ (location - node->GetWorldPosition()).LengthSquared() };

        if (distance < nearestDistance) {

            nearest = c;
            nearestDistance = distance;
        }
    }
    return nearest;
}
```

-------------------------

smellymumbler | 2017-05-24 18:34:13 UTC | #3

That's absurdly useful for my game. Thank you so much sir.

-------------------------

slapin | 2017-05-24 22:15:11 UTC | #4

Some more thing about influence map.

Imagine an NPC. He have
1. "awareness radius" - he knows of extistence of objects in this radius and can enumerate it.
2. Can separate things by type (which means tag). So it can answer "where is closest taxi?" "where is closest vehicle?"
"where is a toilet?" "where i can eat?" questions.
3. Can only consider the target details on close radius, i.e. "is this bus full so I can not fit?", "is there someone in vehicle
on driver seat?" "is this shitty restaurant closed?". BUT NPC should do risk management, i.e. collect data so he can
consider on distance. So to not constantly repeat failed action of previous NPCs, i.e. he "sees" that a man before
failed accessing the restaurant which scores this target -50, which allows selecting another restaurant nearby, if any.
So kind of messaging failures to directly visible NPCs so they select different targets for some time, but
wears off after a few minutes and do not affect nearby NPCs which did not "see" what happened.

So the role for influence map is to accelerate all these considerations for many NPCs.
Which is wat I want to eventually get to. as I see, there are a few data sets there.
1. We need layering system which allows to access all spatial data or by criteria.
https://github.com/jlblancoc/nanoflann allows quick spatial searches, but we also need some way to request tag as key.
This probably can be done by using structure like VariantMap with tags as key, and separate K-D trees,
with main K-D tree for storing all data. Wihch looks like extreme data duplication, but I can't think of anything else.
2. The layering system should be quick and dynamic, i.e. change of tag should allow migration. I did not test nanoflann
with this, but I really hope it will work.

Any ideas on where to look for inspiration and code?

Thanks!

-------------------------

weitjong | 2017-05-25 11:59:58 UTC | #5

Since you don't need the actual distance value for the comparison, you can improve the performance by using LengthSquared() instead.

-------------------------

Modanung | 2017-05-25 12:19:07 UTC | #6

Ah, thanks. Saves a Sqrt() I guess?

-------------------------

