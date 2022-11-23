UrhoIsTheBest | 2020-08-31 06:16:48 UTC | #1

Those text are covered by other objects.

**Is there an easy/quick way to make sure Text3D always on the top?** 
I tried ```text->SetOccludee(false)```, but it does not work.

![image|690x259](upload://6fE8OD3h7hj30WfjnNnjra80Jdt.jpeg)

I saw some discussion about creating new material and setting rendering order there. But I am not sure:
1. Is that the only solution?
2. It's not a scalable solution for me by hard coding some rendering order since the text does not know all the other objects in the scene, and it's not guaranteed the Text3D is the last to render and will not be occluded.

-------------------------

JTippetts1 | 2020-09-01 07:45:24 UTC | #2

If you are using the default material, it doesn't call Pass::SetDepthTestMode(), so it defaults to CMP_LESSEQUAL, meaning that it will be occluded by solid objects that write depth. If you assign the Text3D a custom material, you can set the depth test to CMP_ALWAYS to always draw the text regardless of the depth. You can either do this explicitly (Pass::SetDepthTestMode()) or you can do it as part of the material definition file if you load the material def from a file.

-------------------------

UrhoIsTheBest | 2020-09-01 07:45:21 UTC | #3

Thanks. I checked the default material for Text3D is just one alpha pass with Text shaders. 

One thing I noticed is the ```Text3D.material_``` would be nullptr since the default material is directly applied to each ```batches_[i]```. So I have to access that material instead:
```
auto* material = region_title->GetBatches()[0].material_.Get();
material->GetPass(0, "alpha")->SetDepthTestMode(CMP_ALWAYS);
```
But, yes, I can create a plain simple xml material file based on this setting.

**Another followup question:** any use case that different ```batches_[i]``` for Text3D have different materials?
I am asking this because each batch is clone the material instead of use a pointer to the same material
```
batches_[i].material_ = material_->Clone();
```

-------------------------

Pencheff | 2020-09-09 02:02:56 UTC | #4

UIBatch::material_ was exposed not long ago for another feature - to render UI element with custom shader. I don't think anything else in Urho3D is using it right now.

-------------------------

