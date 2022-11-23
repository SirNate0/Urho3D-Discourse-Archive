evolgames | 2021-08-01 03:38:37 UTC | #1

I'm thinking about how to make a 3d piston work with physics. Basically, a piston connecting two seperate rigid bodies which can push them away and draw them near. There are no slider constraints for 3d. I tried simply adjusting a constraint's world positions (using a hinge constraint with zeroed high/low limits) but that doesn't push the bodies apart, it simply moves the anchor point, as seen in debug renderer.
Anyone have an idea? Feels wasteful to destroy the joint, apply force to the bodies, and recreate the joint.

Maybe it could be done with specifically controlled and hidden hinge joints. I might try this. So green is the piston, connecting two box models, sticks/circles are hinges. Piston is only a static model with animation, no rigid body. Might work.
![Screenshot_20210731-233634_PENUP|343x500](upload://vsg8HP5CVBY9YrJNL5miyjduGxT.jpeg)

-------------------------

SirNate0 | 2021-08-01 19:44:45 UTC | #3

I'm pretty sure there are slider constraints. At least in some versions of Bullet.

https://docs.panda3d.org/1.10/python/programming/physics/bullet/constraints

Edit:

Definitely Urho's version as well:

https://urho3d.io/documentation/HEAD/_constraint_8h.html#a5c5622ec0bb151f27185a4902ff1a4c2

-------------------------

evolgames | 2021-08-01 20:59:38 UTC | #4

I stand corrected. I guess I didn't check the api and probably was confusing Weld and Sliders. There's no Weld constraint. Well, good. I'll just use the slider, then. Can't believe I missed that. Thanks, you probably saved me a few hours of messing with hinges before realizing I didn't need to.

-------------------------

JSandusky | 2021-08-02 05:30:43 UTC | #5

A weld is a fixed constraint. Adding it is pretty much just:

CreateConstraint()
```
    case CONSTRAINT_FIXED:
    {
        btTransform ownFrame(ToBtQuaternion(rotation_), ToBtVector3(ownBodyScaledPosition));
        btTransform otherFrame(ToBtQuaternion(otherRotation_), ToBtVector3(otherBodyScaledPosition));
        constraint_ = new btFixedConstraint(*ownBody, *otherBody, ownFrame, otherFrame);
    } break;
```

ApplyFrames()
```
    case FIXED_CONSTRAINT_TYPE:
    {
        auto* c = static_cast<btFixedConstraint*>(constraint_.Get());
        btTransform ownFrame(ToBtQuaternion(rotation_), ToBtVector3(ownBodyScaledPosition));
        btTransform otherFrame(ToBtQuaternion(otherRotation_), ToBtVector3(otherBodyScaledPosition));
        c->setFrames(ownFrame, otherFrame);
    } break;
```

-------------------------

evolgames | 2021-08-02 05:57:07 UTC | #6

Well Im doing scripting and it wasnt under constraint types is what I meant. Basically I do hinges with 0 lowlimit/highlimit and axis. Seems to work. Should/can I switch to what you said?
Or in most cases I child one of the nodes and add matching collision shapes and bodies to just one.

-------------------------

