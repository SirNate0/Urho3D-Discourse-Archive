dev4fun | 2018-03-05 18:45:03 UTC | #1

Hey guys, Im doing character movement on my server, and I see that is flickering some times, dno why. Im using 60fps update on client and 30fps on server (physicsworld).

Video showing the problem:
https://puu.sh/zBdGu/2826b16857.mp4

Node Settings:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/b/b78ac803baaa74bbab0c73be8064e666425f654b.png'>

Map Floor settings:

		Node * pMapNode = pScene->CreateChild( pMap->GetName(), LOCAL );
		pMapNode->SetPosition( Vector3( 0, 0, 0 ) );
		pMapNode->SetScale( Vector3( 1.0f, 1.0f, 1.0f ) );
		
		auto * pBody = pMapNode->CreateComponent<RigidBody>();
		pBody->SetFriction( 1.0f );

		auto * pShape = pMapNode->CreateComponent<CollisionShape>();
		pShape->SetTriangleMesh( GetSubsystem<ResourceCache>()->GetResource<Model>( 	pMap->GetBaseMap()->GetFileName() ) );

Character Mover on Server:

		Node * pCharacterNode = GetNode();
		auto * pCharacterBody = pCharacterNode->GetComponent<RigidBody>();
		
		const Controls & cControls = pConnection->GetControls();
		const Vector3 & cVelocity = pCharacterBody->GetLinearVelocity();
		
		Quaternion cRotation( 0.0f, cControls.yaw_, 0.0f );
		Vector3 cMoveDirection = Vector3::ZERO;

		Vector3 cPlaneVelocity( cVelocity.x_, 0.0f, cVelocity.z_ );

		if( cControls.buttons_ & CHARACTERCONTROL_Forward )
		{
			cMoveDirection += Vector3::FORWARD;
			pCharacterNode->SetRotation( cRotation );
		}
		
		if( cMoveDirection.LengthSquared() > 0.0f )
			cMoveDirection.Normalize();

		pCharacterBody->ApplyImpulse( cRotation * cMoveDirection * 1.0f );

		Vector3 cBrakeForce = -cPlaneVelocity * 0.1f;
		pCharacterBody->ApplyImpulse( cBrakeForce );

Thanks!

-------------------------

Eugene | 2018-03-05 18:54:34 UTC | #2

Does it work smoothly if simulated locally?

-------------------------

dev4fun | 2018-03-05 19:22:44 UTC | #3

[quote="Eugene, post:2, topic:4075, full:true"]
Does it work smoothly if simulated locally?
[/quote]

Server is running locally, so, shouldnt happen this. Dont know if can be some setting on physics... I tried get the physics settings from 18_CharacterDemo sample.

-------------------------

1vanK | 2018-03-06 08:07:08 UTC | #4

```
node->GetOrCreateComponent<SmoothedTransform>();
```

-------------------------

George1 | 2018-03-06 08:19:21 UTC | #5

I think the below code affecting that motion.

Vector3 cBrakeForce = -cPlaneVelocity * 0.1f;
	pCharacterBody->ApplyImpulse( cBrakeForce );

Can you comment it out to see if it is ok?

-------------------------

1vanK | 2018-03-06 13:24:51 UTC | #6

Do you work with physics in function FixedUpdate() ?

-------------------------

dev4fun | 2018-03-06 15:53:55 UTC | #7

Yes, Im using a Logic Component. ll try about SmoothedTransform.

-------------------------

dev4fun | 2018-03-07 00:57:55 UTC | #8

Didnt work.

@ Could be something on yaw? Dno. Nothing works until now.

    //Manipulating Camera Yaw
    if( INPUT->GetKeyDown( KEY_LEFT ) )
    	fCameraYaw += 0.5f;
    else if( INPUT->GetKeyDown( KEY_RIGHT ) )
    	fCameraYaw -= 0.5f;

    //Getting Mouse Yaw
    fMouseYaw = Atan2( INPUT->GetMousePosition().y_ - (GRAPHICS->GetSize().y_ >> 1), INPUT->GetMousePosition().x_ - (GRAPHICS->GetSize().x_ >> 1) ) + 90.0f;

And to send to server side:

    cControls.yaw_ = CAMERAMANAGER->GetCameraYaw() + CAMERAMANAGER->GetMouseYaw();

