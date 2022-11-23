stark7 | 2017-10-01 03:04:55 UTC | #1

Is there a way to disable scaling on the children when it's applied to the parent?

The use case I am looking at is when I have an animation that I want to scale up such that the WorldPositions of the bones change but I want the models to not change scale.

-------------------------

Eugene | 2017-10-01 09:00:11 UTC | #2

There is such PR, but it is unfinished.

https://github.com/urho3d/Urho3D/pull/2096

-------------------------

stark7 | 2017-10-02 13:26:38 UTC | #3

Oh, it's good that other people are running into this. Something like this feature would allow to do some things without a lot of extra coding around it - like right now I am looking at a slow projectile flying animation from source to target where I don't want the projectile to scale up to the distance between the launcher and target.

-------------------------

Eugene | 2017-10-02 13:32:50 UTC | #4

There is only one problem here.
`Node` has _a lot_... no, _**a lot**_ of different functions that set its position, rotation and scale. And they all should work according to inheritance flags.
However, only world transform computation is implementent in the PR.

-------------------------

Modanung | 2017-10-02 13:56:13 UTC | #5

Maybe some `TransformLock` component could provide a quicker non-intrusive solution?
This component would undo selected inherited transformations.

Or a `FakeParent` component. That would only apply part of another node's transformations.

-------------------------

stark7 | 2017-10-02 14:02:59 UTC | #6

right now I am basically automatically adding intermediary nodes with a scale of 1f/parent.WorldScale - that seems to work well but it does add a bit of extra computation.

I also just found [this discussion](https://discourse.urho3d.io/t/solved-child-node-that-not-inherit-parents-scale/2089) and I agree that all the bools can get pretty nasty and unmaintanable - unless they could somehow be automatically generated.

-------------------------

Dave82 | 2017-10-02 14:03:38 UTC | #7

A TransformLock component which simply inverts the scale of the parent
childScale = 1.0f / parentScale;
of course this way the rotation and position is still transformed
EDIT : I was late :D

-------------------------

stark7 | 2017-10-02 14:04:10 UTC | #8

:) i'm glad we have the same solution because I am feeling less bad about it :smiley:

-------------------------

SirNate0 | 2017-10-07 04:03:40 UTC | #9

Another potential solution, depending on the case in question, is to have the node that needs to be scaled a sibling of the children that don't instead of their parent, and just have them share a common patent that remains unscaled.

-------------------------

stark7 | 2017-10-07 07:04:29 UTC | #10

If a per bone option to not scale while preserving the position and rotation can be made, it will save a lot of headaches when working with a specific kind of animation export from Blender (like a sphere animation going from point A to point B).

As you scale by distance, the sphere will not change shape. My next option is to just animate an armature and attach the sphere in game to the animated bone which might work just as well.

-------------------------

SirNate0 | 2017-10-07 16:26:15 UTC | #11

I see now -- what I suggested probably won't work for your use case. Perhaps you could try having a bone off of the one you are moving around that you keep at uniform scale that you use for the animation. Or you could possibly use object animations. Though I do agree, having a feature like what you suggested would make various things easier, and should certainly be considered.

-------------------------

stark7 | 2017-10-07 17:26:40 UTC | #12

For some reason i haven't yet been able to properly export and play the object animations so far. Last night during this thread I started looking at just animating an armature with a meshless parent - as i wrote above - and i will report in the next 2 days if that works well. For the per bone option i started thinking that there may be a shader or technique somewhere that may need to be modified as well and i can't get to changing urho 3d base code until December 2017 after i launch my current project.

-------------------------

