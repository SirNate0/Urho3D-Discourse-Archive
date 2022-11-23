thebluefish | 2017-01-02 01:10:10 UTC | #1

I recently ran into a problem. I have a couple dozen components that do the bulk of their logic in LogicComponent::FixedUpdate. However I recently decided to forego the current Physics implementation in favour of a non-physics solution. My components do not rely on the physics, but suddenly the FixedUpdate function stopped working when I took out PhysicsWorld. So I wrote this little shim that continues to fire off fixed pre-step and post-step events allowing LogicComponent::FixedUpdate to continue to function properly without actually using Bullet physics.

PhysicsWorld.h
[code]
#ifndef _BLU_PHYSICSWORLD_H
#define _BLU_PHYSICSWORLD_H

#pragma once

#include <Urho3D/Urho3D.h>
#include <Urho3D/Scene/Component.h>

namespace blu
{
    class PhysicsWorld : public Urho3D::Component
    {
        URHO3D_OBJECT(PhysicsWorld, Urho3D::Component);
        
    public:
        PhysicsWorld(Urho3D::Context* context);
        ~PhysicsWorld();

        static void RegisterObject(Urho3D::Context* context);
        
        /// Set simulation substeps per second.
        void SetFps(unsigned fps);
        
    protected:
        /// Handle scene being assigned.
        virtual void OnSceneSet(Urho3D::Scene* scene);

    protected:
        /// Handle the scene subsystem update event, step simulation here.
        void HandleSceneSubsystemUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
        /// Trigger update before each physics simulation step.
        void PreStep(float timeStep);
        /// Trigger update after each physics simulation step.
        void PostStep(float timeStep);
        
    private:
    
        /// Simulation substeps per second.
        unsigned fps_;
        
        /// Internal timestep tracking
        float accumulator_;
    };
}

#endif // _BLU_PHYSICSWORLD_H
[/code]

PhysicsWorld.cpp
[code]
#include "PhysicsWorld.h"

#include <Urho3D/Core/Context.h>
#include <Urho3D/Core/Profiler.h>
#include <Urho3D/Physics/PhysicsEvents.h>
#include <Urho3D/Scene/SceneEvents.h>

namespace blu
{
    static const int DEFAULT_FPS = 60;
    
    PhysicsWorld::PhysicsWorld(Urho3D::Context* context)
    : Urho3D::Component(context)
    , fps_(DEFAULT_FPS)
    , accumulator_(0.f)
    {
        accumulator_ = 0.f;
    }
    
    PhysicsWorld::~PhysicsWorld()
    {
        
    }

    void PhysicsWorld::RegisterObject(Urho3D::Context* context)
    {
        context->RegisterFactory<PhysicsWorld>();
    }
    
    /// Set simulation substeps per second.
    void PhysicsWorld::SetFps(unsigned fps)
    {
        fps_ = (unsigned)Urho3D::Clamp(fps, 1, 1000);

        MarkNetworkUpdate();
    }
    
    void PhysicsWorld::OnSceneSet(Urho3D::Scene* scene)
    {
        // Subscribe to the scene subsystem update, which will trigger the physics simulation step
        if (scene)
        {
            SubscribeToEvent((Urho3D::Object*)GetScene(), Urho3D::E_SCENESUBSYSTEMUPDATE, URHO3D_HANDLER(PhysicsWorld, HandleSceneSubsystemUpdate));
        }
        else
            UnsubscribeFromEvent(Urho3D::E_SCENESUBSYSTEMUPDATE);
    }

    void PhysicsWorld::HandleSceneSubsystemUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
    {
        using namespace Urho3D::SceneSubsystemUpdate;
        
        float timeStep = eventData[P_TIMESTEP].GetFloat();
        
        accumulator_ += timeStep;
        
        float internalTimeStep = 1.0f / fps_;

        // Step
        int iterations = floorf(accumulator_ / internalTimeStep);
        for (int i = 0; i < iterations; i++)
        {
            PreStep(internalTimeStep);
            PostStep(internalTimeStep);
            
            accumulator_ -= internalTimeStep;
        }
    }

    void PhysicsWorld::PreStep(float timeStep)
    {
        // Send pre-step event
        using namespace Urho3D::PhysicsPreStep;

        Urho3D::VariantMap& eventData = GetEventDataMap();
        eventData[P_WORLD] = this;
        eventData[P_TIMESTEP] = timeStep;
        SendEvent(Urho3D::E_PHYSICSPRESTEP, eventData);
    }

    void PhysicsWorld::PostStep(float timeStep)
    {
        // Send post-step event
        using namespace Urho3D::PhysicsPostStep;

        Urho3D::VariantMap& eventData = GetEventDataMap();
        eventData[P_WORLD] = this;
        eventData[P_TIMESTEP] = timeStep;
        SendEvent(Urho3D::E_PHYSICSPOSTSTEP, eventData);
    }
}
[/code]

Licensed under the existing Urho3D MIT license.

Due to a check in LogicComponent::UpdateEventSubscription(), I can't roll my own class name. Instead I provide it under the same class name but under a different namespace. This StringHash collision works well for this purpose.

-------------------------

Enhex | 2017-01-02 01:10:11 UTC | #2

A possible hack is to just have an empty physics world. Since there're no bodies there's no work to be done and shouldn't affect performance.
It's simpler since it doesn't require any customization.

An elegant solution would be to use a dedicated events with fixed framerate, instead of re-purposing the physics ones. If you're not using physics, why are you using physics events? That's just misleading.
This can be done simply by adding time to a variable every Update, and once the time is above frame duration, subtract the duration from the time and fire an event.
It also avoids breaking everything if you'll ever need to enable physics again.

-------------------------

thebluefish | 2017-01-02 01:10:11 UTC | #3

[quote="Enhex"] If you're not using physics, why are you using physics events? That's just misleading.[/quote]

I 100% agree. However the alternative is fixing LogicComponent to use some other counter. While it would be a great idea to fix the issue at its root, this is just a quick n dirty little way of keeping LogicComponent happy while removing Bullet as a dependency for my project.

-------------------------

