f1af | 2017-02-08 16:31:23 UTC | #1

I have next .as code:

	class PlayerVehicle : ScriptObject
	{
		String selfGRightNode;

		void DelayedStart()
		{
			ConstraintRevolute2D@ constraint = node.CreateComponent("ConstraintRevolute2D");
			constraint.otherBody = node.GetChild(selfGRightNode).GetComponent("RigidBody2D");
		}
	}

And another place I have:

    scene.RemoveAllChildren();

After that I crash. Crashdump: http://www.filedropper.com/urho3dtuefeb71357562017
What is wrong?

-------------------------

Eugene | 2017-02-07 11:50:44 UTC | #2

Are you able to post crash callstack here?

-------------------------

f1af | 2017-02-07 17:03:59 UTC | #3

No, but I can give u full version of me code, for reproduce that: http://www.filedropper.com/lessmess

In this arhive have a next files, it's full version:

Main.as

    Scene@ scene_;

    void Start()
    {
        log.Open("log.txt");
        scene_ = Scene();

        scene_.LoadXML(cache.GetFile("Scenes/Level01.xml"));
        renderer.viewports[0] = Viewport(scene_, scene_.GetChild("PlayerCamera").GetComponent("Camera"));

        SubscribeToEvent("innerEvent", "HandleInnerEvent");
    }

    void HandleInnerEvent(StringHash eventType, VariantMap& eventData)
    {
        log.Info("--- send recive ---");
        scene_.RemoveAllChildren();
    }

ProxyNode.as

	class ProxyNode : ScriptObject
	{
		String sourceXML;

		void DelayedStart()
		{
		    XMLFile@ xmlfile = cache.GetResource("XMLFile", sourceXML);
	        Node@ newNode = scene.CreateChild();
	        newNode.LoadXML(xmlfile.GetRoot(), true);
	        newNode.SetTransform(node.position, node.rotation);
		}
	}


PlayerVehicle

	class PlayerVehicle : ScriptObject
	{
		String selfGRightNode;

		private float timeAccamulate;
		private bool isSendDone;

		void DelayedStart()
		{
			ConstraintRevolute2D@ constraint = node.CreateComponent("ConstraintRevolute2D");
			constraint.otherBody = node.GetChild(selfGRightNode).GetComponent("RigidBody2D");
		}	

		void FixedUpdate(float timeStep)
		{
			timeAccamulate += timeStep;
			if ( timeAccamulate > 2.0f and !isSendDone )
			{
				isSendDone = true;
				VariantMap vmap;
				SendEvent("innerEvent", vmap);
			}
		}
	}

And *.xml you can see in arhive, if it need.

-------------------------

Eugene | 2017-02-07 17:46:37 UTC | #4

I have no crash when running your scripts on _my_ Urho Player.
Object disappears after a few seconds.
Maybe it's related to those Angel Script crashes on MinGW...

This dump is absolutely useless (at least, for me) if there are no symbols.

-------------------------

f1af | 2017-02-07 18:18:03 UTC | #5

I get Urho Player from:
https://sourceforge.net/projects/urho3d/files/Urho3D/
I click on **"Download Urho3D-1.6-Windows-64bit-STATIC-3D11.zip (319.1 MB)"**

Thank you, I will try rebuild urho. It's resolve me problem (maybe), but it's not resolve urho-problem (problem in Urho3D-1.6-Windows-64bit, delived throuse official urho web-site)..

-------------------------

weitjong | 2017-02-08 10:46:17 UTC | #6

The 1.6 binary package for 64-bit Windows D3D11 build was test run successfully before the release tag was made.

-------------------------

f1af | 2017-02-08 16:17:18 UTC | #7

**2 weitjong** all example works fine too.
So, I rebuild Urho, and.. crash again.
In this code:

	void Constraint2D::SetOtherBody(RigidBody2D* body)
	{
            ...
		RecreateJoint();
		...
	}

New joint apply on body.
1. BUT! If we remove BOX2D body, it's remove his attached joint. Also it's remove from another body, where use it;s joint.
2. It happen whan remove "otherBody".
3. After that we remove "ownerBody". And it remove joint too, but in (1) BOX2D setup this join in zero. All Fine.
4. After that we remove constraint. And it remove joint.. but.. we remove this joint in (1). And CRUSH.

Help, pleas!!
Otherwise I mast write somthink like that:

    node.GetChild(selfGRightNode).RemoveAllComponents();

...before call scene.RemoveAllChildren()..

------------------------------------------------------------

**LOL! I fix it!!**

I change me code:

    void HandleInnerEvent(StringHash eventType, VariantMap& eventData)
    {
        log.Info("--- send recive ---");
        scene_.RemoveAllChildren();
    }

..on this:

    void HandleInnerEvent(StringHash eventType, VariantMap& eventData)
    {
        log.Info("--- send recive ---");
        scene_.RemoveAllComponents();
        scene_.RemoveAllChildren();
    }

Solved!

-------------------------

Eugene | 2017-02-08 16:25:43 UTC | #8

I think it is something wrong with Urho and need deeper investigation.

-------------------------

