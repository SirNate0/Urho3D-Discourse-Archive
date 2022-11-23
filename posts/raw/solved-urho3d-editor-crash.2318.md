itisscan | 2017-01-02 01:14:42 UTC | #1

I often receive annoying crash after that i have added some codes in AS script. So it looks the following - i write code in AS through CodeBlock IDE, save the script file, open the editor and get the unexpected error. ([url]http://imgur.com/a/tqsam[/url])

Also i have noticed that if i delete these code (basically 2. PART), then all works fine. 

[code]
class ArrowUI : ScriptObject
{	

void Start()
{
	// HERE START 1. PART
	// Clear previous values
	dirsResult.Clear();
	dirsLong.Clear();

	// Push initial values
	dirsLong.Push(balloonNode.position);
	dirsResult.Push(balloonNode.position);

	// Set initial value
	GoalPosition = balloonNode.position;
        
	// Create 5 random points for the distance
	for(int i = 0; i < 5; i++)
	{
		// Generate random rotation around Y axis
		windDirs[i] = Vector3(0.0f, Random(0, 30), 0.0f);
		// Generate random length along Z axis
		dirsLong.Push(Vector3(dirsLong[i].x, 0.0f, dirsLong[i].z + Random(50, 500)));
		
		// Rotate length according to generated random rotation around Y axis
		Quaternion dirRot;
		dirRot.FromEulerAngles(windDirs[i].x, windDirs[i].y, windDirs[i].z);
		Vector3 goalPartDistance = dirRot * dirsLong[i + 1];
		
		// Get the terrain 			
		Node@ terrain = scene.GetChild("Terrain", true);
		Terrain@ terrainComponent = terrain.GetComponent("Terrain", true);	
		// Get the height value
		float height = terrainComponent.GetHeight(goalPartDistance);
		// Set the returned height value to the new point of distance
		goalPartDistance.y = height;
		// Save the distance's point
		dirsResult.Push(goalPartDistance);
	}
	
	// Save the goal position
	goalPosition = dirsResult[5];
        
	// Get the root check node
	Node@ checkNode = scene.GetChild("CheckNode", true);	
	// Remove all childrens
	checkNode.RemoveAllChildren();
        
	// HERE START 2. PART
	// Create 5 nodes for  distance's generated points
	for(int i = 0; i < 5; i++) 
	{
		Node@ checkZone = checkNode.CreateChild("CheckZone_" + i);
		checkZone.AddTag("CheckZone");
		checkZone.position = dirsResult[i + 1];

		RigidBody@ body = checkZone.CreateComponent("RigidBody");
		body.trigger = true;

		CollisionShape@ shape = checkZone.CreateComponent("CollisionShape");
		shape.SetBox(Vector3(200.0f, 150.0f, 1.0f));

		// Create the check zone logic object
		checkZone.CreateScriptObject(scriptFile, "CheckZone");
			
		CheckZone@ checkZoneComponent = cast<CheckZone>(checkZone.scriptObject);
		checkZoneComponent.checkZoneId = i + 1;
	}
}
}
[/code]

[code]class CheckZone : ScriptObject
{	
	int checkZoneId = 1;
	bool isChecked = false;
}[/code]

So basically it removes old nodes, and create new nodes with new position in Start() method.

I suppose it may happens due to old nodes are removed from the scene. (checkNode.RemoveAllChildren()). But old nodes removing happens only in Start() method and in principle the error should not be though I can miss something.

There how looks crashdamp opened in VS2013. 
[url]http://imgur.com/a/jcx2D[/url]
In editor's logs i do not get any errors.

Any ideas why i get crash and how can fix it ?

Thanks.

-------------------------

Lumak | 2017-01-02 01:14:42 UTC | #2

This looks suspicious:
[code]checkZone.position = dirsResult[i + 1];[/code]
because i ={0:4}, but the dirResult[5], hence you go out of bounds.

-------------------------

cadaver | 2017-01-02 01:14:43 UTC | #3

You should get an AngelScript exception from that and not a crash. I recommend running editor in debug to see where in the engine it's crashing.

-------------------------

itisscan | 2017-01-02 01:14:44 UTC | #4

[quote="Lumak"]This looks suspicious:
[code]checkZone.position = dirsResult[i + 1];[/code]
because i ={0:4}, but the dirResult[5], hence you go out of bounds.[/quote]

I declare the 6-element array like this 

[code]Array<Vector3> dirsResult(6);[/code]

hence i should not  go out of bounds.

[quote="cadaver"]You should get an AngelScript exception from that and not a crash. I recommend running editor in debug to see where in the engine it's crashing.[/quote]

Okey, i will try to run editor in debug.

-------------------------

itisscan | 2017-01-02 01:14:44 UTC | #5

[quote="cadaver"]You should get an AngelScript exception from that and not a crash. I recommend running editor in debug to see where in the engine it's crashing.[/quote]

So what i have noticed is following - 

If i run editor with above posted code in debug, then i can't reproduce crash. I tried to do same steps as with release, but nothing. It simply runs fine. 

Also I have noticed that editor randomly crashes in release build. I mean that sometimes editor works fine, but sometimes i get crash, if 
[quote]i write code in AS through CodeBlock IDE, save the script file, open the editor and get the unexpected error. [/quote]

But if I replace this line
[code]checkNode.RemoveAllChildren();[/code]

with these lines, which should provide the same logic. (Just delete old nodes).

[code]
Array<Node@> checkNodes = scene.GetNodesWithTag("CheckZone");   
for( int n = 0; n < checkNodes.length; n++ ) 
{
    // (Note. checkNode does not have tag - "CheckZone")
    checkNode.RemoveChild(checkNodes[n]);
}
[/code]

Then i always get crash in release/debug build. I tried to debug in VS2013 and i got the following situation - [url]https://snag.gy/KO6ER4.jpg[/url].
It seems that old nodes were deleted, but engine still sends event to them.  

if i comment this line [code]checkNode.RemoveChild(checkNodes[n]);[/code] , then also all works fine. 

Any ideas how can fix that ?

-------------------------

cadaver | 2017-01-02 01:14:44 UTC | #6

I tried to adapt and run your code, including script live reloading, in release mode but didn't get a crash.

Can you post the complete working script file? The snippet in the beginning of the thread had missing variables and other errors, so I had to adapt it and was no longer running the original code.

Normally an object should remove itself globally as an event receiver upon destruction.

-------------------------

itisscan | 2017-01-02 01:14:44 UTC | #7

[quote="cadaver"]I tried to adapt and run your code, including script live reloading, in release mode but didn't get a crash.

Can you post the complete working script file? The snippet in the beginning of the thread had missing variables and other errors, so I had to adapt it and was no longer running the original code.

Normally an object should remove itself globally as an event receiver upon destruction.[/quote]

There is full script file [url]http://pastebin.com/rmPE2y0s[/url]. There are 6 classes. (Character, Balloon, CameraScript, HotAirBalloonUI, ArrowUI, CheckZone). 
The snippet in the beginning of the thread is located in ArrowUI class.

-------------------------

cadaver | 2017-01-02 01:14:44 UTC | #8

Thanks. Now I of course notice it also needs some specific scene content, will probably not go into too much detail testing this.

EDIT: Managed to repro a crash using a crude approximation of your scene derived from VehicleDemo, and having some of the named nodes your scripts are expecting.

-------------------------

cadaver | 2017-01-02 01:14:44 UTC | #9

Further detail: this can be reproduced with a minimal script. I believe the trigger is that you hold an array of nodes which have script instances, then you remove those nodes from the scene. Because they're still in the array, they haven't been deleted yet, but exist as detached from the scene. When the script reload event comes, these script instances still try to receive the script reload event, though they should be destroyed by now (as the array fell out of scope at the end of the Start() function)

-------------------------

cadaver | 2017-01-02 01:14:45 UTC | #10

Fixed in master branch. This was a legitimate vulnerable piece of code related to event receivers being added and removed during event sending, in this case the resource reload event.

-------------------------

itisscan | 2017-01-02 01:14:45 UTC | #11

[quote="cadaver"]Fixed in master branch. This was a legitimate vulnerable piece of code related to event receivers being added and removed during event sending, in this case the resource reload event.[/quote]

I have built the master branch. Now it works fine. I mean that it does not crash at once after AS editing and saving. However, very rarely in debug/release i have crash and i can't understand what can cause it. (may be the same code, that remove old nodes) 
Look, [url]http://imgur.com/a/u2A2b[/url] i made screenshots half of call stack.

UPDATED.
I took 4 files from the master branch (Source/Urho3D/Core/Context.cpp, Source/Urho3D/Core/Context.h, Source/Urho3D/Core/Object.cpp, Source/Urho3D/Engine/Console.cpp, basically which you updated)
and replaced in 1.6 release code and built it. Then I have not got any crashes yet.

-------------------------

