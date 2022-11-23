Bluemoon | 2017-01-02 01:01:36 UTC | #1

I have an application written entirely in script, in it you'ld have to shoot down some drone like objects. The Node for the Drone has a ScriptObject implementation named DroneObject created into it while that of the bullet has BulletObject created into it.
Below is the node collision handling routines of the BulletObject script object
[code]
	void HandleNodeCollision(StringHash eventType, VariantMap& eventData)
	{
		Node@ otherNode = eventData["OtherNode"].GetPtr();
		DroneObject@ droneObj = cast<DroneObject>(otherNode.scriptObject);		
		
		if(droneObj !is null)
		{
			droneObj.OnHit();
		}
		
		Destroy();
	}
[/code]

Everything works well. But when I try to implement this same application in c++ I notice a strange issues.
Now just like the fully scripted application, the drone and the bullet nodes have their respective ScriptObject created into them. But the line below in the BulletObjects HandleNodeCollision
[code]DroneObject@ droneObj = cast<DroneObject>(otherNode.scriptObject);[/code]
always returns a null pointer whether the node DroneObject script object or not. Even when I use another method to retrieve the script object, like
[code]
ScriptInstance@ sInst = cast<ScriptInstance>(otherNode.GetComponent("ScriptInstance"));
DroneObject@ droneObj = cast<DroneObject>(sInst.scriptObject);
[/code]
i still get a null pointer. Every other thing works, but in the part were I have to retrieve a scriptObject from a  node null is returned, no error is thrown and the application log shows no error either. What am I doing wrong or is it a bug coz its still the same ScriptObject files I use for both the fully scripted app and the C++ app

-------------------------

Azalrion | 2017-01-02 01:01:36 UTC | #2

Is the HandleNodeCollesion function defined or included in the same ScriptFile as the DroneObject class?

-------------------------

Bluemoon | 2017-01-02 01:01:36 UTC | #3

[quote="Azalrion"]Is the HandleNodeCollesion function defined or included in the same ScriptFile as the DroneObject class?[/quote]

No its not, It is defined in its own ScriptFile but includes the script file for the DroneObject class. Below is the file
[code]
#include "Scripts/DroneObject.as"

///Bullet Object Class
class BulletObject : ScriptObject
{
	float termTime;
	float termTimeCounter;
	
	
	BulletObject()
	{
		termTime = 1;
		termTimeCounter = 0;
	}
	
	
	void Start()
	{
		SubscribeToEvent(node, "NodeCollision", "HandleNodeCollision");
	}
	
	
	void FixedUpdate(float timestep)
	{
		termTimeCounter += timestep;
		
		if(termTimeCounter >= termTime)
		{
			Destroy();
		}
	}
	

	void HandleNodeCollision(StringHash eventType, VariantMap& eventData)
	{
		Node@ otherNode = eventData["OtherNode"].GetPtr();
		DroneObject@ droneObj = cast<DroneObject>(otherNode.scriptObject);
		
		if(droneObj !is null)
		{
			droneObj.OnHit();
		}
		
		Destroy();
	}
	
	void Destroy()
	{
		node.Remove();
	}
}

[/code]

-------------------------

Bluemoon | 2017-01-02 01:01:36 UTC | #4

Now I get it, The ScriptObjects that will inter-relate have to be from the same scriptfile. I made the correction and now its working. Thanks Azalrion

-------------------------

Azalrion | 2017-01-02 01:01:36 UTC | #5

Yep basically, because they were declared in what urho saw as two different script files and bound then into angelscript under different modules so couldn't cast, either you have a master script file like NinjaSnowWars does importing everything into a single module or you can declare them shared: [angelcode.com/angelscript/sd ... hared.html](http://www.angelcode.com/angelscript/sdk/docs/manual/doc_script_shared.html)

-------------------------

