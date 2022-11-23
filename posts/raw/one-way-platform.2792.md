1vanK | 2017-02-13 20:38:02 UTC | #1

Player node should has tag "Player", platform nodes should have tag "Platform"

MyPhysicsWorld2D.h
```
#pragma once
#include <Urho3D/Urho3DAll.h>

class MyPhysicsWorld2D : public PhysicsWorld2D
{
    URHO3D_OBJECT(MyPhysicsWorld2D, PhysicsWorld2D);

public:
    MyPhysicsWorld2D(Context* context);
    static void RegisterObject(Context* context);

    virtual void PreSolve(b2Contact* contact, const b2Manifold* oldManifold) override;
};
```

MyPhysicsWorld2D.cpp
```
#include "MyPhysicsWorld2D.h"

MyPhysicsWorld2D::MyPhysicsWorld2D(Context* context) :
    PhysicsWorld2D(context)
{
}

void MyPhysicsWorld2D::RegisterObject(Context* context)
{
    context->RegisterFactory<MyPhysicsWorld2D>();
}

void MyPhysicsWorld2D::PreSolve(b2Contact* contact, const b2Manifold* oldManifold)
{
    ContactInfo contactInfo(contact);

    if ((contactInfo.nodeA_->HasTag("Player") && contactInfo.nodeB_->HasTag("Platform")) ||
        (contactInfo.nodeB_->HasTag("Player") && contactInfo.nodeA_->HasTag("Platform")))
    {
        Node* playerNode = contactInfo.nodeA_;
        Node* platformNode = contactInfo.nodeB_;
        
        if (contactInfo.nodeB_->HasTag("Player"))
        {
            playerNode = contactInfo.nodeB_;
            platformNode = contactInfo.nodeA_;
        }

        float platformTop = platformNode->GetPosition().y_ + platformNode->GetComponent<CollisionBox2D>()->GetSize().y_ / 2  - b2_linearSlop;
        float playerBottom = playerNode->GetPosition().y_ - playerNode->GetComponent<CollisionCircle2D>()->GetRadius();

        if (playerBottom < platformTop)
            contact->SetEnabled(false);
    }
}
```

Game.cpp
```
class Game : public Application
{
    URHO3D_OBJECT(Game, Application);
    ...
    Game(Context* context) : Application(context)
    {
        MyPhysicsWorld2D::RegisterObject(context);
    }

    void CreateScene()
    {
        scene_ = new Scene(context_);
        scene_->CreateComponent<Octree>();
        scene_->CreateComponent<DebugRenderer>();
        scene_->CreateComponent<MyPhysicsWorld2D>();
        ...
    }
```

-------------------------

