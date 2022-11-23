nergal | 2017-09-16 14:09:33 UTC | #1

My C++ is a bit rusty, so I guess this could be solved by inheritance. I have a class that inherit LogicComponent. This class has a method called "Hit". The object created by my class is then "hit" by a Raycast that has the result in result->drawable_. This object is a private member of my class. 

What's the best way to handle the scenario: result->drawable_->Hit(..); ?

The class pseudo-looks like this:
    class MyClass: public LogicComponent
    {
       public:
             Hit();
       private:
             StaticModel* object;
             CollisionShape* shape;
             RigidBody* body;
    };

Edit #1: I believe I've got this LogicComponent a bit wrong. Guess I should somehow register my class as a component to the engine?

Edit #2: So I've tried to understand the LogicComponent structure but I'm not sure how to use it in my case.

My class is like the above but called Chunk, the Chunk class creates my TriangleMesh model and includes the Node/StaticModel/ etc. But I would like to have my Chunk class as a LogicComponent so that I can get my chunk->Update() function automatically called. Not sure if this is a good idea?

Perhaps this is the way to go?

World->nodes[i] = new Node->CreateComponent<Chunk>();
nodes[i]->GetComponent<Chunk>->Init(positionVector3, some_attrs);

-------------------------

ppsychrite | 2017-09-16 14:54:23 UTC | #2

Yeah your LogicComponent class is a bit off.
Here's a simple example on one being made and used :grin:
https://github.com/urho3d/Urho3D/tree/master/Source/Samples/05_AnimatingScene

-------------------------

nergal | 2017-09-16 14:54:16 UTC | #3

Hehe, thanks! I think I got it now, will have to test it a bit :slight_smile:

-------------------------

Modanung | 2017-09-16 16:50:57 UTC | #4

If you happen to be using QtCreator you might be interested in [these wizards](https://github.com/LucKeyProductions/QtCreatorUrho3DWizards).

-------------------------

nergal | 2017-09-16 16:57:29 UTC | #5

I solved it a bit unconventional perhaps. But I create my node, add my class and save a pointer to the node itself in my class. So that the class itself can add rigidbody/trianglemesh to the node.

This way I can build my mesh in the chunk class and still be able to register for Update events etc. This also makes it work in my Raycasting since I can get result->drawable_->GetNode()->GetComponent<Chunk>();

But one thing though. I don't receive CollisionEvents for node collisions?

In Start() I subscribe to the event: 
SubscribeToEvent(GetNode(), E_NODECOLLISION, URHO3D_HANDLER(Chunk, HandleNodeCollision));

For the function:
void Chunk::HandleNodeCollision(StringHash eventType, VariantMap& eventData)

But I never receive any node collision events? The other events such as Update(), Start() etc are called correctly.

-------------------------

ppsychrite | 2017-09-16 17:07:18 UTC | #6

Are you sure it isn't calling correctly? (Maybe adding a breakpoint or log it when it's called) 

From what you're saying it should work fine unless you don't have the CollisionShape or RigidBody components created.

-------------------------

nergal | 2017-09-16 17:10:37 UTC | #7

haha I found the issue!
        body->SetCollisionEventMode(COLLISION_NEVER);

I added  that to my creation code several days ago since then I thought I didn't needed any events :stuck_out_tongue:

Thanks for helping out!

-------------------------

