mrchrissross | 2018-11-03 15:27:19 UTC | #1

Hi Everyone, 
I'm having a little bit of a material issue, material looks great at first however after a slight movement of the camera, it becomes shiny with patterns on it. I don't know what going on with it, does it have something to do with the directional lighting?

It also seems to happen the further I move away for the models.

Here is the video:

http://imgur.com/a/KJsRGLe

Also with these rocks, I'm able to fly straight through them. I've set a collider up but it seems to be having no effect, here is the code to the rocks:

    const unsigned NUM_ROCKS = 100;
	for (unsigned i = 0; i < NUM_ROCKS; ++i)
	{
		float scale = Random(0.05f) + 0.001f; // Random(0.2f) + 0.01f;

		Node* objectNode = scene_->CreateChild("Rock");
		objectNode->SetPosition(Vector3(Random(90.0f) - 45.0f, Random(5.0f) + 5.0f, Random(90.0f) - 45.0f));
		objectNode->SetRotation(Quaternion(Random(360.0f), Random(360.0f), Random(360.0f)));
		objectNode->SetScale(scale);
		StaticModel* object = objectNode->CreateComponent<StaticModel>();
		object->SetModel(cache->GetResource<Model>("Models/Rock.mdl"));
		object->SetMaterial(cache->GetResource<Material>("Materials/Rock.xml"));
		object->SetCastShadows(true);

		RigidBody* body = objectNode->CreateComponent<RigidBody>();
		body->SetCollisionLayer(2);

		// Bigger Rocks will be heavier and harder to move     
		body->SetMass((scale * 100) * 2.0f);
		CollisionShape* shape = objectNode->CreateComponent<CollisionShape>();
		shape->SetBox(Vector3::ONE);
	}

-------------------------

Sinoid | 2018-11-04 00:36:38 UTC | #2

Can you toss your Rock.mdl file (specifically the Urho MDL file - not w/e source file it came from), material XML file, and the normal map (if any) on the rock (no other textures should be needed unless you have a specular map on the non-PBR shaders).

I'm suspecting that something is horribly wrong with your tangents or normals. 

Except that banding in the corner, which is really bizarre, are there triangles there that align with the banding?

-------------------------

Modanung | 2018-11-04 10:18:08 UTC | #3

@mrchrissross Are you still setting the linear velocity of the spaceship directly? This would explain the lack of collision. Instead apply forces.
Also, are you sure you're using collision layers/masks correctly? With the default values everything should collide.

-------------------------

mrchrissross | 2018-11-04 11:16:49 UTC | #4

I've fixed the collision. It seems I was using box shape instead of using the models mesh.

The Rock.mdl is:

    <material>
	<technique name="Techniques/DiffNormalSpec.xml"/>
	<texture name="Textures/Rock_Diffuse.jpg" unit="diffuse"/>
	<texture name="Textures/Rock_Normal.jpg" unit="normal"/>
	<parameter name="MatDiffColor" value="0.64 0.64 0.64 1"/>
	<cull value="none"/>
	<shadowcull value="none"/>
    </material>

-------------------------

Sinoid | 2018-11-04 20:47:11 UTC | #5

That's your material XML, everything looks fine there (*none* culling is odd, but won't cause this problem).

Need to see your Rock.mdl mesh to inspect the normals and tangents.

