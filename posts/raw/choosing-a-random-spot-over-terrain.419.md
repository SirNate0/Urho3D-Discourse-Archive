vivienneanthony | 2017-01-02 01:00:16 UTC | #1

Hello,

I'm trying to write code that finds a random spot on terrain(especially procedual). It works but not fully. I just want to know if I'm doing it accurately. I don't think its accurately picking up the Terrain Y(y-up / normal location). So, it's not always accurate when placing the Pod.

Future updates would test for collision and probably place objects from vegetation to building structures. Hopefully through weightmaps or rule system.

Vivienne

 
[code]    ///testing
    Vector3 characterPosition = characternode_ -> GetPosition();

    bool levelarea=false;

    int randomSpotx;
    int randomSpotz;

    for(int i=0; i<1000; i++)
    {
        randomSpotx=rand()%256;
        randomSpotz=rand()%256;

        randomSpotx-=128;
        randomSpotz-=128;

        /// Select a position
        Vector3 selectPosition=Vector3(characterPosition.x_+randomSpotx,terrain->GetHeight(Vector3(characterPosition.x_,characterPosition.y_)),characterPosition.z_+randomSpotz);

        float average_y=(
                            terrain->GetHeight(Vector3(selectPosition.x_+(podSize.x_/2),selectPosition.z_+(podSize.z_/2)))+
                            terrain->GetHeight(Vector3(selectPosition.x_+(podSize.x_/2),selectPosition.z_-(podSize.z_/2)))+
                            terrain->GetHeight(Vector3(selectPosition.x_-(podSize.x_/2),selectPosition.z_+(podSize.z_/2)))+
                            terrain->GetHeight(Vector3(selectPosition.x_-(podSize.x_/2),selectPosition.z_-(podSize.z_/2))))/4;

        if((fabs(selectPosition.y_/average_y)<0.995f)||(fabs(selectPosition.y_/average_y)>1.005f))
        {

            //
        }
        else
        {
            levelarea=true;

            randomSpotx=characterPosition.x_+randomSpotx;

            randomSpotz=characterPosition.z_+randomSpotz;            
            
            break;
        }
    }

    /// After the For loop either a spot was found our not
    if(levelarea)
    {
        /// Change position of the box  by using the Bounding Box and terrain information
        position2.y_ = terrain->GetHeight(Vector3(randomSpotx,randomSpotz));

        BoundingBox  podmodelbox = PodObject1 ->GetBoundingBox();
        Vector3 podSize=podmodelbox.Size();

        PodNode1->SetPosition(Vector3(randomSpotx,position2.y_+(podSize.y_/2)+.3,randomSpotz));
        
        Print ("Spot Found");
    }else
    {
        Print("No Spot Found");
    }

