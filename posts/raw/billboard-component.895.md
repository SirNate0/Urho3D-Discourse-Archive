thebluefish | 2017-01-02 01:03:53 UTC | #1

I noticed an odd lack of generic Billboard support. BillboardSet is good for some things, but isn't good for others. Instead, I have created a simple Billboard component, that will Billboard any Node.

For example, let's say I want to use RocketDocument3D to position/scale, but still keep the crispness.

Before (using LookAt):
[url=http://i.imgur.com/RtuBv5U.png][img]http://i.imgur.com/RtuBv5Um.png[/img][/url]

After (using Billboard):
[url=http://i.imgur.com/4rPNLjQ.png][img]http://i.imgur.com/4rPNLjQm.png[/img][/url]

This code is considered public domain.

BillboardComponent.h:
[code]
#ifndef _BILLBOARD_COMPONENT_H
#define _BILLBOARD_COMPONENT_H

#pragma once

#include "Component.h"
#include "Camera.h"

class Billboard : public Urho3D::Component
{
	OBJECT(Billboard);
public:
	Billboard(Urho3D::Context* context, Urho3D::Camera* camera = 0);
	~Billboard();

	static void RegisterObject(Urho3D::Context* context);

	void SetCamera(Urho3D::Camera* camera);

protected:

	void HandleUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);

protected:
	Urho3D::WeakPtr<Urho3D::Camera> _camera;
};

#endif
[/code]

BillboardComponent.cpp:
[code]
#include "BillboardComponent.h"

#include "Context.h"
#include "CoreEvents.h"
#include "Node.h"

Billboard::Billboard(Urho3D::Context* context, Urho3D::Camera* camera) : Urho3D::Component(context)
{
	_camera = camera;

	SubscribeToEvent(Urho3D::E_UPDATE, HANDLER(Billboard, HandleUpdate));
}

Billboard::~Billboard()
{
}

void Billboard::RegisterObject(Urho3D::Context* context)
{
	context->RegisterFactory<Billboard>();
}

void Billboard::SetCamera(Urho3D::Camera* camera)
{
	_camera = camera;
}

void Billboard::HandleUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
{
	Urho3D::Node* node = GetNode();

	if (_camera.NotNull() && node)
	{
		node->SetWorldRotation(_camera->GetFaceCameraRotation(node->GetPosition(), node->GetRotation(), Urho3D::FC_ROTATE_XYZ));
	}
}
[/code]

-------------------------

