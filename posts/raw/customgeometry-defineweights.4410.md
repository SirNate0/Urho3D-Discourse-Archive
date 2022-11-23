simonsch | 2018-07-26 13:29:35 UTC | #1

Hello Community it is me again with a problem related to CustomGeometry.

I have a vertexBuffer which consists out of
MASK_POSITION | MASK_NORMAL | MASK_BLENDWEIGHTS | MASK_BLENDINDICES

Because of a specific reason i have to lock this vertexBuffer, read its vertex data and write it through an CustomGeometry. The point is i see no way for CustomGeometry to define MASK_BLENDWEIGHTS and MASK_BLENDINDICES.

Like with the functions DefinePosition(), DefineNormal(), DefineTangent(), DefineColor(), any help would be great. 

As always if you need more information on the topic feel free to ask.

Best Regards

-------------------------

cadaver | 2018-07-26 14:52:14 UTC | #2

The ideal should be that you never need to go back from a VertexBuffer (which is already the optimal storage format) to CustomGeometry, which is limited in its use cases and only intended for easy programmatic geometry generation for beginners.

Is the reason in the application or in Urho3D API itself? If in Urho3D, it sounds like worth fixing.

There are also other limits in CustomGeometry, like no second texture coords.

-------------------------

Eugene | 2018-07-26 18:19:54 UTC | #3

The issue is much deeper than just absence of few functions.
For sane usage of blend weights and indices you have to prepare and pass skeletal matrices into shader.
And `CustomGeometry` doesn't have such routines.

-------------------------

simonsch | 2018-07-27 07:04:18 UTC | #4

Thank you for the answer i assumed something like this, the problem is that i have a urho scene with an mdl, the scene contains joint information. For this model i want to define vertexcolor information, but the current vertex buffer has now color mask integrated.

My first attempt was to create a new vertex buffer pass in the old position, normal data and add color on a per vertex base. But then replacing the old vertex buffer didn't work and gave me weird render issues. With CustomGeometry i was able to do this except applying the weights.

Simple said i want a 1 to 1 copy of my node with its AnimatedModel component just with some self defined vertex colors.

-------------------------

simonsch | 2018-07-27 07:05:00 UTC | #5

Hi, thank you for your answer. Yeah i also wondered where the skeletal data is read from my scene then. For details see above post.

-------------------------

cadaver | 2018-07-27 08:56:07 UTC | #6

Replacing the vertexbuffer is exactly what you should do, and I can't think of any reason of why it should fail (except if there's a bug in Urho3D, in which case you can open an issue), if you interleave the new data with the old data correctly.

-------------------------

simonsch | 2018-07-27 09:17:57 UTC | #7

