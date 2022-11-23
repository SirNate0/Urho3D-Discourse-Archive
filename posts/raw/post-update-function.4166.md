vivienneanthony | 2018-04-10 15:16:02 UTC | #1

Hello,

I have a logic component derived class. I'm trying to figure out how the PostUpdate(float timestep) works. It works once but doesn't repeat. Anyone know how to properly set a derived class to call Post Update.

I tried the both ways. Creating a virtual void PostUpdate function and also SubscribeToEvent E_SCENEPOSTUPDATE.

Both doesn't work. It seems to only work on the component creation when its also added to a scene.

Vivienne

-------------------------

vivienneanthony | 2018-04-10 18:56:28 UTC | #2

This is the code I have .

[code]
// Initialize
void ComputerCoreComponent::Initialize() {
	// Debug
	ALPHAENGINE_LOGINFO("Initialize Called");

	// Get the Navigation Module
	m_pNavigationModule = GetComponent<NavigationModuleComponent>();

	//  Bunch of code

	// Subscribe to post update
	SetUpdateEventMask(USE_POSTUPDATE);

	// Subscribe to event
	SubscribeToEvent(E_POSTUPDATE,
			URHO3D_HANDLER(ComputerCoreComponent, HandlePostUpdate));
}


void ComputerCoreComponent::HandlePostUpdate(StringHash eventType,
		VariantMap& eventData) {
	if (m_pAutomatedVehicle) {
		// Apply Linear Velocity
		m_pAutomatedVehicle->ApplyLinearVelocity(m_LinearVelocity);
	} else {
		ALPHAENGINE_LOGINFO("Post Update Failed. No Automated Vehicle");
	}
}

[/code]

In the debug info "Post Update Failed. No Automated Vehicle" only appears once but it should show after each physics post update.

-------------------------

Enhex | 2018-04-10 19:09:28 UTC | #3

You should do physics operations in the pre-step event.

E_**SCENE**POSTUPDATE only applys to components which are part of a scene.

Your code isn't helpful since we don't know what sets `m_pAutomatedVehicle`.

-------------------------

vivienneanthony | 2018-04-10 19:21:03 UTC | #4

[quote="Enhex, post:3, topic:4166, full:true"]
You should do physics operations in the pre-step event.

E_SCENEPOSTUPDATE only applys to components which are part of a scene.

Your code isn’t helpful since we don’t know what sets m_pAutomatedVehicle.
[/quote]

Thanks for the reply.

A better idea of what I am trying to implement is here https://www.reddit.com/r/gamedev/comments/8836sb/ship_mechanics_using_thrusters_and_bullet_physics/

It's the first recommendation. It comes from a developer of Star Citizen on how they handle physics of ships.

The full code is below for the function. When the function is called it gets the component AutomatedVehicle and sets the pointer.

[code]
// Initialize
void ComputerCoreComponent::Initialize() {
	// Debug
	ALPHAENGINE_LOGINFO("Initialize Called");

	// Get the Navigation Module
	m_pNavigationModule = GetComponent<NavigationModuleComponent>();

	// Get Automated Vechicle Component
	m_pAutomatedVehicle = GetComponent<AutomatedVehicleComponent>();

	// Get attached propulsion thrusters
	PODVector<PropulsionThrusterComponent *> pPropulsionThrusters;

	// Get Thrusters
	GetNode()->GetComponents<PropulsionThrusterComponent>(pPropulsionThrusters,
			true);

	// Copy thrusters into memory
	if (pPropulsionThrusters.Size() == 0) {
		return;
	} else {
		if (m_pPropulsionThrusters.Size() == 0) {
			// loop thoop each thruster and update
			for (unsigned int i = 0; i < pPropulsionThrusters.Size(); i++) {
				// copy each thruster
				m_pPropulsionThrusters.Push(
						(SharedPtr<PropulsionThrusterComponent> ) pPropulsionThrusters[i]);
			}

		}
	}

	// Subscribe to post update
	SetUpdateEventMask(USE_POSTUPDATE);

	// Subscribe to event
	SubscribeToEvent(E_POSTUPDATE,
			URHO3D_HANDLER(ComputerCoreComponent, HandlePostUpdate));

}
[/code]

