dev4fun | 2018-02-15 21:41:18 UTC | #1

Im using combinned meshes on my game, example: armor its one model, and head its another. Than, I combine the both, and set just one animation for both.

I would like to know if I doing this in correct and better way:

	Node* modelNode = scene_->CreateChild("Pike");
	modelNode->SetPosition(Vector3(Random(40.0f) - 20.0f, 0.0f, Random(40.0f) - 20.0f));
	modelNode->SetRotation(Quaternion(0.0f, Random(360.0f), 0.0f));
	
	auto* modelArmor = modelNode->CreateComponent<AnimatedModel>();
	modelArmor->SetModel(cache->GetResource<Model>("Models/Pike/model.mdl"));
	modelArmor->SetMaterial(cache->GetResource<Material>("Models/Pike/Materials/mat1.xml"));
	modelArmor->SetCastShadows(true);

	auto* modelHead = modelNode->CreateComponent<AnimatedModel>();
	modelHead->SetModel( cache->GetResource<Model>( "Models/Pike/head.mdl" ) );
	modelHead->SetMaterial( cache->GetResource<Material>( "Models/Pike/Materials/mat1.xml" ) );
	modelHead->SetCastShadows( true );

	auto * animationController = modelNode->CreateComponent<AnimationController>();
	animationController->PlayExclusive( "Models/Pike/anim.ani", 0, true, 0.0f );

Im asking this, because all characters will works this way, and need to know if Im using the better way on on performance issues (I dont want to drop so much the FPS).

Thanks!

-------------------------

Lumak | 2018-02-15 23:11:37 UTC | #2

Yes, that is the suggested method. And yes, you should be concerned with performance doing it this way because for a *n* number of animated models you have with a *m* number of bones, you're articulating **n x m** matrix multiplications per frame.  You can circumvent this by creating place-holder geometries (simple quads for example) in your main animated character model and swap in/out your armor at runtime.

edit: here's an example model: https://github.com/Lumak/Urho3D-Skinned-Armor/tree/master/bin/Data/SkinnedArmor/Girlbot

-------------------------

dev4fun | 2018-02-15 23:22:00 UTC | #3

Hmm got it.. have some great advantage using a model with all armors, and this way just set the desired armor at runtime? (I believe that u made something like this, but instead of armors, parts of armor).

Do u know if Urho3D have some cache system or instance to make this system better? Because if have two characters using same armor, the skinning is the same, so I dont know if Urho3D instance this to gain performance.

-------------------------

Sinoid | 2018-02-16 15:36:33 UTC | #4

[quote="Lumak, post:2, topic:4022"]
And yes, you should be concerned with performance doing it this way because for a n number of animated models you have with a m number of bones, you’re articulating n x m matrix multiplications per frame.
[/quote]

Quoting the documentation @ 

https://urho3d.github.io/documentation/1.5/_skeletal_animation.html:

> **Combined skinned models**
To create a combined skinned model from many parts (for example body + clothes), several AnimatedModel components can be created to the same scene node. **These will then share the same bone nodes.** The component that was first created will be the "master" model which drives the animations; the rest of the models will just skin themselves using the same bones. For this to work, all parts must have been authored from a compatible skeleton, with the same bone names. The master model should have all the bones required by the combined whole (for example a full biped), while the other models may omit unnecessary bones. Note that if the parts contain compatible vertex morphs (matching names), the vertex morph weights will also be controlled by the master model and copied to the rest.

Also, GPU skinning is a thing and bones * nodes is pretty much irrelevant - it's the vertex count that matters in skinning ... a weighted blend of matrices and a mult for every vertex. Thus, GPU skinning.

-------------------------

Lumak | 2018-02-16 21:49:29 UTC | #5

Here's snippet of the UpdateSkinning fn.
```
void AnimatedModel::UpdateSkinning()
{
    // Note: the model's world transform will be baked in the skin matrices
    const Vector<Bone>& bones = skeleton_.GetBones();
    // Use model's world transform in case a bone is missing
    const Matrix3x4& worldTransform = node_->GetWorldTransform();

    // Skinning with global matrices only
    if (!geometrySkinMatrices_.Size())
    {
        for (unsigned i = 0; i < bones.Size(); ++i)
        {
            const Bone& bone = bones[i];
            if (bone.node_)
                skinMatrices_[i] = bone.node_->GetWorldTransform() * bone.offsetMatrix_;
            else
                skinMatrices_[i] = worldTransform;
        }
    }
```
This line in particular:
***skinMatrices_[i] = bone.node_->GetWorldTransform() * bone.offsetMatrix_;***
is the **m x n** matrix multiplications per frame.  GPU skinning still requires **skinMatrices_[]** to be computed by the CPU (edit, added the CPU part).

-------------------------