Okay then i will share some code
 
        // Clone root node to get joint information
        Node *bufNode = scene_a_->GetChild("RootNode")->Clone();

        // Extract the model components which store the needed vbo for redrawing
        PODVector<Model *> models{};
        PODVector<StaticModel *> modelComponents{};
        bufNode->GetDerivedComponents<StaticModel>(modelComponents, true);
        for (StaticModel *modelComponent : modelComponents) {
            models.Push(modelComponent->GetModel());
        }
        Skeleton skeletonBuffer = models[0]->GetSkeleton();

        // Get old vbo and ibo
        SharedPtr<VertexBuffer> oldVertexBuffer = models[0]->GetVertexBuffers()[0];
        SharedPtr<IndexBuffer> oldIndicesBuffer = models[0]->GetIndexBuffers()[0];

        unsigned indexSize = oldIndicesBuffer->GetIndexSize();
        unsigned numIndices = oldIndicesBuffer->GetIndexCount();
        unsigned oldVertexSize = oldVertexBuffer->GetVertexSize();
        unsigned numVertices = oldVertexBuffer->GetVertexCount();

        // Define a new child node for drawing
        Node *newNode = bufNode->CreateChild("result");
        // Little offset so both models don't totally overlap
        newNode->SetPosition(Vector3(0.01,0.0,0.0));
        SharedPtr<AnimatedModel> newAnimatedModel(
                newNode->CreateComponent<AnimatedModel>());
        SharedPtr<Model> newModel(new Model(context_));
        SharedPtr<VertexBuffer> newVertexBuffer(new VertexBuffer(context_));
        SharedPtr<Geometry> newGeometry(new Geometry(context_));
        newVertexBuffer->SetSize(numVertices, MASK_POSITION | MASK_NORMAL | MASK_TEXCOORD1 | MASK_BLENDWEIGHTS | MASK_BLENDINDICES);
        unsigned newVertexSize = newVertexBuffer->GetVertexSize();


        // LOCK old and new vbo for editing reading vertex data
        unsigned char *oldVertexData = (unsigned char *) oldVertexBuffer->Lock(0, numVertices);
        unsigned char *newVertexData = (unsigned char *) newVertexBuffer->Lock(0, numVertices);
        if (oldVertexData) {
                unsigned oldMask = oldVertexBuffer->GetElementMask();
                unsigned oldPositionOffset = oldVertexBuffer->GetElementOffset(SEM_POSITION);
                unsigned oldNormalOffset = oldVertexBuffer->GetElementOffset(SEM_NORMAL);
                unsigned oldColorOffset = oldVertexBuffer->GetElementOffset(SEM_COLOR);
                unsigned oldBlendWeightOffset = oldVertexBuffer->GetElementOffset(SEM_BLENDWEIGHTS);
                unsigned oldBlendIndicesOffset = oldVertexBuffer->GetElementOffset(SEM_BLENDINDICES);
                unsigned newMask = newVertexBuffer->GetElementMask();
                unsigned newPositionOffset = newVertexBuffer->GetElementOffset(SEM_POSITION);
                unsigned newNormalOffset = newVertexBuffer->GetElementOffset(SEM_NORMAL);
                unsigned newColorOffset = newVertexBuffer->GetElementOffset(SEM_COLOR);
                unsigned newBlendWeightOffset = newVertexBuffer->GetElementOffset(SEM_BLENDWEIGHTS);
                unsigned newBlendIndicesOffset = newVertexBuffer->GetElementOffset(SEM_BLENDINDICES);

                for (int i = 0; i < numVertices; i++) {
                    // Old vertex buffer data
                    unsigned char *oldVertexPos = (oldVertexData + i * oldVertexSize + oldPositionOffset);
                    unsigned char *oldVertexNormal = (oldVertexData + i * oldVertexSize + oldNormalOffset);
                    unsigned char *oldVertexWeights = (oldVertexData + i * oldVertexSize +
                            oldBlendWeightOffset);
                    unsigned char *oldVertexWeightIndices = (oldVertexData + i * oldVertexSize +
                            oldBlendIndicesOffset);
                    // New vertex buffer data
                    unsigned char *newVertexPos = (newVertexData + i * newVertexSize + newPositionOffset);
                    unsigned char *newVertexNormal = (newVertexData + i * newVertexSize + newNormalOffset);
                    unsigned char *newVertexWeights = (newVertexData + i * newVertexSize +
                            newBlendWeightOffset);
                    unsigned char *newVertexWeightIndices = (newVertexData + i * newVertexSize +
                            newBlendIndicesOffset);
                    if (oldMask & MASK_POSITION) {
                        Vector3 &src_pos = *reinterpret_cast<Vector3 *>( oldVertexPos );
                        Vector3 &target_pos = *reinterpret_cast<Vector3 *>( newVertexPos );
                        target_pos = src_pos;
                    }
                    if (oldMask & MASK_NORMAL) {
                        Vector3 &src_normal = *reinterpret_cast<Vector3 *>( oldVertexNormal );
                        Vector3 &target_normal = *reinterpret_cast<Vector3 *>( newVertexNormal );
                        target_normal = src_normal;
                    }
                    if (oldMask & MASK_BLENDWEIGHTS) {
                        newVertexWeights = oldVertexWeights;
                    }
                    if (oldMask & MASK_BLENDINDICES) {
                        newVertexWeightIndices = oldVertexWeightIndices;
                    }

                oldVertexBuffer->Unlock();
                newVertexBuffer->Unlock();
            }
        }
        newGeometry->SetVertexBuffer(0, newVertexBuffer);
        newGeometry->SetIndexBuffer(oldIndicesBuffer);
        newGeometry->SetDrawRange(TRIANGLE_LIST, 0, 0, 0,numVertices);
        newModel->SetSkeleton(skeletonBuffer);
        newModel->SetNumGeometries(1);
        newModel->SetGeometry(0, 0, newGeometry);
        newAnimatedModel->SetModel(newModel);
        newAnimatedModel->SetMaterial(vcolmat);
        scene_->AddChild(bufNode);

1. This shows only the original model not the new node. This was another try not to replace the vbo but instead creating a copy of the node with a new vbo. 

2. Additionally, i should also mention that i don't know which structure weights and indices have in the vbo the offset tells me    
    Blend weight Offset 32 
    Blend indices Offset 48 
But what are those data? I assume those indices are ints?
For the normals e.g. i can get the stride like
unsigned char *oldVertexNormal = (oldVertexData + i * oldVertexSize + oldNormalOffset);
and cast it
Vector3 &src_normal = *reinterpret_cast<Vector3 *>( oldVertexNormal );
But what if i want the indices and weights as values? How many are in one stride? Which type they are? Sry if this is obvious.

3. And now the problem after the problem (yep it goes on). I need the absolute vertex position for some calculation which should give me those vertex colors, i want to display. Is there an easy way reading joint information from scene.xml, using weights, indices from vbo and applying those to our vertex positions? Or do i need to calculate it all via hand? If so i really need help with 2.

-------------------------

cadaver | 2018-07-27 09:19:23 UTC | #8

