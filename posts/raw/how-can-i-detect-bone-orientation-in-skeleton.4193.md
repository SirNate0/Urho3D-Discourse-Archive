slapin | 2018-04-23 19:04:01 UTC | #1

Hi, all!

Lets imagine I have imported some random characters off the net and I want to apply
some standard transforms to them (like neck rotation), without caring for skeleton structure
and bone orientations. For this I need to calculate bone orientation, so to calculate inverse quat. So the question - is bone orientation information available somewhere?

-------------------------

Lumak | 2018-04-23 21:36:56 UTC | #2

Did you look at this variable animation process to control simple animation? https://discourse.urho3d.io/t/3rd-person-shooter-animation-wip/4027/4

I chose to share that bit of code with you in mind because it alleviates knowing what the joint orientation/transofrm is and can be easily controlled by a key.  In that example, the **pitchInv** is the key which is in the range[0:1].  And the since the neck is a single joint, the cost of the operation is one rotation multiplication.

-------------------------

slapin | 2018-04-23 21:49:18 UTC | #3

Thank you so much for sharing.

That is cool and makes whole thing much easier, but how many animations can AnimationController handle at the same time? As I have the same idea for character customization (body height, arms, legs size, face features (bone-based)), adding all these together, won't it make everything very heavy on CPU/hit some limit? Making animations which do not change most of time is also looks like waste of resources, maybe it is possible to "bake" them into bones as changes complete?

-------------------------

Lumak | 2018-04-23 22:11:27 UTC | #4

In regards to the neck animation, it's very minimal with only one rotation multiplication, and you can even set the joint animation flag to false to save more time and turn it on only when you need. Limit with the layered animation is that there are eight layer channels that you can use. 

But for the remaining animation cost, I took some measurements here, https://discourse.urho3d.io/t/what-if-there-was-animation-controller-proxy/4089, and the entire animation process for a single frame (that model having ~40 joints, I think) was measure in terms of nano seconds.  What costs more is calling PlayExclusive() or Play() every frame because it evaulates fades if you have fade time. Merely checking if the animation is playing first then calling Play()/PlayExclusive() would optimize it.

edit: err, whole body animation per single frame is probably in terms of hundreds of nano seconds, not nano seconds because occasionally, it'll pick up as 1 in high frequency timer.

-------------------------

slapin | 2018-04-23 22:15:52 UTC | #5

An additional problem with not knowing bone orientation is IK. I probably can do animations for all possible angles then  doinverse lerp but that looks way too weird.

I wonder how Unity MecAnim handles these - it imports any character I have like magic and all the controls work perfectly well. So there should be some way to calculate the values...

-------------------------

Lumak | 2018-04-23 22:24:40 UTC | #6

Haven't look at Unity MecAnim, but Unity is now open source, https://blog.github.com/2017-06-28-github-for-unity-is-now-open-source/ , and perhaps you can learn from what they're doing.

-------------------------

slapin | 2018-04-23 22:26:56 UTC | #7

Well, this is Github for Unity extension (which allows Unity to work with github), so no fish there...

-------------------------

Lumak | 2018-04-23 22:30:15 UTC | #8

I remember the news but had to google it to get the link, and apparently got the wrong one. Try this - https://docs.unity3d.com/560/Documentation/Manual/OpenSourceRepositories.html

-------------------------

slapin | 2018-04-23 22:50:30 UTC | #9

Well, looking at this I found no mecanim source, but it is possible I missed something.
Most of source code in the repos are various demo projects.

The other engine source I have before my eyes is UE4, which is HUGE and I still not had much luck looking it up for similar tools...

-------------------------

Lumak | 2018-04-23 22:56:26 UTC | #10

The unity mecanim is free products at the unity asset store, https://www.assetstore.unity3d.com/en/?stay#!/search/page=1/sortby=relevance/query=mecanim&price:0

And now the engine is open source, you should be able to code trace the processes that you're curious about.

-------------------------

slapin | 2018-04-24 02:06:35 UTC | #11

According to "unity source code", mecanim is part of native code which is unline C# stuff was not shown to public (only ones who paid for source license can see this). So I can't see anything  there.

-------------------------

Lumak | 2018-04-24 03:15:45 UTC | #12

Ok, I read what it really means with *"Unity is now open source"* -- it's BS! They should've just said that commonly used source projects with the Unity engine is open source. 

However, I did download a **Mecanim** example - https://www.assetstore.unity3d.com/en/?stay#!/content/5328, and see there's .cs code for every example given.  And you can cross reference with https://github.com/Unity-Technologies/UnityCsReference to get a good idea what's going on.

-------------------------

slapin | 2018-04-24 15:49:25 UTC | #13

Well, after I got some sleep with the problem I was able to split it to better redefine it.

