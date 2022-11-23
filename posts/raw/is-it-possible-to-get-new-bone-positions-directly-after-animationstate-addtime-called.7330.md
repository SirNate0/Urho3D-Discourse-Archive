Jens | 2022-09-22 11:18:00 UTC | #1

Hi forum dwellers, 
The problem is I have an animation driven character who is holding a non-animated object. The object has a collision shape which interacts with other objects in the game. At the end of OnUpdate() the object is manually moved so that it follows the animated character. However, the bone positions at this point are those prior to the added x seconds, so the object lags the animated character. At the very latest the object should be moved to the new position before collision physics is employed for the timeStep, but maybe this is just not possible?
    
```
    protected override void OnUpdate(float timeStep)
        {
            AnimationState AniState.AddTime(x);
//bone positions here are from previous timeStep
        }
```

-------------------------

Jens | 2022-09-22 13:42:35 UTC | #2

Looks like it is possible after all. Previously I had tried call Apply() on the AnimationState, but the bone positions were not updated:
```
                AntiClkWiseAniState.Apply();

```
On reflection, I should've looked closer at the AnimatedModel, since ApplyAnimation() does immediately update the bone positions:
```
AniModelObject.ApplyAnimation();
```
Have only just tried this, and the animations look ok; however, I vaguely remember a while back when there was trouble with an animation jerking as it moved. At that time I tried Apply() on the AnimationState and the animation went completely crazy. (In fact, the jerking was caused by the Blender fbx exporter with this particular model - it had worked fine with other models. The issue was fixed by using the excellent [Urho3D Exporter by Dertom95](https://github.com/dertom95/Urho3D-Blender)). 

What I am trying to say is that from that point I had tried to stay away from Apply(), anyway there was no need as the model exported from the Urho3D Exporter was animating fine. Now it looks like I need to use AnimatedModel.ApplyAnimation(). Does anyone know a reason why that might be a bad idea?

-------------------------

