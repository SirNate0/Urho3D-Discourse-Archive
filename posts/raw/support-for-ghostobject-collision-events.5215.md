Leith | 2020-02-17 09:50:05 UTC | #1

Hey guys,
looking for some comments/opinions/criticism on the following:

I've got a character controller which is based on Bullet's btKinematicCharacterController.
Internally, the Bullet class uses a btPairCachingGhostObject to provide the character's outer physics capsule. Unfortunately for me, Urho3D has no wrapper for GhostObjects, and Urho's PhysicsWorld class does not provide collision events where ghost objects are concerned.
It is worth noting that Ghost Objects are NOT the same thing as trigger volumes (which Urho does support). The distinction between them is subtle, but we can definitely say that btPairCachingGhostObject is quite a different animal to btRigidBody.

In order to remedy this, I began by defining some new Urho events:
[code]
URHO3D_EVENT(GHOST_COLLISION_STARTED, OnGhostCollisionBegin){
    URHO3D_PARAM(P_BODY, Body);             /// RigidBody which collided with btGhostObject
    URHO3D_PARAM(P_GHOST, Ghost);           /// btGhostObject which collided with RigidBody
    URHO3D_PARAM(P_GHOSTNODE, GhostNode);   /// Scene node which acts as Parent to btGhostNode
}

URHO3D_EVENT(GHOST_COLLISION_STAY, OnGhostCollisionStay){
    URHO3D_PARAM(P_BODY, Body);
    URHO3D_PARAM(P_GHOST, Ghost);
    URHO3D_PARAM(P_GHOSTNODE, GhostNode);
}

URHO3D_EVENT(GHOST_COLLISION_ENDED, OnGhostCollisionEnded){
    URHO3D_PARAM(P_BODY, Body);
    URHO3D_PARAM(P_GHOST, Ghost);
    URHO3D_PARAM(P_GHOSTNODE, GhostNode);
}
[/code]

You can see I chose not to provide contact information for ghost object collisions, and also I am only handling collisions between ghosts and rigidbodies (not ghosts and other ghosts).

I chose to track my collisions across frames in a simplified fashion:
[code]
HashSet<WeakPtr<RigidBody>> prevCollisions;
HashSet<WeakPtr<RigidBody>> currentCollisions;
[/code]

Finally, here's the code to deal with collision events for a single ghost object.
I chose not to iterate the world collision manifolds, because the ghost object is already keeping track of a list of objects that it (potentially) collides with (since it represents a broadphase list of objects whose AABB are intersecting that of the ghost)...
[code]
/// After physics update, move character root node to suit the physics
/// We also deal with collision detection / event sourcing
void KinematicCharacterController::HandlePostPhysicsUpdate(StringHash eventType, VariantMap& eventData){

    if(ghostObject_){

        currentCollisions.Clear();

        /// Query the current world transform of the ghost object
        btTransform t=ghostObject_->getWorldTransform();

        /// Teleport this character's parent node to suit the physics object
        Vector3 worldPos = ToVector3(t.getOrigin()) + Vector3::DOWN * height_*0.5f;
        node_->SetWorldPosition( worldPos );


        btManifoldArray manifoldArray;

        /// Process all current collision events
        /// (Ask ghost shape for a list of objects that it is potentially "colliding" with)
        ///
        int numObjects = ghostObject_->getNumOverlappingObjects();
        for(int i=0;i<numObjects;i++){


            manifoldArray.clear();

            /// Access the next collision object whose AABB overlaps with that of our ghost shape
            btCollisionObject* obj = ghostObject_->getOverlappingObject(i);

            /// Try to cast the current collision object to bullet rigidbody
            /// If this fails, its not a rigidbody - could be another ghost etc.
            btRigidBody* rb = dynamic_cast<btRigidBody*>(obj);
            if(rb){

                /// Query the physics broadphase for deeper information about the colliding pair
                auto* paircache = node_->GetScene()->GetComponent<PhysicsWorld>()->GetWorld()->getPairCache();
                btBroadphasePair* collisionPair = paircache->findPair(ghostObject_->getBroadphaseHandle(), obj->getBroadphaseHandle());
                if (collisionPair == nullptr)
                    continue;

                /// Query the colliding pair for deeper information about the contact manifold(s)
                if (collisionPair->m_algorithm != nullptr)
                    collisionPair->m_algorithm->getAllContactManifolds(manifoldArray);

                if(manifoldArray.size()==0)
                    continue;

                /// Confirm that the two objects are in contact
                int numContacts=0;
                for(int i=0;i<manifoldArray.size();i++){
                     btPersistentManifold* manifold = manifoldArray[i];
                     numContacts += manifold->getNumContacts();
                }
                if(numContacts==0)
                  continue;

                    /// Cast the bullet rigidbody userpointer to Urho RigidBody
                    /// Dangerous assumption that this can never fail - hope springs eternal!
                    RigidBody* RB = (RigidBody*)rb->getUserPointer();

                    /// Wrap the object pointer
                    WeakPtr<RigidBody> weakRB(RB);

                    VariantMap& newData = GetEventDataMap();

                    /// Determine if this collision is "new", or "persistant"
                    if(!prevCollisions.Contains(weakRB))
                    {
                        /// Send "collision started" event
                        newData[OnGhostCollisionBegin::P_BODY] = RB;
                        newData[OnGhostCollisionBegin::P_GHOST] = ghostObject_;
                        newData[OnGhostCollisionBegin::P_GHOSTNODE] = node_;
                        RB->GetNode()->SendEvent(GHOST_COLLISION_STARTED, newData);
                        URHO3D_LOGINFO( RB->GetNode()->GetName()+" BEGIN!");

                        /// Collect the new collision
                        currentCollisions.Insert(weakRB);

                    }else{
                        /// Send "collision ongoing" event
                        newData[OnGhostCollisionStay::P_BODY] = RB;
                        newData[OnGhostCollisionStay::P_GHOST] = ghostObject_;
                        newData[OnGhostCollisionStay::P_GHOSTNODE] = node_;
                        RB->GetNode()->SendEvent(GHOST_COLLISION_STAY, newData);
                        URHO3D_LOGINFO( RB->GetNode()->GetName()+" STAY!");
                    }


            }
        }

        /// Process any collisions which have ended
        for(auto it=prevCollisions.Begin();it!=prevCollisions.End();it++){

            /// Check that the object has not been destroyed, and that the collision has ceased
            if( (*it)!=nullptr &&  !currentCollisions.Contains(*it))
            {
                VariantMap& newData = GetEventDataMap();
                newData[OnGhostCollisionEnded::P_BODY] = *it;
                newData[OnGhostCollisionEnded::P_GHOST] = ghostObject_;
                newData[OnGhostCollisionEnded::P_GHOSTNODE] = node_;
                (*it)->GetNode()->SendEvent(GHOST_COLLISION_ENDED, newData);
                URHO3D_LOGINFO( (*it)->GetNode()->GetName()+" ENDED!");
            }

        }

        /// Keep track of collisions across frames
        prevCollisions = currentCollisions;
    }

}
[/code]