The idea is the following - we have a character (lets assume we have very simple one), having 2 limbs and a set of bones which are parents to these limbs. All bones orientation is random (we want use skeletons made in different software). We have our controls which we want to use, which work always the same (I rotate control over X axis then my bone rotates over character-relative (local) X axis, not around bone X axis.
So idea is to find conversion quaternion, which would allow converting character space to bone local space. The conversion is required every frame as bone spaces change.
So LookAt approach will almost never work as it assumes that in local space Z is always front and Y is up. The magic will work for axis-oriented bones (fully vertical or horizontal for humanoid) with wrapping up vector so, that it points in bone direction, but it is not enough if bone's front is reversed.

The magic resolution to this problem is "inserting" a parent "bone" which is oriented in character space. if we rotate "child", the "child" will obey and rotate in space we like.
Of course we do not want to change actual skeleton to implement this, so this have to be done with quaternion math.

The good thing about this approach is that we calculate the conversion only once, during skeleton load, we don't need to convert this every frame. I think this is actual power behind mecanim.

But now I need to find out which mith I need which is really complex for my poor brain now, but understanding that is a progress already.

btw, mecanim is not a part f that C# code drop, grepping through that one can find that mecanim is native code (written in whatever compiled language they use, C, C++ or something).

-------------------------

Lumak | 2018-04-24 18:01:28 UTC | #14

I don't know whether Mecanim is a class in Unity engine. I thought it was just project example on the asset store. Anyway, having bought many character packs in the past, one distinguishing feature that I can see common in all to test whether the char needs to be rotated 180 degrees or not is the direction of the toes.
pseudo code:
[code]
if ((toenode->GetWorldDirection() - footnode->GetWorldDirection()).DotProduct(Vector3::FORWARD)  >= near 1)
 // don't need to rotate 180
else
// rotate 180
[/code]

-------------------------

slapin | 2018-04-24 22:03:05 UTC | #15

To illustrate the idea:
![extra-bone|500x1000](upload://idGh21ly51OSs8a7XNOOZFot8kU.png)

Adding extra "bone" allows easier procedural posing. Now I need to find the required math.

As I understand I need wanted rotation (0, 0, 0 but YMMV, 0, 0, 0 mean direction 0, 0, 1), parent bone world rotation, and base character node rotation. so I need to multiply Quaternion(0, 0, 0) to
inverse of (parent_world_rotation * character_world_rotation.Inverse()). So whole expression for extra node rotation will be Quaternion() * (parent_world_rotation * character_world_rotation.Inverse()).Inverse() is it correct? I never was able to properly catch quaternion math :(

-------------------------

Lumak | 2018-04-24 21:49:46 UTC | #16

I have no idea what you're trying to do, and I don't think more guessing would help. If you don't think Unity or UE would be helpful then perhaps, learning how Urho3D's IK handles rotation multiplication would help.

-------------------------

slapin | 2018-04-24 22:46:33 UTC | #17

Well the code for finding the transform for parent is this:
```c++
/* This is run at skeleton load time, not at run time to calculate the correction value
the character node should be at origin for this to work
control is initial control rotation */
Quaternion correction(Node *bone, Quaternion control = Quaternion::IDENTITY)
{
        Node *parent = bone->GetParent();
        Quaternion parent_rotation = parent->GetWorldRotation();
        Quaternion local_rotation = parent_rotation.Inverse() * control;
        return local_rotation;
}
...
/* Fixup local rotation for a bone */
Quaternion fixup_rotation(Quaternion control, Quaternion fixup)
{
        Quaternion rotation = control * fixup;
        return rotation;
}

....
/* use like this in main loop */
bone->SetRotation(fixup_rotation(control_data[bone].control, control_data[bone].fixup));

```

The idea behind this is simple - we have manually-created or procedural "skeleton" where all bone "nodes" are set like it is easier for us to animate procedurally. This "skeleton" is the same for all characters. It might or might not be used for animations. It contains subset of bones which are important for average animations (not the highly detailed most important ones). It can be implemented as array of bone names or ids in real skeleton (which are used for procedural animation) and correction values. It is what is used to for procedural animations most of time (IK, ragdoll, etc).

We also have our skeleton exported from application, which can have any topology and any number of bones. When procedural animation running (even on some of the bones) it gets rotations from "control" skeleton, converts them to actual rotations on real skeleton and apply them to bones.
Does it sound reasonable?

-------------------------

slapin | 2018-04-25 00:17:48 UTC | #18

Well, the code above is not quite correct, but I'm close as ever to implement what I need.
I basically need node->Rotate()-like code, but for absolute value, which will work as basis.

-------------------------

slapin | 2018-04-26 05:34:51 UTC | #19

Looks like I found proper way for bone rotation which does not make my brain explode.
It is quite simple actually
```c++
                protected:
                        Urho3D::Quaternion proper_rotation(Urho3D::Node *bone, Urho3D::Quaternion control)
                        {
                                Urho3D::Quaternion  ret;
                                ret = default_rot * world_rot_inv * control * world_rot;
                                return ret;
                        }
                public:
                        void update_transforms()
                        {
                                world_rot = node->GetWorldRotation();
                                world_rot_inv = world_rot.Inverse();
                        }
 ```

update_transforms() is run once on skeleton load while it is at origin.
Then all the values stay the same. If the values are updated per frame,
the rotation is extremely unstable. But retaining the values allow quite intuitive rotations,
which are not world space, but in local space, but they are rotated properly regardless of the
skeleton.

Will work-out demo for this on a weekend, I think something nice should come out of it.

-------------------------