The hardcoded vertex elements (referred to with mask bits) are defined in GraphicsDefs.cpp. You'll see that a blendweights element is a Vector4, and blendindices is 4 bytes (so practically an unsigned int).

So it looks in your code you're not copying enough data for the weights & indices.

-------------------------

simonsch | 2018-07-27 09:27:53 UTC | #9

Sry was still editing my post :slight_smile:. So it is possible you missed part 3.

That helps a lot! So both include 4 values? 4 indices with 4 weights.
I will try fix that, but at least i should see something when copy the position to the vbo. The loop is iterated correct but after replacing the vbo 
        models[0]->GetGeometry(0,0)->SetVertexBuffer(0,newVertexBuffer);
Nothing is rendering.

-------------------------

cadaver | 2018-07-27 09:31:24 UTC | #10

Urho doesn't offer software skinning, so your best bet would be to run your calculation in vertex shader, where you have the skinned world positions.

In skeletal animation, nothing will render correctly without correct blend weights / indices, as the vertex position is multiplied by matrices selected by the index.

-------------------------

simonsch | 2018-07-27 10:21:05 UTC | #11

Hm 

        // Clone root node to get joint information
        Node *bufNode = scene_a_->GetChild("RootNode")->Clone();

        // Extract the model components which store the needed vbo for redrawing
        PODVector<Model *> models{};
        PODVector<StaticModel *> modelComponents{};
        bufNode->GetDerivedComponents<StaticModel>(modelComponents, true);
        for (StaticModel *modelComponent : modelComponents) {
            models.Push(modelComponent->GetModel());
        }
        Skeleton skeletonBuffer = models[0]->GetSkeleton();

        // Get old vbo and ibo
        SharedPtr<VertexBuffer> oldVertexBuffer = models[0]->GetVertexBuffers()[0];
        SharedPtr<IndexBuffer> oldIndicesBuffer = models[0]->GetIndexBuffers()[0];

        unsigned indexSize = oldIndicesBuffer->GetIndexSize();
        unsigned numIndices = oldIndicesBuffer->GetIndexCount();
        unsigned oldVertexSize = oldVertexBuffer->GetVertexSize();
        unsigned numVertices = oldVertexBuffer->GetVertexCount();

        // Define a new child node for drawing
        Node *newNode = bufNode->CreateChild("result");
        // Little offset so both models don't totally overlap
        newNode->SetPosition(Vector3(0.01,0.0,0.0));
        SharedPtr<AnimatedModel> newAnimatedModel(
                newNode->CreateComponent<AnimatedModel>());
        SharedPtr<Model> newModel(new Model(context_));
        SharedPtr<VertexBuffer> newVertexBuffer(new VertexBuffer(context_));
        SharedPtr<Geometry> newGeometry(new Geometry(context_));
        newVertexBuffer->SetSize(numVertices, MASK_POSITION | MASK_NORMAL | MASK_TEXCOORD1 | MASK_BLENDWEIGHTS | MASK_BLENDINDICES);
        unsigned newVertexSize = newVertexBuffer->GetVertexSize();


        // LOCK old and new vbo for editing reading vertex data
        unsigned char *oldVertexData = (unsigned char *) oldVertexBuffer->Lock(0, numVertices);
        unsigned char *newVertexData = (unsigned char *) newVertexBuffer->Lock(0, numVertices);
        if (oldVertexData) {
                unsigned oldMask = oldVertexBuffer->GetElementMask();
                unsigned oldPositionOffset = oldVertexBuffer->GetElementOffset(SEM_POSITION);
                unsigned oldNormalOffset = oldVertexBuffer->GetElementOffset(SEM_NORMAL);
                unsigned oldColorOffset = oldVertexBuffer->GetElementOffset(SEM_COLOR);
                unsigned oldBlendWeightOffset = oldVertexBuffer->GetElementOffset(SEM_BLENDWEIGHTS);
                unsigned oldBlendIndicesOffset = oldVertexBuffer->GetElementOffset(SEM_BLENDINDICES);

                unsigned newMask = newVertexBuffer->GetElementMask();
                unsigned newPositionOffset = newVertexBuffer->GetElementOffset(SEM_POSITION);
                unsigned newNormalOffset = newVertexBuffer->GetElementOffset(SEM_NORMAL);
                unsigned newColorOffset = newVertexBuffer->GetElementOffset(SEM_COLOR);
                unsigned newBlendWeightOffset = newVertexBuffer->GetElementOffset(SEM_BLENDWEIGHTS);
                unsigned newBlendIndicesOffset = newVertexBuffer->GetElementOffset(SEM_BLENDINDICES);
        
                         for (int i = 0; i < numVertices; i++) {
                             // Old vertex buffer data
                             unsigned char *oldVertexPos = (oldVertexData + i * oldVertexSize + oldPositionOffset);
                             unsigned char *oldVertexNormal = (oldVertexData + i * oldVertexSize + oldNormalOffset);
                             unsigned char *oldVertexWeights = (oldVertexData + i * oldVertexSize +
                                     oldBlendWeightOffset);
                             unsigned char *oldVertexWeightIndices = (oldVertexData + i * oldVertexSize +
                                     oldBlendIndicesOffset);
                             // New vertex buffer data
                             unsigned char *newVertexPos = (newVertexData + i * newVertexSize + newPositionOffset);
                             unsigned char *newVertexNormal = (newVertexData + i * newVertexSize + newNormalOffset);
                             unsigned char *newVertexWeights = (newVertexData + i * newVertexSize +
                                     newBlendWeightOffset);
                             unsigned char *newVertexWeightIndices = (newVertexData + i * newVertexSize +
                                     newBlendIndicesOffset);
                             if (oldMask & MASK_POSITION) {
                                 Vector3 &src_pos = *reinterpret_cast<Vector3 *>( oldVertexPos );
                                 Vector3 &target_pos = *reinterpret_cast<Vector3 *>( newVertexPos );
                                 target_pos.x_ = src_pos.x_;
                                 target_pos.y_ = src_pos.y_;
                                 target_pos.z_ = src_pos.z_;
                             }
                             if (oldMask & MASK_NORMAL) {
                                 Vector3 &src_normal = *reinterpret_cast<Vector3 *>( oldVertexNormal );
                                 Vector3 &target_normal = *reinterpret_cast<Vector3 *>( newVertexNormal );
                                 target_normal.x_ = src_normal.x_;
                                 target_normal.y_ = src_normal.y_;
                                 target_normal.z_ = src_normal.z_;
                             }
                             if (oldMask & MASK_BLENDWEIGHTS) {
                                 Vector4 &src_weights = *reinterpret_cast<Vector4 *>( oldVertexWeights );
                                 Vector4 &target_weights = *reinterpret_cast<Vector4 *>( newVertexWeights );

                                 target_weights.x_ = src_weights.x_;
                                 target_weights.y_ = src_weights.y_;
                                 target_weights.z_ = src_weights.z_;
                                 target_weights.w_ = src_weights.w_;
                             }
                             if (oldMask & MASK_BLENDINDICES) {
                                 unsigned int &src_weights = *reinterpret_cast<unsigned int  *>( oldVertexWeightIndices );
                                 unsigned int &target_weights = *reinterpret_cast<unsigned int  *>( newVertexWeightIndices );

                                 target_weights = src_weights;
                             }

                         oldVertexBuffer->Unlock();
                         newVertexBuffer->Unlock();
                     }
                 }
        models[0]->GetGeometry(0,0)->SetVertexBuffer(0,newVertexBuffer);
        scene_->AddChild(bufNode);