@@ 've tried remove brake force, change the value that Im multiplying the impulse, but nothing is changed. Same problem on all changes.

@@@ Same making the physics on PhysicsPreStep..

-------------------------

1vanK | 2018-03-07 01:01:29 UTC | #9

> pCharacterNode->SetRotation( cRotation );

actually you can not set rotations and positions for dynamics bodies, you can use only forces and impulses

-------------------------

1vanK | 2018-03-07 01:06:00 UTC | #10

Honestly, you do not need to rotate the capsule, just push it in the direction you want. Just rotate camera around object in Update (in Update you can use standart input->GetMouseMove() for yaw)

-------------------------

1vanK | 2018-03-07 01:23:58 UTC | #11

You can calculate impulses which will move the body.
For example I use this code for control movement speed:
```
        Vector3 desiredVel = rotation * dir * MOVE_SPEED;
        Vector3 impulse = (desiredVel - playerBody->GetLinearVelocity()) * playerBody->GetMass();// * 0.1f;
        playerBody->ApplyImpulse(impulse);
```
Same for rotations

EDIT: based on http://www.iforce2d.net/b2dtut/constant-speed

-------------------------

dev4fun | 2018-03-07 01:39:42 UTC | #12

Hmm ic. Same after all changes quoted on this topic, the problem always appears, dno why.

If I use ur code out this condition **if( cControls.buttons_ & CHARACTERCONTROL_Forward )**, this happens (beyond flickr)
https://puu.sh/zCc1X/0acb440e15.mp4

Its strange, in every way the flicker happens lol.

-------------------------

Don | 2018-03-07 06:42:34 UTC | #13

Could you provide a repository that we could look at? This seems like an issue that could encompass many parts of the code, and providing the full scope could help. Also I want to say, your graphical style is really slick.

-------------------------

Eugene | 2018-03-07 08:31:00 UTC | #14

+1 for @Don
I could investigate the problem if there is something run-able.

-------------------------

Eugene | 2018-03-07 08:44:55 UTC | #15

Haa, I have an idea.

Ensure that:

1) You have turned off server physics interpolation.
1) You have `RigidBody` of your character only on server side. The code _may_ work even if you have bodies both on client and server side. I'd like not to tempt fate.

> Position and rotation are Node attributes, while linear and angular velocities are RigidBody attributes. To cut down on the needed network bandwidth the physics components can be created as local on the server: in this case the client will not see them at all, and will only interpolate motion based on the node's transform changes. Replicating the actual physics components allows the client to extrapolate using its own physics simulation, and to also perform collision detection, though always non-authoritatively.

> By default the physics simulation also performs interpolation to enable smooth motion when the rendering framerate is higher than the physics FPS. This should be disabled on the server scene to ensure that the clients do not receive interpolated and therefore possibly non-physical positions and rotations. See SetInterpolation().

-------------------------

dev4fun | 2018-03-07 14:07:02 UTC | #16

Hmm ye I have character only on server side... I should create in client replicated or local? I will not have 2 characters at same time?

Thanks for ur help, I believe that u solved the problem, ll try this later.

-------------------------

Eugene | 2018-03-07 14:20:14 UTC | #17

[quote="dev4fun, post:16, topic:4075"]
Hmm ye I have character only on server side… I should create in client replicated or local? I will not have 2 characters at same time?
[/quote]

If you have character on the server side only, it should be fine.
Then, just turn off physics interpolation on the server side.
If it doen't help... well, make a sample for ppl to try it. I've never seen such bugs with sample network app.

-------------------------

dev4fun | 2018-03-07 15:07:20 UTC | #18

Interpolation was already turned off lol.

SVN Repo:
client: https://subversion.assembla.com/svn/dev-client/trunk
server: https://subversion.assembla.com/svn/dev-server/trunk
shared: https://subversion.assembla.com/svn/dev-shared/trunk

If someone want to see this in-game: https://puu.sh/zCy4x/f004273bf4.rar
(should run login server, after game server)(can type any login and pw, and dont need a character nick)(to walk let mouse button left pressing or double click with mouse button left)

    void CMapHandler::CreateScene() - create scene to server and maps collision
    CCharacter * CCharacterHandler::LoadCharacter( Connection * pConnection, String strCharacterName ) - instantie XML responsible for character node and create the logic component CCharacter
    void CCharacter::FixedUpdate( float fTime ) - physics of each character at scene

