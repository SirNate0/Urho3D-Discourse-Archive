fnadalt | 2019-07-18 16:04:06 UTC | #1

Hi everyone. I'm having trouble with an angelscript runtime error. I can't find where it is generated exactly, since I didn't find a way to reproduce it. It happens on scene change, after Scene::LoadXML. I change scenes back and forth until it takes place. The entire app is run from a Main.as. This scripts receives the "SwitchScene" event and loads the new scene. The error does not happen after switching to a particular scene. The engine if compiled from git 3be92ea61e39d8a31999ab5a0833473ea220e6ca (2019-07-17), but the error started from an one moth old git pull. gdb backtrace including some app log https://pastebin.com/KT3fH5FT. Would anyone please help me at least suggesting where to continue the search from? If full source needed I can push it to github.

The game consists of a flying transporter that lands on platforms and picks people and goods to carry to some other location. There are local and replicated nodes since it supports single player mode as well as client and server functionality. I observed that there seems to be a problem with the avatar (ship) to call its ScriptObject::Stop function, and, that seems to be underlying the issue. From time to time it reports [Thu Jul 18 12:57:27 2019] ERROR: :0,0 Failed in call to function 'Prepare' with 'void Ship::Stop()' (Code: asCONTEXT_ACTIVE, -2).... ...?

-------------------------

Avagrande | 2019-07-18 18:10:01 UTC | #2

Might not be exactly what you are facing.. 
but I have been dealing with runtime errors in LUA for quite a bit now and I got the hang of whats going on ( I think )  Urho3d handles is pointers based on scenes so each scene has control over its resources such that if you create a texture in code ( without the cache ) and assign it to a scene and then delete the node that holds that resource, the resource itself will be deleted as-well and any further attempts to use it will cause either a SIGABRT or SIGSEGV. This can also occur if you double delete the resource by deleting it via the garbage collector and then the shared_ptr c++ wise. 

So if you are transferring objects between scenes you may wish to create a "transition" scene where you will place those resources as the first scene is being deleted this will assure that the assets are not deleted and then once the next scene has completed loading you can delete the transition scene.  Note that this applies mainly to resources generated in the scripting world and not via the asset cache. 

hope that helps.

-------------------------

Leith | 2019-07-19 03:15:45 UTC | #3

What I noticed about your stack dump was the calls to angelscript GarbageCollection - which is meant to be disabled (at least for script objects!) This occurs at around line 96 in the dump you provided.

-------------------------

Leith | 2019-07-20 05:52:26 UTC | #4

Did you get this issue resolved? I'd be happy to take a crack at debugging the issue if you still want help. I used to be great at ASM, on 8, 16 and 32 bit platforms. When we went to 64 bit, I chose not to pursue assembly language, but I learned a crapload about debugging from my time in asm, which holds me in good stead today. I can recognize the registers which hold input arguments, and I can recognize which pointers are bad. I can step asm and set breakpoints intelligently to track down issues in code, and even without appropriate debug symbols being available in the code I am debugging. Also, I like puzzles.

-------------------------

fnadalt | 2019-07-21 01:07:55 UTC | #5

Little embarrasing I think. Just when I thought I had been quite "neat and clean" on setting object references to null in every ScriptObject::Stop(), I figured out I hadn't set null the very Node@ avatarNode in GamePlay scene Stop method. That seemed to have solved the thing, at least so far.

-------------------------

