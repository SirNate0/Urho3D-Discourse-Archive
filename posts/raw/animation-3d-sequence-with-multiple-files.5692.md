Askhento | 2019-10-29 07:23:00 UTC | #1

Hello forum. I've read some docs and asked here about **animation controller**, so I can start, pause and set speed of 3d animation. But imagine if a 3d model will have **multiple animation files**  and I want to play them in a sequence with knots. Does it possible to achieve with **animation controller**, or do I need to use other?
My idea for now is to use IsAtEnd() method to reassign the animation.

-------------------------

Modanung | 2019-10-29 11:46:16 UTC | #2

You'll probably want to use this _drawable event_ to trigger the next animation:
```
/// AnimatedModel animation finished or looped.
URHO3D_EVENT(E_ANIMATIONFINISHED, AnimationFinished)
{
    URHO3D_PARAM(P_NODE, Node);                    // Node pointer
    URHO3D_PARAM(P_ANIMATION, Animation);          // Animation pointer
    URHO3D_PARAM(P_NAME, Name);                    // String
    URHO3D_PARAM(P_LOOPED, Looped);                // Bool
}
```

-------------------------

