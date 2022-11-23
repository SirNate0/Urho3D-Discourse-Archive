Lumak | 2017-04-07 19:45:56 UTC | #1

Vehicle dynamics is one of my interests and I recently discovered Bullet's btRaycastVehicle example and ported to Urho Vehicle demo.
Replace the Vehicle.cpp/.h files in Samples/19_VehicleDemo/ and you should be good to go.
[b]Note:[/b] this code sample is intended to show the raycastVehicle basics and should be refactored, and it also breaks saving/restoring the scene.

Edit: added video
https://youtu.be/tGX0gglA9UQ

### Vehicle.cpp
[code]
#include <Urho3D/Urho3D.h>

#include <Urho3D/Physics/CollisionShape.h>
#include <Urho3D/Physics/Constraint.h>
#include <Urho3D/Core/Context.h>
#include <Urho3D/Graphics/Material.h>
#include <Urho3D/Graphics/Model.h>
#include <Urho3D/Physics/PhysicsEvents.h>
#include <Urho3D/Physics/PhysicsWorld.h>
#include <Urho3D/Physics/PhysicsUtils.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Physics/RigidBody.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Graphics/StaticModel.h>
#include <Urho3D/Graphics/DebugRenderer.h>

#include "Vehicle.h"

#include <SDL/SDL_log.h>
#include <Bullet/BulletDynamics/Vehicle/btRaycastVehicle.h>
#include <Bullet/BulletDynamics/Dynamics/btDynamicsWorld.h>

//=============================================================================
//=============================================================================
#define CUBE_HALF_EXTENTS   1
#define DELETE_NULL(x)      { if (x) delete x; x = NULL; }

//=============================================================================
//=============================================================================
Vehicle::Vehicle(Context* context) 
    : LogicComponent( context )
    , steering_( 0.0f )
{
    // fixed update() for inputs and post update() to sync wheels for rendering
    SetUpdateEventMask( USE_FIXEDUPDATE | USE_POSTUPDATE );

    m_fEngineForce = 0.0f;                                                 
    m_fBreakingForce = 0.0f;                                               
                                                                        
    m_fmaxEngineForce = 2500.f;//this should be engine/velocity dependent  
    m_fmaxBreakingForce = 100.f;                                           
                                                                        
    m_fVehicleSteering = 0.0f;                                             
    m_fsteeringIncrement = 0.04f;                                          
    m_fsteeringClamp = 0.3f;                                               
    m_fwheelRadius = 0.5f;                                                 
    m_fwheelWidth = 0.4f;                                                  
    m_fwheelFriction = 1000;//BT_LARGE_FLOAT;                              
    m_fsuspensionStiffness = 14.0f;//20.f;                                 
    m_fsuspensionDamping = 2.0f;//2.3f;                                    
    m_fsuspensionCompression = 4.0f;//4.4f;                                
    m_frollInfluence = 0.01f;//1.0f;                                       
    m_fsuspensionRestLength = 0.6f;//0.6

    m_vehicleRayCaster = NULL;
    m_vehicle = NULL;

    m_vpNodeWheel.Clear();
}

//=============================================================================
//=============================================================================
Vehicle::~Vehicle()
{
    DELETE_NULL( m_vehicleRayCaster );
    DELETE_NULL( m_vehicle );
    
    m_vpNodeWheel.Clear();
}

//=============================================================================
//=============================================================================
void Vehicle::RegisterObject(Context* context)
{
    context->RegisterFactory<Vehicle>();
    
    ATTRIBUTE("Controls Yaw", float, controls_.yaw_, 0.0f, AM_DEFAULT);
    ATTRIBUTE("Controls Pitch", float, controls_.pitch_, 0.0f, AM_DEFAULT);
    ATTRIBUTE("Steering", float, steering_, 0.0f, AM_DEFAULT);
}

//=============================================================================
//=============================================================================
void Vehicle::ApplyAttributes()
{
}

