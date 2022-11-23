tni711 | 2018-08-26 20:52:30 UTC | #1

I am working on my first Urho3D game using the Character Demo as the starting point.
I have the basic scene setup and some logic to shoot some table tennis balls to the table tennis table surface. The problem is, some balls just get stuck on the tables, some balls can bounce over to the other side of the table and some just pass through the table surface and drop tot he floor.

It seems like the collision mesh of the table is not setup correctly but I could not figure where is the problem. Any advise here is appreciated. 

Below are the source code for the setup:
```
   // set this one up manually to explore the parameters of these functions
    Node* tableNode = scene_->CreateChild("Table");
    tableNode->SetPosition(Vector3(0.0f, 0.8f, 0.0f));
    tableNode->SetRotation(Quaternion(0.0f, 90.0f, 90.0f));
    tableNode->SetScale(1.0f);

    auto* tableObject = tableNode->CreateComponent<StaticModel>();
    tableObject->SetModel(cache->GetResource<Model>("Models/Table3D.mdl"));
    tableObject->SetMaterial(cache->GetResource<Material>("Materials/Table.xml"));

    auto* tableBody = tableNode->CreateComponent<RigidBody>();
    tableBody->SetMass(10.0f);
    tableBody->SetRestitution(0.6f);
    tableBody->SetKinematic(false);

    auto* tableShape = tableNode->CreateComponent<CollisionShape>();
    tableShape->SetTriangleMesh(tableObject->GetModel(), 0);
```
The function which instantiates the balls and shoot at the table based on the camera direction:
```
void TableTennisDemo::SpawnObject()
{
    auto* cache = GetSubsystem<ResourceCache>();
    Node* boxNode = scene_->CreateChild("Ball");
    boxNode->SetPosition(cameraNode_->GetPosition());
    boxNode->SetRotation(cameraNode_->GetRotation());
    boxNode->SetScale(1.00f);

    auto* boxObject = boxNode->CreateComponent<StaticModel>();
    boxObject->SetModel(cache->GetResource<Model>("Models/ball.mdl"));
    boxObject->SetMaterial(cache->GetResource<Material>("Materials/Ball.xml"));
    boxObject->SetCastShadows(true);

    auto* body = boxNode->CreateComponent<RigidBody>();
    body->SetMass(0.027f);
    body->SetRollingFriction(0.05f);
    body->SetRestitution(0.8f);
    body->SetLinearDamping(0.2f);

    auto* shape = boxNode->CreateComponent<CollisionShape>();
    shape->SetSphere(0.04f);

    const float OBJECT_VELOCITY = 6.0f;

    // Set initial velocity for the RigidBody based on camera forward vector. Add also a slight up component
    // to overcome gravity better
    body->SetLinearVelocity(cameraNode_->GetRotation() * Vector3(0.0f, 0.25f, 1.0f) * OBJECT_VELOCITY);
}
```
A snapshot of the game scene:

![Game%20Scene%20Screenshot|632x500](upload://eX1VPQt6DestIkeQHJ2hnKkGV8N.jpeg)

-------------------------

Modanung | 2018-08-26 21:06:03 UTC | #2

From the [Bullet Physics Manual](http://www.cs.kent.edu/~ruttan/GameEngines/lectures/Bullet_User_Manual.pdf):
> #### Avoid very small and very large collision shapes
> The minimum object size for moving objects is about 0.2 units, 20 centimeters for Earth gravity. If smaller objects or bigger gravity are manipulated, reduce the internal simulation frequency accordingly, using the third argument of btDiscreteDynamicsWorld::stepSimulation. By default it is 60Hz. For instance, simulating a dice throw (1cm wide box with a gravity of 9.8m/s2) requires a frequency of at least 300Hz (1./300.). It is recommended to keep the maximum size of moving objects smaller then about 5 units/meters.

In Urho3D the simulation frequency can be changed using `PhysicsWorld::SetFps(int)`.

Also, did you know you can enable debug rendering of collision shapes? This is done by calling `DrawDebugGeometry(true)` on the `PhysicsWorld` during the `PostRenderUpdate`.

-------------------------

tni711 | 2018-08-27 01:37:35 UTC | #3

[quote="Modanung, post:2, topic:4495"]
60Hz
[/quote]

Thanks a lot! I am aware of the DrawDebugGeometry function but not able to get it to work. Maybe that is the best path to get a better handle of the collision mesh problem. The Bullet Physics manual reference definitely helps. Lets me dig a bit more in it. Thanks again.

-------------------------

Modanung | 2018-08-27 07:41:32 UTC | #4

To draw the debug geometry you'll need to subscribe to the PostRenderUpdate event as such:
```
SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(TableTennisDemo, HandlePostRenderUpdate));
```
The function itself should look something like this:
```
void TableTennisDemo::HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
{
    scene_->GetComponent<PhysicsWorld>()->DrawDebugGeometry(true);
}
```

And you're welcome! :)

-------------------------

QBkGames | 2018-08-27 10:24:10 UTC | #5

I had a similar problem starting with Urho and Bullet physics and I'm also pretty sure it's the size of the objects being too small. I suggest scaling everything up, i.e. making the balls 1m in diameter and scale the table and everything else accordingly.

You could also increase the simulation rate, but if you are aiming for low power devices (mobiles), it could take a toll on performance.

-------------------------

SirNate0 | 2018-08-27 14:44:10 UTC | #6

Another thing that might help is to not use triangle meshes - break the table into components like convex hulls, cubes, cylinders, etc. The triangle meshes aren't actually filled - they behave like rigid shells, but if an object (say the ball) passes through the skin it can get stuck in the table, whereas the other shapes will push the ball out.

-------------------------

tni711 | 2018-08-27 15:05:22 UTC | #7

Thanks for both of your replies! 

I increased the scale of the ball from 1.0f to 2.0f. It resolved the problem.
I also got the debug render working.  

I want to try to set the FPS to a higher rate if it can support the real life scale of table tennis models.
However my program crashes with a core dumped. I tried different value such as 10, 60, 300, 600 with no success yet.

I add the SetFps logic during the CreateScene function as below:
 
void TableTennisDemo::CreateScene()
{
    auto* cache = GetSubsystem<ResourceCache>();
    scene_ = new Scene(context_);
    scene_->CreateComponent<Octree>();
    scene_->CreateComponent<DebugRenderer>();
    scene_->GetComponent<PhysicsWorld>()->SetFps(10);

The work in progress so far:
[https://www.youtube.com/watch?v=YMEBHLqOYH8](https://www.youtube.com/watch?v=YMEBHLqOYH8)

-------------------------

tni711 | 2018-08-27 14:51:03 UTC | #8

[quote="SirNate0, post:6, topic:4495"]
break the table into components like convex hulls, cubes, cylinders, etc. T
[/quote]

Thanks for the advise. I would try that if the SetFPS does not work for me. To break up the model is more effort for me.

-------------------------

guk_alex | 2018-08-27 16:20:44 UTC | #9

You can also use information from node collision for visualising forces that affects the ball.

In the setup function:

        float lineHeightMultiplier = 0.1f; // depends on mass
        int maxLines = 1000; // = physics fps * seconds to display lines
        SubscribeToEvent(ballNode_, E_NODECOLLISION, [=](auto eventType, auto& eventData) {            

            using namespace NodeCollision;

            MemoryBuffer contacts(eventData[P_CONTACTS].GetBuffer());

            while (!contacts.IsEof()) {
                Vector3 contactPosition = contacts.ReadVector3();
                Vector3 contactNormal = contacts.ReadVector3();
                float contactDistance = contacts.ReadFloat();
                float contactImpulse = contacts.ReadFloat();
                
                lines_.push_back({ contactPosition, contactPosition + contactNormal*contactImpulse*lineHeightMultiplier });
                if (lines_.size() > maxLines) // erase old lines
                    lines_.pop_front();
            }

        });

Where `lines_` is:

    struct DebugLines {
        Vector3 from;
        Vector3 to;
    };
    std::deque<DebugLines> lines_;

And add these lines to `HandlePostRenderUpdate`:

    DebugRenderer* debug = scene_->GetComponent<DebugRenderer>();
    for (const auto& it : lines_)
        debug->AddLine(it.from, it.to, Color::BLUE);

Blue lines will show position of impulses and their strength.

-------------------------

tni711 | 2018-08-28 07:11:34 UTC | #10

Hi, thanks for the tips. I implemented the logic you suggested with minor modification to fit in the sample program structure. It actually works! I can see the ball force and impact directions visualized with yellow lines in my setup. It is really cool to have this feature handy to help debugging the game.

1) The collision update handler:
```
void TableTennisDemo::HandleBallCollisionUpdate(StringHash eventType, VariantMap& eventData)
{
  using namespace NodeCollision;

  // subscribe to ball collision node data
  float lineHeightMultiplier = 0.5f; // depends on mass
  int maxLines = 1000; // = physics fps * seconds to display lines

  MemoryBuffer contacts(eventData[P_CONTACTS].GetBuffer());
  while (!contacts.IsEof()) {
    Vector3 contactPosition = contacts.ReadVector3();
    Vector3 contactNormal = contacts.ReadVector3();
    float contactDistance = contacts.ReadFloat();
    float contactImpulse = contacts.ReadFloat();
    lines_.push_back({ contactPosition, contactPosition + contactNormal * contactImpulse * lineHeightMultiplier });
    if (lines_.size() > maxLines) // erase old lines
      lines_.pop_front();
  }
}
```
2) subscribe the event for each ball instantiated
```
SubscribeToEvent(ballNode, E_NODECOLLISION, URHO3D_HANDLER(TableTennisDemo, HandleBallCollisionUpdate));
```
3) Draw the debug geometry
```
void TableTennisDemo::HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
{
    // If draw debug mode is enabled, draw physics debug geometry. Use depth test to make the result easier to interpret
  if (drawDebug_) {
    DebugRenderer* debug = scene_->GetComponent<DebugRenderer>();
    //Blue lines will show position of impulses and their strength.
    for (const auto& it : lines_) {
      debug->AddLine(it.from, it.to, Color::YELLOW);
    }
    scene_->GetComponent<PhysicsWorld>()->DrawDebugGeometry(debug, false);
  }
}
```

-------------------------

