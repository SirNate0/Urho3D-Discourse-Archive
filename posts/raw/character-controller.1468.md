JamesK89 | 2017-01-02 01:07:55 UTC | #1

The character demo is nice and all but as most of us may know dynamic force based character controllers are highly unpredictable and don't feel natural unless that is what you are going for.

That being said I'm just wondering if anyone has come up with a kinematic character controller that uses custom movement and collision logic for that traditional FPS feel and control (? la Quake, Half-Life, Unreal, etc..)?

I've been tinkering with Urho3D seeing if I can come up with something using ConvexCast but I am inexperienced with the library thus far so if someone has already written something and wants to share I'd appreciate it.

-------------------------

Enhex | 2017-01-02 01:07:56 UTC | #2

[quote="JamesK89"]The character demo is nice and all but as most of us may know dynamic force based character controllers are highly unpredictable and don't feel natural unless that is what you are going for.

That being said I'm just wondering if anyone has come up with a kinematic character controller that uses custom movement and collision logic for that traditional FPS feel and control (? la Quake, Half-Life, Unreal, etc..)?

I've been tinkering with Urho3D seeing if I can come up with something using ConvexCast but I am inexperienced with the library thus far so if someone has already written something and wants to share I'd appreciate it.[/quote]

The problem with dynamic controllers is that you can't implement advanced features for them like stair stepping.
Other than that you can make them control and move just like quake/hl ones. (I did myself)

I'm working on a hybrid controller now - rigid body with kinematic movement to let the physics engine handle pushing and getting pushed by stuff.
Stair stepping is difficult to implement in Bullet Physics because Bullet relies on collision margins(tons of features break without it, including sweeps & raycasts), and they make everything round.
So combining features like auto stair stepping with maximum walkable ground slope angle creates a problem: if you step on a rounded corner (which all stairs will be) you'll get a steep slope and the traditional quake-style stepping doesn't handle such a thing, so you'll bump into the stair and perhaps some other undesired behaviors.

I'm almost done solving all the problems with my controller, so it should be possible to handle the roundness from the collision margins.

Other than that the quake games and doom 3 are open source on github and u can try to see what they do.
Valve's Source SDK is also open source on Github.

