noals | 2017-03-18 02:06:27 UTC | #1

hi,

1/ my mesh doesn't show up. i had a similar problem before, i just had to check the weights box in the exporter but it doesn't do the trick here.
here is my .blend file : http://s000.tinyupload.com/index.php?file_id=00770724021487880499
[URL=http://www.hostingpics.net/viewer.php?id=316717ragdollhead.png][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/51f6f3d8b49fd36b9a9aa317eac56109052be50d.png[/img][/URL]

[URL=http://www.hostingpics.net/viewer.php?id=452664headnotshowing.png][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/196e89dd0e3ff9f26b9d4090a0ae4b825c79e20c.png[/img][/URL]
the model is well loaded since it show the physic infos but that's it.


2/ and can i have my model shown without using texture ?
i mean if i just put a color to the material in blender and want this color to be rendered on the model in the app, how must i do ?


3/ while testing a weird problem came up, the app does't go fullscreen properly. it shows the top-left part, no clue why.
what it show windowed : 
[URL=http://www.hostingpics.net/viewer.php?id=399024render1.png][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/d9e382c016050e93d0aad66b45954f182b88c542.png[/img][/URL]
then in fullscreen : 
[URL=http://www.hostingpics.net/viewer.php?id=834615render1fullscreenbug.png][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/9e90f569162236df78a388c2bcb8b5f78026a99e.png[/img][/URL]
it eats part of the thing, and this problem just came up today for no special reason, maybe it will be fixed after restarting my computer, dunno because it was working fine few days ago.

i use urho 1.5 (will update to 1.6 soon i think)

thx

-------------------------

noals | 2017-03-07 00:01:31 UTC | #2

here is my code for loading but i don't thing it is the problem as it works fine with the floor.
[code]
        floorNode = my_scene->CreateChild("floor");
        floorNode->SetWorldPosition(Vector3::ZERO);        
        floorNode->SetWorldRotation(Quaternion::IDENTITY);
    
        floorObject=floorNode->CreateComponent<AnimatedModel>();    //<AnimatedModel>();
        floorObject->SetModel(cache->GetResource<Model>("Models/floor.mdl"));
        floorObject->SetMaterial(cache->GetResource<Material>("Materials/blank.xml"));

//add physic     
        floorBody = floorNode->CreateComponent<RigidBody>();
        floorBody->SetMass(0);  //0 for static object
        //floorBody->SetUseGravity(false);
        //m_Body->SetTrigger(false);
        floorBody->SetFriction(0.6);        // friction with other objects (like the ground)
        floorBody->SetCollisionLayer(1);  // !!

//add collision shape
        floorBBox = floorNode->CreateComponent<CollisionShape>();
        floorBBox->SetConvexHull(cache->GetResource<Model>("Models/floor.mdl"));

//add collision check
       //collisionEvent = m_Node->CreateComponent<OnCollision>();



        mNode = my_scene->CreateChild("box");
        mNode->SetWorldPosition(Vector3(0,5,0));     //Vector3::ZERO);        
        mNode->SetWorldRotation(Quaternion::IDENTITY);
    
        mObject=mNode->CreateComponent<AnimatedModel>();    //<AnimatedModel>();
        mObject->SetModel(cache->GetResource<Model>("Models/bb_head.mdl"));
        mObject->SetMaterial(cache->GetResource<Material>("Materials/peau.xml"));

//add physic     
        mBody = mNode->CreateComponent<RigidBody>();
        mBody->SetMass(1);  //0 for static object
        //mBody->SetUseGravity(true);
        //m_Body->SetTrigger(false);
        mBody->SetFriction(0.6);        // friction with other objects (like the ground)
        mBody->SetCollisionLayer(1);  // !!

//add collision shape
        mBBox = mNode->CreateComponent<CollisionShape>();
        mBBox->SetConvexHull(cache->GetResource<Model>("Models/bb_head.mdl"));[/code]

-------------------------

1vanK | 2017-03-07 00:44:04 UTC | #3

___
any info in log?

-------------------------

noals | 2017-03-07 02:16:03 UTC | #4

nothing unusual.
[code]
[Tue Mar  7 00:39:31 2017] INFO: Opened log file Urho3D.log
[Tue Mar  7 00:39:31 2017] INFO: Created 3 worker threads
[Tue Mar  7 00:39:31 2017] INFO: Added resource path /home/noname/Bureau/game_build/bin/Data/
[Tue Mar  7 00:39:31 2017] INFO: Added resource path /home/noname/Bureau/game_build/bin/CoreData/
[Tue Mar  7 00:39:31 2017] DEBUG: Skipped autoload path 'Autoload' as it does not exist, check the documentation on how to set the 'resource prefix path'
[Tue Mar  7 00:39:32 2017] INFO: Set screen mode 1280x720 windowed resizable
[Tue Mar  7 00:39:32 2017] INFO: Initialized input
[Tue Mar  7 00:39:32 2017] INFO: Initialized user interface
[Tue Mar  7 00:39:32 2017] DEBUG: Loading resource Textures/Ramp.png
[Tue Mar  7 00:39:32 2017] DEBUG: Loading temporary resource Textures/Ramp.xml
[Tue Mar  7 00:39:32 2017] DEBUG: Loading resource Textures/Spot.png
[Tue Mar  7 00:39:32 2017] DEBUG: Loading temporary resource Textures/Spot.xml
[Tue Mar  7 00:39:32 2017] DEBUG: Loading resource Techniques/NoTexture.xml
[Tue Mar  7 00:39:32 2017] DEBUG: Loading resource RenderPaths/Forward.xml
[Tue Mar  7 00:39:32 2017] INFO: Initialized renderer
[Tue Mar  7 00:39:32 2017] INFO: Set audio mode 44100 Hz stereo interpolated
[Tue Mar  7 00:39:32 2017] DEBUG: Loading resource UI/MessageBox.xml
[Tue Mar  7 00:39:32 2017] DEBUG: Loading UI layout UI/MessageBox.xml
[Tue Mar  7 00:39:32 2017] INFO: Initialized engine
[Tue Mar  7 00:39:32 2017] DEBUG: Loading resource Models/floor.mdl
[Tue Mar  7 00:39:32 2017] DEBUG: Loading resource Materials/blank.xml
[Tue Mar  7 00:39:32 2017] DEBUG: Loading resource Techniques/Diff.xml
[Tue Mar  7 00:39:32 2017] DEBUG: Loading resource Textures/floor_texture.png
[Tue Mar  7 00:39:32 2017] DEBUG: Loading resource Models/bb_head.mdl
[Tue Mar  7 00:39:32 2017] DEBUG: Loading resource Materials/peau.xml
[Tue Mar  7 00:39:32 2017] DEBUG: Loading resource Fonts/Anonymous Pro.ttf
[Tue Mar  7 00:39:32 2017] DEBUG: Font face Anonymous Pro (14pt) has 624 glyphs
[Tue Mar  7 00:39:32 2017] DEBUG: Reloading shaders
[Tue Mar  7 00:39:32 2017] DEBUG: Loading resource Shaders/GLSL/LitSolid.glsl
[Tue Mar  7 00:39:32 2017] DEBUG: Compiled vertex shader LitSolid(PERPIXEL POINTLIGHT)
[Tue Mar  7 00:39:32 2017] DEBUG: Compiled pixel shader LitSolid(AMBIENT DIFFMAP PERPIXEL POINTLIGHT SPECULAR)
[Tue Mar  7 00:39:32 2017] DEBUG: Linked vertex shader LitSolid(PERPIXEL POINTLIGHT) and pixel shader LitSolid(AMBIENT DIFFMAP PERPIXEL POINTLIGHT SPECULAR)
[Tue Mar  7 00:39:32 2017] DEBUG: Loading resource Shaders/GLSL/Basic.glsl
[Tue Mar  7 00:39:32 2017] DEBUG: Compiled vertex shader Basic(VERTEXCOLOR)
[Tue Mar  7 00:39:32 2017] DEBUG: Compiled pixel shader Basic(VERTEXCOLOR)
[Tue Mar  7 00:39:32 2017] DEBUG: Linked vertex shader Basic(VERTEXCOLOR) and pixel shader Basic(VERTEXCOLOR)[/code]

my first guess was that there are some face missing (on purpose) so the engine wasn't able to render meshes with missing faces or something but it was the same problem after adding the missing faces as a test.
the other thing i can think of is that this model is exported as .dmx from a scene and reimported in a new scene, and then exported as mdl with the urho3D exporter so maybe it lose some infos in the process that make it unable to render, dunno.

-------------------------

Modanung | 2017-03-18 02:06:14 UTC | #5

The object in Blender lacks:

- An armature modifier
- Vertex groups

Clear the parenting by selecting the head and pressing **Alt+P**. Then select the armature as well, hit **Ctrl+P** and select _Armature deform with automatic weights_.
This will create both an armature modifier as well as a vertex group for every bone. Then export and see.

-------------------------

noals | 2017-03-08 00:48:05 UTC | #6

it works fine with texture or not.
[URL=http://www.hostingpics.net/viewer.php?id=701332loadcheckOK.png][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/1f62b529fa5f009a4765bbbc87467e1d9b6a27e7.png[/img][/URL]

[URL=http://www.hostingpics.net/viewer.php?id=639244splitimagefullscreen.png][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/3ce0c91b2431069dfb193accc9b42193c5990acb.png[/img][/URL]
i still have the fullscreen problem but dunno, it's weird. i had to update ubuntu so it changed my config file, maybe it have something to do with the resolution there. i think i tested my app after the update and the bug kinda came magically but dunno, i will check the config file later. 

thx.

-------------------------

