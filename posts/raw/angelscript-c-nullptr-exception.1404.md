itisscan | 2017-01-02 01:07:31 UTC | #1

I created scene in the editor and try to load it. I have followed AngelScript file, that does not want to work.

First, I load the scene like this

[code]   SharedPtr<File> file = g_pApp->GetConstantResCache()->GetFile(levelResource);
	m_pScene = new Scene(context_);
	m_pScene->LoadXML(*level);

	m_pCameraNode = m_pScene->CreateChild("MainCamera");
	m_pCameraNode->CreateComponent<Camera>();

	// Set an initial position for the camera scene node above the plane
	m_pCameraNode->SetPosition(Vector3(0.0f, 2.0f, -10.0f));
	SharedPtr<Viewport> viewport(new Viewport(context_, m_pScene, m_pCameraNode->GetComponent<Camera>()));
	m_pRenderer->SetViewport(1, viewport);

[/code]

2) Then I have followed action script, which attachedto the object. All work fine, until I pressed space, in order to create prefab  and try to set initial impulse.

[code]class Cannon : ScriptObject
{
        if (input.keyDown[KEY_SPACE] && shootDelay <= 0.0f)
        {
            shootDelay = 1.0f;  
            Shoot();
            AnimationController@ animCtrl = node.GetComponent("AnimationController");
            animCtrl.SetTime("Models/Shoot.ani", 0.0f);                
            animCtrl.PlayExclusive("Models/Shoot.ani", 0, false, 0.0f);
        }
    }

    void Shoot()
    {
        Vector3 position = node.GetChild("CannonballPlace", true).worldPosition;

        XMLFile@ xml = cache.GetResource("XMLFile", "Objects/Cannonball.xml");
        Node@ newNode = scene.InstantiateXML(xml, position, Quaternion());
        
        RigidBody@ body = newNode.GetComponent("RigidBody");
        body.ApplyImpulse(node.rotation * Vector3(0.0f, 1.0f, 0.0f) * 15.0f);
    }
}[/code]

When I try to InstantiateXML, my program crashed and I have the following output.

[b]ERROR: Scripts/Cannon.as:47,13 - Exception 'Null pointer access' in 'void Cannon::Update(float)'
AngelScript callstack:
	Scripts/Cannon.as:void Cannon::Update(float):47,13
[/b]

I have checked that all path are correct.

How I can fix it ?

-------------------------

itisscan | 2017-01-02 01:07:31 UTC | #2

[quote="Sinoid"]Are you using 1.4 or HEAD from git?

Also, include the entire code from your Cannon.as file - or at least prefix the lines you do provide with their line numbers. Almost impossible to help with what you've given.[/quote]

I am not quite sure, but I think I use 1.4 version. I just clone repository from [github.com/urho3d/Urho3D](https://github.com/urho3d/Urho3D), and compiled it with vs2013. But, what is HEAD version ? 

I uploaded Cannon.as file below. I get error, when press space, like this 

[b][Sat Oct 03 09:51:27 2015] ERROR: Scripts/Cannon.as:19,9 - Exception 'Null pointer access' in 'void Cannon::Shoot()'
AngelScript callstack:
	Scripts/Cannon.as:void Cannon::Shoot():19,9
	Scripts/Cannon.as:void Cannon::Update(float):7,4
[/b]

Also I have checked, that if I comment [b]Shoot[/b] function, animation works fine.
 
[img]http://s15.postimg.org/fb922ay0r/cannonscript.png[/img]

UPDATED.

I have written function Shoot() in C++. All works fine. So, there is problem with AngelScript, especially with InstantiateXML fucntion.  :exclamation:

[code]Vector3 pos = m_pScene->GetChild("CannonballPlace", true)->GetWorldPosition();
			XMLFile* xml = g_pApp->GetConstantResCache()->GetResource<XMLFile>("Objects/Cannonball.xml");
			Node* newNode = m_pScene->InstantiateXML(xml->GetRoot(), pos, Quaternion());
			RigidBody* body = newNode->GetComponent<RigidBody>("RigidBody");
			body->ApplyImpulse(m_pScene->GetChild("Cannon")->GetRotation() * Vector3(0.0f, 1.0f, 0.0f) * 15.0f);[/code]

I tried to write in script [b]xml.root[/b] too, but it failed anyway.

-------------------------

itisscan | 2017-01-02 01:07:31 UTC | #3

[quote="Sinoid"][quote]I am not quite sure, but I think I use 1.4 version. I just clone repository from [github.com/urho3d/Urho3D](https://github.com/urho3d/Urho3D), and compiled it with vs2013. But, what is HEAD version ?[/quote]

That would be HEAD/master. Angelscript was recently updated in master, I just needed to know whether you were using Angelscript 2.29 or 2.30.2.

Everything appears to be fine with InstantiateXML.

Can you post the XML of your Objects/Cannonball.xml that you're trying to instantiate?[/quote]

This is [b]Cannonball.xml [/b].

[code]<?xml version="1.0"?>
<node id="3">
	<attribute name="Is Enabled" value="true" />
	<attribute name="Name" value="Cannonball" />
	<attribute name="Position" value="0 3.5 3.5" />
	<attribute name="Rotation" value="1 0 0 0" />
	<attribute name="Scale" value="1 1 1" />
	<attribute name="Variables" />
	<component type="StaticModel" id="12">
		<attribute name="Model" value="Model;Models/Cannonball.mdl" />
		<attribute name="Material" value="Material;Materials/Cannonball.xml" />
	</component>
	<component type="ScriptInstance" id="14">
		<attribute name="Delayed Method Calls" value="0" />
		<attribute name="Script File" value="ScriptFile;Scripts/CannonBall.as" />
		<attribute name="Class Name" value="Dying" />
		<attribute name="time" value="0" />
	</component>
	<component type="CollisionShape" id="15">
		<attribute name="Shape Type" value="Sphere" />
		<attribute name="Size" value="0.8 0.5 1" />
	</component>
	<component type="RigidBody" id="16">
		<attribute name="Physics Position" value="0 3.5 3.5" />
		<attribute name="Mass" value="1" />
	</component>
</node>
[/code]

-------------------------

Bluemoon | 2017-01-02 01:07:31 UTC | #4

From what I'm suspecting its either a null reference was returned for the rigid body when instantiated from xml or the Node@ reference held by the "node" attribute of the Canon ScriptClass was lost. Can you post the code of CanonBall.as, it might be a bit helpful.

-------------------------

itisscan | 2017-01-02 01:07:32 UTC | #5

[quote="Bluemoon"]From what I'm suspecting its either a null reference was returned for the rigid body when instantiated from xml or the Node@ reference held by the "node" attribute of the Canon ScriptClass was lost. Can you post the code of CanonBall.as, it might be a bit helpful.[/quote]

[b]CanonBall.as[/b]
[code]
class Dying : ScriptObject
{
    float time = 0.0f;
    void Update(float timeStep)
    {
        time += timeStep;
        if (time > 10.0f)
            node.Remove();
    }
}[/code]

-------------------------