-------------------------

Enhex | 2018-04-10 19:24:16 UTC | #5

it's most likely you're calling `GetComponent<AutomatedVehicleComponent>()` before you created that component.

You may need to use DelayedStart():
https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_logic_component.html#ab87accfdac685351fde43278dca1fa1f

-------------------------

vivienneanthony | 2018-04-10 19:24:25 UTC | #6

The automated class is this. Right now it's a container component as I work on how the physics works.

[code]
/*
 * AutomatedVehicle.cpp
 *
 *  Created on: Feb 22, 2018
 *      Author: vivienne
 */

#include "HangarsClientStd.h"

#include "GameAsset/GAFactory.h"

#include "GameAsset/Components/PhysicsComponent/RigidBodyComponent/RigidBodyComponent.h"

// Add Computer Core to Automated Vehicle
#include "GameAssets/Components/AutomatedVehicle/AutomatedVehicleComponent.h"
#include "GameAssets/Components/ComputerCore/ComputerCoreComponent.h"
#include "GameAssets/Components/PropulsionThruster/PropulsionThrusterComponent.h"

#include "AlphaEngine/GameAsset/Components/PhysicsComponent/RigidBodyComponent/RigidBodyComponentEvent.h"

AutomatedVehicleComponent::AutomatedVehicleComponent(Context* context) :
		LogicComponent(context), m_VehicleType(Vehicle_NULL), m_Name(""), m_pComputerCore(
				nullptr), m_bInitialized(false), m_bLoadedXML(false) {

}

AutomatedVehicleComponent::~AutomatedVehicleComponent() {

	//UnsubscribeFromAllEvents();
}

void AutomatedVehicleComponent::RegisterObject(Context* context) {
	context->RegisterFactory<AutomatedVehicleComponent>();
}

bool AutomatedVehicleComponent::LoadXML(const XMLElement& source,
		bool setInstanceDefault) {
	ResourceCache* cache = g_pApp->GetConstantResCache();

	// Get Name
	XMLElement node = source.GetChild("UniqueID");

	if (node) {
		m_Name = node.GetAttribute("value").CString();
	}

	// Get Vehicle Type
	node = source.GetChild("VehicleType");

	if (node) {
		m_VehicleType = (AutomatedVehicleType) node.GetUInt("value");
	}

	// Set Loaded XML
	m_bLoadedXML = true;

	return true;
}

bool AutomatedVehicleComponent::SaveXML(XMLElement& dest) const {
	XMLElement componentNode = GAFactory::SaveComponentToXML(dest,
			GetTypeName(), node_);

	// Create name
	XMLElement childNode = componentNode.CreateChild("UniqueID");

	// Set the name
	childNode.SetAttribute("value", String(m_Name.c_str()));

	// Set vehicle type
	childNode = componentNode.CreateChild("VehicleType");

	// Set value
	// NEED TO CONVERT
	childNode.SetUInt("value", m_VehicleType);

	return true;
}

// Process per frame
void AutomatedVehicleComponent::FixedUpdate(float timeStep) {
	// If loaded XML and not initialized
	if (m_bLoadedXML && m_bInitialized == false && node_)// Handle Per Frame Update
			{
		Initialize();
	}

	return;
}

void AutomatedVehicleComponent::Initialize() {
	// Rigid Body
	m_pRigidBody = GetComponent<RigidBodyComponent>();

	// Get computer core
	m_pComputerCore = GetComponent<ComputerCoreComponent>();

	// Initialize computer core if attached
	if (m_pComputerCore) {
		m_pComputerCore->Initialize();
	}

//	// Get attached propulsion thrusters
//	PODVector<PropulsionThrusterComponent *> pPropulsionThrusters;
//
//	// Get Thrusters
//	GetNode()->GetComponents<PropulsionThrusterComponent>(pPropulsionThrusters,
//			true);
//
//	// If thrusters detected
//	if (int size = pPropulsionThrusters.Size()) {
//		for (unsigned int i = 0; i < size; i++) {
//			m_pPropulsionThrusters.push_back(pPropulsionThrusters[i]);
//		}
//	}

	// If the computer core found and propulsion thruster size then m_bInitialized;
	//if (!m_pComputerCore && !pPropulsionThrusters.Size()) {
	if (!m_pComputerCore) {
		// Set initialized to false
		m_bInitialized = false;
	} else {
		m_bInitialized = true;
	}
}

