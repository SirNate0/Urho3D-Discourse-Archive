Enhex | 2017-01-02 01:07:44 UTC | #1

Hopefully I'm not doing something wrong, but what I noticed is that NodeCollision event only fires once for each node, even if it collides with more than 1 other node.

In my case I'm shooting a projectile which is a trigger body.
On NodeCollision if the other node is the shooter of the projectile the collision is skipped, so collision with the shooter is avoided.
I noticed that if the player shoots a projectile straight down, it won't collide with the floor until it's no longer in contact with the player.
That causes bugs for example with explosive projectiles that need to make sure they have line of sight with damageable objects because it will penetrate into the ground.

Right now my workaround is doing GetRigidBodies(projectile_body) when colliding with the shooter, to check if there's any collision with other bodies, which is re-testing for collisions.
An elegant solution would be to have all the collisions available, either via multiple NodeCollision events, or an event that lists all the nodes.
The most elegant solution is to completely ignore collision between the shooter and the projectile (layers aren't suitable because there could be many different shooters & projectiles).

-------------------------

cadaver | 2017-01-02 01:07:44 UTC | #2

Collision pairs should be treated as separate, so this sounds like a logic bug in PhysicsWorld::SendCollisionEvents(). I recommend stepping through it and seeing if it early-outs in a wrong place. Alternatively, Bullet is just being stupid.

-------------------------

Enhex | 2017-01-02 01:07:45 UTC | #3

I didn't debug because I'm using Urho as external library.
Looking at PhysicsWorld::SendCollisionEvents() it seems like it should work fine - creating unique pairs and only skipping if the nodes/bodies are removed.

I looked at Bullet's wiki and found this:
[bulletphysics.org/mediawiki-1.5. ... nformation](http://bulletphysics.org/mediawiki-1.5.8/index.php/Collision_Callbacks_and_Triggers#Contact_Information)
"The best way to determine if collisions happened between existing objects in the world, is to iterate over all contact manifolds. This should be done during a simulation tick (substep) callback, because contacts might be added and removed during several substeps of a single stepSimulation call."

PhysicsWorld::SendCollisionEvents() is called in the PostStep(), so maybe the collision gets removed in the substeps?
A possible solution could be to populate the pairs hashmap in the substeps, and send the events in the PostStep().

Though a simple test case is required to verify that missing substep contacts is real.

-------------------------

cadaver | 2017-01-02 01:07:45 UTC | #4

PostStep is called for each substep.

-------------------------

cadaver | 2017-01-02 01:07:45 UTC | #5

I'm not able to replicate your problem in CharacterDemo. I make the character drop "bullets" and log the collided nodes in the bullet script's FixedPostUpdate.

This was inserted to somewhere in the camera/controls per-frame code:

[code]
        if (input.mouseButtonPress[MOUSEB_LEFT])
            SpawnObject();
[/code]

And the new code:

[code]
void SpawnObject()
{
    Node@ boxNode = scene_.CreateChild("SmallBox");
    boxNode.position = characterNode.position + Vector3(0,1,0);
    boxNode.rotation = characterNode.rotation;
    boxNode.SetScale(0.25f);
    StaticModel@ boxObject = boxNode.CreateComponent("StaticModel");
    boxObject.model = cache.GetResource("Model", "Models/Box.mdl");
    boxObject.material = cache.GetResource("Material", "Materials/StoneEnvMapSmall.xml");
    boxObject.castShadows = true;

    RigidBody@ body = boxNode.CreateComponent("RigidBody");
    body.mass = 0.25f;
    body.friction = 0.75f;
    body.trigger = true;
    CollisionShape@ shape = boxNode.CreateComponent("CollisionShape");
    shape.SetBox(Vector3(1.0f, 1.0f, 1.0f));

    boxNode.CreateScriptObject(scriptFile, "Bullet");
}

class Bullet : ScriptObject
{
    Array<String> collidingObjects;

    void Start()
    {
        SubscribeToEvent(node, "NodeCollision", "HandleNodeCollision");
    }

    void HandleNodeCollision(StringHash type, VariantMap& data)
    {
        Node@ otherNode = data["OtherNode"].GetPtr();
        collidingObjects.Push(otherNode.name);
    }

    void FixedUpdate(float dt)
    {
        collidingObjects.Clear();
    }

    void FixedPostUpdate(float dt)
    {
        if (collidingObjects.length > 0)
        {
            String objectNames;
            for (uint i = 0; i < collidingObjects.length; ++i)
                objectNames += collidingObjects[i] + " ";
            Print("Collisions " + collidingObjects.length + ": " + objectNames);
        }
    }
}
[/code]

The log output would look like expected, when the bullet intersects momentarily both the Jack and the floor:

[code]
Collisions 1: Jack 
Collisions 1: Jack 
Collisions 1: Jack 
Collisions 1: Jack 
Collisions 2: Jack Floor 
Collisions 2: Jack Floor 
Collisions 2: Jack Floor 
Collisions 2: Jack Floor 
Collisions 1: Floor 
Collisions 1: Floor 
Collisions 1: Floor
[/code]

-------------------------

Enhex | 2017-01-02 01:07:45 UTC | #6

I replicated your test and it works fine.
When I was tweaking to fix it I did add both "body.collisionEventMode = COLLISION_ALWAYS;", use CCD, and check line of sight to center of mass instead of node position (which in my case is the very bottom of the body, which caused problems).
maybe one of them fixed it.

My bad.

-------------------------