//=============================================================================
//=============================================================================
void Vehicle::Init()
{
    // This function is called only from the main program when initially creating the vehicle, not on scene load
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    
    StaticModel* hullObject = node_->CreateComponent<StaticModel>();
    hullBody_ = node_->CreateComponent<RigidBody>();
    CollisionShape* hullColShape = node_->CreateComponent<CollisionShape>();

    hullBody_->SetMass(800.0f);
    hullBody_->SetLinearDamping(0.2f); // Some air resistance
    hullBody_->SetAngularDamping(0.5f);
    hullBody_->SetCollisionLayer(1);
    
    int rightIndex = 0;
    int upIndex = 1;
    int forwardIndex = 2;
    Scene* scene = GetScene();
    PhysicsWorld *pPhysWorld = scene->GetComponent<PhysicsWorld>();
    btDynamicsWorld *pbtDynWorld = (btDynamicsWorld*)pPhysWorld->GetWorld();

    m_vehicleRayCaster = new btDefaultVehicleRaycaster( pbtDynWorld );
    m_vehicle = new btRaycastVehicle( m_tuning, hullBody_->GetBody(), m_vehicleRayCaster );
    pbtDynWorld->addVehicle( m_vehicle );

    m_vehicle->setCoordinateSystem( rightIndex, upIndex, forwardIndex );

    node_->SetScale( Vector3(1.5f, 1.0f, 3.5f) );
    Vector3 v3BoxExtents = Vector3::ONE;//Vector3(1.5f, 1.0f, 3.0f);
    hullColShape->SetBox( v3BoxExtents );

    hullObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
    hullObject->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
    hullObject->SetCastShadows(true);

    float connectionHeight = -0.4f;//1.2f;
    bool isFrontWheel=true;
    btVector3 wheelDirectionCS0(0,-1,0);
    btVector3 wheelAxleCS(-1,0,0);

    btVector3 connectionPointCS0(CUBE_HALF_EXTENTS-(0.3f*m_fwheelWidth),connectionHeight,2*CUBE_HALF_EXTENTS-m_fwheelRadius);
    m_vehicle->addWheel(connectionPointCS0,wheelDirectionCS0,wheelAxleCS,m_fsuspensionRestLength,m_fwheelRadius,m_tuning,isFrontWheel);

    connectionPointCS0 = btVector3(-CUBE_HALF_EXTENTS+(0.3f*m_fwheelWidth),connectionHeight,2*CUBE_HALF_EXTENTS-m_fwheelRadius);
    m_vehicle->addWheel(connectionPointCS0,wheelDirectionCS0,wheelAxleCS,m_fsuspensionRestLength,m_fwheelRadius,m_tuning,isFrontWheel);

    isFrontWheel = false;
    connectionPointCS0 = btVector3(-CUBE_HALF_EXTENTS+(0.3f*m_fwheelWidth),connectionHeight,-2*CUBE_HALF_EXTENTS+m_fwheelRadius);
    m_vehicle->addWheel(connectionPointCS0,wheelDirectionCS0,wheelAxleCS,m_fsuspensionRestLength,m_fwheelRadius,m_tuning,isFrontWheel);

    connectionPointCS0 = btVector3(CUBE_HALF_EXTENTS-(0.3f*m_fwheelWidth),connectionHeight,-2*CUBE_HALF_EXTENTS+m_fwheelRadius);
    m_vehicle->addWheel(connectionPointCS0,wheelDirectionCS0,wheelAxleCS,m_fsuspensionRestLength,m_fwheelRadius,m_tuning,isFrontWheel);

    for ( int i = 0; i < m_vehicle->getNumWheels(); i++ )
    {
        btWheelInfo& wheel = m_vehicle->getWheelInfo( i );
        wheel.m_suspensionStiffness = m_fsuspensionStiffness;
        wheel.m_wheelsDampingRelaxation = m_fsuspensionDamping;
        wheel.m_wheelsDampingCompression = m_fsuspensionCompression;
        wheel.m_frictionSlip = m_fwheelFriction;
        wheel.m_rollInfluence = m_frollInfluence;
    }

	if ( m_vehicle )
	{
		m_vehicle->resetSuspension();

		for ( int i = 0; i < m_vehicle->getNumWheels(); i++ )
		{
			//synchronize the wheels with the (interpolated) chassis worldtransform
			m_vehicle->updateWheelTransform(i,true);

            btTransform transform = m_vehicle->getWheelTransformWS( i );
            Vector3 v3Origin = ToVector3( transform.getOrigin() );
            Quaternion qRot = ToQuaternion( transform.getRotation() );

            // create wheel node
            Node *wheelNode = GetScene()->CreateChild();
            m_vpNodeWheel.Push( wheelNode );

            wheelNode->SetPosition( v3Origin );
            btWheelInfo whInfo = m_vehicle->getWheelInfo( i );
            Vector3 v3PosLS = ToVector3( whInfo.m_chassisConnectionPointCS );

            wheelNode->SetRotation( v3PosLS.x_ >= 0.0 ? Quaternion(0.0f, 0.0f, -90.0f) : Quaternion(0.0f, 0.0f, 90.0f) );
            wheelNode->SetScale(Vector3(1.0f, 0.65f, 1.0f));

            StaticModel *pWheel = wheelNode->CreateComponent<StaticModel>();
            pWheel->SetModel(cache->GetResource<Model>("Models/Cylinder.mdl"));
            pWheel->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
            pWheel->SetCastShadows(true);
		}
	}
}

