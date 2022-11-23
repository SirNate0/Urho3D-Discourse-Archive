GodMan | 2019-05-13 04:19:09 UTC | #1

I looked in the docs, and all I can find is `shape->SetTriangleMesh(tutorialCollision)` for static mesh. Is it not possible to make a very simple collision mesh for a character, and use this instead of a sphere or box or capsule.

Thanks

-------------------------

Leith | 2019-05-13 07:35:05 UTC | #2

Hi, GodMan!

The clue is in the name: static mesh - it's typically not animated. That does not mean it is impossible to assign a dynamic mesh at runtime, but it is impractical to modify a physics mesh in realtime using today's consumer-grade technology.

A more feasible approach is to provide an armature of simple collision hulls (they can be detailed meshes, or primitives like in this screen shot). We can animate the armature, by connecting it to the model's skeleton. This is just like a Ragdoll, except that these rigidbodies are "kinematic" - they are being driven by animation.

![Screenshot%20from%202019-05-13%2017-24-03|690x403](upload://xekPa5i9LnJm3dsmWFJtem0E4y0.jpeg)

These ragdoll bodies are using a different collision layer / mask than the outer hull, meaning that the number of collision tests required at runtime remains reasonably low. The collision mask ensures that ALL collisions between bodyparts are disabled (not just those between directly connected bodyparts), and no joint constraints are required - we rely on entirely on the animation of the skeleton.

-------------------------

Modanung | 2019-05-13 07:34:42 UTC | #3

When basic shapes are not an option for you, dynamic collision shapes _can_ be [convex hulls](https://en.wikipedia.org/wiki/Convex_hull); simply use `SetConvexHull` instead.

-------------------------

GodMan | 2019-05-13 16:57:27 UTC | #4

If I use a simple model which is basically some smaller hit boxes, and use convexhull does this behave like the skinned mesh "animated model" or do I have to assign them manually to each bone.

-------------------------

Modanung | 2019-05-13 22:29:09 UTC | #5

ConvexHulls "cannot" change shape, if that's what you mean.
If you're looking for pixel-perfect sniping (for instance) you might be better off using *octree* raycasts, btw. For something like a ragdoll you'll need separate shapes.

-------------------------

GodMan | 2019-05-13 23:00:41 UTC | #6

So this is what I'm trying to do. I was trying to use a very very simple collision geometry for an animated character.

![collision|690x291](upload://c8UoVTjDo8igSydcMC3eWH7u8Zb.png)

-------------------------

Leith | 2019-05-14 01:45:22 UTC | #7

Yes, you can use your own mesh shapes for the physics hull on your animated character, just noting that they won't deform correctly when the character is animated. If you can live with that, then yeah sure, you can provide your own shapes that closely match your geometry. There's a few more rules, such as, the shapes must be convex. If they are not convex shapes, they can always be split into convex shapes. But know that Bullet physics does not like concave shapes to move around at runtime. So think in convex terms.

-------------------------

GodMan | 2019-05-14 01:54:17 UTC | #8

Well what did you do in your screenshot where you have individual pieces?

-------------------------

GodMan | 2019-05-14 02:02:16 UTC | #9

I see. I took at look at the Rag Doll Sample. I will see what I can come up with.

-------------------------

Leith | 2019-05-14 04:18:58 UTC | #10

I used a bunch of primitive convex shapes - mostly capsules, but theres at least two box shapes in there too - I was able to get a "close enough fit" without actually defining any custom geometry.
For each major bone in my skeleton, there is a corresponding bodypart.
For things like the spine, I simplified the number of bodyparts / active bones, thus, there is not a strictly one to one relationship between bones and bodyparts.

So, in Urho3D, when we load our animated model and instantiate it in our scene, there are a bunch of nodes with names matching our skeleton bones. Before playing any animations, we are in the "bind pose" ... We attach rigidbody components to those bone nodes, and set the rigidbodies to "kinematic mode". Now the rigidbodies will automatically be animated when we play animations on that character - but we won't get any collision responses on our armature because its in kinematic mode. If we want the armature to respond to collisions, we need to do a bit more work.

I used the Ragdoll Sample as a guide to help me construct my armature, but I did not leave the rigidbodies in "dynamic mode" (aka ragdoll mode). Making them kinematic means they get their world transform from their parent node, which in our case means a bone node, which in turn, is likely to be animated.

I separated the hardcoded data from the sourcecode, and moved it into an xml file per character:
[quote]
    <Comment>Ragdoll Bodypart Descriptors</Comment>
    <BodyPart Name="Hips"         Shape="Box"     Size=".3 .15 .2"   Position="0 .05 0"    Orientation="0 0 0" />
    <BodyPart Name="Spine1"       Shape="Box"     Size=".35 .35 .25" Position="0 .1 0"     Orientation="0 0 0" />
    <BodyPart Name="Head"         Shape="Capsule" Size=".25 .35 0"   Position="0 .125 0"   Orientation="0 0 0" />

    <BodyPart Name="RightUpLeg"   Shape="Capsule" Size=".2 .45 0"    Position="0 -.2 0"    Orientation="0 0 0" />
    <BodyPart Name="RightLeg"     Shape="Capsule" Size=".2 .45 0"    Position="0 -.2 0"    Orientation="0 0 0" />
    <BodyPart Name="RightFoot"    Shape="Capsule" Size=".125 .25 0"  Position="0 -.07 -.1" Orientation="90 0 0" />

    <BodyPart Name="LeftUpLeg"    Shape="Capsule" Size=".2 .45 0"    Position="0 -.2 0"    Orientation="0 0 0" />
    <BodyPart Name="LeftLeg"      Shape="Capsule" Size=".2 .45 0"    Position="0 -.2 0"    Orientation="0 0 0" />
    <BodyPart Name="LeftFoot"     Shape="Capsule" Size=".125 .25 0"  Position="0 -.07 -.1" Orientation="90 0 0" />

    <BodyPart Name="LeftArm"      Shape="Capsule" Size=".15 .25 0"   Position=".15 0 0"    Orientation="0 0 90" />
    <BodyPart Name="LeftForeArm"  Shape="Capsule" Size=".1  .25 0"   Position=".15 0 0"    Orientation="0 0 90" />

    <BodyPart Name="RightArm"     Shape="Capsule" Size=".15 .25 0"   Position="-.15 0 0"   Orientation="0 0 -90" />
    <BodyPart Name="RightForeArm" Shape="Capsule" Size=".1  .25 0"   Position="-.15 0 0"   Orientation="0 0 -90" />


    <Comment>Ragdoll Joint Constraint Descriptors</Comment>
    <Joint BodyPart="LeftUpLeg"  ParentPart="Hips" Type="ConeTwist"   Axis="0 0 -1" ParentAxis="0 0 1"  HighLimit="45 45" LowLimit="0 0" Collides="false" />
    <Joint BodyPart="LeftLeg"    ParentPart="LeftUpLeg" Type="Hinge"  Axis="0 0 -1" ParentAxis="0 0 -1" HighLimit="90 0" LowLimit="0 0" Collides="false" />
    <Joint BodyPart="LeftFoot"   ParentPart="LeftLeg" Type="ConeTwist" Axis="0 1 0" ParentAxis="0 -1 0" HighLimit="30 30" LowLimit="0 0" Collides="false" />

    <Joint BodyPart="RightUpLeg" ParentPart="Hips" Type="ConeTwist"   Axis="0 0 -1" ParentAxis="0 0 1"  HighLimit="45 45" LowLimit="0 0" Collides="false" />
    <Joint BodyPart="RightLeg"    ParentPart="RightUpLeg" Type="Hinge"  Axis="0 0 -1" ParentAxis="0 0 -1" HighLimit="90 0" LowLimit="0 0" Collides="false" />
    <Joint BodyPart="RightFoot"   ParentPart="RightLeg" Type="ConeTwist" Axis="0 1 0" ParentAxis="0 -1 0" HighLimit="30 30" LowLimit="0 0" Collides="false" />

     <Joint BodyPart="LeftArm"   ParentPart="Spine1" Type="ConeTwist" Axis="0 -1 0" ParentAxis="0 1 0" HighLimit="45 45" LowLimit="0 0" Collides="false" />
    <Joint BodyPart="LeftForeArm" ParentPart="LeftArm" Type="Hinge" Axis="0 0 -1" ParentAxis="0 0 -1" HighLimit="90 0" LowLimit="0 0" Collides="false" />

     <Joint BodyPart="RightArm"   ParentPart="Spine1" Type="ConeTwist" Axis="0 -1 0" ParentAxis="0 1 0" HighLimit="45 45" LowLimit="0 0" Collides="false" />
     <Joint BodyPart="RightForeArm" ParentPart="RightArm" Type="Hinge" Axis="0 0 -1" ParentAxis="0 0 -1" HighLimit="90 0" LowLimit="0 0" Collides="false" />

    <Joint BodyPart="Spine1" ParentPart="Hips"   Type="Hinge"     Axis="0 0 1"  ParentAxis="0 0 1"  HighLimit="45 0" LowLimit="-10 0" Collides="false" />
    <Joint BodyPart="Head"   ParentPart="Spine1" Type="ConeTwist" Axis="-1 0 0" ParentAxis="-1 0 0" HighLimit="0 30" LowLimit="0 0" Collides="false" />



</Character>
[/quote]

When this xml file is read back in at runtime, the data completely informs the code how to construct the armature for that character - this is my understanding of a "data-driven approach". Note that our code requires no knowledge of the bone topology - this will "just work" for any skeleton, from an octopus to a dinosaur. We just need to craft the right data! 
Since the names of bones might differ between character models, we are specifying the bone names explicitly in the per character data, so that is never a problem. Oh yeah - the position and rotation values are relative to the space of the parent node , ie, "in bonespace". We use them as "offsets" to position and orient the bodyparts, relative to their parent bones, IN THE BIND POSE.

I have data for joint constraints, but I don't need any joints until I want to switch from animated to ragdoll mode... and when that happens, I may choose to set only part of the armature to ragdoll mode, and leave the rest animated...

-------------------------

Modanung | 2019-05-14 08:44:27 UTC | #11

[quote="GodMan, post:6, topic:5147"]
I was trying to use a very very simple collision geometry for an animated character.
[/quote]
What should this character collide with? Is it for actual ragdoll purposes? If not, it's likely for there to be a more efficient solution to your problem.

-------------------------

Leith | 2019-05-14 08:58:27 UTC | #12

In my case? The provision of ragdoll bodyparts was an experiment, to see if I could derive momentum / acceleration stuff at the moment in time when we hand over control from animation to physics. I needed a way to carry on, from the animated state, to the physically plausible result state.
As a bonus, I found myself able to discern which bodypart was being hit during attacks (and where, and at what angle), and therefore implement plausible response.

-------------------------

Modanung | 2019-05-14 10:42:32 UTC | #13

Which causes clashes between dynamic and animated-kinematic bodies that are hard to fix. Therefor I'm trying to figure out whether a two-state solution (capsule & ragdoll) would maybe make more sense for @GodMan's sake. :stuck_out_tongue:

-------------------------

GodMan | 2019-05-14 16:16:28 UTC | #14

@Modanung I want something a little bit closer to the mesh of the character like in my pic above, but something still really simple and fast. I just need the collision for the characters environment which is mostly static, and a few dynamic things. I do not currently have ragdolls on the characters.

-------------------------

Modanung | 2019-05-14 20:26:26 UTC | #15

You may want to stick to spheres, capsules and boxes for the shapes where feasible to save a bit of resources.

-------------------------

GodMan | 2019-05-14 23:19:20 UTC | #16

So could I use capsules for the limbs and maybe a box for his head. Similar to the ragdoll demo? Using bullet physics shapes.

-------------------------

Leith | 2019-05-15 05:25:54 UTC | #17

I certainly did. It's not the only option, but the result is "good enough" for me.
The "good part" of using convex physics primitive shapes, is that you get "curves for free" - the shapes are usually only expressions of mathematical formulas describing the surfaces (capsule is a perfect example), although the low-quality physics debug drawing could lead you to believe otherwise - you have more fine detail on curved surfaces, and more plausible physical outcomes, using simple physics shapes than you can generally achieve with a triangle based mesh.
I just wish that Bullet supported "ellipsoids", where we can set the radius for the capsule different at each end. The tangent is naturally derived in such a case, and the mathematical expression of the shape is not difficult to cope with.

-------------------------

Leith | 2019-05-16 06:18:33 UTC | #18

I still use an outer capsule hull around my animated ragdoll - but the collision group and masking values are set up to ensure that the bodyparts can't hit the hull, given that they have entirely different purposes. I've extended (but respected) Bullet's default enumeration for filter groups (layers in urho), and probably already have more than I need, but I note there's not much fuss made in the Urho3D Samples, or in Bullet, about exactly how these are intended to be used. I'm happy to share something back in terms of how to effectively apply collision filtering in Urho (ie in Bullet), if I felt it might end up being posted in, or referenced by a FAQ for future reference, and not lost in a haystack.

-------------------------

