Cpl.Bator | 2017-01-02 01:12:28 UTC | #1

Hi, i try to create myself a mini-game like this : [habrahabr.ru/post/265749/](https://habrahabr.ru/post/265749/) from 1vanK ( thank for that ) 

[url=http://www.hostingpics.net/viewer.php?id=464162shoot.png][img]http://img11.hostingpics.net/thumbs/mini_464162shoot.png[/img][/url]

and i've got a problem when i call inside my script :

[code]Node@ newNodeParticle = scene.InstantiateXML(smoke_xml, position, Quaternion(0.0f, yaw, pitch));[/code]

i call this method when i shoot a bullet , but, i noticed a small freeze when i use particle. but not when i use the bullet only without particle. 
the problem is the same with the 1vank's demo ( only for the first bullet , me , for all bullet... :/ )

it is possible to "preload"  the xml file to prevent the freeze ?

the complete script :

[code]class Canon : ScriptObject{
	
	float pitch 		= 0.0f;
	float yaw 			= 0.0f;
	float shootDelay 	= 0.0f;
	XMLFile@ bullet_xml = cache.GetResource("XMLFile", "Objects/bullet.xml");
	XMLFile@ smoke_xml 	= cache.GetResource("XMLFile", "Objects/smokeCanon.xml");
	
	
	
	void Update(float timeStep){
	
		if (input.keyDown[KEY_UP]){
			pitch += 45 * timeStep;
		}
	
		if (input.keyDown[KEY_DOWN]){
			pitch -= 45 * timeStep;
		}
		
		if (input.keyDown[KEY_RIGHT]){
			yaw += 20 * timeStep;
		}
	
		if (input.keyDown[KEY_LEFT]){
			yaw -= 20 * timeStep;
		}
			
				
		if( yaw >= 100.0f){
			yaw = 100.0f;
		}
		
		if( yaw <= 80.0f){
			yaw = 80.0f;
		}		
		
		
		
		if (input.keyDown[KEY_SPACE] && shootDelay <= 0.0f){
			shootDelay = 1.0f;
			Shoot();
		}
		
		pitch -= 1.5f * timeStep;
		
		if (shootDelay > 0.0f)
			shootDelay -= timeStep;		
				
		if( pitch >= -50.0f){
			pitch = -50.0f;
		}
		
		if( pitch <= -95.0f){
			pitch = -95.0f;
		}		
			
			
		//node.rotation = Quaternion(pitch, yaw, 0);
	
		node.GetChild("base",true).rotation = Quaternion(0, yaw, 0);
		node.GetChild("canon",true).rotation = Quaternion(0, 0, pitch);
	}
	
	
	void Shoot()
    {       
        Vector3 position    = node.GetChild("hotpoint", true).worldPosition;
	
        Node@ newNode = scene.InstantiateXML(bullet_xml, position, Quaternion());
        
		Node@ newNodeParticle = scene.InstantiateXML(smoke_xml, position, Quaternion(0.0f, yaw, pitch));
        
        RigidBody@ 		body  = newNode.GetComponent("RigidBody");
				
		body.ApplyImpulse( Quaternion(0.0f, yaw, pitch) * Vector3(0.0f,1.0f,0.0f) * 1950.0f);
    }

}[/code]

-------------------------

1vanK | 2017-01-02 01:12:28 UTC | #2

Xml files with particles is ultra big. May be reason of freeze is parsing but lot loading. Are you using release version of engine? (Debug version is really slowly)

-------------------------

1vanK | 2017-01-02 01:12:28 UTC | #3

You can not use instaniate for particles, just add particle emitter componet with particle effect

-------------------------

Cpl.Bator | 2017-01-02 01:12:28 UTC | #4

yes , i use release version of the player, i compiled myself with vs2015.
but, there is no way to pre-load all xml in memory and instanciate particle / whatever directly with the RAM ?

[quote]You can not use instaniate for particles, just add particle effect componet[/quote]

yes, it's good idea , but my particle object have a script for remove itself. i will try this way. but, my first question still valid :slight_smile:

-------------------------

cadaver | 2017-01-02 01:12:29 UTC | #5

In the AngelScript API there some convenience overloads for InstantiateXML that don't directly exist in C++ API. One of them is to instantiate from a XMLFile, which you can preload into RAM, in which case XML parsing has already happened and it should be fairly fast. Another overload (also in C++) takes an XMLElement that should be the root of the scene/prefab data.

[urho3d.github.io/documentation/1 ... lass_Scene](http://urho3d.github.io/documentation/1.5/_script_a_p_i.html#Class_Scene)

-------------------------

Cpl.Bator | 2017-01-02 01:12:29 UTC | #6

hi cadaver, thx for reply.

well , if i understand the processus :

- load xml with scene@
- disable node@ with SetEnabledRecursive(true)
- clone the node@ when needed with Clone() and enable it.

it's the correct way ?

-------------------------

Cpl.Bator | 2017-01-02 01:12:29 UTC | #7

ok, my way is not the good way , the problem still here , this is a part of my script :

[code]class Canon : ScriptObject{
	
	...
	
	XMLFile@ 	smoke_xml 	= cache.GetResource("XMLFile", "Objects/smokeCanon.xml");
	Node@		particle_instance;
	
	void DelayedStart(){
		
		particle_instance = scene.InstantiateXML(smoke_xml, Vector3(), Quaternion());
		particle_instance.SetEnabledRecursive(false);
	
	}
	
	
	...
	
	void Shoot()
    {       
		// no freeze here
		//
        Vector3 position    = node.GetChild("hotpoint", true).worldPosition;
        Node@ newNode = scene.InstantiateXML(bullet_xml, position, Quaternion());
        
		// freeze here
		//
		Node@ newNodeParticle = particle_instance.Clone();
		newNodeParticle.SetEnabledRecursive(true);
        newNodeParticle.SetTransform(position, Quaternion(0,yaw,pitch)); // axis inverted xyz -> zyx , no error ;)
		
		// apply impulse on the heavy bullet
		//
        RigidBody@ 		body  = newNode.GetComponent("RigidBody");
		body.ApplyImpulse( Quaternion(0.0f, yaw, pitch) * Vector3(0.0f,1.0f,0.0f) * 1950.0f);
		
    }
	
}[/code]


i use DelayedStart() for instanciate the xml file, and i use clone method inside shoot() method for create new instance. but freeze still here when i shoot.

-------------------------

Cpl.Bator | 2017-01-02 01:12:29 UTC | #8

Resolved.
i use the technique described above, and i unchecked "Serialize particles" in the particle emitter.

-------------------------

