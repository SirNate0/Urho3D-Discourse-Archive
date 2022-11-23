dev4fun | 2018-04-14 20:38:55 UTC | #1

Hey guys, I have this code on my game:

	CScreen::Init();

	//Setar a Scene na conexão com a Game Server
	if( SOCKETG )
	   SOCKETG->SetScene( pScene );

	//Criar a Cena
	CreateScene();

On CreateScene() function, if I make the code manually (I mean for coding), like this:

    pScene->CreateComponent<Octree>( LOCAL );
    pScene->CreateComponent<PhysicsWorld>( LOCAL );
    pScene->CreateComponent<DebugRenderer>( LOCAL );

    Node* zoneNode = pScene->CreateChild( "Zone", LOCAL );
    auto* zone = zoneNode->CreateComponent<Zone>();
    zone->SetBoundingBox( BoundingBox( -1000.0f, 1000.0f ) );
    zone->SetAmbientColor( Color( 0.1f, 0.1f, 0.1f ) );
    zone->SetFogStart( 100.0f );
    zone->SetFogEnd( 300.0f );

    // Create a directional light without shadows
    Node* lightNode = pScene->CreateChild( "DirectionalLight", LOCAL );
    lightNode->SetDirection( Vector3( 0.5f, -1.0f, 0.5f ) );

    auto* light = lightNode->CreateComponent<Light>();
    light->SetLightType( LIGHT_DIRECTIONAL );
    light->SetColor( Color( 1, 1, 1 ) );
    light->SetCastShadows( true );
    light->SetSpecularIntensity( 1.0f );

    Node* floorNode = pScene->CreateChild( "FloorTile", LOCAL );
    floorNode->SetPosition( Vector3( 0, 0, 0 ) );
    floorNode->SetScale( Vector3( 100.0f, 1.0f, 100.0f ) );

    auto* floorObject = floorNode->CreateComponent<StaticModel>();
    floorObject->SetCastShadows( true );
    floorObject->SetModel( RESOURCECACHE->GetResource<Model>( "Models/Box.mdl" ) );
    floorObject->SetMaterial( RESOURCECACHE->GetResource<Material>( "Materials/Test/dae.xml" ) );

    auto* body = floorNode->CreateComponent<RigidBody>();
    body->SetFriction( 1.0f );

    auto* shape = floorNode->CreateComponent<CollisionShape>();
    shape->SetBox( Vector3::ONE );

All works good, but if I create this way, loading from XML, don't.

	XMLFile * pXMLFile = RESOURCECACHE->GetResource<XMLFile>( "Scenes/World.xml" );
	
	if( pXMLFile )
		pScene->LoadXML( pXMLFile->GetRoot() );


Window stay black, nothing is rendered and I got this:

	No Octree component in scene, drawable will not render

Ok, now if I create components manually (Octree,Render,PhysicsWorld), nothing from XML its on Scene... I believe that is something on SetScene(), but dno what. 

@Scene XML File
https://puu.sh/A3atk/d280efe4e9.txt

Anybody knows what can be?
Thanks.

-------------------------

Sinoid | 2018-04-14 23:15:32 UTC | #2

You're going to have to step through it all in the debugger, there's no getting around it.

-------------------------

Lumak | 2018-04-15 20:59:02 UTC | #3

These must also be local:
[code]
<component type="Octree" id="1"/>
<component type="DebugRenderer" id="2"/>
<component type="PhysicsWorld" id="11"/>
[/code]

-------------------------

dev4fun | 2018-04-15 06:16:08 UTC | #4

Hmm ye I understand it. But if I simply load XML, and after this use  GetOrCreateComponent for Octree,DebugRender and PhysicsWorld something is shown on window, but nothing from XML (don't see nodes etc).

I was debugging already, but I dont understand why this happens yet... Ic that its something on SetScene and only when load from XML. Just checking if someone else already got this same problem.

Thanks for anwsers.

-------------------------

johnnycable | 2018-04-15 20:58:54 UTC | #5

Use this trick: 
Add this code to your HandleUpdate (snippet from 18_characterdemo example)

    // Check for loading / saving the scene
    if (input->GetKeyPress(KEY_F5))
    {
        File saveFile(context_, GetSubsystem<FileSystem>()->GetProgramDir() + "GameData/Scenes/SceneDump.xml", FILE_WRITE);
        scene_->SaveXML(saveFile);
    }

    if (input->GetKeyPress(KEY_F7))
    {
        File loadFile(context_, GetSubsystem<FileSystem>()->GetProgramDir() + "GameData/Scenes/SceneDump.xml", FILE_READ);
        scene_->LoadXML(loadFile);
        // // After loading we have to reacquire the weak pointer to the Character component, as it has been recreated
        // // Simply find the character's scene node by name as there's only one of them
        modelNode = scene_->GetChild("Model", true);
    }

load everything using code, the save a scene dump with F5. Check the result with your original scene in xml. So you can spot differences.
Moreover, consider the line:

`modelNode = scene_->GetChild("Model", true);`

Everytime you load a scene dump in xml, you have to "restore" some object to their original state... 
Looks like xml is more conceived like a scene dump, than a scene setup. This makes things difficult, for instance, gettting an animation to play since the correct starting point...
HTH

-------------------------

Modanung | 2018-04-15 14:10:36 UTC | #6

[quote="johnnycable, post:5, topic:4173"]
Check the result with your original scene in xml. So you can spot differences.
[/quote]

One way to do this in Linux is by running `diff OldScene.xml NewScene.xml` in a terminal.

-------------------------

lexx | 2018-04-15 14:59:57 UTC | #7

And if git is installed,  
`  git diff    file1.xml  file2.xml`
shows differences.

-------------------------

