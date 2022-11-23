Pihozamo | 2017-03-18 02:09:32 UTC | #1

[Edit] Solution: Use a custom LogicComponent instead.

> weitjong:

> The Node class is not designed to be subclass by user. See also the discussion in http://discourse.urho3d.io/t/alternatives-to-node-subclassing/230612.

Hello folks,

I have this problem when I add a Sprite2D to a StaticSprite2D component created from a custom class that extends Urho3D::Node. I'm using VS 2015 with Urho 1.6. This is my custom class:

NodeExt.h :

    #pragma once
    #include "stdafx.h"

    using namespace Urho3D;

    class NodeExt : public Node
    {
    	URHO3D_OBJECT(NodeExt, Node);

    public:
    	NodeExt(Context* context);
    	virtual ~NodeExt();
    };


NodeExt.cpp

    #include "NodeExt.h"


    NodeExt::NodeExt(Context* context) : Node(context)
    {
    	RigidBody2D* body = CreateComponent<RigidBody2D>();
    	body->SetBodyType(BT_DYNAMIC);
    	body->SetGravityScale(0);

    	CollisionBox2D* box = CreateComponent<CollisionBox2D>();
    	box->SetSize(Vector2(0.32f, 0.32f));
    	box->SetDensity(1.0f);
    	box->SetFriction(0.5f);
    	box->SetRestitution(0.1f);

    	ResourceCache* cache = GetSubsystem<ResourceCache>();
    	StaticSprite2D* staticSprite = CreateComponent<StaticSprite2D>();
    	staticSprite->SetSprite(cache->GetResource<Sprite2D>("Images/ship.png")); // This is where the error happens
    }


    NodeExt::~NodeExt()
    {
    }


And the error:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/14bbb8b1a1155ecf296b41a95ab0276da9d9ad2e.png'>


Now, if I comment the line where the SetSprite happens, everything proceeds as usual. And if I use a Urho3D::Node instead my custom class, using the same code, no error happens. 

Is there something missing that I should include in my custom class to successfully extend Urho3D::Node?

-------------------------

weitjong | 2017-01-27 11:30:51 UTC | #2

The Node class is not designed to be subclass by user. See also the discussion in http://discourse.urho3d.io/t/alternatives-to-node-subclassing/2306.

-------------------------

Pihozamo | 2017-01-26 15:49:35 UTC | #3

Oh I see, thanks for your answer.

Should I mark this as solved? I know it technically didn't get solved but it seems like it's not possible.

-------------------------

