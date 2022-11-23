NiteLordz | 2017-01-02 01:02:48 UTC | #1

I am trying to load a scene that has a ScriptInstance attached to it. The Start() method of the script does not fire though.  Inspecting the scene xml file, i have the following component attached to the scene node

[code]
<component type="ScriptInstance" id="10">
	<attribute name="Delayed Method Calls" value="0" />
	<attribute name="Script File" value="ScriptFile;Scripts/TestInstance.as" />
	<attribute name="Class Name" value="BasicInput" />
</component>
[/code]

How can you make a script auto execute ? 

Note, in the cpp file that generated the scene xml file, the following code was executed

[code]
ScriptInstance* instance = scene_->CreateComponent<ScriptInstance>();
result = instance->CreateObject(cache->GetResource<ScriptFile>("Scripts/TestInstance.as"), "DoSomething");
instance->Execute("void Start()");
[/code]

-------------------------

cadaver | 2017-01-02 01:02:49 UTC | #2

Does the class name match what's in the script file? Does the class inherit from the empty interface ScriptObject? (this is only required so that C++ side can pass a known class to AngelScript when you request the script object)

Here's a minimal example I tested completely inside the editor. The print from the Start function gets printed each time I load the scene.

Scene file:

[code]
<?xml version="1.0"?>
<scene id="1">
	<attribute name="Name" value="" />
	<attribute name="Time Scale" value="1" />
	<attribute name="Smoothing Constant" value="50" />
	<attribute name="Snap Threshold" value="5" />
	<attribute name="Elapsed Time" value="0" />
	<attribute name="Next Replicated Node ID" value="3" />
	<attribute name="Next Replicated Component ID" value="4" />
	<attribute name="Next Local Node ID" value="16777216" />
	<attribute name="Next Local Component ID" value="16777216" />
	<attribute name="Variables" />
	<attribute name="Variable Names" value="" />
	<component type="Octree" id="1" />
	<component type="DebugRenderer" id="2" />
	<node id="2">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="" />
		<attribute name="Position" value="0 -3.94427 7.88854" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="ScriptInstance" id="3">
			<attribute name="Delayed Method Calls" value="0" />
			<attribute name="Script File" value="ScriptFile;Scripts/TestScriptObject.as" />
			<attribute name="Class Name" value="TestScriptObject" />
		</component>
	</node>
</scene>
[/code]

TestScriptObject.as:

[code]
class TestScriptObject : ScriptObject
{
  void Start()
  {
    Print("TestScriptObject Start() called");
  }
}
[/code]

-------------------------

NiteLordz | 2017-01-02 01:02:49 UTC | #3

Thank you!  so i figured out what the problem was.  When i setup the test bed for this, i called

[code]context_->RegisterSubsystem(new Script(context_));[/code] 

after i loaded the scene. 

Thanks again !

-------------------------

cadaver | 2017-01-02 01:02:50 UTC | #4

Ah yes, as it's Script subsystem constructor which does RegisterScriptLibrary() (register component types and factories) in that case you should get unknown component errors in the log.

-------------------------

NiteLordz | 2017-01-02 01:02:50 UTC | #5

Yep, was a product of coding late at night.

-------------------------

rogerdv | 2017-01-02 01:02:50 UTC | #6

A question about this, where should I declare a variable to make it global and acccesible by that script? I need to implement same mechanism (execute script on scene loading), but the script must access the list of NPCs, the player, etc.

-------------------------