Still not rendering anything.

Yeah for a single model that would make sense but i want to compare those values to another model, think i will try doing it on the cpu. It is only done once at scene creation.

-------------------------

simonsch | 2018-07-27 13:05:04 UTC | #12

I am stupid had some mutex lock issues on my vbo caused by incorrect brackets. It renders 'something' now. Will update the status asap.

UPDATE:
So finally it works i can replace the vertex buffer of the model with another vertex buffer where i add vertex colors. (For now) only red, here is the working code:

        // Clone root node to get joint information
        Node *bufNode = scene_a_->GetChild("RootNode")->Clone();

        // Extract the model components which store the needed vbo for redrawing
        PODVector<StaticModel *> modelComponents{};
        bufNode->GetDerivedComponents<StaticModel>(modelComponents, true);
        
        // Get old vbo and ibo
        SharedPtr<VertexBuffer> oldVertexBuffer = modelComponents[0]->GetModel()->GetVertexBuffers()[0];
        SharedPtr<IndexBuffer> oldIndicesBuffer = modelComponents[0]->GetModel()->GetIndexBuffers()[0];

        unsigned indexSize = oldIndicesBuffer->GetIndexSize();
        unsigned numIndices = oldIndicesBuffer->GetIndexCount();
        unsigned oldVertexSize = oldVertexBuffer->GetVertexSize();
        unsigned numVertices = oldVertexBuffer->GetVertexCount();

        // Define a new child node for drawing
        Node *newNode = bufNode->GetChild("output.obj");
        // Little offset so both models don't totally overlap
        newNode->SetPosition(Vector3(0.0, 0.0, 0.0));
        SharedPtr<Model> newModel(new Model(context_));
        SharedPtr<VertexBuffer> newVertexBuffer(new VertexBuffer(context_));
        SharedPtr<Geometry> newGeometry(new Geometry(context_));
        newVertexBuffer->SetSize(numVertices,
                                 MASK_POSITION | MASK_NORMAL | MASK_COLOR | MASK_BLENDWEIGHTS |
                                 MASK_BLENDINDICES);
        unsigned newVertexSize = newVertexBuffer->GetVertexSize();

        // LOCK old and new vbo for editing reading vertex data
        unsigned char *oldVertexData = (unsigned char *) oldVertexBuffer->Lock(0, numVertices);
        unsigned char *newVertexData = (unsigned char *) newVertexBuffer->Lock(0, numVertices);
        if (oldVertexData) {
            unsigned oldMask = oldVertexBuffer->GetElementMask();
            unsigned oldPositionOffset = oldVertexBuffer->GetElementOffset(SEM_POSITION);
            unsigned oldNormalOffset = oldVertexBuffer->GetElementOffset(SEM_NORMAL);
            unsigned oldColorOffset = oldVertexBuffer->GetElementOffset(SEM_COLOR);
            unsigned oldBlendWeightOffset = oldVertexBuffer->GetElementOffset(SEM_BLENDWEIGHTS);
            unsigned oldBlendIndicesOffset = oldVertexBuffer->GetElementOffset(SEM_BLENDINDICES);

            unsigned newMask = newVertexBuffer->GetElementMask();
            unsigned newPositionOffset = newVertexBuffer->GetElementOffset(SEM_POSITION);
            unsigned newNormalOffset = newVertexBuffer->GetElementOffset(SEM_NORMAL);
            unsigned newColorOffset = newVertexBuffer->GetElementOffset(SEM_COLOR);
            unsigned newBlendWeightOffset = newVertexBuffer->GetElementOffset(SEM_BLENDWEIGHTS);
            unsigned newBlendIndicesOffset = newVertexBuffer->GetElementOffset(SEM_BLENDINDICES);

            for (int i = 0; i < numVertices; i++) {
                // Old vertex buffer data
                unsigned char *oldVertexPos = (oldVertexData + i * oldVertexSize +
                                               oldPositionOffset);
                unsigned char *oldVertexNormal = (oldVertexData + i * oldVertexSize +
                                                  oldNormalOffset);
                unsigned char *oldVertexWeights = (oldVertexData + i * oldVertexSize +
                                                   oldBlendWeightOffset);
                unsigned char *oldVertexWeightIndices = (oldVertexData + i * oldVertexSize +
                                                         oldBlendIndicesOffset);
                // New vertex buffer data
                unsigned char *newVertexPos = (newVertexData + i * newVertexSize +
                                               newPositionOffset);
                unsigned char *newVertexColor = (newVertexData + i * newVertexSize +
                                               newColorOffset);
                unsigned char *newVertexNormal = (newVertexData + i * newVertexSize +
                                                  newNormalOffset);
                unsigned char *newVertexWeights = (newVertexData + i * newVertexSize +
                                                   newBlendWeightOffset);
                unsigned char *newVertexWeightIndices = (newVertexData + i * newVertexSize +
                                                         newBlendIndicesOffset);
                if (oldMask & MASK_POSITION) {
                    Vector3 &src_pos = *reinterpret_cast<Vector3 *>( oldVertexPos );
                    Vector3 &target_pos = *reinterpret_cast<Vector3 *>( newVertexPos );
                    target_pos.x_ = src_pos.x_;
                    target_pos.y_ = src_pos.y_;
                    target_pos.z_ = src_pos.z_;
                }
                if (oldMask & MASK_NORMAL) {
                    Vector3 &src_normal = *reinterpret_cast<Vector3 *>( oldVertexNormal );
                    Vector3 &target_normal = *reinterpret_cast<Vector3 *>( newVertexNormal );
                    target_normal.x_ = src_normal.x_;
                    target_normal.y_ = src_normal.y_;
                    target_normal.z_ = src_normal.z_;
                }
                if (oldMask & MASK_BLENDWEIGHTS) {
                    Vector4 &src_weights = *reinterpret_cast<Vector4 *>( oldVertexWeights );
                    Vector4 &target_weights = *reinterpret_cast<Vector4 *>( newVertexWeights );

                    target_weights.x_ = src_weights.x_;
                    target_weights.y_ = src_weights.y_;
                    target_weights.z_ = src_weights.z_;
                    target_weights.w_ = src_weights.w_;
                }
                if (oldMask & MASK_BLENDINDICES) {
                    unsigned int &src_weights = *reinterpret_cast<unsigned int *>( oldVertexWeightIndices );
                    unsigned int &target_weights = *reinterpret_cast<unsigned int *>( newVertexWeightIndices );
                    target_weights = src_weights;

                }
                unsigned int &target_color = *reinterpret_cast<unsigned int *>( newVertexColor );
                target_color = Color(1.0,0.0,0.0,1.0).ToUInt();
            }
        }
        oldVertexBuffer->Unlock();
        newVertexBuffer->Unlock();
        modelComponents[0]->GetModel()->GetGeometry(0,0)->SetVertexBuffer(0,newVertexBuffer);
        modelComponents[0]->SetMaterial(vcolmat);

        scene_->AddChild(scene_a_);
        scene_->AddChild(bufNode);