If you want to troubleshoot it yourself, this function will draw the normals, tangents, and binormals to inspect for discontinuity (**warning** it's super slow, only use when absolutely needed):

    void DrawGeometryNormals(DebugRenderer* renderer, StaticModel* drawable)
    {
        auto geomCt = drawable->GetNumGeometries();
        auto drawableTransform = drawable->GetNode()->GetWorldTransform();
        auto drawableRotation = drawable->GetNode()->GetWorldRotation();

        for (unsigned i = 0; i < geomCt; ++i)
        {
            if (auto geo = drawable->GetLodGeometry(i, 0))
            {
                const unsigned char* vertData;
                const unsigned char* indexData;
                unsigned vertSize;
                unsigned indexSize;
                const PODVector<VertexElement>* elements;
                geo->GetRawData(vertData, vertSize, indexData, indexSize, elements);

                const unsigned posOffset = VertexBuffer::GetElementOffset(*elements, TYPE_VECTOR3, SEM_POSITION);
                const unsigned normOffset = VertexBuffer::GetElementOffset(*elements, TYPE_VECTOR3, SEM_NORMAL, 0);
                const unsigned tangentOffset = VertexBuffer::GetElementOffset(*elements, TYPE_VECTOR4, SEM_TANGENT, 0);

                const auto vertStart = geo->GetVertexStart();
                const auto vertCt = geo->GetVertexCount();
                for (unsigned i = 0; i < vertCt; ++i)
                {
                    Vector3 vertPos = *(Vector3*)(vertData + (i+vertStart) * vertSize + posOffset);
                    Vector3 vertNor = *(Vector3*)(vertData + (i + vertStart) * vertSize + normOffset);
                    Vector4 vertTan = *(Vector4*)(vertData + (i + vertStart) * vertSize + tangentOffset);

                    auto worldPos = drawableTransform * vertPos;
                    auto worldNor = drawableRotation * vertNor;
                    auto worldTan = drawableRotation * Vector3(vertTan.x_, vertTan.y_, vertTan.z_);
                    auto binormal = worldNor.CrossProduct(worldTan);
                    binormal *= Sign(vertTan.w_);

                    renderer->AddLine(worldPos, worldPos + worldNor, Color::CYAN);
                    renderer->AddLine(worldPos, worldPos + binormal, Color::RED);
                    renderer->AddLine(worldPos, worldPos + worldTan, Color::MAGENTA);
                }
            }
        }
    }

If it crashes then your mesh is missing one of the required vertex elements for normal mapping to work.

-------------------------

mrchrissross | 2018-11-04 21:43:09 UTC | #6

Here is the Rock.mdl:

https://drive.google.com/file/d/1csJpAFWGVEXamBqud-25G1457XeSqAnJ/view?usp=sharing

And thank you, ill try that but wont be able to try it until Tuesday as for some reason the game wont build on my home PC :confused:

-------------------------

orefkov | 2018-11-04 21:29:42 UTC | #7

It looks like it sometimes happens if the model has no tangents. How you create model and import it? Do you import it with tangents?

-------------------------

mrchrissross | 2018-11-04 21:43:53 UTC | #8

The Rock.mdl is downloadable from the comment above.

-------------------------

orefkov | 2018-11-04 22:03:38 UTC | #9

You offer me to download your model and understand, is there any tangents in it, instead of checking it yourself?

-------------------------

Sinoid | 2018-11-05 01:35:44 UTC | #10

The problem is in your model. I'm surprised it renders at all actually (expected vertex layout errors).

It has normals but does not have tangents. Reconvert it and use the **-t** flag to generate tangents. That should fix it, apparently vert-layout errors were reduced / smoothed or something in master ... that **should've** spat an error at you for even trying to render it with that material.

    "Usage: AssetImporter <command> <input file> <output file> [options]\n"
    "See http://assimp.sourceforge.net/main_features_formats.html for input formats\n\n"
    "Commands:\n"
    "model       Output a model\n"
    "anim        Output animation(s)\n"
    "scene       Output a scene\n"
    "node        Output a node and its children (prefab)\n"
    "dump        Dump scene node structure. No output file is generated\n"
    "lod         Combine several Urho3D models as LOD levels of the output model\n"
    "            Syntax: lod <dist0> <mdl0> <dist1 <mdl1> ... <output file>\n"
    "\n"
    "Options:\n"
    "-b          Save scene in binary format, default format is XML\n"
    "-j          Save scene in JSON format, default format is XML\n"
    "-h          Generate hard instead of smooth normals if input has no normals\n"
    "-i          Use local ID's for scene nodes\n"
    "-l          Output a material list file for models\n"
    "-na         Do not output animations\n"
    "-nm         Do not output materials\n"
    "-nt         Do not output material textures\n"
    "-nc         Do not use material diffuse color value, instead output white\n"
    "-nh         Do not save full node hierarchy (scene mode only)\n"
    "-ns         Do not create subdirectories for resources\n"
    "-nz         Do not create a zone and a directional light (scene mode only)\n"
    "-nf         Do not fix infacing normals\n"
    "-ne         Do not save empty nodes (scene mode only)\n"
    "-mb <x>     Maximum number of bones per submesh. Default 64\n"
    "-p <path>   Set path for scene resources. Default is output file path\n"
    "-r <name>   Use the named scene node as root node\n"
    "-f <freq>   Animation tick frequency to use if unspecified. Default 4800\n"
    "-o          Optimize redundant submeshes. Loses scene hierarchy and animations\n"
    "-s <filter> Include non-skinning bones in the model's skeleton. Can be given a\n"
    "            case-insensitive semicolon separated filter list. Bone is included\n"
    "            if its name contains any of the filters. Prefix filter with minus\n"
    "            sign to use as an exclude. For example -s \"Bip01;-Dummy;-Helper\"\n"
    "-t          Generate tangents\n"
    "-v          Enable verbose Assimp library logging\n"
    "-eao        Interpret material emissive texture as ambient occlusion\n"
    "-cm         Check and do not overwrite if material exists\n"
    "-ct         Check and do not overwrite if texture exists\n"
    "-ctn        Check and do not overwrite if texture has newer timestamp\n"
    "-am         Export all meshes even if identical (scene mode only)\n"
    "-bp         Move bones to bind pose before saving model\n"
    "-split <start> <end> (animation model only)\n"
    "            Split animation, will only import from start frame to end frame\n"
    "-np         Do not suppress $fbx pivot nodes (FBX files only)\n"

-------------------------

mrchrissross | 2018-11-05 01:49:16 UTC | #11

I had converted it in blender using the add-on. Is there a way to do it within blender? As well thank you so much for you help its much appreciated :)

-------------------------

Sinoid | 2018-11-05 01:50:37 UTC | #12

I don't know the answer to that, I don't use blender.

-------------------------

orefkov | 2018-11-05 05:36:15 UTC | #13

In blender addon set check on "Tangent" option.
![image|218x141](upload://asqKRcB666xMGT4ZdelhsfgBItH.png)

-------------------------