void AutomatedVehicleComponent::SetState(bool state) {
	if (m_pComputerCore) {
		m_pComputerCore->SetState(state);
	}
}

void AutomatedVehicleComponent::InitializeAllDelegates() {
	// Initialize
	//Initialize();

	// DEBUG LOG
	//ALPHAENGINE_LOGINFO("Vehicle initialize delegates");

	//SubscribeToEvent(E_NODECOLLISION, URHO3D_HANDLER(AutomatedVehicle, HandleCollisionBoxDelegate));
}

void AutomatedVehicleComponent::HandleCollisionBoxDelegate(StringHash eventType,
		VariantMap& eventData) {

	// Get Data
	m_OtherNode =
			static_cast<Node *>(eventData[RIGIDBODY_COLLISIONBOX::P_OTHERNODE].GetPtr());

	//ALPHAENGINE_LOGINFO(node->GetName());

	// Check if box hit gravity
	if (m_OtherNode->GetName().Contains("BoxGravity")) {
		ALPHAENGINE_LOGINFO("Ship hit box gravity");
	}
}

// Apply Linear Velocity
void AutomatedVehicleComponent::ApplyLinearVelocity(Vector3 linearVelocity) {
}

// Apply Angular Velocity
void AutomatedVehicleComponent::ApplyAngularVelocity(Vector3 angularVelocity) {
}

// Apply Impulse
void AutomatedVehicleComponent::ApplyImpulse(Vector3 impulse) {
}

[/code]

-------------------------

vivienneanthony | 2018-04-10 19:26:34 UTC | #7

[quote="Enhex, post:5, topic:4166"]
t’s most likely you’re calling GetComponent&lt;AutomatedVehicleComponent&gt;() before you created that component.

You may need to use DelayedStart():
[/quote]


I'll look. I'll check but I should at least get some message "Post Update Failed. No Automated Vehicle" in the console log info repeatedly.

-------------------------

vivienneanthony | 2018-04-11 17:55:08 UTC | #9

After taking a break. It was working as coded. I changed temporarily the intended way I would apply impulse. All good now.

-------------------------

vivienneanthony | 2018-04-14 19:09:32 UTC | #10

[quote="vivienneanthony, post:7, topic:4166"]
t’s most likely you’re calling GetComponent&lt;AutomatedVehicleComponent&gt;() before you created that component.

You may need to use DelayedStart():
[/quote]

This is for anyone but I found this code.  It might be useful in a way just figuring the Urho3D translation.
I code I revised works some ignoring the whole cardinal system setup temporary. I am just setting longitude, latitude, and vertical movement. I'm using a similiar method like Star Citizen.

The key question will the code on the link help stabilize rotation in a scene that has gravity. Additionally, 

[code]
 newAngularVelocity = angularVelocity.PerpProjectOnto(jetAngularImpulse);
[/code]

I'm not sure of the equivalent. I think the link has a clue then afterward I could possible set the rotation to be Vector3::Identity * the Y axis angle 

http://twistedoakstudios.com/blog/Post8623_angular-velocity-is-simple


My current code is 