So let us talk about weights again. I have 4 for weights and an uint for weight indices, are those indices corresponding to the models skeleton and its bones? How does the uint split into 4 indices for the for weights?

-------------------------

cadaver | 2018-07-27 13:30:47 UTC | #13

Check skinning code (UpdateSkinning function) in AnimatedModel.cpp + the skinning shader transformation (GetSkinMatrix) in Transform.glsl / hlsl. In the easy case, where skeleton as a whole doesn't go over skinning bone limit, the 8-bit indices are directly the skeleton bone indices. Otherwise they go through a per-submodel mapping.

The lowest 8 bits (or the first byte) of the index correspond to the weight stored in the x component of the weight Vector4, the next correspond to y and so on.

-------------------------

simonsch | 2018-07-30 08:03:16 UTC | #14

Just if someone wants to know how to extract the 4 bytes from the unsigned int extracted from vbo.
      
    unsigned int i1 = target_indices & 0x000000FF;
    unsigned int i2 = (target_indices >> 8) & 0x000000FF;
    unsigned int i3 = (target_indices >> 16) & 0x000000FF;
    unsigned int i4 = (target_indices >> 24) & 0x000000FF;

-------------------------

simonsch | 2018-07-30 16:43:49 UTC | #15

I need to bother you and the community again ;).

