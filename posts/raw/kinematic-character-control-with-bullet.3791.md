mazataza | 2017-11-26 13:52:32 UTC | #1

i am trying to implement character control with bullet
i use the following code to initialise the ghost object 

    const Vector3 &postion = _cameraNode->GetWorldPosition();
    const Quaternion &rot = _cameraNode->GetWorldRotation();
    startTransform.setOrigin (ToBtVector3(postion + rot * Vector3::ZERO));
    startTransform.setRotation(ToBtQuaternion(rot));
    physicsWorld_->GetWorld()->getPairCache()->setInternalGhostPairCallback(new btGhostPairCallback());
    ghostObject = new btPairCachingGhostObject();
    ghostObject->setWorldTransform(startTransform);
    btScalar characterHeight=1;
    btScalar characterWidth =0.5;
    ghostShape = new btCapsuleShape(characterWidth,characterHeight);
    ghostObject->setCollisionShape (ghostShape);
    ghostObject->setCollisionFlags (btCollisionObject::CF_CHARACTER_OBJECT);

    btScalar stepHeight = btScalar(0.35);
    btVector3 up(0.0,1.0,0.0);
    characterController = new btKinematicCharacterController (ghostObject,ghostShape,stepHeight, up);

but then the ghost has rotation in x-axis which i can't understand

i update the node transform like

    btTransform &worldTrans = ghostObject->getWorldTransform();
    Quaternion newWorldRotation = ToQuaternion(worldTrans.getRotation());
    const Vector3 &rot = newWorldRotation * Vector3::ZERO;
    Vector3 newWorldPosition = ToVector3(worldTrans.getOrigin()) - rot;

    _cameraNode->SetWorldPosition(newWorldPosition);
    _cameraNode->SetWorldRotation(newWorldRotation);

the rotatotion matrix is
w= 0.7
x= -0.7
y=0
z=0

this what without appling transformation
![urho3d_cc1|689x415](upload://AtA6fmBDsy229ionjx3npFTIgVK.jpg)

and this with transformation
![urho3d_cc2|690x414](upload://kao2AzV4ABNuPbd1CFf3RQn9hlN.jpg)

when i dont set UP vector to (0.0,1.0,0.0) the character fall in x-axis 

i will be happy if someone can guide me what i am doing wrong.

-------------------------

Modanung | 2017-11-26 18:57:38 UTC | #2

The first thing I notice is:
[quote="mazataza, post:1, topic:3791"]
`startTransform.setOrigin (ToBtVector3(postion + rot * Vector3::ZERO));`
[/quote]
and
[quote="mazataza, post:1, topic:3791"]
`const Vector3 &rot = newWorldRotation * Vector3::ZERO;`
[/quote]
Rotating a { 0, 0, 0 } vector (which is what `Vector3::ZERO` is) will always return a zero vector.
You'll probably want to replace ZERO with FORWARD or BACK.

Also, what's the `_cameraNode`'s rotation at this point?
[quote="mazataza, post:1, topic:3791"]
`const Quaternion &rot = _cameraNode->GetWorldRotation();`
[/quote]
...since it's rotation relies on the ghost object's rotation.

I must add I have hardly any experience with directly using `bt` objects.

-------------------------

mazataza | 2017-11-26 18:55:04 UTC | #3

[quote="Modanung, post:2, topic:3791"]
Also, what’s the _cameraNode's rotation at this point?
[/quote]

the rotation is zero (w=1 x=0 y=0 z=0)

[quote="Modanung, post:2, topic:3791"]
I must add I have hardly any experience with directly using bt objects.

Which does makes me think: Isn’t up { 0, 0, 1 } in Bullet? :bulb:
[/quote]
no it is {0 1 0} (x y z)

-------------------------

Modanung | 2017-11-26 18:58:37 UTC | #4

[quote="mazataza, post:3, topic:3791"]
no it is {0 1 0} (x y z)
[/quote]


Check :white_check_mark:

-------------------------

mazataza | 2017-11-26 19:02:57 UTC | #5

[quote="Modanung, post:4, topic:3791"]
Check :white_check_mark:
[/quote]

i don't understand what you mean but here can check the coordinate system on bullet

http://bulletphysics.org/mediawiki-1.5.8/index.php/Coordinate_system

-------------------------

Modanung | 2017-11-26 19:04:14 UTC | #6

I meant you're right. :)

-------------------------

mazataza | 2017-11-26 19:47:53 UTC | #7

the problem i found that when i set

    ghostObject->setWorldTransform(startTransform);

before the kinematic controller this got rotated because the up vector got changed

but when i set after creation of kinematic the rotation doesn't done, and the character can now move, but i have some trouble but i will check if i could solve them by myself

-------------------------

Modanung | 2017-11-26 19:56:26 UTC | #8

Glad to hear you're making progress.

-------------------------

mazataza | 2017-11-29 17:45:16 UTC | #9

I still stuck with the conversion betweeen bullet to urho3d.. as i know bullet use right hand coordinate and urho3d use left hand.
the following code which i use at first to update ghostobject walking direction

        btTransform xform;
        xform = ghostObject->getWorldTransform ();
        btVector3 forwardDir = xform.getBasis()[2];
        forwardDir.normalize ();
        ....
        btVector3 walkDirection = btVector3(0.0, 0.0, 0.0);
        ...
        if (gForward) {
            walkDirection += forwardDir;
        }
        ...
        characterController->setWalkDirection(walkDirection*walkSpeed);

this code works when there is no rotation. if there is a rotation then the object move very strange for me
now i use following code and it works but i can't understands why it works and that what I don't like - to have a code which i can't understand totaly.

      btTransform xform;
      xform = ghostObject->getWorldTransform ();
      Quaternion newWorldRotation = ToQuaternion(xform.getRotation());
      const Vector3 &forwardDir= newWorldRotation * Vector3::FORWARD;
      
      if (gForward) {
        walkDirection += forwardDir;
      }
      ...
      characterController->setWalkDirection(walkDirection*walkSpeed);

as you see i use urho3d quaterion and calculate forward direction.

then i use following code to update character node in urho3d

    btTransform &worldTrans = ghostObject->getWorldTransform();
    Quaternion newWorldRotation = ToQuaternion(worldTrans.getRotation());
    const Vector3 &rot = newWorldRotation * Vector3::FORWARD;
    Vector3 newWorldPosition = ToVector3(worldTrans.getOrigin()) - rot;

    _cameraNode->SetWorldPosition(newWorldPosition);
    _cameraNode->SetWorldRotation(newWorldRotation);

if someone can explain me how urho3d handle these differences between bullet and urho3d i will be happy

-------------------------

1vanK | 2017-11-29 22:14:27 UTC | #10

 https://discourse.urho3d.io/t/kinematic-character-controllers/3555

-------------------------

mazataza | 2017-11-30 06:55:34 UTC | #11

thank you for the link..
i have some question there  but i will write them there

-------------------------

