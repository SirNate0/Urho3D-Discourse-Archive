Dave82 | 2017-01-02 01:09:27 UTC | #1

Hi , so i can't tell whats exacly happening but in some cases calling ScriptInstance::CrateObject crashes. I couldn't figure out why...
The script works fine until i add another method then the game starts crashing afterwards.

[code]if (!scriptName.Empty())
{
	Urho3D::ScriptInstance * scrInst = this->CreateComponent<Urho3D::ScriptInstance>();
              // Cript instance is successfully created
	scrInst->CreateObject(GetSubsystem<Urho3D::ResourceCache>()->GetResource<Urho3D::ScriptFile>(scriptName + ".as") , "INFScript");
              // The program never reaches this part !
}[/code]

i think that (i suppose) there's a dangling pointer somewhere in either anglescript's or Urho's CreateObject function...


Here's the latest test i ran :

This works :

[code]class INFScript : ScriptObject
{
	void onPick()
	{
		INFGame@ game = getGame();
		Node@ key = node.GetChild("Security Key" , true);
		
		if (key !is null) game.switchToPuzzleMode();
		else game.enableDialog("The security panel is turned off.There's a keyhole on the panel" , 0 , 0 , null);
	}
}[/code]

changing to this and it just keeps crashing.

[code]class INFScript : ScriptObject
{
	void onPick()
	{
		INFGame@ game = getGame();
		Node@ key = node.GetChild("Security Key" , true);
		
		if (key !is null) game.switchToPuzzleMode();
		else game.enableDialog("The security panel is turned off.There's a keyhole on the panel" , 0 , 0 , null);
	}
         
	Overloaded function with a Node as a parameter
 	void onPick(Node@ inNode)
	{
	          
	}
}[/code]


[b]EDIT:[/b]

now thats strange... deleting few lines remove empty lines and now it works again...
The crash is totally unpredictable...

-------------------------

TheComet | 2017-01-02 01:09:36 UTC | #2

Can you give us a backtrace? Otherwise it's just guess work.

[code]scrInst->CreateObject(GetSubsystem<Urho3D::ResourceCache>()->GetResource<Urho3D::ScriptFile>(scriptName + ".as") , "INFScript");[/code]

If CreateObject() fails (for some reason) it could explain the crash.

-------------------------

Dave82 | 2017-01-02 01:09:37 UTC | #3

[quote]If CreateObject() fails (for some reason) it could explain the crash.[/quote]

Hi ! Yes the crash happens somewhere inside CreateObject (like i stated in my first post).When the crash happens the program never leaves the CreateObject function

[code]inst->CreateObject(blahblah);
LOGDEBUG("This line will never be written in the console if the program crashed...")[/code]

The problem is the crash is sooo rare i couldn't investigate it yet.It could be a dangling pointer or null pointer access but could be some *.as file parsing error... i have no idea.
I didn't modified my scripts for a week (i'm working on level design right now). So now the crash doesn't happen at all. The crash only happens if i add/remove some code to the script. But after a bit modifying (removing empty lines , swap function definitions in the script file etc) then the SAME code just works without crashing.

-------------------------

weitjong | 2017-01-02 01:09:41 UTC | #4

[quote="Dave82"]now thats strange... deleting few lines remove empty lines and now it works again...
The crash is totally unpredictable...[/quote]
It does not make any sense. IMHO, AngelScript should not be the root cause of your problem. Let me guess. You are using MSVC as your compiler toolchain and your project is 64-bit using DetourCrowd? If so, I think the root cause of the problem is with our integration of DetourCrowd into Urho3D. I have not done any investigation yet, but since we have enabled AppVeyor (our CI server using VS2015) to test run all the sample apps as part of the CI jobs, we have observed random segfault on 64-bit build of 39_CrowdNavigation for both STATIC and SHARED lib types. Note this is just a wild guess that your problem is related to this observation. You should probably log this as an issue to our GitHub issue tracker.

-------------------------

Dave82 | 2017-01-02 01:09:41 UTC | #5

[quote="weitjong"]
It does not make any sense. IMHO, AngelScript should not be the root cause of your problem. Let me guess. You are using MSVC as your compiler toolchain and your project is 64-bit using DetourCrowd? If so, I think the root cause of the problem is with our integration of DetourCrowd into Urho3D. I have not done any investigation yet, but since we have enabled AppVeyor (our CI server using VS2015) to test run all the sample apps as part of the CI jobs, we have observed random segfault on 64-bit build of 39_CrowdNavigation for both STATIC and SHARED lib types. Note this is just a wild guess that your problem is related to this observation. You should probably log this as an issue to our GitHub issue tracker.[/quote]

Thanks weitjong ! Yes i use MSVC but on a 32 bit system. I found some issues with DetourCrowd but only in the previous (1.4) version of Urho. Since 1.5 these issues were gone (Crashes in CrowdManager, and NavigationMesh->Build()). It seems that this is working now.
The problem is that the program never leaves the ScriptInstance's CreateObject function after the crash. But i only tested it like this :


[code]
URHO3D_LOGINFO("The program reaches this point");
scrInst->CreateObject(cache->GetResource<ScriptFile>("Scripts/" + scriptName + ".as") , "INFScript");
URHO3D_LOGINFO("If the program crashes this will not print");[/code]

Thats just my experience but ofcourse i could be wrong... I didn't have time to examine ScriptInstance's source code yet , i'm busy with job and life , all my free time goes into level design and modelling.

-------------------------