I have the weights and their indices, now i am trying to get the bone information from the scene. Here is the Root Node:
```
    <node id="4">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="RootNode" />
		<attribute name="Tags" />
		<attribute name="Position" value="0 0 -0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="0.01 0.01 0.01" />
		<attribute name="Variables" />
		<node id="5">
			<attribute name="Is Enabled" value="true" />
			<attribute name="Name" value="world_offset" />
			<attribute name="Tags" />
			<attribute name="Position" value="0 0 -0" />
			<attribute name="Rotation" value="1 0 0 0" />
			<attribute name="Scale" value="1 1 1" />
			<attribute name="Variables" />
			<node id="6">
				<attribute name="Is Enabled" value="true" />
				<attribute name="Name" value="base" />
				<attribute name="Tags" />
				<attribute name="Position" value="0.010468 0.883459 -0.008136" />
				<attribute name="Rotation" value="1 0 0 0" />
				<attribute name="Scale" value="1 1 1" />
				<attribute name="Variables" />
				<node id="7">
					<attribute name="Is Enabled" value="true" />
					<attribute name="Name" value="spine1" />
					<attribute name="Tags" />
					<attribute name="Position" value="-0.000507 0.179195 0.015135" />
					<attribute name="Rotation" value="1 0 0 0" />
					<attribute name="Scale" value="1 1 1" />
					<attribute name="Variables" />
					<node id="8">
						<attribute name="Is Enabled" value="true" />
						<attribute name="Name" value="spine2" />
						<attribute name="Tags" />
						<attribute name="Position" value="-6.3e-05 0.144263 0.002484" />
						<attribute name="Rotation" value="1 0 0 0" />
						<attribute name="Scale" value="1 1 1" />
						<attribute name="Variables" />
						<node id="9">
							<attribute name="Is Enabled" value="true" />
							<attribute name="Name" value="spine3" />
							<attribute name="Tags" />
							<attribute name="Position" value="-0.003294 0.206917 0.022406" />
							<attribute name="Rotation" value="1 0 0 0" />
							<attribute name="Scale" value="1 1 1" />
							<attribute name="Variables" />
							<node id="10">
								<attribute name="Is Enabled" value="true" />
								<attribute name="Name" value="spine4" />
								<attribute name="Tags" />
								<attribute name="Position" value="-0.010595 0.112027 -0.018882" />
								<attribute name="Rotation" value="1 0 0 0" />
								<attribute name="Scale" value="1 1 1" />
								<attribute name="Variables" />
								<node id="11">
									<attribute name="Is Enabled" value="true" />
									<attribute name="Name" value="spine5" />
									<attribute name="Tags" />
									<attribute name="Position" value="-0.000212 0.034025 -0.001683" />
									<attribute name="Rotation" value="1 0 0 0" />
									<attribute name="Scale" value="1 1 1" />
									<attribute name="Variables" />
									<node id="12">
										<attribute name="Is Enabled" value="true" />
										<attribute name="Name" value="skullbase" />
										<attribute name="Tags" />
										<attribute name="Position" value="-0.005587 0.065566 -0.009266" />
										<attribute name="Rotation" value="1 0 0 0" />
										<attribute name="Scale" value="1 1 1" />
										<attribute name="Variables" />
										<node id="13">
											<attribute name="Is Enabled" value="true" />
											<attribute name="Name" value="head" />
											<attribute name="Tags" />
											<attribute name="Position" value="-0.003432 0.063759 -0.005846" />
											<attribute name="Rotation" value="1 0 0 0" />
											<attribute name="Scale" value="1 1 1" />
											<attribute name="Variables" />
										</node>
									</node>
								</node>
							</node>
							<node id="14">
								<attribute name="Is Enabled" value="true" />
								<attribute name="Name" value="r_shoulder" />
								<attribute name="Tags" />
								<attribute name="Position" value="-0.1955 -0.047464 0.045533" />
								<attribute name="Rotation" value="0.998081 0.0525232 -0.0219416 0.0243751" />
								<attribute name="Scale" value="1 1 1" />
								<attribute name="Variables" />
								<node id="15">
									<attribute name="Is Enabled" value="true" />
									<attribute name="Name" value="r_elbow" />
									<attribute name="Tags" />
									<attribute name="Position" value="-0.117085 -0.24122 0.035155" />
									<attribute name="Rotation" value="0.996067 0.0461258 -0.0196229 0.0730643" />
									<attribute name="Scale" value="1 1 1" />
									<attribute name="Variables" />
									<node id="16">
										<attribute name="Is Enabled" value="true" />
										<attribute name="Name" value="r_wrist" />
										<attribute name="Tags" />
										<attribute name="Position" value="-0.173698 -0.228774 0.048215" />
										<attribute name="Rotation" value="0.986227 -0.154335 0.0435345 0.0405159" />
										<attribute name="Scale" value="1 1 1" />
										<attribute name="Variables" />
										<node id="17">
											<attribute name="Is Enabled" value="true" />
											<attribute name="Name" value="r_hand" />
											<attribute name="Tags" />
											<attribute name="Position" value="-0.019034 -0.021876 -0.048998" />
											<attribute name="Rotation" value="1 -0.00034527 0 0" />
											<attribute name="Scale" value="1 1 1" />
											<attribute name="Variables" />
										</node>
									</node>
								</node>
							</node>
							<node id="18">
								<attribute name="Is Enabled" value="true" />
								<attribute name="Name" value="l_shoulder" />
								<attribute name="Tags" />
								<attribute name="Position" value="0.207959 -0.029926 -0.012704" />
								<attribute name="Rotation" value="0.998255 -0.025097 -0.0123939 -0.0519856" />
								<attribute name="Scale" value="1 1 1" />
								<attribute name="Variables" />
								<node id="19">
									<attribute name="Is Enabled" value="true" />
									<attribute name="Name" value="l_elbow" />
									<attribute name="Tags" />
									<attribute name="Position" value="0.131096 -0.22705 -0.009158" />
									<attribute name="Rotation" value="0.998264 0.0218539 0.0196249 -0.0510582" />
									<attribute name="Scale" value="1 1 1" />
									<attribute name="Variables" />
									<node id="20">
										<attribute name="Is Enabled" value="true" />
										<attribute name="Name" value="l_wrist" />
										<attribute name="Tags" />
										<attribute name="Position" value="0.167438 -0.226738 -0.015483" />
										<attribute name="Rotation" value="0.998184 0.0328593 0.0485305 -0.0139181" />
										<attribute name="Scale" value="1 1 1" />
										<attribute name="Variables" />
										<node id="21">
											<attribute name="Is Enabled" value="true" />
											<attribute name="Name" value="l_hand" />
											<attribute name="Tags" />
											<attribute name="Position" value="0.029413 -0.037956 -0.062907" />
											<attribute name="Rotation" value="1 -0.00034527 0 0" />
											<attribute name="Scale" value="1 1 1" />
											<attribute name="Variables" />
										</node>
									</node>
								</node>
							</node>
						</node>
					</node>
				</node>
				<node id="22">
					<attribute name="Is Enabled" value="true" />
					<attribute name="Name" value="r_hip" />
					<attribute name="Tags" />
					<attribute name="Position" value="-0.094009 0.00271 1e-05" />
					<attribute name="Rotation" value="0.999917 -0.0125657 0.00120387 0.00274575" />
					<attribute name="Scale" value="1 1 1" />
					<attribute name="Variables" />
					<node id="23">
						<attribute name="Is Enabled" value="true" />
						<attribute name="Name" value="r_knee" />
						<attribute name="Tags" />
						<attribute name="Position" value="-0.026486 -0.404262 0.056034" />
						<attribute name="Rotation" value="0.999748 0.0218696 -0.00155574 0.00483476" />
						<attribute name="Scale" value="1 1 1" />
						<attribute name="Variables" />
						<node id="24">
							<attribute name="Is Enabled" value="true" />
							<attribute name="Name" value="r_ankle" />
							<attribute name="Tags" />
							<attribute name="Position" value="-0.029707 -0.43241 -0.004766" />
							<attribute name="Rotation" value="0.994716 -0.0682225 0.0767137 -0.000671012" />
							<attribute name="Scale" value="1 1 1" />
							<attribute name="Variables" />
							<node id="25">
								<attribute name="Is Enabled" value="true" />
								<attribute name="Name" value="r_forefoot" />
								<attribute name="Tags" />
								<attribute name="Position" value="-0.039961 -0.036539 -0.114447" />
								<attribute name="Rotation" value="1 0 0 0" />
								<attribute name="Scale" value="1 1 1" />
								<attribute name="Variables" />
								<node id="26">
									<attribute name="Is Enabled" value="true" />
									<attribute name="Name" value="r_toe" />
									<attribute name="Tags" />
									<attribute name="Position" value="-0.002013 3.9e-05 -0.059707" />
									<attribute name="Rotation" value="1 0 0 0" />
									<attribute name="Scale" value="1 1 1" />
									<attribute name="Variables" />
								</node>
							</node>
						</node>
					</node>
				</node>
				<node id="27">
					<attribute name="Is Enabled" value="true" />
					<attribute name="Name" value="l_hip" />
					<attribute name="Tags" />
					<attribute name="Position" value="0.094852 -0.010535 -0.00648" />
					<attribute name="Rotation" value="0.998716 -0.0150379 -0.00910026 -0.0475184" />
					<attribute name="Scale" value="1 1 1" />
					<attribute name="Variables" />
					<node id="28">
						<attribute name="Is Enabled" value="true" />
						<attribute name="Name" value="l_knee" />
						<attribute name="Tags" />
						<attribute name="Position" value="0.058439 -0.390751 0.056339" />
						<attribute name="Rotation" value="0.99998 -0.00315468 -0.000490237 0.0055404" />
						<attribute name="Scale" value="1 1 1" />
						<attribute name="Variables" />
						<node id="29">
							<attribute name="Is Enabled" value="true" />
							<attribute name="Name" value="l_ankle" />
							<attribute name="Tags" />
							<attribute name="Position" value="0.042653 -0.429339 -0.013703" />
							<attribute name="Rotation" value="0.992421 -0.0870902 -0.0855505 -0.0140242" />
							<attribute name="Scale" value="1 1 1" />
							<attribute name="Variables" />
							<node id="30">
								<attribute name="Is Enabled" value="true" />
								<attribute name="Name" value="l_forefoot" />
								<attribute name="Tags" />
								<attribute name="Position" value="0.050877 -0.031824 -0.121819" />
								<attribute name="Rotation" value="1 0 0 0" />
								<attribute name="Scale" value="1 1 1" />
								<attribute name="Variables" />
								<node id="31">
									<attribute name="Is Enabled" value="true" />
									<attribute name="Name" value="l_toe" />
									<attribute name="Tags" />
									<attribute name="Position" value="-0.000362 0.001208 -0.06159" />
									<attribute name="Rotation" value="1 0 0 0" />
									<attribute name="Scale" value="1 1 1" />
									<attribute name="Variables" />
								</node>
							</node>
						</node>
					</node>
				</node>
			</node>
		</node>
		<node id="32">
			<attribute name="Is Enabled" value="true" />
			<attribute name="Name" value="model" />
			<attribute name="Tags" />
			<attribute name="Position" value="0 0 -0" />
			<attribute name="Rotation" value="1 0 0 0" />
			<attribute name="Scale" value="1 1 1" />
			<attribute name="Variables" />
			<component type="AnimatedModel" id="6">
				<attribute name="Model" value="Model;Models/model.mdl" />
				<attribute name="Material" value="Material;Materials/noname.xml" />
				<attribute name="Animation States">
					<variant type="Int" value="0" />
				</attribute>
			</component>
		</node>
```

