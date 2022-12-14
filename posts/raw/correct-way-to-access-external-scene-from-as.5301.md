Leith | 2019-07-17 04:43:06 UTC | #1

My C++ application 'asynchronously' loads a scene that contains a ScriptInstance attached to an otherwise empty node... it's just a simplified test for c++/angelscript interop.
I rely on Urho to instantiate the test angelscript object during scene loading...

The following script appears to run without problems in the (old) editor, but when called from a c++ app built against the current master branch (with no changes to the codebase), the commented lines cause Urho to crash when the Update script method "tries" to return to Scene::Update... basically I'm trying to get access, from within script, to the scene which owns the node which owns the ScriptInstance...

No exception is generated by angelscript - execution of the method always completes, but "on the way out" (as we return to caller Scene::Update) we crash for some odd reason in StringHash equality compare with a clearly corrupted callstack (RAX holds an invalid pointer sourced from a corrupt input parameter on the stackframe).

What am I doing wrong here, that could cause stack corruption on the c++ call stack?

[code]
class Actor:ScriptObject
{
	String actorName="zombie1";
	Node@ ownNode_;

	bool hasTarget_;
	Actor@ Target_;
}


class Zombie:Actor
{
	void Start(){
		ownNode_ = node;
	}

	void Update(float dT){
		Print("Update ZOMBIE: "+actorName);

	//	Scene@ myScene = scene;
//		if(myScene is null)
//			return;

		Print("DONE!");
	}
[/code]

-------------------------

Leith | 2019-07-19 03:37:39 UTC | #2

I did a bit more digging into this issue, starting with a backtrace of the call stack... with those lines uncommented, the Scene::Update(float) method is crashing just after broadcasting the scene update event... at that point, the code is attempting to access the Scene::smoothedTransforms_ variantmap, and we crash, evidentally because the Scene has somehow been destroyed, such that "this" has become an invalid pointer, and as a consequence, accessing any member is an invalid operation.

Now I was curious, so I tracked down where the "scene" global is being registered, which is in SceneAPI.cpp:
[code]
    engine->RegisterGlobalFunction("Scene@+ get_scene()", asFUNCTION(GetScriptContextScene), asCALL_CDECL);
[/code]

Note the "+" symbol... that's an auto-handle, my understanding is that the "+" tells angelscript to automatically add one to the RefCount, such that the object in question won't be destroyed when it goes out of scope in the script.
However according to my experiment, accessing the scene global property from script is causing the scene to be garbage collected by angelscript, despite the use of auto handle in the declaration.

Am I not understanding something here? :)

-------------------------

Leith | 2019-07-20 06:05:12 UTC | #3

Storing the scene object handle (returned by global property getter) in a script global variable makes the problem go away - since the object reference never goes out of scope, the scene is not destroyed out from under our feet... this is definitely not an ideal solution.

I have to ask myself about this ownership arrangement, whereby querying for access to the container Scene transfers ownership of the Scene object lifetime from C++ to AngelScript... at least now I know exactly what's been going on, even if I don't completely understand why things are the way they are (with respect to how we register certain classes with angelscript).

I'm going to mark this workaround as a Solution because it does solve the problem, however I am far from happy with this outcome.

-------------------------

SirNate0 | 2019-07-19 13:06:33 UTC | #4

Is the scene in question stored in a shared pointer somewhere else in your application? It occurs to me that if it's not there behavior described might be expected, as when we leave the AngelScript code the ref count would be zero and the scene would be destroyed.

-------------------------

Leith | 2019-07-20 06:05:12 UTC | #5

Yep, the scene is held by a sharedptr within my state manager (implemented as a separate scene and a fistful of custom components).

[EDIT]
NOPE - On closer inspection, the GamePlayState object is using a raw pointer to store the current game scene - mystery solved! I should know better than to use a raw pointer for a storage type - its acceptable to hand around raw pointers as call arguments, but bad form to use them to hold anything... mea culpa
I had initially considered the possibility that I was not holding onto the scene correctly, and made the very blind assumption that since I had a manager in place, ownership should be clear - but the manager was poorly formed, and is currently undergoing some brutal refactoring and verification - where one egg is bad, there's usually more

-------------------------

