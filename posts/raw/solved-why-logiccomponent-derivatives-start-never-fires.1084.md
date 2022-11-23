grumbly | 2017-01-02 01:05:18 UTC | #1

I must be missing something simple. The goal here is to get a simple custom component based on LogicComponent working with Start and Update correctly being invoked. Any ideas? The OnNodeSet works, but Start and Update do not.

Thing.h
[spoiler][code]
#pragma once
#include <Urho3D/Scene/LogicComponent.h>
using namespace Urho3D;

class Thing : public LogicComponent {

	OBJECT(Thing);

	public:
		Thing(Context* context);
		static void RegisterObject(Context *context);
		virtual void Start();
		virtual void Update(float timestep);
	protected:
		virtual void OnNodeSet(Node *node);
	private:
};
[/code][/spoiler]

Thing.cpp
[spoiler][code]
#include <Urho3D/Urho3D.h>
#include <Urho3D/Scene/Node.h>
#include <Urho3D/Core/Context.h>
#include <Urho3D/IO/Log.h>
#include <Urho3D/Core/Object.h>

#include "Thing.h"

using namespace Urho3D;

Thing::Thing(Context* context) : LogicComponent(context) {}

void Thing::RegisterObject(Context *context) { context->RegisterFactory<Thing>(); }

void Thing::Start() { LOGINFO("(I never see this) Component Started"); }

void Thing::Update(float timestep) { LOGINFO(String("(I never see this) component update step: ")+String(timestep)); }

void Thing::OnNodeSet(Node* node) { LOGINFO("This works fine."); }
[/code][/spoiler]

Main Application Constructor (registering the component)
[spoiler][code]
    CustomTest(Context * context) : Application(context)
    {
		 Thing::RegisterObject(context);
    }
[/code][/spoiler]

Adding the Component
[spoiler][code]
boxNode_->CreateComponent<Thing>();
[/code][/spoiler]

-------------------------

grumbly | 2017-01-02 01:05:18 UTC | #2

Ah, thank you. This makes sense now that I look at the headers for LogicComponent and Component.

-------------------------

