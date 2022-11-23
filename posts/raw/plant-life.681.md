vivienneanthony | 2017-01-02 01:02:05 UTC | #1

I'm trying to reproduce plant life at least grass. I'm getting this from the following code. The grass ends up in the air although the center point is exactly on the bottom of the mesh.

[i.imgur.com/JgHclY5.png](http://i.imgur.com/JgHclY5.png)

[code] /// Define random point variables
    int randomSpotx;
    int randomSpotz;

    /// Loop 1,000 times to find a suitable location
    for(int i=0; i<40000; i++)
    {
        randomSpotx=rand()%512;
        randomSpotz=rand()%512;

        randomSpotx-=256;
        randomSpotz-=256;

        /// Select a possible position to place a plant
        Vector3 selectPosition=Vector3(randomSpotx,terrain->GetHeight(Vector3(randomSpotx,randomSpotz)),randomSpotz);

        /// Add a plant to the seen - plant Node
        Node * plantNode = scene_ -> CreateChild("plantNode");
        StaticModel* plantStaticModel = plantNode ->CreateComponent<StaticModel>();

        plantStaticModel->SetModel(cache->GetResource<Model>("Resources/Models/Grass01.mdl"));
        plantStaticModel->ApplyMaterialList("Resources/Models/Grass01.txt");
        plantStaticModel->SetCastShadows(true);

        //RigidBody* plantBody= plantNode->CreateComponent<RigidBody>();
        //CollisionShape* plantshape = plantNode->CreateComponent<CollisionShape>();

        //plantshape->SetBox(Vector3::ONE);
        //plantshape ->SetLodLevel(1);

      //  plantBody->SetCollisionLayer(1);

        /// Set plant position
        plantNode->SetPosition(selectPosition);
    }[/code]

-------------------------

vivienneanthony | 2017-01-02 01:02:05 UTC | #2

There has to be a more efficient way of doing this to create grass. I made a lower poly version of the grass. Also I'm thinking anything in the distance can be a billboard grass.

[img]http://i.imgur.com/peUwStp.png[/img]


[code]  /// Create life -  Move this to a funcion

    /// Define random point variables
    int Spotx;
    int Spotz;

    float randomSpotx;
    float randomSpotz;

    ///Loop 1,000 times to find a suitable location
    for(int i=0; i<80000; i++)
    {
        Spotx=rand()%12800;
        Spotz=rand()%12800;

        randomSpotx=((float)Spotx/100)-64.0f;
        randomSpotz=((float)Spotz/100)-64.0f;

        /// Select a possible position to place a plant
        Vector3 selectPosition=Vector3(randomSpotx,terrain->GetHeight(Vector3(randomSpotx,0.0f,randomSpotz)),randomSpotz);

        /// Add a plant to the seen - plant Node
        Node * plantNode = scene_ -> CreateChild("plantNode");
        StaticModel* plantStaticModel = plantNode ->CreateComponent<StaticModel>();

        plantStaticModel->SetModel(cache->GetResource<Model>("Resources/Models/Grass01.mdl"));
        plantStaticModel->ApplyMaterialList("Resources/Models/Grass01.txt");
        plantStaticModel->SetCastShadows(true);

        //RigidBody* plantBody= plantNode->CreateComponent<RigidBody>();
        //CollisionShape* plantshape = plantNode->CreateComponent<CollisionShape>();

        //plantshape->SetBox(Vector3::ONE);
        //plantshape ->SetLodLevel(1);

      //  plantBody->SetCollisionLayer(1);

        /// Set plant position
        plantNode->SetPosition(selectPosition);
    }
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:02:05 UTC | #3

How does instancing work? I tried changing the code  to use instances to cut down on geometry but it seems to be stuck in a loop.

Changing the node name fix the problem!

[code]// Add a plant to the seen - plant Node
    Node * plantNode = scene_ -> CreateChild("plantNode");

    StaticModelGroup * plantStaticModelGroup = plantNode->CreateComponent<StaticModelGroup>();

    plantStaticModelGroup->SetModel(cache->GetResource<Model>("Resources/Models/Grass01highres.mdl"));
    plantStaticModelGroup->ApplyMaterialList("Resources/Models/Grass01highres.txt");
    plantStaticModelGroup->SetCastShadows(true);

    /// Define random point variables
    int Spotx;
    int Spotz;

    float randomSpotx;
    float randomSpotz;

    ///Loop 1,000 times to find a suitable location
    for(int i=0; i<1000; i++)
    {
        Spotx=rand()%6400;
        Spotz=rand()%6400;

        randomSpotx=((float)Spotx/100)-32.0f;
        randomSpotz=((float)Spotz/100)-32.0f;

        /// Select a possible position to place a plant
        Vector3 selectPosition=Vector3(randomSpotx,terrain->GetHeight(Vector3(randomSpotx,0.0f,randomSpotz)),randomSpotz);

        /// Add a plant to the seen - plant Node
        Node * plantNodeInstance = plantNode -> CreateChild("plantNode");

        /// Set plant position
        plantNodeInstance->SetPosition(selectPosition);

        plantStaticModelGroup->AddInstanceNode(plantNodeInstance);
    }
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:02:05 UTC | #4

Still  high for only 100,000 plants but I think they are super clumped.  4 minutes to start.

[i.imgur.com/nZlT3km.png](http://i.imgur.com/nZlT3km.png)

[img]http://i.imgur.com/nZlT3km.png[/img]

-------------------------

weitjong | 2017-01-02 01:02:06 UTC | #5

I think you should seriously consider to use Billboard instead.

-------------------------

vivienneanthony | 2017-01-02 01:02:06 UTC | #6

[quote="weitjong"]I think you should seriously consider to use Billboard instead.[/quote]

I was thinking using billboards for objects a certain distance away from the camera and up close lowres and midres static model.

Now implementing it I'm not sure. I can't tell Urho3D to say 10m (10.0f) away from the camera use billboards. Then (5m)5.0f to 10m(10.0f) use lowres. Then closer use fullres grass.

-------------------------

weitjong | 2017-01-02 01:02:06 UTC | #7

I don't think what you plan to do is currently supported by Urho out of the box. What you describing is similar to asking a component to somehow dynamically change its type from StaticModel to Billboard based on the camera distance in the runtime. Although I believe if you really insist on doing so, it should be doable but at what cost. I don't think your players would pay attention on the grass anyway. I have played a number of AAA games in the past and I see them get away with it just by using billboard.

-------------------------

vivienneanthony | 2017-01-02 01:02:06 UTC | #8

[quote="weitjong"]I don't think what you plan to do is currently supported by Urho out of the box. What you describing is similar to asking a component to somehow dynamically change its type from StaticModel to Billboard based on the camera distance in the runtime. Although I believe if you really insist on doing so, it should be doable but at what cost. I don't think your players would pay attention on the grass anyway. I have played a number of AAA games in the past and I see them get away with it just by using billboard.[/quote]

Okay. Larger objects which I think are more noticeable might have to be mesh like rocks or trees(Not sure how I'll do the leaves per say in billboards).

-------------------------

friesencr | 2017-01-02 01:02:06 UTC | #9

I don't know exactly what you are doing but each of those objects still needs to be tested for occlusion and sorted/batched.  You can use a static model group which reduces this.  I did this in on my little dungeon games.  I did static model groups in patches.  You can play around with your settings to trade off batches for over drawn vertices.  Start of with 50x50 meters or something.  I found that very simple geometry was not very sensitive to vertex count.  So sending those extra vertices will waste vertex shader resources then should get clipped before fragment shading.  It took me a while rewrite my code for this kind of batching.  Be sure to set draw distance too.  For static model groups the master node is in charge of being occluded.  So if it gets hidden the whole patch does.

-------------------------

weitjong | 2017-01-02 01:02:06 UTC | #10

For larger objects that user may pay attention to their details, you can control their level of detail (LOD) based on view distance. The good news is, StaticModel supports it. I think the mushroom model and sample app 04_StaticScene has demonstrated this feature.

-------------------------

vivienneanthony | 2017-01-02 01:02:06 UTC | #11

[quote="friesencr"]I don't know exactly what you are doing but each of those objects still needs to be tested for occlusion and sorted/batched.  You can use a static model group which reduces this.  I did this in on my little dungeon games.  I did static model groups in patches.  You can play around with your settings to trade off batches for over drawn vertices.  Start of with 50x50 meters or something.  I found that very simple geometry was not very sensitive to vertex count.  So sending those extra vertices will waste vertex shader resources then should get clipped before fragment shading.  It took me a while rewrite my code for this kind of batching.  Be sure to set draw distance too.  For static model groups the master node is in charge of being occluded.  So if it gets hidden the whole patch does.[/quote]

I think I understand what you mean conceptually. How I would implement it would be another thing.

I'm going experiment with billboards then go to that option.

-------------------------

vivienneanthony | 2017-01-02 01:02:06 UTC | #12

[quote="weitjong"]I don't think what you plan to do is currently supported by Urho out of the box. What you describing is similar to asking a component to somehow dynamically change its type from StaticModel to Billboard based on the camera distance in the runtime. Although I believe if you really insist on doing so, it should be doable but at what cost. I don't think your players would pay attention on the grass anyway. I have played a number of AAA games in the past and I see them get away with it just by using billboard.[/quote]

I changed the method to billboard from the example code. I'm getting some weird transparency issues.

[img]http://i.imgur.com/kyW69Hm.png[/img]

[code]/// Define random point variables
    int Spotx;
    int Spotz;
 
    float randomSpotx;
    float randomSpotz;
 
 
 
// Create billboard sets (floating grass)
    const unsigned NUM_BILLBOARDNODES = 10;
    const unsigned NUM_BILLBOARDS = 100;
    for (unsigned int i = 0; i < NUM_BILLBOARDNODES; ++i)
    {
        Node* grassNode = scene_->CreateChild("Grass");
        grassNode->SetPosition(Vector3(0.0f,0.0f,0.0f));
        BillboardSet* billboardObject = grassNode->CreateComponent<BillboardSet>();
        billboardObject->SetNumBillboards(NUM_BILLBOARDS);
        billboardObject->SetMaterial(cache->GetResource<Material>("Resources/Materials/Grass.xml"));
        billboardObject->SetSorted(true);
 
        for (unsigned int j = 0; j < NUM_BILLBOARDS; ++j)
        {
 
            Spotx=rand()%1000;
            Spotz=rand()%1000;
 
            randomSpotx=((float)Spotx/100)-5.0f;
            randomSpotz=((float)Spotz/100)-5.0f;
 
            Billboard* bb = billboardObject->GetBillboard(j);
 
            /// Select a possible position to place a plant
            Vector3 selectPosition=Vector3(randomSpotx,terrain->GetHeight(Vector3(randomSpotx,0.0f,randomSpotz)),randomSpotz);
 
            bb->position_ =selectPosition;
            bb->size_ = Vector2(Random(0.2f) + 0.1f, Random(0.2f) + 0.1f);
            bb->enabled_ = true;
        }
 
        billboardObject->Commit();
    }
 
 [/code]

The xml is this 

[code]<material>
    <technique name="Techniques/DiffUnlitAlpha.xml" />
    <parameter name="MatDiffColor" value="0.5 0.5 0.5 0.5" />    
    <texture unit="diffuse" name="Textures/grasscard.png" />
</material>[/code]

-------------------------

vivienneanthony | 2017-01-02 01:02:06 UTC | #13

[img]http://i.imgur.com/HImRo3B.png[/img]

-------------------------

Mike | 2017-01-02 01:02:07 UTC | #14

Try DiffUnlitAlphaMask instead of DiffUnlitAlpha.
You can also try other cutouts, for example those of the "Yo Frankie!" project give good results [url]https://svn.blender.org/svnroot/yofrankie/trunk/textures/[/url]

-------------------------

Mike | 2017-01-02 01:02:07 UTC | #15

Also set alpha transparency to 1:
[code]<parameter name="MatDiffColor" value="0.5 0.5 0.5 1" />[/code]
and give some specularity.

-------------------------

vivienneanthony | 2017-01-02 01:02:07 UTC | #16

[quote="Mike"]Try DiffUnlitAlphaMask instead of DiffUnlitAlpha.
You can also try other cutouts, for example those of the "Yo Frankie!" project give good results [url]https://svn.blender.org/svnroot/yofrankie/trunk/textures/[/url][/quote]

I'll try that tomorrow. I added a .dds plugin to Gimp which I was able to get better results. Still the color is off and material weird.

[img]http://i.imgur.com/0sXSpvS.png[/img]

-------------------------

