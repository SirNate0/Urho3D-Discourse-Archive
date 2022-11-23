slapin | 2017-06-09 14:29:08 UTC | #1

Hi, all!
Recently I got random crash with Bullet. The debug shows it happens after removing of RigidBodies + Constraints
(after ragdoll recovery)

    #0  0x00005555563f63aa in btCompoundCollisionAlgorithm::preallocateChildAlgorithms(btCollisionObjectWrapper const*, btCollisionObjectWrapper const*) ()
    #1  0x00005555563f6a25 in btCompoundCollisionAlgorithm::processCollision(btCollisionObjectWrapper const*, btCollisionObjectWrapper const*, btDispatcherInfo const&, btManifoldResult*) ()
    #2  0x0000555555d903e4 in btCollisionDispatcher::defaultNearCallback(btBroadphasePair&, btCollisionDispatcher&, btDispatcherInfo const&) ()
    #3  0x0000555555d90698 in btCollisionPairCallback::processOverlap(btBroadphasePair&) ()
    #4  0x0000555556400cc2 in btHashedOverlappingPairCache::processAllOverlappingPairs(btOverlapCallback*, btDispatcher*) ()
    #5  0x0000555555d8fa7c in btCollisionDispatcher::dispatchAllCollisionPairs(btOverlappingPairCache*, btDispatcherInfo const&, btDispatcher*) ()
    #6  0x0000555555d4416c in btDiscreteDynamicsWorld::internalSingleStepSimulation(float) ()
    #7  0x0000555555d3e3ba in btDiscreteDynamicsWorld::stepSimulation(float, int, float) ()
    #8  0x0000555555cd5d62 in Urho3D::PhysicsWorld::Update(float) ()
    #9  0x0000555555cdbbc1 in Urho3D::EventHandlerImpl<Urho3D::PhysicsWorld>::Invoke(Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&) ()
    #10 0x0000555555be52fb in Urho3D::Object::SendEvent(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&) ()
    #11 0x00005555560cd987 in Urho3D::Scene::Update(float) ()
    #12 0x00005555560d0551 in Urho3D::EventHandlerImpl<Urho3D::Scene>::Invoke(Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&) ()
    #13 0x0000555555be5ad7 in Urho3D::Object::SendEvent(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&) ()
    #14 0x0000555555c0c58d in Urho3D::Engine::Update() ()
    #15 0x0000555555c0da93 in Urho3D::Engine::RunFrame() ()
    #16 0x0000555555c0aaf5 in Urho3D::Application::Run() ()
    #17 0x000055555587ba3a in RunApplication () at /home/slapin/dungeon/rework/Urho3DPlayer.cpp:48
    #18 0x000055555587bae1 in main (argc=1, argv=0x7fffffffe248) at /home/slapin/dungeon/rework/Urho3DPlayer.cpp:48

Looks like Bullet detected collision of nonexistent RigidBody. So I wonder how to safely remove RigidBodies and constraints. (Disabling these lead to the same result).

-------------------------

