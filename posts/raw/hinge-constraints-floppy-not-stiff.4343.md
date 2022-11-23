mechsect | 2018-06-21 14:27:14 UTC | #1

Hello all... first post here.

I am trying to build a legged creature using constraints to set angles between leg segments. This works but the results are kind of floppy in the physics simulation. I am trying to have stiff leg joints set at exactly the angle I set the hinge too.

Any help would be most appreciated.

Here's code for a leg segment:

```

Node* Hexapod::
CreateSegment( Node*         aParentSegNode,
               const Vector3 aParentConstraintOffset,
               double        aRotFromParent,
               const String& aName,
               double        aLen,
               const Vector3 aAxis,
               double        aAngle )
        {
        auto ballRestitution = 0.75f;
        auto NewSegNode = aParentSegNode->CreateChild(aName);
        NewSegNode->SetName(aName);
        //NewSegNode->Roll(180.0);
        //NewSegNode->SetPosition( Vector3(0.5 * aLen, 0.0f, 0.f));
        Vector3 xoffs;
        if( aParentConstraintOffset.x_ > 0.0 )
            xoffs = Vector3(aLen / 2.0, 0, 0);
        else
            {
            xoffs = Vector3(-aLen / 2.0, 0, 0);
            }

        NewSegNode->SetPosition( aParentConstraintOffset + xoffs);
        NewSegNode->SetRotation(Quaternion(0., aRotFromParent, 0.));

        auto shape = NewSegNode->CreateComponent<CollisionShape>();
        // set the collision shape slightly smaller than the bone so ends don't collide.
        shape->SetBox(Vector3( 0.9 * aLen, .1, .3));

        auto body = NewSegNode->CreateComponent<RigidBody>();
        // Gravity override
        body->SetGravityOverride(Vector3(0.0f, -1.0f, 0.0f));
        //body->SetRestitution(ballRestitution);
        body->SetRestitution(0.);      // legs shouldn't bounce
        // Set mass to make movable
        body->SetMass(1.0f);
        body->SetFriction(2.0f);
        // Set damping parameters to smooth out the motion
        body->SetLinearDamping(0.05f);
        body->SetAngularDamping(0.85f);
        // Set rest thresholds to ensure the rigid bodies come to rest to not consume CPU endlessly
        body->SetLinearRestThreshold(1.5f);
        body->SetAngularRestThreshold(2.5f);

        auto* constraint = NewSegNode->CreateComponent<Constraint>();
        constraint->SetConstraintType(CONSTRAINT_HINGE);
        // Most of the constraints will work better when the connected bodies don't collide against each other
        constraint->SetDisableCollision(true);
        // The connected body must be specified before setting the world position
        constraint->SetOtherBody(aParentSegNode->GetComponent<RigidBody>());

        constraint->SetOtherPosition(aParentConstraintOffset);
        constraint->SetPosition(Vector3(-0.5 * aLen,0,0));
        //constraint->SetWorldPosition(aParentSegNode->GetWorldPosition() + aParentConstraintOffset);

        constraint->SetCFM( 0 );
        constraint->SetERP( 0.8 );
        //std::cerr << "CFM *** " << constraint->GetCFM() << " ERP " << constraint->GetERP() << std::endl;

        constraint->SetAxis(aAxis);
        constraint->SetOtherAxis(aAxis);
        constraint->SetHighLimit(Vector2(aAngle,0.f));
        constraint->SetLowLimit(Vector2(aAngle,0.f));

        return NewSegNode;
        }
```

-------------------------

mechsect | 2018-07-16 13:03:08 UTC | #2

Floppy constraints was most solved by doing the following:

```
btHingeConstraint* btConst = (btHingeConstraint*) constraint->GetConstraint();
btConst->setOverrideNumSolverIterations(100);
```
Basically, reach past Urho3D to the underlying Bullet constraint and do more iterations. Not sure if 100 is the right number, but it does make the joints behave as expected.

Also, setting ERP and CRM to 1 and 0 respectively seems right. This is based on:

https://doc.lagout.org/programmation/OpenGL/Learning%20Game%20Physics%20with%20Bullet%20Physics%20and%20OpenGL%20%5BDickinson%202013-10-25%5D.pdf



"CFM is essentially a measure of the strength of the constraint. A value of 0 means a  perfectly rigid constraint, while increasing values make the constraint more spring like, up to a value of 1where it has no effect at all.

ERP represents the fraction of how much joint error will be used in the next simulation step. Many constraints could be working in unison to create a complex interaction (imagine a rope bridge, which can be simulated by a attaching a bunch of  springs connected together) and ERP is used to determine how much of the previous data will affect the calculation of future data. This is a difficult concept to explain in such a short space, but imagine that we have multiple constraints acting on the same object, each forcing the others into breaking their own rules. ERP is then the  priority of this constraint relative to the others, and helps determine who has higher importance during these types of complex constraint scenarios."

-------------------------