[CODE]
// All Updates
void ComputerCoreComponent::Update(float timeStep) {
	// If command buffer
	if (m_CommandBuffer.size()) {
		ComputerCoreCommand currentCommand = m_CommandBuffer.front();

		// Output command
		if (!currentCommand.command.Empty()) {
			//	ALPHAENGINE_LOGINFO(currentCommand.command);
		}

		// Ship Controls
		if (currentCommand.command.Contains("Pitch+") == true) {
			m_MovementPitch += .10;
			if (m_MovementPitch > 1.0f)
				m_MovementPitch = 1.0f;
		}
		if (currentCommand.command.Contains("Pitch-") == true) {
			m_MovementPitch -= .10;
			if (m_MovementPitch < -1.0f)
				m_MovementPitch = -1.0f;
		}
		if (currentCommand.command.Contains("Longitude+") == true) {
			m_MovementLongitude += .10;
			if (m_MovementLongitude > 1.0f)
				m_MovementLongitude = 1.0f;
		}
		if (currentCommand.command.Contains("Longitude-") == true) {
			m_MovementLongitude -= .10;
			if (m_MovementLongitude < -1.0f)
				m_MovementLongitude = -1.0f;
		}
		if (currentCommand.command.Contains("Vertical+") == true) {
			m_MovementVertical += .10;
			if (m_MovementVertical > 1.0f)
				m_MovementVertical = 1.0f;
		}
		if (currentCommand.command.Contains("Vertical-") == true) {
			m_MovementVertical -= .10;
			if (m_MovementVertical < -1.0f)
				m_MovementVertical = -1.0f;
		}

		if (currentCommand.command.Contains("Latitude+") == true) {
			m_MovementLatitude += .10;
			if (m_MovementLatitude > 1.0f)
				m_MovementLatitude = 1.0f;
		}
		if (currentCommand.command.Contains("Latitude-") == true) {
			m_MovementLatitude -= .10;
			if (m_MovementLatitude < -1.0f)
				m_MovementLatitude = -1.0f;
		}
		if (currentCommand.command.Contains("Longitude+") == true) {
			m_MovementLongitude += .10;
			if (m_MovementLongitude > 1.0f)
				m_MovementLongitude = 1.0f;
		}
		if (currentCommand.command.Contains("Longitude-") == true) {
			m_MovementLongitude -= .10;
			if (m_MovementLongitude < -1.0f)
				m_MovementLongitude = -1.0f;
		}
		if (currentCommand.command.Contains("Vertical+") == true) {
			m_MovementVertical += .10;
			if (m_MovementVertical > 1.0f)
				m_MovementVertical = 1.0f;
		}
		if (currentCommand.command.Contains("Vertical-") == true) {
			m_MovementVertical -= .10;
			if (m_MovementVertical < -1.0f)
				m_MovementVertical = -1.0f;
		}

		// Clear Command Buffer
		m_CommandBuffer.clear();
	}

	// Convert Movement to Velocity
	ConvertMovementToVelocity();
}

// Set State of modules
void ComputerCoreComponent::SetState(bool state) {
	// If navigation module
	if (m_pNavigationModule) {
		m_pNavigationModule->SetState(state);
	}
}
void ComputerCoreComponent::HandlePostUpdate(StringHash eventType,
		VariantMap& eventData) {
	if (m_pAutomatedVehicle) {
		if (m_LinearVelocity != Vector3::ZERO) {
			// Apply Linear Velocity
			m_pAutomatedVehicle->ApplyImpulse(m_LinearVelocity);

			// Reset all forces
			m_MovementLatitude = m_MovementLongitude = m_MovementVertical = 0.0f;
		}
	} else {
		ALPHAENGINE_LOGINFO("Post Update Failed. No Automated Vehicle");
	}
}

// Convert Movement to Velocity
void ComputerCoreComponent::ConvertMovementToVelocity() {
	// Create a zero vector
	Vector3 LinearVelocity = Vector3::ZERO;

	// Calculate impulse amount by Latitiude, Vertical, and Longititude
	LinearVelocity = Vector3(m_MovementLatitude * 2, m_MovementVertical * 2,
			m_MovementLongitude * 2);

	// Set Linear Velocity Impulse
	m_LinearVelocity = LinearVelocity;

}
[/code]

-------------------------

vivienneanthony | 2018-04-19 20:27:11 UTC | #11

Sorry. I know its a lot of question. I'm reading docs and pdf's and it's semi gibberish. I visually can see what to do but seeing a bunch formulas ins't help.

The non-gibberish method. I would think is get the current rotation and velocity. Multiply the rotation by velocity and inverse it.  Setting the angular velocity. Then next frame or after simply set the angular velocity to Identity or Identity times the Y axis rotation.  If gravity exist.

-------------------------

