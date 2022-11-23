thebluefish | 2017-01-02 00:58:59 UTC | #1

Hi,

I am having some difficulty loading game objects via Scene::InstantiateXML. Consider the following snippet from the Character Demo:

[code]// Create movable boxes. Let them fall from the sky at first
    const unsigned NUM_BOXES = 100;
    for (unsigned i = 0; i < NUM_BOXES; ++i)
    {
        float scale = Urho3D::Random(2.0f) + 0.5f;
        
        Urho3D::Node* objectNode = _scene->CreateChild("Box");
        objectNode->SetPosition(Urho3D::Vector3(Urho3D::Random(180.0f) - 90.0f, Urho3D::Random(10.0f) + 10.0f, Urho3D::Random(180.0f) - 90.0f));
        objectNode->SetRotation(Urho3D::Quaternion(Urho3D::Random(360.0f), Urho3D::Random(360.0f), Urho3D::Random(360.0f)));
        objectNode->SetScale(scale);
        Urho3D::StaticModel* object = objectNode->CreateComponent<Urho3D::StaticModel>();
        object->SetModel(cache->GetResource<Urho3D::Model>("Models/Box.mdl"));
        object->SetMaterial(cache->GetResource<Urho3D::Material>("Materials/Stone.xml"));
        object->SetCastShadows(true);
        
        Urho3D::RigidBody* body = objectNode->CreateComponent<Urho3D::RigidBody>();
        body->SetCollisionLayer(2);
        // Bigger boxes will be heavier and harder to move
        body->SetMass(scale * 2.0f);
        Urho3D::CollisionShape* shape = objectNode->CreateComponent<Urho3D::CollisionShape>();
        shape->SetBox(Urho3D::Vector3::ONE);
    }[/code]

This creates 100 boxes that fall due to gravity. Now consider the following modified snippet:

[code]const unsigned NUM_KEYS = 200;
	Urho3D::XMLFile* keyFile = GetSubsystem<Urho3D::ResourceCache>()->GetResource<Urho3D::XMLFile>("Objects/key.xml");
    for (unsigned i = 0; i < NUM_KEYS; ++i)
    {
		Urho3D::Vector3 position = Urho3D::Vector3(Urho3D::Random(180.0f) - 90.0f, Urho3D::Random(1.0f) + 1.0f, Urho3D::Random(180.0f) - 90.0f);
		Urho3D::Quaternion rotation = Urho3D::Quaternion(Urho3D::Random(360.0f), Urho3D::Random(360.0f), Urho3D::Random(360.0f));

		_scene->InstantiateXML(keyFile->GetRoot(), position, rotation);
    }[/code]

Here is my key.xml file:
[code]<?xml version="1.0"?>
<node id="2">
	<attribute name="Is Enabled" value="true" />
	<attribute name="Name" value="Cylinder01" />
	<attribute name="Position" value="0 0 0" />
	<attribute name="Rotation" value="1 0 0 0" />
	<attribute name="Scale" value="1 1 1" />
	<attribute name="Variables" />
	<component type="StaticModel" id="3">
		<attribute name="Model" value="Model;Models/Cylinder01.mdl" />
		<attribute name="Material" value="Material;Materials/key_01.xml" />
	</component>
	<component type="RigidBody" id="4">
		<attribute name="Mass" value="1" />
	</component>
	<component type="CollisionShape" id="5">
		<attribute name="Shape Type" value="ConvexHull" />
		<attribute name="Model" value="Model;Models/Cylinder01.mdl" />
	</component>
</node>
[/code]

This spawns the keys correctly, however they do not respect gravity. For example:
[url=http://i.imgur.com/49HqtCj.jpg][img]http://i.imgur.com/49HqtCjl.jpg[/img][/url]

Edit: Something definitely seems odd. Consider the following changes:
[code]const unsigned NUM_KEYS = 200;
	Urho3D::XMLFile* keyFile = GetSubsystem<Urho3D::ResourceCache>()->GetResource<Urho3D::XMLFile>("Objects/key.xml");
    for (unsigned i = 0; i < NUM_KEYS; ++i)
    {
		Urho3D::Vector3 position = Urho3D::Vector3(Urho3D::Random(180.0f) - 90.0f, Urho3D::Random(1.0f) + 1.0f, Urho3D::Random(180.0f) - 90.0f);
		Urho3D::Quaternion rotation = Urho3D::Quaternion(Urho3D::Random(360.0f), Urho3D::Random(360.0f), Urho3D::Random(360.0f));

		Urho3D::Node* objectNode = _scene->InstantiateXML(keyFile->GetRoot(), position, rotation);

		Urho3D::RigidBody* body = objectNode->CreateComponent<Urho3D::RigidBody>();
        body->SetCollisionLayer(2);
        body->SetMass(2.0f);
        Urho3D::CollisionShape* shape = objectNode->CreateComponent<Urho3D::CollisionShape>();
        shape->SetBox(Urho3D::Vector3::ONE);
    }[/code]

and my new key.xml:
[code]<?xml version="1.0"?>
<node id="2">
	<attribute name="Is Enabled" value="true" />
	<attribute name="Name" value="Cylinder01" />
	<attribute name="Position" value="0 0 0" />
	<attribute name="Rotation" value="1 0 0 0" />
	<attribute name="Scale" value="1 1 1" />
	<attribute name="Variables" />
	<component type="StaticModel" id="3">
		<attribute name="Model" value="Model;Models/Cylinder01.mdl" />
		<attribute name="Material" value="Material;Materials/key_01.xml" />
	</component>
</node>
[/code]

It should just load the StaticModel via the xml file, then setup the RigidBody and CollisionShape as how the boxes are setup. This time they do respect gravity, however now they are simply falling through the ground! Very weird indeed.

Any ideas?

-------------------------

cadaver | 2017-01-02 00:58:59 UTC | #2

If I can reproduce this reliably, it sounds like bugs in adding the physics components correctly when using the Instantiate..() functions. Will check. NinjaSnowWar example should be successfully instantiating physical object prefabs.

-------------------------

thebluefish | 2017-01-02 00:58:59 UTC | #3

Alright, I figured it out. It turns out that the editor had put in some undesirable default values:
[code]	<attribute name="Anisotropic Friction" value="0 0 0" />
		<attribute name="Linear Factor" value="0 0 0" />
		<attribute name="Angular Factor" value="0 0 0" />
		<attribute name="Linear Rest Threshold" value="0" />
		<attribute name="Angular Rest Threshold" value="0" />
		<attribute name="Contact Threshold" value="0" />[/code]

I didn't even realize that I had a post-build step in my Visual Studio solution to automatically sync data from my Data folder, so all of my changes when testing were being reversed. Wow that took me way too long last night and I figured it out in 30 minutes after waking up  :laughing:

-------------------------