So how i can get the joint information of those nodes? I tried
```
        Node *bufNode = scene_a_->GetChild("RootNode")->Clone();
        bufNode->GetDerivedComponents<StaticModel>(modelComponents, true);
        bufNode->GetComponent<StaticModel>()->GetModel()->GetSkeleton();
```
But the bones are empty and have no transformation information. My second approach was 
```
Vector<SharedPtr<Node> > bones = bufNode->GetChild("world_offset")->GetChildren(true);
        skinningMatrices.resize(bones.Size());
        skinningMatrices.push_back(bufNode->GetChild("world_offset")->GetWorldTransform());
        for(int i = 0; i < bones.Size(); i++){
            Matrix3x4 skinMat = bones[i]->GetWorldTransform();
            skinningMatrices.push_back(skinMat);
        }
```
Which leads to weird model morphing.

EDIT 2.0:
Was wrong i just had the world transformation of my parent node in each bone. So the following code was not working.
```
    Vector<Bone> sk = animatedModel->GetModel()->GetSkeleton().GetBones();
        for(int i = 0; i < sk.Size(); i++){
            if(sk[i].node_)
                Matrix3x4 skinMat = sk[i].node_->GetWorldTransform();
            Matrix3x4 skinMat = bufNode->GetWorldTransform();
            skinningMatrices.push_back(skinMat);
        }
```
The checking if the node exists makes the code runnable but the Skeleton from the `AnimatedModel` seems not to refer to the scene nodes.

-------------------------