Oh an last time I checked the bullet kinematic char controller demo wasn't good and it had flawed manual recovery from penetration algorithm.
I made a post asking for a better method on the Bullet forums and got a good answer: [bulletphysics.org/Bullet/php ... =9&t=10843](http://www.bulletphysics.org/Bullet/phpBB3/viewtopic.php?f=9&t=10843)

-------------------------

JamesK89 | 2017-01-02 01:07:56 UTC | #3

It's been while since I looked at the SDK code but if I'm not mistaken Valve's character controller in Half-Life basically does manual collision detection against the world with a kinematic body attached for interaction with dynamic objects. I'm thinking it may be the only way to get the best of both worlds if Bullet is that terrible at this.

-------------------------

Enhex | 2017-05-31 17:53:15 UTC | #4

[quote="JamesK89"]It's been while since I looked at the SDK code but if I'm not mistaken Valve's character controller in Half-Life basically does manual collision detection against the world with a kinematic body attached for interaction with dynamic objects. I'm thinking it may be the only way to get the best of both worlds if Bullet is that terrible at this.[/quote]

Not sure what you mean by "at this" but using a kinematic body won't change any of the problems I mentioned.
The kinematic control can be the same with no problem, and so is interaction with dynamic objects. The problem is that everything is round.
In case you don't know what collision margins are or how they behave, you have to watch this video because it's very important for working with Bullet:
https://www.youtube.com/watch?v=BGAwRKPlpCw

-------------------------

JamesK89 | 2017-01-02 01:07:56 UTC | #5

[quote="Enhex"]using a kinematic body won't change any of the problems I mentioned.[/quote]

What I meant was doing the majority of collision detections yourself [i]outside[/i] of Bullet but using either a kinematic body that shadows your player object to interact with dynamic objects or otherwise applying forces upon collision with dynamic objects yourself.

As much work as it is that seems to be the best way to get the best of both worlds and it seems to be what Valve has done.
Of course every project has its own requirements so I imagine such an approach would be overblown in some cases.

-------------------------

Dave82 | 2017-01-02 01:07:56 UTC | #6

[quote="JamesK89"]The character demo is nice and all but as most of us may know dynamic force based character controllers are highly unpredictable and don't feel natural unless that is what you are going for.

That being said I'm just wondering if anyone has come up with a kinematic character controller that uses custom movement and collision logic for that traditional FPS feel and control (? la Quake, Half-Life, Unreal, etc..)?

I've been tinkering with Urho3D seeing if I can come up with something using ConvexCast but I am inexperienced with the library thus far so if someone has already written something and wants to share I'd appreciate it.[/quote]

Hi James ! I saw your private message so i decided to write here so other might find it useful too.

Kinematic Controller : It's a bad idea , since the interaction withe the physics world won't work properly and you will need workarounds which is a bad thing i think.
ConvexCast : Thats a bad idea either beacuse this way the character controller tries to solve collision detection externally , and you will need hell of a lot work to get things working (manual force calculations , contact manual manifold sorting etc) and still you will have problems.

Here's how i did it in Infested :

I modified Urho's existing character controller :

1. Set Friction to 0.0f ! This will disable the ice-skate simulator :smiley: 
[code]characterBody->SetFriction(0.0f);[/code]

2.You need to modify the MOVE_FORCE , JUMP_FORCE etc variables to your game world and character size (this will take some time to have good results and sync the movement with walk and run animations)

3.The meat and potato.I rewrote the onGround_ check. Urho uses simple intersection test (handled in HandleNodeCollision) i handle it in FixedUpdate like this :

[code]void INFCharacterController::FixedUpdate(float timeStep)
{
       
      // Reset grounded and falling flag for next frame
      onGround_ = false;
      falling = false;
     
      Vector3 planeVelocity(velocity.x_, 0.0f, velocity.z_);
      Vector3 brakeForce = -planeVelocity * BRAKE_FORCE;

      if (controls_.IsDown(CTRL_FORWARD)) moveDir -= Vector3::FORWARD;
      if (controls_.IsDown(CTRL_BACK)) moveDir -= Vector3::BACK * 2.0f;
      if (controls_.IsDown(CTRL_LEFT)) moveDir -= Vector3::LEFT;
      if (controls_.IsDown(CTRL_RIGHT)) moveDir -= Vector3::RIGHT;
    
      // Normalize move vector so that diagonal strafing is not faster
      if (moveDir.LengthSquared() > 0.0f) moveDir.Normalize();

      Urho3D::Vector3 inairMoveForce = rot * moveDir * INAIR_MOVE_FORCE;  // if the player jumps or falling this extra force is applied to allow slight movement
      
      // Temporarily set collision flag to 0 to avoid self collisiojn check
      unsigned int flag = body->GetCollisionMask();
      body->SetCollisionMask(0);

     // raycast from the center of the player downwards and see if we hit something in certain distance
     Urho3D::PhysicsRaycastResult prr;
    
     pw->SphereCast(prr,Urho3D::Ray(characterCenter , Urho3D::Vector3(0,-1,0)),radius , 1000.0f); 
     
     if (prr.distance_ <= distTreshold)
     {
          // this means we are hitting the floor now set the onGround and fall flag to 
          onGround_ = true;
          falling = false;
       
          inairMoveForce = Urho3D::Vector3::ZERO; // if we are moving no inair force
          if (!jumping) moveForce = rot * moveDir * (controls_.IsDown(CTRL_BACK) ? MOVE_FORCE * 0.5f : MOVE_FORCE); // Moving slower backwards...
    
    }
   else
   {
          onGround_ = false;
          falling = true;
    }
    
   // Reset collision flag back :
   body->SetCollisionMask(flag);
   
   
   // This is part of the jump code : If we are in jump mode we start counting and reset our "jumping" flag to false only if some time passed and linear velocity is smaller thatn 0 (e.g the character is falling !)
   if (jumping)
   {
        jumpTimer += timeStep;
        if (jumpTimer >= 0.5f && body->GetLinearVelocity().y_ <= 0.0f)
        {
	jumping = false;
	jumpTimer = 0.0f;
        }
   }
      // and finally apply the necessary forces calculated this frame : (the scaleForce is a normalized value and is used to slow down or speed up the player.
     // For an example : if the player walks in water the scaleForce changes. The deeper that water is the smaller the scaleForce value is...

     body->ApplyImpulse(moveForce * scaleForce);   // The general move force
     body->ApplyImpulse(inairMoveForce); // Move force applied if the player is jumping (its 0 if not jumping)
     body->ApplyImpulse(brakeForce);  // and apply some brake force to avoid the character to accelerate to infinity.
}[/code]

So in nuthshell : Check wether the player stands or floor or not by doing a raycast from the center of the player downwards.If yes simply apply move force if not , apply inair move force.
When doing SphereCast you have 3 variables to set up properly the : characterCenter (the center of your shape) the radius and distTreshold.
1 the center of the character is given in world space. (bodyWorldPos.y_ += characterHeight / 2);
2 . radius is a bit smaller than your capsule's radius (eg if capsule radius is 10 then radius is 9 or 8)
3. distTreshold is the distance that shows what is smallest distance where the player is considered to standing on floor.This is usually a bit bigger number than your capsule's half height.
    if the half height of your character is 15 this value should be 18 (you can calculate it simply distTreshold = capsuleHalgHeight * 1.2f);



4. jumping : Is done simply by checking if the player already jumping ? if not apply jumpForce , or do nothing

[code]void INFCharacterController::jump()
{
    if (!jumping && onGround_)
    {
	jumping = true;
	RigidBody* body = GetComponent<RigidBody>();
	float n = -(body->GetLinearVelocity().y_ * 0.5f);
	body->ApplyImpulse(Vector3::UP * (jumpForce + n));
    }
}[/code]

Also there is a bit of trick that should be mentioned : you have to take into account the current linear velocity when apply jumping , because the jump height while going downhill or uphill will be different due to physisc engine (To achieve the same jump height bigger force is needed when the character is going downwards and smaller if going upwards. Use the current linear velocity to calculate te required force).
 

PS : There's a lot of variables you have to tweak to have good result the forces , timers , dimensions , mass , etc. But i suggest to have one unique scalar variable that can change everything.
calculate everything for characterScale = 1.0f; if your set thin value to 2.0f everything will  be recalculated (forces masses sizes etc).So you don't need additional code to handle different size enemies/players.

Stairs and slopes... the Phiscs Engines' worst enemies :smiley: So instead of writing some code to handle these situations i suggest to use some hidden helper meshes as i did
Wrong Geometry : you have to plan your levels wisely ! No matter how professional  your character controller is , if the level geometry is wrong it will stuck in walls , narrow streets , invalid polygons etc.

Don't hesitate to ask if you need further help
Regards

-------------------------

Enhex | 2017-01-02 01:07:57 UTC | #7

[quote="JamesK89"]
What I meant was doing the majority of collision detections yourself [i]outside[/i] of Bullet but using either a kinematic body that shadows your player object to interact with dynamic objects or otherwise applying forces upon collision with dynamic objects yourself.[/quote]

I know, and I'm telling you it won't change anything because you'll still be colliding with collision margins, unless you plan to write your own physics engine.


[quote="Dave82"]
Kinematic Controller : It's a bad idea , since the interaction withe the physics world won't work properly and you will need workarounds which is a bad thing i think.
ConvexCast : Thats a bad idea either beacuse this way the character controller tries to solve collision detection externally , and you will need hell of a lot work to get things working (manual force calculations , contact manual manifold sorting etc) and still you will have problems.
[/quote]
That's bad advice. JamesK89 mentioned he wants something like quake-based controllers and those have auto stair stepping.
Just moving around a rigid body is trivial, but to implement something that can step over stairs is impossible using a rigid body because:
[img]http://i.imgur.com/Ja8IoDL.png[/img]
Note that Bullet can't add time on individual bodies so you can't split up the movement.
The only way to achieve that is with sweeps (AKA convextCasts in urho).
The common "workaround" is using capsule shapes, but you'll still have a bump that will kill the player's velocity, it's far inferior solution.

Note that an alternative path is to make sure you don't have stairs in your game, usually by using ramps - either visible, or invisible over stairs.
With this limitation a simple character controller will be enough.

-------------------------

Zaroio | 2017-01-02 01:07:58 UTC | #8

To cimb a stair user a Kinematic Body and and a leg (raycast downward). Use a Kinematic Body, it will give you more controll


[img]http://s2.postimg.org/cfwiq8fdl/lol.png[/img]

-------------------------

Dave82 | 2017-01-02 01:07:58 UTC | #9

[quote]That's bad advice. JamesK89 mentioned he wants something like quake-based controllers and those have auto stair stepping.[/quote]

As i mentioned i used invisible helper meshes in my game for stairs.I found this approach a lot easier than adding extra calculations which need lots of testing and tweaking. But adding some extra polys in a level editor is a lot faster and easier.You can even add invisible walls to forbid movement on a steep terrain etc Rigid bodies give far the best result as character controller.

1. A lot easier to implement (i wrote my own 3d and 2d collsion detection and response library including quad/octrees , swept volumes (rectangle , circle/box sphere) and sliding vector calculation for practicing and learning purposes and it was a pain in the ass , and still missed some features and had some issues.It was really great and most of my linear algebra knowledge comes from these books and practicing , but i rather stick with a out of a box solution if a want to write a game)
2. Automatic interaction with dynamic world (Using kinematic controllers you need extra steps to push crates or be pushed by elevators etc)
3. Utomatic  velocity calculation (with kinematic controllers you need extra step for that , e.g : character jumps and hit the ceiling with his head , bullet will automatically calculate the necessary "reversed" velocity)

It's up to James what he trying to do.If he want to learn how collision detection and response and character controllers work , then he can use kinematic bodies or convex cast , but if his plans are to write a game i would stick with built in features. (personal opinion)

I implemented a rigid body character controller in my game and i say you can have a decent (almost kinematic) character controller. I tried both kinematic bodies and swept test , and found both to be lot harder to implement and always had the stucking in walls problem

-------------------------

Enhex | 2017-01-02 01:07:58 UTC | #10

[quote="Zaroio"]To cimb a stair user a Kinematic Body and and a leg (raycast downward). Use a Kinematic Body, it will give you more controll[/quote]


Raycasting will fail to detect ground if the character stands above a gap, or when you don't stand directly above the higher platform. It has to be a sweep test or a ghost object.

-------------------------

JamesK89 | 2017-01-02 01:07:58 UTC | #11

Oh dear what can of worms have I opened?

-------------------------

weitjong | 2017-01-02 01:07:58 UTC | #12

[quote="JamesK89"]Oh dear what can of worms have I opened?[/quote]
No worry. So far, the gentlemen in this thread are well behaved. I will be watching you  :wink:

-------------------------

Bananaft | 2017-01-02 01:07:59 UTC | #13

[quote="Enhex"][quote="Zaroio"]To cimb a stair user a Kinematic Body and and a leg (raycast downward). Use a Kinematic Body, it will give you more controll[/quote]


Raycasting will fail to detect ground if the character stands above a gap, or when you don't stand directly above the higher platform. It has to be a sweep test or a ghost object.[/quote]

Or more raycasts, like Lemma did: [etodd.io/2015/04/03/poor-mans-ch ... ontroller/](http://etodd.io/2015/04/03/poor-mans-character-controller/)

[img]http://etodd.io/assets/SuQjLaQ.png[/img]

-------------------------

Dave82 | 2017-01-02 01:07:59 UTC | #14

I still can't get why is everyone against my sphere cast solution ?  :smiley:

-------------------------

Enhex | 2017-01-02 01:07:59 UTC | #15

[quote="Bananaft"]
Or more raycasts, like Lemma did: [etodd.io/2015/04/03/poor-mans-ch ... ontroller/](http://etodd.io/2015/04/03/poor-mans-character-controller/)

[img]http://etodd.io/assets/SuQjLaQ.png[/img][/quote]

You're just bolting hacks upon hacks.
It will always break when you only have ground where there's no raycasts, and unless you're going to do infinite raycasts it isn't going to cover all cases.
Insisting on not learning more advanced concepts has no advantages, just learn how to use sweep tests or ghost objects (AKA trigger in urho).



[quote="Dave82"]I still can't get why is everyone against my sphere cast solution ?  :smiley:[/quote]
Sphere cast is the same as a sweep test. It's fine when you're using capsule/sphere body because it's a specific shape.

Basically it's adding "leg extra length" at the bottom of the body and staying "step up when something touches the leg at bottom of the body".
You can do the same by using a trigger body and getting the highest contact point.
This method could actually work if you don't have low ceilings (Unless there are more failure cases I didn't think about):
[img]http://i.imgur.com/1BHKj7O.png[/img]

That also means that you can't reuse the body for hit detection, in an shooter game for example, because the rigid body hovers over the ground. So an additional body is required.

Advanced character controllers are difficult! And you ain't gonna top John Carmack's Quake method that easily  :wink: (which isn't general enough to handle Bullet's collision margin roundness which makes it even more difficult)

-------------------------

Enhex | 2017-01-02 01:08:48 UTC | #16

Actually if the leg is a spring, this could work since the body will end up in a crouching position.

-------------------------

Zaroio | 2017-01-02 01:08:48 UTC | #17

[quote="Enhex"]Actually if the leg is a spring, this could work since the body will end up in a crouching position.[/quote]

Yes it does works. I've implemented it on Godot.

-------------------------

JamesK89 | 2017-01-02 01:08:48 UTC | #18

Enhex that is quite a genius idea!

I seem to recall a post-mortem for Call of Juarez where one of the developers described representing the player as a capsule overlapping with a sphere where the sphere would roll around according to player input with its angular velocity set to zero each physics frame.

I thought that article was on Gamasutra but I can't find it there, maybe it was in one of books somewhere.

-------------------------

bvanevery | 2017-01-02 01:08:49 UTC | #19

Do I understand from this that a "mountain goat demo" would be really compelling?  Something that simply walks on uneven procedurally generated surfaces no problemo?  AKA the "stumbling Roman legions in the rough" problem.

-------------------------

JamesK89 | 2017-01-02 01:08:53 UTC | #20

Here is a novel approach from an excerpt in the book, which I highly recommend; Game Coding Complete Third Edition on Page 538:
[url=http://postimg.org/image/fkysr1dm1/][img]http://s4.postimg.org/fkysr1dm1/Excerpt.jpg[/img][/url]


It seems like it would work for a variety of environments. The purposed character hull looks like a [url=https://en.wikipedia.org/wiki/Bacteriophage]Bacteriophage virus[/url] to me.

-------------------------

bvanevery | 2017-01-02 01:08:54 UTC | #21

[quote="JamesK89"]The purposed character hull looks like a [url=https://en.wikipedia.org/wiki/Bacteriophage]Bacteriophage virus[/url] to me.[/quote]

I've considered making more abstract geometric games of entities that are actually such, although I think of pawns in chess, not viruses.  Hey if Minecraft can be ugly and eventually sell to MS for billions, why do we have to make nice human appearances and canned animations?

-------------------------

JamesK89 | 2017-01-02 01:09:07 UTC | #22

I found this article if anyone wants to look at it: [codefreax.org/tutorials/view/id/3](http://codefreax.org/tutorials/view/id/3)
From what I can tell from a preliminary standpoint is that it seems to manually control player movement using a ghost convex shape and performs convex sweep tests against Bullet's collision world.

It's written in Ogre and Bullet but should be adaptable to Urho3D especially given that the same physics engine is used.


On the other hand last evening I was looking at some of the assets from Frictional Games' SOMA in Blender and noticed that objects like stairs have an invisible collision ramp enveloping the stairs and after taking a look at the source code for [url=https://github.com/FrictionalGames]Penumbra and HPL1 Engine[/url] I'm thinking maybe dynamic character controllers are not as bad as they used to be.

-------------------------

Enhex | 2017-01-02 01:09:07 UTC | #23

I implemented convex cast suspension based dynamic controller and it works fine. Though it complicates interactions since the rigidbody doesn't span all the way to the ground so another body is required, and a way to attach it to the controller body without parenting it if u want to detect collision with inactive objects like pickups (fixed constraint may work for it).

-------------------------

thebluefish | 2017-01-02 01:09:08 UTC | #24

It should be easy to make a small component which takes the world transformation for one node and set it to the node that the component is attached to. Then all you need to do is plug a node id in, possibly as an attribute that can be set in the editor, and voila.

-------------------------

Zaroio | 2017-01-02 01:13:03 UTC | #25

[quote="Enhex"]I implemented convex cast suspension based dynamic controller and it works fine. Though it complicates interactions since the rigidbody doesn't span all the way to the ground so another body is required, and a way to attach it to the controller body without parenting it if u want to detect collision with inactive objects like pickups (fixed constraint may work for it).[/quote]


Sorrey for reviving this again...

I've lost my whole hd... realy want to kill myself know  :laughing: 

[code]    btCapsuleShape foot(0.4f, 0.5f);

    PhysicsRaycastResult ray;

    //world->SphereCast(ray, Ray(node_->GetPosition(), Vector3::DOWN), 0.4, 1.0f);

     world->ConvexCast(ray, &foot, node_->GetPosition(), Quaternion::IDENTITY,
                       node_->GetPosition() + Vector3(0, -1.0f, 0), Quaternion::IDENTITY);

    if (ray.body_ && ray.body_ != m_body) {
        Vector3 newPos = node_->GetPosition();
        newPos.y_ = ray.position_.y_ + 1.0f;
        node_->SetPosition(newPos);
        std::cout << ray.distance_ << std::endl;
        ray.body_->SetMass(0);
    }[/code]

After losing my other engine project, I?ve desired to move to Urho3D again. I?ve done the casting and everything seems to work all right. Except that it does some annoying jitter when getting slowly out of an edge. Am i setting it?s position on the right time?

-------------------------

TheComet | 2017-05-31 17:59:19 UTC | #26

I thought I'd dump my camera controller implementation here for people to look at. I've found that managing your own velocities and applying them with body->SetLinearVelocity() gives you a lot more freedom in how you want to control your character, without having to screw around with the physics engine [i]too much[/i]. One thing I'll most likely add is collision feedback from bullet. Currently, the velocity is applied regardless of what you're colliding with, so when interacting with other collision objects you just tear through them with constant force. This makes it impossible to jump on top of other collision objects, for example.

My implementation feels almost identical to Half Life 2 (which is what I was inspired by). When you jump your velocity increases, and I've deliberately made it possible for you to chain jumps to gain more speed (known as "Bunny Hopping").

Sources can be found here:
[url=https://github.com/TheComet93/iceweasel/blob/master/software/game/iceweasel/include/iceweasel/CameraController.h]CameraController.h[/url]
[url=https://github.com/TheComet93/iceweasel/blob/master/software/game/iceweasel/src/CameraController.cpp]CameraController.cpp[/url]

It's still a work in progress, as you can see with all of the TODOs in the code. You can switch between freecam mode and FPS mode by calling CameraController::SetMode().

Video:
https://www.youtube.com/watch?v=y68cd2Su-M8

This is the relevant section of code:
[code]void CameraController::UpdateFPSCameraMovement(float timeStep)
{
    RigidBody* body = moveNode_->GetComponent<RigidBody>();

    // Get input direction vector
    float speed = 8.0f; // TODO read this from an XML config file
    Vector3 targetPlaneVelocity(Vector2::ZERO);
    if(input_->GetKeyDown(KEY_W))     targetPlaneVelocity.z_ += 1;
    if(input_->GetKeyDown(KEY_S))     targetPlaneVelocity.z_ -= 1;
    if(input_->GetKeyDown(KEY_A))     targetPlaneVelocity.x_ += 1;
    if(input_->GetKeyDown(KEY_D))     targetPlaneVelocity.x_ -= 1;
    if(targetPlaneVelocity.x_ != 0 || targetPlaneVelocity.z_ != 0)
        targetPlaneVelocity = targetPlaneVelocity.Normalized() * speed;

    // Rotate input direction by camera angle using a 3D rotation matrix
    targetPlaneVelocity = Matrix3(-Cos(angleY_), 0, Sin(angleY_),
                              0, 1, 0,
                              Sin(angleY_), 0, Cos(angleY_)) * targetPlaneVelocity;

    // Controls the player's Y velocity. The velocity is reset to 0.0f when
    // E_NODECOLLISION occurs and the player is on the ground. Allow the player
    // to jump by pressing space while the velocity is 0.0f.
    if(input_->GetKeyDown(KEY_SPACE) && downVelocity_ == 0.0f)
    {
        downVelocity_ = playerParameters_.jumpForce;
        // Give the player a slight speed boost so he moves faster than usual
        // in the air.
        planeVelocity_ *= playerParameters_.jumpSpeedBoostFactor;
    }

    // TODO limit velocity on slopes?

    // TODO Take upwards velocity into account when bunny hopping (e.g. on ramps)

    // smoothly approach target direction if we're on the ground. Otherwise
    // just maintain whatever plane velocity we had previously.
    float smoothness = 16.0f;
    if(downVelocity_ == 0.0f)
        planeVelocity_ += (targetPlaneVelocity - planeVelocity_) * timeStep * smoothness;

    // Integrate gravity to get Y velocity
    downVelocity_ += physicsWorld_->GetGravity().y_ * timeStep;

    // update camera position
    Vector3 velocity(planeVelocity_.x_, downVelocity_, planeVelocity_.z_);
    body->SetLinearVelocity(velocity);
}

// ----------------------------------------------------------------------------
void CameraController::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
{
    using namespace NodeCollision;
    (void)eventType;
    (void)eventData;

    RigidBody* body = moveNode_->GetComponent<RigidBody>();

    // Temporarily disable collision checks for the player's rigid body, so
    // raycasts don't collide with ourselves.
    unsigned int storeCollisionMask = body->GetCollisionMask();
    body->SetCollisionMask(0);

        // Cast a ray down and check if we're on the ground
        PhysicsRaycastResult result;
        float rayCastLength = playerParameters_.height * 1.05;
        Ray ray(moveNode_->GetWorldPosition(), Vector3::DOWN);
        physicsWorld_->RaycastSingle(result, ray, rayCastLength);
        if(result.distance_ < rayCastLength)
            // Reset player's Y velocity
            downVelocity_ = 0.0f;

    // Restore collision mask
    body->SetCollisionMask(storeCollisionMask);
}[/code]

-------------------------

Zaroio | 2017-01-02 01:13:06 UTC | #27

Thank you very very much my friend.  :smiley:

-------------------------

hdunderscore | 2017-01-02 01:13:07 UTC | #28

In my fps controller experiment, I stuck with the bullet forces method to avoid the extra work of collision detection/response. I started with the character sample and made use of several collision triggers to control different behaviors (like ground detect, drop detect, stand detect), and added some fudge. I added a half-life style crouch-jump (or at least how I remember it). In most cases it behaves well as I've limited extreme responses, but there are some glitches like wall climbing and it doesn't handle stairs well (although ramps are good).

I used a simple trick to smooth out the collisions by separating the character controller physics from the visual model, that way even if there are hiccups, the visual model is always moving fluidly. If you wanted to then do hitboxes, or IK steps, you would do it based on the visual model position rather than the character controller.

Source: [github.com/hdunderscore/Urho3D-FPS-Controller](https://github.com/hdunderscore/Urho3D-FPS-Controller)

-------------------------

Lumak | 2017-05-31 17:55:01 UTC | #29

I don't play FPS games but always wondered why capsule shape rigid body can't be used.
I tested this to see if can be done, and below is the video.
https://youtu.be/OSRAUEXIKBI

-------------------------

Eugene | 2017-01-02 01:15:39 UTC | #30

I know one annoying problem of true-RB character controller that I've seen on Bullet few years ago: nobody promises that rigid body will move with speed that you set.
E.g. try to move RB rapidly over heightmap/trimesh geometry. You may notice that character sometimes don't move smoothly with expected speed because of inaccuracy of physics computation and colliding with ground.

-------------------------

Lumak | 2017-05-31 18:01:28 UTC | #31

Single-shot step up to step heights looked ugly, but what if we can do incremental height stepping.
https://youtu.be/w6PtBgm4uaQ

-------------------------

rasteron | 2017-01-02 01:15:40 UTC | #32

Looking good! :slight_smile:

-------------------------

Lumak | 2017-01-02 01:15:40 UTC | #33

Code to do this is rather simple.

In Character::HandleNodeCollision() func, in the while() loop, I have
[code]
        // relative contact height
        float yOffset = contactPosition.y_ - node_->GetPosition().y_;

        // not the ground
        if ( yOffset > M_EPSILON && yOffset < MAX_STEP_HEIGHT)
        {
            // moving into an object in the direction that we're moving (approximately)
            if (contactImpulse > 1.0f && curMoveDir_.DotProduct(contactNormal) < -0.8f)
            {
                if (yOffset > stepHeightVec_.y_ )
                {
                    stepHeightVec_.y_ = yOffset;
                }
            }
        }

[/code]
MAX_STEP_HEIGHT = 0.4f

then in Character::FixedUpdate() func., I evaluate if the stepHeightVec_.y_ > 0 and if (stepHeightVec_.y_ > INCREMENTAL_HEIGHT) set stepHeightVec_.y_ = INCREMENTAL_HEIGHT (0.06f)
and calculate linear velocity based on set stepHeightVec_.y_

[code]
    // swat move speed:
    // walk - 1.842 m/s
    // run - 4.78 m/s
    // sprint - 7.164 m/s
    const float velWalk = 1.842f;
    const float velRun = 4.78f;
    moveForce_ = !runKey ? velWalk : velRun;

    if (moveDir.LengthSquared() > 0.0f)
    {
        moveDir.Normalize();
        moveDir = rot * moveDir;
    }

    curMoveDir_ = moveDir;

    // If in air, allow control, but slower than when on ground
    if (softGrounded)
    {
        if (stepHeightVec_.y_ > M_EPSILON)
        {
            if (stepHeightVec_.y_ > INCREMENTAL_STEP_HEIGHT)
            {
                stepHeightVec_.y_ = INCREMENTAL_STEP_HEIGHT;
            }

            // convert to vertical step velocity
            stepHeightVec_ = stepHeightVec_ / timeStep;

            body->SetLinearVelocity(stepHeightVec_ + moveDir * moveForce_);
        }
        else
        {
            body->SetLinearVelocity(moveDir * moveForce_);
        }
    }
    else
    {
        body->ApplyImpulse(moveDir * INAIR_MOVE_FORCE);
    }

   . . . 
   stepHeightVec_ = Vector3::ZERO;

[/code]
INCREMENTAL_STEP_HEIGHT = 0.06f

Edit: added code changes in my Character::FixedUpdate() func.

-------------------------

Lumak | 2017-01-02 01:15:41 UTC | #34

Remainder of changes in the Character::FixedUpdate() func (just changed Swat_JumpUp to Swat_JumpDown animation - not shown in the videos)

[code]
    if (!onGround_)
    {
        float rayDistance = 5.0f;
        PhysicsRaycastResult result;
        GetScene()->GetComponent<PhysicsWorld>()->RaycastSingle(result, Ray(node_->GetPosition(), Vector3::DOWN), rayDistance, 2);

        if (result.body_  == NULL || result.distance_ > MAX_STEPDOWN_HEIGHT)
        {
            animCtrl->Play("Models/Swat/Swat_JumpDown.ani", 0, false, 0.2f);
        }
    }
    else
. . .

[/code]

MAX_STEPDOWN_HEIGHT = 0.5f

That's all the changes that I made for the step height movement.  Other changes were adding an over-the-shoulderCamera and having the main cameraNode_ interpolate the position/rotation with it.

-------------------------

smellymumbler | 2017-05-30 21:57:23 UTC | #35

I'm using a mix of Lumak's changes and the CharacterDemo for my own Character Controller. Unfortunately, i'm having a hard time understanding how i could do something like crouching and proning. Would you guys just dynamically reduce the size of the capsule? 

Also, is there a networked version of that example, Lumak? Would be nice to see which fields need to go over the network to animate properly across clients.

-------------------------

Lumak | 2017-05-30 22:48:35 UTC | #36

When I was investigating this, I didn't realize there was https://github.com/hdunderscore/Urho3D-FPS-Controller 
I haven't tried his fps controller but have seen a youtube vid of someone using it and it looked very functional to me. I'd use that instead of what I've posted.

-------------------------

smellymumbler | 2017-05-30 23:25:14 UTC | #37

Yeah, but his controller is not using a rigidbody, apparently. It does not use forces, but changes the position arbitrarily. I prefer the version with ApplyImpulse because it gives me a ground truth to make calculations and changes. Also, it's much easier to do different states, such as crouched, prone, etc. BTW, that controller does not work with slopes very well.

In fact, since it's using the physics engine, i could attach a second model to the character, an invisible one, composed of collision hulls. I can use this simple model of boxes and cylinders to not only dictate where the character has been shot, but where the collision takes place, making it easy to do crouched collision and prone collision.

-------------------------

Lumak | 2017-05-30 23:26:22 UTC | #38

But it does use rigidbody. Take a closer look:
https://github.com/hdunderscore/Urho3D-FPS-Controller/blob/master/Source/Character.cpp

-------------------------

smellymumbler | 2017-05-30 23:29:59 UTC | #39

I'm confused. What's going on here, then? https://github.com/hdunderscore/Urho3D-FPS-Controller/blob/master/Source/Character.cpp#L301

-------------------------

Lumak | 2017-05-31 00:19:38 UTC | #40

@hdunderscore is the person to ask.

-------------------------

darkirk | 2017-06-02 14:02:42 UTC | #41

I've noticed this problem when doing crouch/prone and other capsule changes:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/0f49bba670ead0b437b062a19b3f8a2cddbb6e2f.png'>

Anyone else?

-------------------------

hdunderscore | 2017-06-08 05:43:14 UTC | #42

I believe that line is keeping the visual model close to the rigid body. Some fudge is used to reposition some rigid bodies to behave as expected like @darkirk's image indicates.

-------------------------

