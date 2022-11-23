smellymumbler | 2018-01-18 03:32:08 UTC | #1

Does anyone know if Urho has something similar to Unity's Blend Trees? https://docs.unity3d.com/Manual/class-BlendTree.html

Or Root Motion? https://docs.unity3d.com/Manual/RootMotion.html

-------------------------

Eugene | 2018-01-18 06:10:52 UTC | #2

Nope, Urho has only `AnimationController` that is code-driven.
I agree that Urho lacks good animation setup pipeline and want to implement it at some point.

-------------------------

smellymumbler | 2018-01-18 13:28:15 UTC | #3

I mean, i wasn't really looking for something visual. But is there a way of creating what BlendTrees do in Unity with Urho? They allow me to blend multiple animation layers into one, using linear interpolation. 

https://www.youtube.com/watch?v=YgaLKrSApWM

-------------------------

Eugene | 2018-01-18 13:59:03 UTC | #4

[quote="smellymumbler, post:3, topic:3951"]
I mean, i wasn’t really looking for something visual.
[/quote]

Visual part is just a half of the problem.
Urho is trying to be data-driven as much as possible, but there is no chance to define animation with data.
You have to write animation driver code working with `AnimationController`. That sucks.

-------------------------

smellymumbler | 2018-01-18 15:04:47 UTC | #5

By animation driver code you mean the state structure? If walking, play this, if idle, play that? 

But does the AnimationController support blending between animations and layering animations? Is that something that is possible to do, or i have to write my own blending code and my own linear interpolation? I think i need to rephrase my questions a little better.

-------------------------

Modanung | 2018-01-18 15:11:36 UTC | #6

Yes, it is possible, using these `AnimationController` methods:
```
    /// Set animation blending layer priority. Return true on success.
    bool SetLayer(const String& name, unsigned char layer);
    /// Set animation start bone. Return true on success.
    bool SetStartBone(const String& name, const String& startBoneName);
```
```
    /// Set animation weight. Return true on success.
    bool SetWeight(const String& name, float weight);
```
```
    /// Set animation blending mode. Return true on success.
    bool SetBlendMode(const String& name, AnimationBlendMode mode);
```

-------------------------

smellymumbler | 2018-01-18 20:04:21 UTC | #7

OH! That's what i was kind of looking for. Thanks guys.

-------------------------

