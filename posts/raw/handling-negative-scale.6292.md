glebedev | 2020-07-31 23:17:39 UTC | #1

In Urho3D the render code always respects culling set in the material.

Batch::Prepare:

            CullMode effectiveCullMode = pass_->GetCullMode();
        // Get cull mode from material if pass doesn't override it
        if (effectiveCullMode == MAX_CULLMODES)
            effectiveCullMode = isShadowPass ? material_->GetShadowCullMode() : material_->GetCullMode();

In Unity3D if Scale of an object is set to negative value so the object matrix changes handedness it flips culling mode (at least it looks like in). As a result an object with a scale (1,1,-1) still looks correct.

Should Urho3D do the same thing?

Or maybe I'm getting this wrong and there is another way to achieve same effect.

-------------------------

Modanung | 2020-08-04 00:00:42 UTC | #2

This might be useful:

https://discourse.urho3d.io/t/missing-faces-obj-to-mdl/6029/32

Maybe change the condition of the if-statement to one checking for a negative scale product of the ModelViewMatrix? ...and then negate `vNormal`.

-------------------------

glebedev | 2020-08-04 07:19:20 UTC | #3

Something should be done on engine side to culling otherwise vertex shader won't be executed. Actually this could be done in compute shader but there isn't one available for all platforms :-(

-------------------------

Eugene | 2020-08-04 09:07:02 UTC | #4

[quote="Modanung, post:2, topic:6292"]
and then negate `vNormal`
[/quote]
`vNormal` has nothing to do with the culling, so shaders are not a solution.

@glebedev culling is currently configured here:
https://github.com/urho3d/Urho3D/blob/97b09f848b9388c0b3cd116906cc0ab3b442ded0/Source/Urho3D/Graphics/Batch.cpp#L213 

But the issue is that drawable scale is already lost at thus point, you only have an array of world transforms that may have different meanings depending on geometry type.
What's worse, you may have instancing enabled here, and you cannot render both inverted and normal geometry in one call.
So if you want to do something, you have to do it somewhere before instancing.

-------------------------

Modanung | 2020-08-04 12:46:39 UTC | #5

[quote="Eugene, post:4, topic:6292"]
`vNormal` has nothing to do with the culling, so shaders are not a solution.
[/quote]

Thanks, I'm spitting in the dark here. :slightly_smiling_face:

-------------------------