//=============================================================================
//=============================================================================
void Vehicle::FixedUpdate(float timeStep)
{
    float newSteering = 0.0f;
    float accelerator = 0.0f;

    // Read controls
    if (controls_.buttons_ & CTRL_LEFT)
        newSteering = -1.0f;
    if (controls_.buttons_ & CTRL_RIGHT)
        newSteering = 1.0f;
    if (controls_.buttons_ & CTRL_FORWARD)
        accelerator = 1.0f;
    if (controls_.buttons_ & CTRL_BACK)
        accelerator = -0.5f;

    // When steering, wake up the wheel rigidbodies so that their orientation is updated
    if ( newSteering != 0.0f )
    {
        steering_ = steering_ * 0.95f + newSteering * 0.05f;
    }
    else
    {
        steering_ = steering_ * 0.8f + newSteering * 0.2f;
    }

    // Set front wheel angles
    m_fVehicleSteering = steering_;
    int wheelIndex = 0;
    m_vehicle->setSteeringValue(m_fVehicleSteering,wheelIndex);
    wheelIndex = 1;
    m_vehicle->setSteeringValue(m_fVehicleSteering,wheelIndex);

    if ( newSteering != 0.0f || accelerator != 0.0f )
    {
        hullBody_->Activate();
    }

    // apply forces
    m_fEngineForce = m_fmaxEngineForce * accelerator;
    m_fBreakingForce = 0.f;

    // 2x wheel drive
    for ( int i = 2; i < 4; ++i )
    {
        m_vehicle->applyEngineForce( m_fEngineForce, i );
        //m_vehicle->setBrake( m_fBreakingForce, i );
    }
}

//=============================================================================
// sync wheels for rendering
//=============================================================================
void Vehicle::PostUpdate(float )
{
    for ( int i = 0; i < m_vehicle->getNumWheels(); i++ )
    {
		m_vehicle->updateWheelTransform( i, true );

        btTransform transform = m_vehicle->getWheelTransformWS( i );
        Vector3 v3Origin = ToVector3( transform.getOrigin() );
        Quaternion qRot = ToQuaternion( transform.getRotation() );

        Node *pWheel = m_vpNodeWheel[ i ];
        pWheel->SetPosition( v3Origin );
        
        btWheelInfo whInfo = m_vehicle->getWheelInfo( i );
        Vector3 v3PosLS = ToVector3( whInfo.m_chassisConnectionPointCS );
        Quaternion qRotator = ( v3PosLS.x_ >= 0.0 ? Quaternion(0.0f, 0.0f, -90.0f) : Quaternion(0.0f, 0.0f, 90.0f) );
        pWheel->SetRotation( qRot * qRotator );
    }
}
[/code]

### Vehicle.h
[code]
#pragma once

#include <Urho3D/Input/Controls.h>
#include <Urho3D/Scene/LogicComponent.h>
#include <Bullet/BulletDynamics/Vehicle/btRaycastVehicle.h>

namespace Urho3D
{
class Constraint;
class Node;
class RigidBody;
}

using namespace Urho3D;


//=============================================================================
//=============================================================================
const int CTRL_FORWARD = 1;
const int CTRL_BACK = 2;
const int CTRL_LEFT = 4;
const int CTRL_RIGHT = 8;

const float YAW_SENSITIVITY = 0.1f;
const float ENGINE_POWER = 10.0f;
const float DOWN_FORCE = 10.0f;
const float MAX_WHEEL_ANGLE = 22.5f;

