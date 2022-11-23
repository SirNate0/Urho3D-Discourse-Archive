TrevorCash | 2017-09-12 20:31:45 UTC | #1

Hello,

I have a line in AngleScript:
>     WeakHandle weakGridHandle = gridworld.GetGrid(gridworld.RealToGrid(node.position));
>     	currentGrid = weakGridHandle.Get();

The function GetGrid returns a WeakPtr<Grid>.

However whenever these lines are run, i get an assert error in ReCounted::AddRef() on the c++ side.

Both gridWorld and grid objects are registered in c++:
>     RegisterObject<GridWorld>(engine, "GridWorld");
>     RegisterObject<Grid>(engine, "Grid");

And the registration for the function that causes the issue:

> engine->RegisterObjectMethod("GridWorld", "Grid& GetGrid(Vector3 globalPos)", asMETHODPR(GridWorld, GetGrid, (Vector3), WeakPtr\<Grid>), asCALL_THISCALL);

Grid is directly derived from Object.

Any Ideas of what i could be missing? 

Thanks, Trevor

-------------------------

Eugene | 2017-09-12 11:00:02 UTC | #2

[quote="TrevorCash, post:1, topic:3557"]
engine-&gt;RegisterObjectMethod(“GridWorld”, “Grid& GetGrid(Vector3 globalPos)”, asMETHODPR(GridWorld, GetGrid, (Vector3), WeakPtr), asCALL_THISCALL);
[/quote]

I see that you are lying here
> **Grid&** GetGrid(Vector3 globalPos)
> GetGrid, (Vector3), **WeakPtr**

What's actual `GetGrid` signature?

-------------------------

TrevorCash | 2017-09-12 13:50:52 UTC | #3

Sorry did not notice the signature got messed up when I pasted in:

Here is the full signature for GetGrid:
> engine->RegisterObjectMethod("GridWorld", "Grid& GetGrid(Vector3 globalPos)", asMETHODPR(GridWorld, GetGrid, (Vector3), WeakPtr\<Grid>), asCALL_THISCALL);

Updating Original Post.

-------------------------

Eugene | 2017-09-12 13:59:26 UTC | #4

Signature of AngelScript function should match the signature of C++ function. If you tell AS that `Grid&` is returned, `Grid&` shall be returned.
You probably cannot expose template things to AS including `WeakPtr<Grid>` (I may be wrong here), so you should return something like `Grid*` in both C++ and AS signatures. Urho usually use wrappes to not disturb public interface.

-------------------------

Eugene | 2017-09-12 14:14:39 UTC | #5

You could also try to use `WeakHandle` return value in AS signature, but it's a bit hacky.

-------------------------

TrevorCash | 2017-09-12 19:30:49 UTC | #6

The problem seems to be with AngleScript attempting to delete the GridWorld Object after the following call in the API:

> static SharedPtr\<GridWorld> GetGridWorld()
> {
>     return SharedPtr\<GridWorld>(GetScriptContext()->GetSubsystem\<GridWorld>());
> }

On the C++ side, 1 new GridWorld is created and registered as a subsystem in the global context.
A SharedPtr to the GridWorld also exists as a member in my Application class just to make sure I don't run out of references.  

I put a break point in the destructor of GridWorld and that is never called.  However I keep getting crashes in ReleaseRef()

-------------------------

Victor | 2017-09-12 19:56:31 UTC | #7

I've not used AngleScript before, however that does look odd the way it's written. If GridWorld is already created as a Subsystem singleton, couldn't you do something like:

    SharedPtr<GridWorld> GetGridWorld() { 
            return GetScriptContext()->GetSubsystem<GridWorld>();
    }

Again, I've not used AngleScript, but your return statement looks like you're creating a new object that deletes itself once it's outside of the scope of the function.

-------------------------

TrevorCash | 2017-09-12 20:06:15 UTC | #8

[quote="Victor, post:7, topic:3557, full:true"]
I've not used AngleScript before, however that does look odd the way it's written. If GridWorld is already created as a Subsystem singleton, couldn't you do something like:

    SharedPtr<GridWorld> GetGridWorld() { 
            return GetScriptContext()->GetSubsystem<GridWorld>();
    }

Again, I've not used AngleScript, but your return statement looks like you're creating a new object that deletes itself once it's outside of the scope of the function.
[/quote]

Does casting a pointer to a shared pointer result in a new object?  I thought perhaps that cast would simply temporarily increase the reference of the GridWorld Itself.

If I do what you suggest - I get a compiler error because there is no implicit conversion from raw pointer to SharedPtr.

I did try simply this:
> static GridWorld* GetGridWorld()
> {
>     return GetScriptContext()->GetSubsystem\<GridWorld>();
> }

Which interestingly now does result in the GridWorld destructor being invoked. which of course still crashes..

There must be a way to keep Angel-script from taking control of singleton subsystems like this.

Again the AngelScript code:

> WeakHandle weakGridHandle = gridworld;

Results in the crash.

-------------------------

Eugene | 2017-09-12 20:06:56 UTC | #9

[quote="TrevorCash, post:6, topic:3557"]
The problem seems to be with AngleScript attempting to delete the GridWorld Object after the following call in the API:
[/quote]

If you have a problem with AngelScript, always share both C++ signature and binding code, it really helps.
Keep in mind that **AngelScrpt has no signature validation in any form** (except simple syntax errors). So, incorrect signature usually lead to crash during function call.

-------------------------

TrevorCash | 2017-09-12 20:18:43 UTC | #10

In my Application::Start():

> RegisterGridWorldAPI(GetSubsystem<Script>()->GetScriptEngine());
> context_->RegisterSubsystem(new GridWorld(scene_, cache, camera, cameraPivot, 4, context_));

In my GridWorldAPI.cpp:
> void RegisterGridWorldAPI(asIScriptEngine* engine)
> {
>     RegisterGridWorld(engine);
> }

> static void RegisterGridWorld(asIScriptEngine* engine)  
> {
>      RegisterObject<GridWorld>(engine, "GridWorld");
>
> 	engine->RegisterGlobalFunction("GridWorld@ get_gridworld()", asFUNCTION(GetGridWorld), asCALL_CDECL);
> }

> static GridWorld* GetGridWorld()
> {
>     return GetScriptContext()->GetSubsystem\<GridWorld>();
> }

Edited

-------------------------

Eugene | 2017-09-12 20:30:45 UTC | #11

Try `GridWorld@+ get_gridworld()`

-------------------------

TrevorCash | 2017-09-12 20:31:13 UTC | #12


[quote="Eugene, post:11, topic:3557, full:true"]
Try `GridWorld@+ get_gridworld()`
[/quote]

Thanks Eugene, this worked. Also adding @+ to the member method signatures worked for the GetGrid functions.

Closing

-------------------------

Eugene | 2017-09-12 20:34:14 UTC | #13

I recommend you to read a bit about AS bindings, they are quite sophisticated sometimes.
The main usage of `@` references is to give new object to AS (you should AddRef here)
I suggest to always use `@+` references because they behave as native pointers in bindings.

-------------------------