I really dno what more can be, Im "newbie" on Urho3D, and until now this is the unique problem I dont solved.
Thanks.

-------------------------

Eugene | 2018-03-09 06:33:07 UTC | #19

~~Archive seems broken. Or maybe some very new version of winRAR.
Tried to download&open it two times.~~

And... I have no idea how to download SVN repos w/o any installed SVN client.

-------------------------

Eugene | 2018-03-07 16:49:38 UTC | #20

[quote="dev4fun, post:16, topic:4075"]
Hmm ye I have character only on server side…
[/quote]

I'm looking at your code and I'm not sure that the Client doesn't have `RigidBody` component: in the file `Server Data\Objects\Character.xml` there is replicated `RigidBody` component that is probably replicated on the client side.

-------------------------

dev4fun | 2018-03-07 21:20:35 UTC | #21

Oh ya, its replicated... so maybe I understood wrong your question in previous post.

-------------------------

dev4fun | 2018-03-07 21:38:48 UTC | #22

lol its really strange, when I believe that is solved, ll check and the problem appears again and again. Sometimes I got less flickering, sometimes more..

-------------------------

Eugene | 2018-03-07 21:48:26 UTC | #23

So even if you 100% don't have any `RigidBody` for characters on the client side, you still get artifacts?

Try this test plan:

Do you have artifacts with standard SceneReplication sample?
If yes... that's strange, I don't want to even think about it.
If no, do you have artifacts if use your character controller in SceneReplication sample?
If yes... that's strange, I don't want to even think about it.
If no, artifacts occur somewhere in your code that is different from SceneReplication sample...

-------------------------

dev4fun | 2018-03-07 23:16:03 UTC | #24

Hmm ya probably its something on my source. 've implemented the movement code and camera code on scene replication sample and all works good..

So it isnt:

* Camera (yaw)
* Object (xml) from character
* Movement Physics Code (ApplyImpulse etc)
* Collision (used same collision as used on SceneReplication)
* Logic Component (CCharacter)

Jesus, 'll need to review whole source code haha.

-------------------------

Eugene | 2018-03-07 23:33:59 UTC | #25

Well, bisection isn’t so hard, much better than “nothing works”.
I suggest you to compare scenes in sample an in your project.
E.g. just dump them in XML. 
IMO it’s quite hard to break inbuilt interpolation from code unless you intentionally do something outside your server instance of the Character.

-------------------------

dev4fun | 2018-03-07 23:42:20 UTC | #26

Hmm ya, 'll try this haha.

Just to know, scene on server, needs to be identical on game? Bcoz on my server 'll use just to coliision, this way I put all maps (models) on same scene. But on game, I load just one map, and when necessary I load other map. This way scene game != scene server.

-------------------------

Eugene | 2018-03-07 23:46:51 UTC | #27

Replicated nodes and components must be identical. They will be, regardless of your will. Local nodes and components.. you know. They don’t have to.

-------------------------

dev4fun | 2018-03-08 01:32:09 UTC | #28

Things I've tested:

* Camera (yaw)
* Object (xml) from character
* Movement Physics Code (ApplyImpulse etc)
* Collision (used same collision as used on SceneReplication)
* Logic Component (CCharacter)
* Multiple connections to server (client connect to login server and game server)
* Scene Settings

Comparing dumped scenes...
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/8/81a85c2ad720cbd0922c9e09777fe8be4ccc635b.png'>

My alternatives are practically exhausted, I really could pay someone to help me 
I dont have the slightest idea of what might be happening :frowning:

-------------------------

dev4fun | 2018-03-08 03:10:48 UTC | #29

Sure, I made some tests and I came to the conclusion that the problem is the game.. :roll_eyes: Why?

My Game with **Server of Scene Replication Sample** = flickering
**Scene Replication Game** with My Server = all works good

Now I need to check game code to see what could be happening. Any idea?

-------------------------

dev4fun | 2018-03-09 00:23:34 UTC | #30

Problem was bcoz camera was updating by HandleUpdate and dont HandlePostUpdate... :tired_face:
I have to made many tests to discover this and think on this haha, thanks and sorry to all who helped me :smiley:

-------------------------