//=============================================================================
// Vehicle component, responsible for physical movement according to controls.
//=============================================================================
class Vehicle : public LogicComponent
{
    OBJECT(Vehicle)

public:
    /// Construct.
    Vehicle(Context* context);
    ~Vehicle();
    
    /// Register object factory and attributes.
    static void RegisterObject(Context* context);
    
    /// Perform post-load after deserialization. Acquire the components from the scene nodes.
    virtual void ApplyAttributes();

    /// Initialize the vehicle. Create rendering and physics components. Called by the application.
    void Init();

    /// Handle physics world update. Called by LogicComponent base class.
    virtual void FixedUpdate(float timeStep);
    virtual void PostUpdate(float timeStep);
    
    /// Movement controls.
    Controls controls_;
    
private:
    // Hull RigidBody
    WeakPtr<RigidBody> hullBody_;
    
    /// Current left/right steering amount (-1 to 1.)
    float steering_;

    // raycast vehicle
    btRaycastVehicle::btVehicleTuning	m_tuning;
    btVehicleRaycaster                  *m_vehicleRayCaster;
    btRaycastVehicle                    *m_vehicle;

    // IDs of the wheel scene nodes for serialization.
    Vector<Node*>           m_vpNodeWheel;

    float	m_fEngineForce;
    float	m_fBreakingForce;

    float	m_fmaxEngineForce;
    float	m_fmaxBreakingForce;

    float	m_fVehicleSteering;
    float	m_fsteeringIncrement;
    float	m_fsteeringClamp;
    float	m_fwheelRadius;
    float	m_fwheelWidth;
    float	m_fwheelFriction;
    float	m_fsuspensionStiffness;
    float	m_fsuspensionDamping;
    float	m_fsuspensionCompression;
    float	m_frollInfluence;
    float   m_fsuspensionRestLength;

};

[/code]

-------------------------

Lumak | 2017-01-02 01:06:42 UTC | #2

You can lower the wheel connection height to:
    float connectionHeight = 0.0f; (Line 147, I think)

and have more stability to allow you to increase the engine force a bit:
    m_fmaxEngineForce = 3000.f;

Try adjusting suspension parameters to your liking.

-------------------------

rasteron | 2017-01-02 01:06:43 UTC | #3

This is nice, and the suspension feature is really an upgrade. Maybe this can be PR'd for next release?

-------------------------

cadaver | 2017-01-02 01:06:43 UTC | #4

Nice example. For a pull request this should be refactored into a component so that the Bullet raycastvehicle class is not directly exposed to users, as otherwise it will be hard to expose to scripting languages.

-------------------------

Lumak | 2017-01-02 01:06:55 UTC | #5

added an archived video

-------------------------

Mike | 2017-01-02 01:06:55 UTC | #6

Great!  :stuck_out_tongue:

-------------------------

Mike | 2017-01-02 01:07:02 UTC | #7

Iv've started porting to component.
I'm thinking of creating 2 separate components: a Vehicle component for vehicle chassis and a Wheel component for each wheel. As many settings are per wheel, it could be handy at reloading time to re-create the whole vehicle that way. Wheel would store the vehicle node ID.
Before going further, I'd like to have feedback about this option or other better options.

-------------------------

Lumak | 2017-01-02 01:07:03 UTC | #8

I think that's an excellent idea. Having a wheel component would definitely give more flexibility on how the vehicle is constructed.

-------------------------

Mike | 2017-01-02 01:07:03 UTC | #9

Thanks Lumak, I will follow this path.

-------------------------

Mike | 2017-01-02 01:07:05 UTC | #10

I can't figure out how to remove a wheel from the vehicle.
I haven't found a method to do this in btRaycastVehicle, so I'm trying to use 'remove' from LinearMath/btAlignedObjectArray.h, but it fails to compile:
[code]void Vehicle::RemoveWheel(int wheelID)
{
	if (!vehicle_)
		return;
	btWheelInfo& wheel = vehicle_->getWheelInfo(wheelID);
	vehicle_->m_wheelInfo.remove(wheel);
}[/code]
where vehicle_ is the btRaycastVehicle and m_wheelInfo is the btAlignedObjectArray from btRaycastVehicle.h.

