darkirk | 2017-06-16 15:14:44 UTC | #1

Does Urho have any built-in shader for eye adaptation effects?

Something similar to this: 

https://docs.unrealengine.com/latest/INT/Engine/Rendering/PostProcessEffects/AutomaticExposure/

-------------------------

Modanung | 2017-06-16 15:14:11 UTC | #2

It can be achieved by appending the [`AutoExposure`](https://github.com/urho3d/Urho3D/blob/master/bin/Data/PostProcess/AutoExposure.xml) post-processing effect to your `Vieport`'s `RenderPath`.

-------------------------

