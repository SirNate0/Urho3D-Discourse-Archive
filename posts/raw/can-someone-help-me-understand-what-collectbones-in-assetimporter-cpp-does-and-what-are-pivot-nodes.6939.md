Elfstone | 2021-07-30 14:43:39 UTC | #1

```
    for (unsigned i = 0; i < model.meshes_.Size(); ++i)
    {
        aiMesh* mesh = model.meshes_[i];
        aiNode* meshNode = model.meshNodes_[i];
        aiNode* meshParentNode = meshNode->mParent;
        aiNode* rootNode = nullptr;

        for (unsigned j = 0; j < mesh->mNumBones; ++j)
        {
            aiBone* bone = mesh->mBones[j];
            String boneName(FromAIString(bone->mName));
            aiNode* boneNode = GetNode(boneName, scene_->mRootNode, true);
            if (!boneNode)
                ErrorExit("Could not find scene node for bone " + boneName);
            necessary.Insert(boneNode);
            rootNode = boneNode;

            for (;;)
            {
                boneNode = boneNode->mParent;
                if (!boneNode || ((boneNode == meshNode || boneNode == meshParentNode) && !animationOnly))
                    break;
                rootNode = boneNode;
                necessary.Insert(boneNode);
            }

            if (rootNodes.Find(rootNode) == rootNodes.End())
                rootNodes.Insert(rootNode);
        }

        // When model is partially skinned, include the attachment nodes of the rigid meshes in the skeleton
        if (haveSkinnedMeshes && !mesh->mNumBones)
        {
            aiNode* boneNode = meshNode;
            necessary.Insert(boneNode);
            rootNode = boneNode;

            for (;;)
            {
                boneNode = boneNode->mParent;
                if (!boneNode || ((boneNode == meshNode || boneNode == meshParentNode) && !animationOnly))
                    break;
                rootNode = boneNode;
                necessary.Insert(boneNode);
            }

            if (rootNodes.Find(rootNode) == rootNodes.End())
                rootNodes.Insert(rootNode);
        }
    }

    if (rootNodes.Empty())
        return;

    model.rootBone_ = *rootNodes.Begin();
```

I understand it's trying to follow every bone node in a mesh, until it reaches the root bone. And if there are multiple roots it has to find a common root for them.

But what is the purpose of "animationOnly"? `(boneNode == meshNode || boneNode == meshParentNode) && !animationOnly`

So the loop breaks if it reaches a meshNode or its parent only when animationOnly is false -- You'd expect when a parameter is named *Only* , certain operations are skipped when it's true.

And after some failures, trying to manipulate the root bone while importing, I found out that when there are so called "Pivot" nodes in the FBX, the resulting model.rootBone_ seems to be wrong. The pivot nodes (***$AssimpFbx$_PreRotation/_Rotation/_Translation) that are parents to the real root bone seem to be the reason.

I set the AI_CONFIG_IMPORT_FBX_PRESERVE_PIVOTS flag false, the pivot nodes are gone, and my code is working for the moment. The innermost loops break when the new boneNode == meshParentNode, which shouldn't be a bone -- when the pivots are present, the meshParentNode is the first pivot, and the loop breaks when boneNode == NULL and rootBone is the root of the entire scene.

But what are Pivot nodes really? Are they literally just pivots that I can ignore if the transformations from the root node are handled correctly? What am I risking if I don't preserve them?

-------------------------