-------------------------

Lumak | 2017-01-02 01:07:06 UTC | #11

Verified the compile error when calling remove() which results in a compare error in findLinearSearch() function at:
    if (m_data[i] == key) 

btAlignedObjectArray class seems to have a problem with this when you declare btAlignedObjectArray vector with a non-pointer data type.

But the work around for this is to do something similar to what the remove() function attempts:
[code]
void Vehicle::RemoveWheel(int wheelID)
{
   if (!m_vehicle)
      return;

   if ( wheelID < m_vehicle->m_wheelInfo.size() )
   {
       if ( wheelID != m_vehicle->m_wheelInfo.size() - 1 )
       {
           m_vehicle->m_wheelInfo.swap( wheelID, m_vehicle->m_wheelInfo.size() - 1 );
       }
       m_vehicle->m_wheelInfo.pop_back();
   }
}

[/code]

Hope this helps.

-------------------------

Mike | 2017-01-02 01:07:07 UTC | #12

Thanks Lumak, this is indeed a good way to get rid of findLinearSearch() issue.

-------------------------

slapin | 2017-04-07 19:10:59 UTC | #13

Is there any update on vehicle components in Urho?

Sorry for reviving old topic, but I'm really-really interested :)

-------------------------

smellymumbler | 2017-04-08 00:15:07 UTC | #14

Me too! This is a great example btw.

-------------------------

Modanung | 2017-04-10 16:01:10 UTC | #15

It most certainly is. I merged the Vehicle from this sample with the Vehicles in [OGTatt](https://github.com/LucKeyProductions/OGTatt). I couldn't quite get the visual wheels to update correctly somehow, but the cars can drive! :)

https://vimeo.com/212604275

-------------------------

slapin | 2017-04-11 09:18:02 UTC | #16

Well, I packed-up reasonable component for a vehicle. With examples, can be found
here: https://github.com/urho3d/Urho3D/pull/1903 A problem with this PR is that win32 shared library builds fail for
no reason I understand :( Please help find the culprit.

https://youtu.be/LKjzcN3s65Y

-------------------------

1vanK | 2017-04-11 06:34:25 UTC | #17

> A problem with this PR is that win32 shared library builds fail for

add URHO3D_API to component

-------------------------

Modanung | 2017-04-11 09:17:39 UTC | #18

[quote="slapin, post:16, topic:1306"]
p.s. how do you add video in view mode?
[/quote]

Simply put it on its own line. This is called a onebox

https://github.com/discourse/onebox

-------------------------

slapin | 2017-04-11 13:43:15 UTC | #19

I added these and put all accessors to .cpp. This is not enough.
I see

> CMakeFiles/46_RaycastVehicle.dir/objects.a(RaycastVehicleDemo.cpp.obj):RaycastVehicleDemo.cpp:(.text$_ZN17btTypedConstraintD0Ev[btTypedConstraint::~btTypedConstraint()]+0xb): undefined reference to btAlignedFreeInternal(void*)' CMakeFiles/46_RaycastVehicle.dir/objects.a(RaycastVehicleDemo.cpp.obj):RaycastVehicleDemo.cpp:(.data$_ZTV17btTypedConstraint[vtable for btTypedConstraint]+0x60): undefined reference to btTypedConstraint::serialize(void*, btSerializer*) const'

errors which are from some low-level bullet stuff. Looks like I won't have enough time to resolve this if
nobody points on what to do, so that is going to rot.

-------------------------

slapin | 2017-04-11 17:04:22 UTC | #20

Sorry, I deleted PR, this was too ambitious for me with time I have. If anybody wants the code
and have some ideas feel free to pull from

https://github.com/slapin/Urho3D/tree/raycast-vehicle

I will continue to add features there, but as I don't use windows and shared library builds I will not fix
problems with shared library on windows, as it looks quite complicated issue and I have zero motivation
to fix that.
So I will keep changes local and add features to have full btRaycastVehicle wrapper.

-------------------------

slapin | 2017-04-11 19:33:57 UTC | #21

Well, emergency help arrived and I was able to resolve this issue (at least on my machine).
Github did not allow me to reopen PR, so I created new one.
All mingw builds I did try built successfully.

https://github.com/urho3d/Urho3D/pull/1904

-------------------------

