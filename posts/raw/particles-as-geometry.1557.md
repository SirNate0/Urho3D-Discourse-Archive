sabotage3d | 2017-01-02 01:08:29 UTC | #1

Hi guys, is it currently possible to change the particles to geometry for example to cubes? I can see only that sprites are available if there is any hack or workaround please let me know.

-------------------------

codingmonkey | 2017-01-02 01:08:29 UTC | #2

Hi, 
I think it's a stupid idea but you can try get the position, rotation of particle and apply it to node with cube )

-------------------------

sabotage3d | 2017-01-02 01:08:29 UTC | #3

How do we query the transform of the particle system? If we use the node system it would be inefficient for many particles.

-------------------------

codingmonkey | 2017-01-02 01:08:29 UTC | #4

>How do we query the transform of the particle system?
I guessing with
PODVector< Billboard > &  GetBillboards () <- Return all billboards.  [urho3d.github.io/documentation/H ... itter.html](http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_particle_emitter.html)
Billboard -> [urho3d.github.io/documentation/H ... board.html](http://urho3d.github.io/documentation/HEAD/struct_urho3_d_1_1_billboard.html)  Use single angle rotation from billboard as q=  Quaternion(rot, rot, rot)

>If we use the node system it would be inefficient for many particles.
Yes you are right, but you may do not use many of thousands particles only few... tens or hundreds  :slight_smile:

Also probably you will need faked billboard mat's with smaller texture and primitive tech (low compute cost), or even probably do not use at all any material for particle system. But I do not know in this case is still working properly?  I mean it does compute transformation for particles or not.

also you may create request feature for add supporting of emitter with 3d objects ) [github.com/urho3d/Urho3D/issues](https://github.com/urho3d/Urho3D/issues)

-------------------------

