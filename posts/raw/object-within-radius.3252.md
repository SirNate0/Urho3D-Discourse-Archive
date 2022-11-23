darkirk | 2017-06-16 15:51:30 UTC | #1

Is there a built-in routine in Urho to detect what objects are within X radius of another one?

-------------------------

Eugene | 2017-06-15 06:27:11 UTC | #2

Probably, triggers??

-------------------------

lezak | 2017-06-15 11:04:26 UTC | #3

Or if You dont't want to use physics, there is <a href=https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_octree.html#af7879fc425b198b216932bb2a694bdd4>Octree::GetDrawables</a> that can be used with a <a href=https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_sphere_octree_query.html>SphereOctreeQuery</a>

-------------------------

johnnycable | 2017-06-15 11:59:35 UTC | #4

Raycast < distance during update?
Object Position (vector) - Object Position (Vector) < distance during update?

-------------------------

Eugene | 2017-06-15 12:57:13 UTC | #5

[quote="johnnycable, post:4, topic:3252, full:true"]
Raycast &lt; distance during update?
Object Position (vector) - Object Position (Vector) &lt; distance during update?
[/quote]

Are you sure about performance of this approach?

-------------------------

johnnycable | 2017-06-15 13:28:47 UTC | #6

Well, if you have no other choice...:wink:

-------------------------

darkirk | 2017-06-15 19:47:06 UTC | #7

Thanks for the help guys! :)

-------------------------

Modanung | 2017-06-16 15:56:39 UTC | #8

[quote="Eugene, post:5, topic:3252"]
Are you sure about performance of this approach?
[/quote]

I guess both methods have their pros-n-cons. I'd expect the octree query to efficiently looks only within the specified range while ignoring the rest of the world and returning visually accurate results.
Whereas when simply checking the distance between nodes you could start with applying a filter through calling `GetChildrenWithTag`, `GetChildrenWithComponent` and `GetDerivedComponents` on the `Scene` with `recursive` set to `true`. Once you get the node's position checking distances is in essence a simple pythagorean problem.

In many cases triggers could also do the trick.

-------------------------

Modanung | 2017-06-16 15:51:13 UTC | #9

[quote="johnnycable, post:4, topic:3252"]
Object Position (vector) - Object Position (Vector) &lt; distance
[/quote]

Note that this is comparing a `Vector3` and `float`.
I implemented the function as such:
```
float LucKey::Distance(const Vector3 from, const Vector3 to, bool planar)
{
    if (!planar)
        return (to - from).Length();
    else
        return ((to - from) * Vector3(1.0f, 0.0f, 1.0f)).Length();
}
```
With `planar` having `false` as its default value.

-------------------------

johnnycable | 2017-06-16 17:28:00 UTC | #10

What if I'm spiderman and I'm walking on the side of a skyscraper? :rofl:

-------------------------

Modanung | 2017-06-16 17:30:49 UTC | #11

[quote="johnnycable, post:10, topic:3252"]
What if I'm spiderman and I'm walking on the side of a skyscraper? :rofl:
[/quote]

Then the distance to the skyscraper would be zero. :P

-------------------------

johnnycable | 2017-06-16 17:38:49 UTC | #12

[quote="Modanung, post:9, topic:3252"]
float LucKey::Distance(const Vector3 from, const Vector3 to, bool planar)
{
    if (!planar)
        return (to - from).Length();
    else
        return ((to - from) * Vector3(1.0f, 0.0f, 1.0f)).Length();
}
[/quote]


float LucKey::Distance(const Vector3 from, const Vector3 to, Vector3 complanarity = Vector3(1,1,1))
{
        return ((to - from) * complanarity).Length();
}
spiderman is served :wink:

-------------------------

Modanung | 2017-06-20 18:45:29 UTC | #14

How about:
```
float Distance(Vector3 from, Vector3 to, const bool planar = false, Vector3 normal = Vector3::UP);
```
```
float LucKey::Distance(Vector3 from, Vector3 to, const bool planar, Vector3 normal)
{
    Vector3 difference{ to - from };
    if (planar) {
        difference -= difference.ProjectOntoAxis(normal) * normal.Normalized();
    }
    return difference.Length();
}
```
Should work for any plane. Not just axial planes. :slight_smile:

-------------------------

johnnycable | 2017-06-16 19:24:01 UTC | #15

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b53e80d99df015318997d4039760c86b6350f44c.jpeg" width="690" height="388">

-------------------------

Modanung | 2017-06-17 21:16:07 UTC | #16

Seems to work. :slight_smile:
 
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/9b8eee09a0875a641d3127f5f0f8ccb82fb58259.jpg" width="690" height="388">

The size of the boxes in the images relies on: `LucKey::Distance(boxPos, Vector3::ZERO, ..., ...)`

Here's a video:

https://vimeo.com/222029488

-------------------------

Modanung | 2017-06-20 18:42:34 UTC | #17

Spiderman may like this `DistanceToPlane` function as well:
```
float DistanceToPlane(Vector3 from, Vector3 normal = Vector3::UP, Vector3 origin = Vector3::ZERO);
```
```
float LucKey::DistanceToPlane(Vector3 from, Vector3 normal, Vector3 origin)
{
    return Abs((from - origin).ProjectOntoAxis(normal));
}
```

-------------------------

johnnycable | 2017-06-19 10:33:19 UTC | #18

Yeah. Could do for another dynamic geometry example... or better swipe plane raycast... or so...:slightly_smiling_face:

-------------------------

slapin | 2017-06-20 06:18:45 UTC | #19

Aw, seen that word again and want to ask for a meaning...

What is swipe?
What is swipe plane raycast?

-------------------------

