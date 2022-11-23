cirosantilli | 2017-12-13 10:44:32 UTC | #1

This is a copy of https://discourse.urho3d.io/t/why-dont-2d-bodies-with-a-constraintprismatic2d-collide-in-urho3d-despite-setcollideconnected-true-ask-question/3840 with everything inlined here to remove any political references.

For other types of constraints, e.g. `ConstraintRope2D`, `SetCollideConnected(true)` has the expected effect.

However, for `ConstraintPrismatic2D`, I can't make the bodies collide when the constraint is applied.

To test this out, take 5e8a2756db27ff88098cab351822c6f2f1ed9ea9 and hack the sample `Source/Samples/32_Urho2DConstraints/Urho2DConstraints.cpp` so that the prismatic constraint allows both bodies to touch:

    // Create a ConstraintPrismatic2D
    CreateFlag("ConstraintPrismatic2D", 2.53f, 3.0f); // Display Text3D flag
    Node* boxPrismaticNode = box->Clone();
    tempBody = boxPrismaticNode->GetComponent<RigidBody2D>(); // Get body to make it static
    tempBody->SetBodyType(BT_STATIC);
    Node* ballPrismaticNode = ball->Clone();
    boxPrismaticNode->SetPosition(Vector3(3.3f, 2.5f, 0.0f));
    ballPrismaticNode->SetPosition(Vector3(3.3f, 2.0f, 0.0f));

    ConstraintPrismatic2D* constraintPrismatic = boxPrismaticNode->CreateComponent<ConstraintPrismatic2D>();
    constraintPrismatic->SetOtherBody(ballPrismaticNode->GetComponent<RigidBody2D>()); // Constrain ball to box
    constraintPrismatic->SetAxis(Vector2(0.0f, 1.0f)); // Slide from [0,0] to [1,1]
    constraintPrismatic->SetAnchor(Vector2(3.3f, 2.5f));
    constraintPrismatic->SetLowerTranslation(-1.0f);
    constraintPrismatic->SetUpperTranslation(0.5f);
    constraintPrismatic->SetEnableLimit(true);
    constraintPrismatic->SetMaxMotorForce(1.0f);
    constraintPrismatic->SetMotorSpeed(0.0f);
    constraintPrismatic->SetCollideConnected(true);

Now, the anchor and dynamic bodies can be superposed with the mouse, and they don't collide despite `constraintPrismatic->SetCollideConnected(true);`.

I have also uploaded a minimalistic test on GitHub: https://github.com/cirosantilli/Urho3D-cheat/blob/e6cc904660fcf89ec558415d7da1f191f38b42f1/prismatic_collide_connected.cpp

Collision works as expected for `ConstraintRope2D`, which has `SetCollideConnected(true);` set by default, in the same example if you move the bodies with the mouse.

If I test the same thing on the Box2D testbed, by hacking the `Prismatic.h` testbed example at f655c603ba9d83f07fc566d38d2654ba35739102
 slightly to contain:

    #ifndef PRISMATIC_H
    #define PRISMATIC_H
    
    // The motor in this test gets smoother with higher velocity iterations.
    class Prismatic : public Test
    {
    public:
    	Prismatic()
    	{
    		b2Body* ground = NULL;
    		{
    			b2BodyDef bd;
    			ground = m_world->CreateBody(&bd);
    
    			b2EdgeShape shape;
    			shape.Set(b2Vec2(-40.0f, 0.0f), b2Vec2(40.0f, 0.0f));
    			ground->CreateFixture(&shape, 0.0f);
    		}
    
    		{
    			b2PolygonShape shape;
    			shape.SetAsBox(1.0f, 1.0f);
    
    			b2BodyDef bd;
    			bd.type = b2_dynamicBody;
    			bd.position.Set(0.0f, 0.0f);
    			bd.angle = b2_pi;
    			bd.allowSleep = false;
    			b2Body* body = m_world->CreateBody(&bd);
    			body->CreateFixture(&shape, 5.0f);
    
    			b2PrismaticJointDef pjd;
    
    			// Bouncy limit
    			b2Vec2 axis(0.0f, 1.0f);
    			axis.Normalize();
    			pjd.Initialize(ground, body, b2Vec2(0.0f, 0.0f), axis);
    
    			// Non-bouncy limit
    			//pjd.Initialize(ground, body, b2Vec2(-10.0f, 10.0f), b2Vec2(1.0f, 0.0f));
    
    			pjd.motorSpeed = 10.0f;
    			pjd.maxMotorForce = 10000.0f;
    			pjd.enableMotor = true;
    			pjd.lowerTranslation = -20.0f;
    			pjd.upperTranslation = 20.0f;
    			pjd.enableLimit = true;
    			pjd.collideConnected = true;
    
    			m_joint = (b2PrismaticJoint*)m_world->CreateJoint(&pjd);
    		}
    	}
    
    	void Keyboard(int key)
    	{
    		switch (key)
    		{
    		case GLFW_KEY_L:
    			m_joint->EnableLimit(!m_joint->IsLimitEnabled());
    			break;
    
    		case GLFW_KEY_M:
    			m_joint->EnableMotor(!m_joint->IsMotorEnabled());
    			break;
    
    		case GLFW_KEY_S:
    			m_joint->SetMotorSpeed(-m_joint->GetMotorSpeed());
    			break;
    		}
    	}
    
    	void Step(Settings* settings)
    	{
    		Test::Step(settings);
    		g_debugDraw.DrawString(5, m_textLine, "Keys: (l) limits, (m) motors, (s) speed");
    		m_textLine += DRAW_STRING_NEW_LINE;
    		float32 force = m_joint->GetMotorForce(settings->hz);
    		g_debugDraw.DrawString(5, m_textLine, "Motor Force = %4.0f", (float) force);
    		m_textLine += DRAW_STRING_NEW_LINE;
    	}
    
    	static Test* Create()
    	{
    		return new Prismatic;
    	}
    
    	b2PrismaticJoint* m_joint;
    };
    
    #endif

then those bodies do obey `pjd.collideConnected = true;` as expected.

-------------------------

