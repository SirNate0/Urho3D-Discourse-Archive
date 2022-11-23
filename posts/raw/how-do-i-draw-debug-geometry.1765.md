TheComet | 2017-01-02 01:09:57 UTC | #1

I'm trying to draw CollisionShapes because things aren't doing what they're supposed to in my physics but I can't figure out how to do that. 

I thought it would have been as simple as:
[code]PhysicsWorld* world = scene_->GetComponent<PhysicsWorld>();
world->DrawDebugGeometry(scene_->CreateComponent<DebugRenderer>());[/code]

I also tried that in conjunction with:
[code]viewport->SetDrawDebug(true);[/code]

I'm not getting anywhere because there's no mention of it in the documentation. At least not in a way I can understand.

-------------------------

Dave82 | 2017-01-02 01:09:57 UTC | #2

[quote="TheComet"]I'm trying to draw CollisionShapes because things aren't doing what they're supposed to in my physics but I can't figure out how to do that. 

I thought it would have been as simple as:
[code]PhysicsWorld* world = scene_->GetComponent<PhysicsWorld>();
world->DrawDebugGeometry(scene_->CreateComponent<DebugRenderer>());[/code]

I also tried that in conjunction with:
[code]viewport->SetDrawDebug(true);[/code]

I'm not getting anywhere because there's no mention of it in the documentation. At least not in a way I can understand.[/quote]


The easiest way is you create a debug renderer and draw necessary data in E_POSTRENDERUPDATE. This will ensure your debug data will be drawed on top of other graphical elements in the scene.


Just subscribe to this event and draw your debug data there :

[code]void MyApp::Start()
{
   scene->CreateComponent<DebugRenderer>();
   SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(MyApp, drawDebug));
}

void MyApp::drawDebug(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
{
     DebugRenderer * dbgRenderer = scene->GetComponent<DebugRenderer>();
     if (dbgRenderer)
     {
            // Draw navmesh data
           DynamicNavigationMesh * navMesh = scene->GetComponent<DynamicNavigationMesh>();
           navMesh->DrawDebugGeometry(dbgRenderer,false);
           
           // Draw Physics data :
           PhysicsWorld * phyWorld = scene->GetComponent<PhysicsWorld>();
           phyWorld->DrawDebugGeometry(dbgRenderer,false); 

          // etc
      } 
}[/code]

It is recommended to nullcheck your components (PhysicsWorld , DynamicMesh etc) before you draw them

-------------------------

TheComet | 2017-01-02 01:09:58 UTC | #3

Thanks a lot, that worked!

-------------------------

cirosantilli | 2017-10-15 07:47:16 UTC | #4

Now also shown on the Physics sample: https://github.com/urho3d/Urho3D/blob/9b22e16324276ad58eafff645d3f5721059a29f6/Source/Samples/11_Physics/Physics.cpp#L315

-------------------------

