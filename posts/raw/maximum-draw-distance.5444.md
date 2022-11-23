codexhound | 2019-08-10 10:37:31 UTC | #1

There seems to be a maximum drawable distance in the engine since if I have objects that are more than 650 in game units away, the engine wont draw them. I set everything to 3000 draw distance just to test. Is there a way to get past this limit? Or is it a camera mask I don't know about

-------------------------

Modanung | 2019-08-10 11:12:31 UTC | #2

Could it be the size of your `Octree`?

Also, scale is an illusion. ;)

-------------------------

Modanung | 2019-08-10 11:48:46 UTC | #3

If there's no space walks, space could be a different scene that is rendered seperately from what happens inside a craft or on a planet.

-------------------------

codexhound | 2019-08-10 11:59:01 UTC | #4

Yeah, that's true. I could do it that way but I don't think it should be necessary to render a different scene. Tried changing the bounding box of the scene octree but it didn't do anything. On a side note, because of my OCD, I have to say space is definitely not an illusion. I always need more, especially when dealing with floats and quantum zoom levels. It just doesn't work :). Pixel 1 keeps rounding up.

-------------------------

Leith | 2019-08-10 13:12:33 UTC | #5

Did you change the size of your Zone to suit?

-------------------------

Leith | 2019-08-10 13:15:36 UTC | #6

I'm just thinking inside the box - what else has a bounding volume and affects rendering?
@Modanung, Scale is the root of all evil. I hate you, scale. You make my life hard. Why do you need to be the difficult child?

-------------------------

codexhound | 2019-08-10 13:21:51 UTC | #7

SetScale really annoys me too (I never am completely sure what it's relative too, but life is hard:). I wish there was a set size function. Maybe ill just make one internally. Leith, what zone do I need to change the size of? Could you explain.

-------------------------

Leith | 2019-08-10 13:40:03 UTC | #8

Your game scene probably has an Octree attached to its root, and likely, there is (also) a Zone attached to it, or to another node, since zones can move..
Zone is an AABB, it provides ambient lighting and fog, and I think that's all.
Zones can overlap... if something is inside a zone, it gets ambient light from the zone. If its in more than one zone, theres I think some rules about which zone gets to be in charge... Not sure, not really needed multiple zones so far.
Since it provides ambient lighting, Zones could help show up objects that are not receiving other sources of light, just a thought. If objects are outside of all zones, then they get no ambient lighting.
To be clear - an object does not need to be a child of a zone, it just has to be inside the zone's volume, inside the box, to receive ambient lighting and fog.

-------------------------

Leith | 2019-08-10 13:43:11 UTC | #9

As for SetSize, well, in some cases, I would attach extra nodes to my armature, and use SetWorldScale on them, so that my attachments were scaled in world terms, messy, but it works

-------------------------

Modanung | 2019-08-10 20:42:59 UTC | #10

If no `Zone` is actively define, the default zone is used. It can be accessed through:
`GetSubsystem<Renderer>()->GetDefaultZone()`

[quote="Leith, post:6, topic:5444"]
Scale is the root of all evil. I hate you, scale. You make my life hard.
[/quote]

Ah yes, the [scales](https://usaherald.com/wp-content/uploads/2017/07/Lady-Justice.jpg)...

@codexhound What puzzles you about node scales?
When splitting your scene up you'd simply store a scale factor somewhere to use for intermediating.

-------------------------

Leith | 2019-08-10 14:04:53 UTC | #11

I was not aware there was a default zone - what size is it? ;)

-------------------------

Modanung | 2019-08-10 14:12:26 UTC | #12

@Leith You have much to learn, young padawan. ;)
```
static const Vector3 DEFAULT_BOUNDING_BOX_MIN(-10.0f, -10.0f, -10.0f);
static const Vector3 DEFAULT_BOUNDING_BOX_MAX(10.0f, 10.0f, 10.0f);
```

-------------------------

codexhound | 2019-08-10 14:15:46 UTC | #13

I get what the scales do, I just prefer more absolute measurements! The Scales! It's like someone writing an engineering document and never once mentioning what the units are. It's bothersome. I am using a kind of system like you were mentioning though for different scales.

-------------------------

codexhound | 2019-08-10 14:34:19 UTC | #14

So attemping to change the defaults zones bounding box gave the the dreaded nullptr segfault.
                     
               /// Return world space transform matrix.
    const Matrix3x4& GetWorldTransform() const
    {
        if (dirty_) <<<<<<<------
            UpdateWorldTransform();

        return worldTransform_;
    }

I'm gonna take a break now:)

-------------------------

JTippetts | 2019-08-10 14:48:43 UTC | #15

Don't change the default zone, just create your own zone. If you have a zone, it won't fall back to the default.

-------------------------

lezak | 2019-08-10 21:24:58 UTC | #16

My guess would be that Your objects are covered by a fog (fog is set up through zone), try changing fog start and end to some high values.

-------------------------

Modanung | 2019-08-10 20:46:35 UTC | #17

@codexhound And just to be sure. Did you check the `Octree` size?

-------------------------

codexhound | 2019-08-10 21:11:32 UTC | #18

Yes, it was smaller than wanted, but I changed it to no effect.

-------------------------

codexhound | 2019-08-10 21:15:44 UTC | #19

Finally got stuff to show up with lezaks suggestion.

-------------------------

