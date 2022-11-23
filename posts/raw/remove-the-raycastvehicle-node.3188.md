redmouth | 2017-06-02 02:40:56 UTC | #1

In Sample 46 RayCastVehicle Demo,
1 Removing the Vehicle Node and all it's child Wheel nodes
2 Recreating the Vehicle, got the following crash:<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/150a2122ddeb5036257bedd5b5cd359447083bae.png" width="690" height="318">

-------------------------

slapin | 2017-06-02 02:55:30 UTC | #2

Which version hash do you use? Also could you please report to github?

-------------------------

slapin | 2017-06-02 02:56:17 UTC | #3

Also could you please attach *text* log dump of backtrace?

-------------------------

redmouth | 2017-06-02 03:23:54 UTC | #4

// Code In Extended Application to remove the vehicle
//Node* vehicleNode;

    Vehicle* vehicle = vehicleNode->GetComponent<Vehicle>();
    bool sameNode = vehicle->GetNode() == vehicleNode;
    vehicle->Destroy();
    scene_->RemoveChild(vehicleNode);




// Here I want to remove the emitter nodes and all the wheel nodes.

    void Vehicle::Destroy()
    {
        for (int i=0; i<particleEmitterNodeList_.Size(); ++i)                                                                           
            GetScene()->RemoveChild(particleEmitterNodeList_[i]);
        particleEmitterNodeList_.Clear();
        RaycastVehicle* vehicle = node_->GetComponent<RaycastVehicle>();
        for (int i=0; i<vehicle->GetNumWheels(); ++i)
            GetScene()->RemoveChild(vehicle->GetWheelNode(i));

        //delete vehicle;
    }




I don't know if it's the correct way to  remove the vehicle.  The crash happens after recreating the vehicle.

-------------------------

slapin | 2017-06-02 05:35:48 UTC | #5

Just deleting node, as long as RemoveComponent should work.
If they don't you better submit a bug with full backtrace and complete code sample, I will resolve it.
Please do it on github.

-------------------------

redmouth | 2017-06-02 09:26:24 UTC | #6

It works on Linux platform, but  crashs on Android.

(lldb) bt
* thread #13, name = 'SDLThread', stop reason = signal SIGSEGV: invalid address (fault address: 0x60)
  * frame #0: libworldexplore.so`btRaycastVehicle::updateWheelTransformsWS(this=0xa184f100, wheel=0x00000000, interpolatedTransform=false) at btRaycastVehicle.cpp:154
    frame #1: libworldexplore.so`btRaycastVehicle::updateWheelTransform(this=0xa184f100, wheelIndex=0, interpolatedTransform=false) at btRaycastVehicle.cpp:107
    frame #2: libworldexplore.so`btRaycastVehicle::updateVehicle(this=0xa184f100, step=0.0166666675) at btRaycastVehicle.cpp:273
    frame #3: libworldexplore.so`btRaycastVehicle::updateAction(this=0xa184f100, collisionWorld=0xb4086790, step=0.0166666675) at btRaycastVehicle.h:88
    frame #4: libworldexplore.so`btDiscreteDynamicsWorld::updateActions(this=0xb4086790, timeStep=0.0166666675) at btDiscreteDynamicsWorld.cpp:614
    frame #5: libworldexplore.so`btDiscreteDynamicsWorld::internalSingleStepSimulation(this=0xb4086790, timeStep=0.0166666675) at btDiscreteDynamicsWorld.cpp:513
    frame #6: libworldexplore.so`btDiscreteDynamicsWorld::stepSimulation(this=0xb4086790, timeStep=0.0167804994, maxSubSteps=2, fixedTimeStep=0.0166666675) at btDiscreteDynamicsWorld.cpp:455
    frame #7: libworldexplore.so`Urho3D::PhysicsWorld::Update(this=0xb4286200, timeStep=0.0167804994) at PhysicsWorld.cpp:256
    frame #8: libworldexplore.so`Urho3D::PhysicsWorld::HandleSceneSubsystemUpdate(this=0xb4286200, eventData=0xb43a43b0) at PhysicsWorld.cpp:796
    frame #9: libworldexplore.so`Urho3D::EventHandlerImpl<Urho3D::PhysicsWorld>::Invoke(this=0xa18c29e0, eventData=0xb43a43b0) at Object.h:307
    frame #10: libworldexplore.so`Urho3D::Object::OnEvent(this=0xb4286200, sender=0xa18ba280, eventType=(value_ = 1997371372), eventData=0xb43a43b0) at Object.cpp:113
    frame #11: libworldexplore.so`Urho3D::Object::SendEvent(this=0xa18ba280, eventType=(value_ = 1997371372), eventData=0xb43a43b0) at Object.cpp:325
    frame #12: libworldexplore.so`Urho3D::Scene::Update(this=0xa18ba280, timeStep=0.0167804994) at Scene.cpp:787
    frame #13: libworldexplore.so`Urho3D::Scene::HandleUpdate(this=0xa18ba280, eventData=0xb43f2ca0) at Scene.cpp:1171
    frame #14: libworldexplore.so`Urho3D::EventHandlerImpl<Urho3D::Scene>::Invoke(this=0xa18c2800, eventData=0xb43f2ca0) at Object.h:307
    frame #15: libworldexplore.so`Urho3D::Object::OnEvent(this=0xa18ba280, sender=0xb43fc740, eventType=(value_ = 915638697), eventData=0xb43f2ca0) at Object.cpp:121
    frame #16: libworldexplore.so`Urho3D::Object::SendEvent(this=0xb43fc740, eventType=(value_ = 915638697), eventData=0xb43f2ca0) at Object.cpp:355
    frame #17: libworldexplore.so`Urho3D::Engine::Update(this=0xb43fc740) at Engine.cpp:695
    frame #18: libworldexplore.so`Urho3D::Engine::RunFrame(this=0xb43fc740) at Engine.cpp:519
    frame #19: libworldexplore.so`Urho3D::Application::Run(this=0xb4266600) at Application.cpp:86
    frame #20: libworldexplore.so`RunApplication() at TestRayVehicleEnvironment.cpp:45
    frame #21: libworldexplore.so`::SDL_main(argc=0, argv=0xae7ff9e0) at TestRayVehicleEnvironment.cpp:45
    frame #22: libworldexplore.so`Java_org_libsdl_app_SDLActivity_nativeInit(env=0xb43f9940, cls=0xae7ffa8c, array=0xae7ffa90, filesDir="/data/data/co.deepstudio.worldexplore/files") at SDL_android_main.c:69
    frame #23: 0xa463572b

-------------------------

redmouth | 2017-06-02 09:40:36 UTC | #7

github link: https://github.com/urho3d/Urho3D/issues/1967

-------------------------