[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:16 UTC | #2

I tried moving the RigidBody, StaticModel, and the Node. They all didn't work.

-------------------------

friesencr | 2017-01-02 01:00:16 UTC | #3

Are you saying setting the position doesn't move the PodNode1?

-------------------------

vivienneanthony | 2017-01-02 01:00:16 UTC | #4

[quote="friesencr"]Are you saying setting the position doesn't move the PodNode1?[/quote]


It does. The problem is placement 1 out of 4 times it fails.
[code]

        float average_y=(
                            terrain->GetHeight(Vector3(selectPosition.x_+(podSize.x_/2),selectPosition.z_+(podSize.z_/2)))+
                            terrain->GetHeight(Vector3(selectPosition.x_+(podSize.x_/2),selectPosition.z_-(podSize.z_/2)))+
                            terrain->GetHeight(Vector3(selectPosition.x_-(podSize.x_/2),selectPosition.z_+(podSize.z_/2)))+
                            terrain->GetHeight(Vector3(selectPosition.x_-(podSize.x_/2),selectPosition.z_-(podSize.z_/2))))/4;

        if((fabs(selectPosition.y_/average_y)<0.995f)||(fabs(selectPosition.y_/average_y)>1.005f))
     randomSpotx=characterPosition.x_+randomSpotx;

            randomSpotz=characterPosition.z_+randomSpotz;           
           
            break;
        }
    }


    /// After the For loop either a spot was found our not
    if(levelarea)
    {
        /// Change position of the box  by using the Bounding Box and terrain information
        position2.y_ = terrain->GetHeight(Vector3(randomSpotx,randomSpotz));

        BoundingBox  podmodelbox = PodObject1 ->GetBoundingBox();
        Vector3 podSize=podmodelbox.Size();

        PodNode1->SetPosition(Vector3(randomSpotx,position2.y_+(podSize.y_/2)+.3,randomSpotz));

[/code]

If I average out the height of 4 points then test a center point.   The difference I set is no less or no more then .005 float up or down.  Meaning I test for a leveled spot at least the size of the object to be placed.

The problem I have is when it's placed. Sometimes it's below the terrain although. I think I'm calculating right.

[code]
   randomSpotx=characterPosition.x_+randomSpotx;

            randomSpotz=characterPosition.z_+randomSpotz;           
           
            break;
        }
    }

    /// After the For loop either a spot was found our not
    if(levelarea)
    {
        /// Change position of the box  by using the Bounding Box and terrain information
        position2.y_ = terrain->GetHeight(Vector3(randomSpotx,randomSpotz));

        BoundingBox  podmodelbox = PodObject1 ->GetBoundingBox();
        Vector3 podSize=podmodelbox.Size();

        PodNode1->SetPosition(Vector3(randomSpotx,position2.y_+(podSize.y_/2)+.3,randomSpotz));[/code]


This is the initial code creating the Node and Terrain.
[code]/// Generate Terrain
    Node* terrainNode = scene_->CreateChild("Terrain");

    Terrain* terrain = terrainNode->CreateComponent<Terrain>();
    terrain->SetPatchSize(64);
    terrain->SetSpacing(Vector3(2.0f, 0.8f, 2.0f)); // Spacing between vertices and vertical resolution of the height map
    terrain->SetSmoothing(true);
    terrain->SetCastShadows(true);

    /// generatescene
    terrain->GenerateProceduralHeightMap(planetrule);

    terrain->SetMaterial(cache->GetResource<Material>("Materials/TerrainTriPlanar.xml"));

    RigidBody* terrainbody = terrainNode->CreateComponent<RigidBody>();

    CollisionShape* terrainshape = terrainNode->CreateComponent<CollisionShape>();

    terrainbody->SetCollisionLayer(1);
    terrainshape->SetTerrain();


    Vector3 position(0.0f,0.0f);
    position.y_ = terrain->GetHeight(position) + 1.0f;

    /// Position character
    Node * characternode_ = scene_->CreateChild("Character");
    characternode_->SetPosition(Vector3(0.0f, position.y_ , 0.0f));

    /// Create chacter
    //CreateCharacter();

    /// Add a object to the seen - Pod Node
    Node * PodNode1 = scene_ -> CreateChild("podNode");

    StaticModel* PodObject1 = PodNode1 ->CreateComponent<StaticModel>();

    PodObject1->SetModel(cache->GetResource<Model>("Resources/Models/pod.mdl"));
    PodObject1->ApplyMaterialList("Resources/Models/pod.txt");
    PodObject1->SetCastShadows(true);

    RigidBody* PodBody= PodNode1->CreateComponent<RigidBody>();
    CollisionShape* Podshape = PodNode1->CreateComponent<CollisionShape>();

    Podshape->SetTriangleMesh (cache->GetResource<Model>("Resources/Models/pod.mdl"));
    PodBody->SetCollisionLayer(1);
    Podshape ->SetLodLevel(1);

    /// Change position of the box  by using the Bounding Box and terrain information
    Vector3 position2(4.0f,4.0f);
    position2.y_ = terrain->GetHeight(position2);

    BoundingBox  podmodelbox = PodObject1 ->GetBoundingBox();
    Vector3 podSize=podmodelbox.Size();

    PodNode1->SetPosition(Vector3(4.0f, position2.y_+(podSize.y_/2)+.3,4.0f));[/code]
Vivienne

-------------------------

friesencr | 2017-01-02 01:00:17 UTC | #5

The vehicle demo spawns mushrooms randomly on the terrain i think.  It might be worth a look.

-------------------------

vivienneanthony | 2017-01-02 01:00:17 UTC | #6

[[quote="friesencr"]The vehicle demo spawns mushrooms randomly on the terrain i think.  It might be worth a look.[/quote]

I modified the code. It somewhat works better. I'm using the bounding box to determine the size of a object which isn't fully accurate BUT the pod object work and a building object work. The building object because of the size I think is setting a wrong size to the bounding box which isn't matching.

[code]

/// Generate Terrain
    Node* terrainNode = scene_->CreateChild("Terrain");

    Terrain* terrain = terrainNode->CreateComponent<Terrain>();
    terrain->SetPatchSize(64);
    terrain->SetSpacing(Vector3(2.0f, 0.8f, 2.0f)); // Spacing between vertices and vertical resolution of the height map
    terrain->SetSmoothing(true);
    terrain->SetCastShadows(true);

    /// generatescene
    terrain->GenerateProceduralHeightMap(planetrule);

    terrain->SetMaterial(cache->GetResource<Material>("Materials/TerrainTriPlanar.xml"));

    RigidBody* terrainbody = terrainNode->CreateComponent<RigidBody>();

    CollisionShape* terrainshape = terrainNode->CreateComponent<CollisionShape>();

    terrainbody->SetCollisionLayer(1);
    terrainshape->SetTerrain();

    Vector3 position(0.0f,0.0f);
    position.y_ = terrain->GetHeight(position) + 1.0f;

    /// Position character
    Node * characternode_ = scene_->CreateChild("Character");
    characternode_->SetPosition(Vector3(0.0f, position.y_ , 0.0f));

    /// Add a object to the seen - object Node
    Node * objectNode = scene_ -> CreateChild("objectNode");

    StaticModel* objectStaticModel = objectNode ->CreateComponent<StaticModel>();

    objectStaticModel->SetModel(cache->GetResource<Model>("Resources/Models/SciFiBuildingA.mdl"));
    objectStaticModel->ApplyMaterialList("Resources/Models/SciFiBuildingA.txt");
    objectStaticModel->SetCastShadows(true);

    RigidBody* objectBody= objectNode->CreateComponent<RigidBody>();
    CollisionShape* objectshape = objectNode->CreateComponent<CollisionShape>();

    objectshape->SetTriangleMesh (cache->GetResource<Model>("Resources/Models/SciFiBuildingA.mdl"));
    objectBody->SetCollisionLayer(1);
    objectshape ->SetLodLevel(1);

    /// Change position of the box  by using the Bounding Box and terrain information
    BoundingBox  objectBoundingBox = objectStaticModel ->GetBoundingBox();
    Vector3 objectSize=objectBoundingBox.Size();

    /// Get the materials
    Material * skyboxMaterial = skybox->GetMaterial();

    /// Get the current character position
    Vector3 characterPosition = characternode_ -> GetPosition();

    /// Set timer and required level area flag
    srand(512);
    bool levelarea=false;

    /// Define random point variables
    int randomSpotx;
    int randomSpotz;

    /// Loop 1,000 times to find a suitable location
    for(int i=0; i<2000; i++)
    {
        randomSpotx=rand()%512;
        randomSpotz=rand()%512;

        randomSpotx-=256;
        randomSpotz-=256;

       /// Select a possible position to place a object
        Vector3 selectPosition=Vector3(characterPosition.x_+randomSpotx,terrain->GetHeight(Vector3(characterPosition.x_,characterPosition.y_)),characterPosition.z_+randomSpotz);

        float average_y=(
                            terrain->GetHeight(Vector3(selectPosition.x_+(objectSize.x_/2),0.0f,selectPosition.z_+(objectSize.z_/2)))+
                            terrain->GetHeight(Vector3(selectPosition.x_+(objectSize.x_/2),0.0f,selectPosition.z_-(objectSize.z_/2)))+
                            terrain->GetHeight(Vector3(selectPosition.x_-(objectSize.x_/2),0.0f,selectPosition.z_+(objectSize.z_/2)))+
                            terrain->GetHeight(Vector3(selectPosition.x_-(objectSize.x_/2),0.0f,selectPosition.z_-(objectSize.z_/2))))/4;

        /// Check the points averaged height is in acceptable values of -.01 to .01
        if((fabs(selectPosition.y_/average_y)<0.99)||(fabs(selectPosition.y_/average_y)>1.01f))
        {

            /// Skip and continue the loop
        }
        else
        {
            /// Change flag to area found
            levelarea=true;

            /// Set the new x,z locations
            randomSpotx=characterPosition.x_+randomSpotx;
            randomSpotz=characterPosition.z_+randomSpotz;

            break;
        }
    }

    /// Check if a leveled area was found
    if(levelarea)
    {
        /// Change position of the box  by using the Bounding Box and terrain information
        Vector3 position2= Vector3(0.0f,0.0f,0.0f);

        position.y_= terrain->GetHeight(Vector3(randomSpotx,0.0f,randomSpotz));

        BoundingBox  objectBoundingBox = objectStaticModel ->GetBoundingBox();
        Vector3 objectSize=objectBoundingBox.Size();

        objectNode->SetPosition(Vector3(randomSpotx,position2.y_+(objectSize.y_/2),randomSpotz));
    }
    else
    {
        /// Output spot not found
        Print("No Spot Found");
    }[/code]

-------------------------