-------------------------

Lumak | 2019-06-05 16:55:20 UTC | #2

After googling the Bullet's Kinematic Character Controller and issues related with it, what you're proposing will become essential if one needs to know about the kinematic character collision.  And the routines you've written are very close to how the PhysicsWorld::SendCollisionEvents() is written IIRC.

It looks good to me and would like to see a github project of this for people to test, if possible.

-------------------------

Leith | 2019-06-06 05:28:34 UTC | #3

Although the code I've presented could be optimized, I have taken advantage of several logical optimizations: mainly, I've leveraged the fact that we are working with a reduced list of candidate objects, and since my use-case did not require me to gather and send contact information (ie hit points and normals), I didn't have to bother with that stuff.
My use-case also did not require three separate collision events, but I thought it would be astute (as you noticed) to model my solution on Urho's existing one.

This is, nonetheless, a clumsy workaround.
Ideally, I should write a custom component that implements/wraps GhostObject, and adjust my character controller component to expect that sibling component (similar to RigidBody and CollisionShape). I think that would make a far better candidate for any future PR.

[EDIT]
I've just tested the code and it appears to work perfectly.
I've registered the ragdoll bodyparts of my zombie armature (rigidbodies) as "senders" of ghost collision events, and I am receiving the events in a separate controller component. My code uses the rigidbody parent node as the event sender, so that is the sender we should provide per rigidbody when registering to receive these events.

[code]
/// Handle collisions between zombie bodyparts and ghost objects (ie player character's physics hull)
void DynamicCharacter::OnGhostStart(StringHash eventType, VariantMap& eventData){

    using namespace OnGhostCollisionBegin;

    /// Unpack pointer to RigidBody, and query it for its owner node
    RigidBody* rb = static_cast<RigidBody*>(eventData[P_BODY].GetPtr());
    Node* rbnode = rb->GetNode();

    /// Unpack pointer to ghost object
    /// TODO: pass this object using a WeakPtr to guard against object invalidation
    btPairCachingGhostObject* ghost =  static_cast<btPairCachingGhostObject*>(eventData[P_GHOST].GetVoidPtr());
    
    /// Unpack pointer to ghost's owner node
    /// TODO: Tag that owner node with pointer to its character controller!
    Node* gn = static_cast<Node*>(eventData[P_GHOSTNODE].GetPtr());

    /// Now do something useful with this information!
    /// If the zombie is not performing an attack, we'll ignore this collision.
    /// But if the zombie is attacking, we'll make it count!
    ///
    if(okToAttack_==false) // ie zombie is attacking!
    {
        /// Temporarily disable ghost collisions (1.5 seconds) on this zombie character
         ignoreCollisions_ = true;
         ignoreCollisionsTimer_ = 0;

        /// Query ghostnode for its owner character controller        
         
        /// Zombie Deals Damage To Player Character !!

    }

}
[/code]

-------------------------

Leith | 2019-06-06 12:40:59 UTC | #4

Happy to explain this further, because its interesttng how urho eventing works and where we can step in and what implications that has, and I am open to the idea that i may still not quite get it, that i can learn more

-------------------------

Leith | 2019-06-08 04:39:13 UTC | #5

Slightly off-topic:
Really my collision logic, as I am showing it, is stupidly simple - if a zombie is attacking you, and any part of its body touches your hull, then you are damaged - since I have information about the bodyparts involved as well as the state of the characters involved, I can certainly make more informed decisions about how damage is dealt, but we start with the "basics", being able to detect and respond to certain states in the game in a highly contextualized fashion.
I needed to know more than just, a zombie bumped into me, I needed deeper information about the contact than could be provided by simple collision hulls alone. I may go further and add a full armature to the player character too, and set up a matrix of collision handlers to deal with the extra information in a structured way.

-------------------------

