primem0ver | 2018-10-01 15:04:48 UTC | #1

I am trying to decide between this and Panda3D.  So far I am leaning toward Urho3D.  However, I am growing more convinced I will need to rewrite part of the engine so that it will work with my project (I would need to do the same with Panda).  I have a few basic questions about object access.

The basic problem with this engine when it comes to my project is security.  I know this may sound a bit strange for a graphics engine meant to be used for gaming but my project is not a game and there is an important collection of use cases where objects in a scene and in the UI must be kept secure from arbitrary script access.

Since scripts are giving access to the engine, I am guessing there is a way to gain access to most Urho3D objects (such as scene nodes and UI elements) through scripting.  So here are my questions:
1. Is this true?
2. How does a script gain access to objects?  Is there a hash table of object names?
3. If so... where in the code does this table exist? (I have found several tables so far but all are of object attributes, types, categories, factories, etc... I have not not found the table for the objects themselves)

My guess is that my project will need to provide or modify the underlying object management layer so that any script that should not have access to an object will get a null pointer/object if the object requires a higher security level than the script (or the application detects that security has been compromised).  My last two questions are: does this sound feasible?  If not, can scripting be disabled entirely?  (Perhaps build a version without scripting included?)

-------------------------

Modanung | 2018-10-01 16:24:23 UTC | #2

If you'd like to avoid scripting altogether you can compile the engine without scripting support using [build flags](https://urho3d.github.io/documentation/1.7/_building.html#Build_Options). Would that be what you're looking for?

-------------------------

primem0ver | 2018-10-01 16:48:40 UTC | #3

@ [Modanung](https://discourse.urho3d.io/u/Modanung)
Only if I am not able to replace the object management functionality.  Scripting is an essential part of my project.  It would be nice if some support is already there.  However, I cannot allow scripting that can indiscriminately gain access to any object in the scene or UI.  So if I can't limit access by replacing the object retrieval (lookup) mechanism, then yes.

-------------------------

Sinoid | 2018-10-02 03:22:34 UTC | #4

In theory you can use Angelscript to support more than one main context (presently there's the *app* and *immediate* contexts) with different constraints. 

---

In practice though, no - lots of work. What you describe is also fundamentally impossible without a client-server model. You will never have any degree of security if you intend this to be entirely client local.

I can't imagine what industry you'd be in that not letting clients (well, their IT dept) touch stuff would be okay, I've worked on PHA, FMEA, SIL, LOPA, leak-down, etc chemical safety software and always we never offered enough customization. It was a constant bitching point even though our software was so ephemeral that there was `nothing` beyond what the user defined (or a template).

End-user can't touch it ... that sounds like a job for robots like an assembly line.

Please don't tell me your company is in Ohio.

-------------------------

primem0ver | 2018-10-02 05:26:04 UTC | #5

@Sinoid 
lol.  Nope.  Not in Ohio.  Software like this doesn't exist yet.  I hope to get it out there before someone else thinks of it.  It does use a type of client-server model.  However, I would think that controlling access like I am suggesting wouldn't be that difficult if one thought of the need (specific set of use cases) ahead of time. From what your suggesting though, it sounds like that wasn't the intention of any 3D engine currently in existence.  If the source code doesn't provide a "neat", centrallly located way of resolving what object is being looked up by a script, I can just not use the internal script engine and build my own later (or have it built by someone more capable).

As for my approach: Since I currently don't have any formal training in security techniques there may be a few things I am not considering regarding security.  However, I designed my object manager like this: basically I have a lookup table of objects with both a saved key and an authorization level.  If a lookup is attempted using a script that originates from a user without the proper access level, or that script was inserted without the proper access key, trying to do a lookup for a "secured" object will fail and return a null object.  The point of this "security" in the gui/3d interface is not to keep "information" private.  It is to keep end users of a specific role from being able to perform specific tasks in certain use cases and/or contexts

As I said in my introductory post, I am prototyping.  My current task is to get the prototype out there and show it could work.  Then I will find a company that sees the potential of what I am building (which I am certain I can if done right) and together we will flesh out the real product.

-------------------------

Eugene | 2018-10-02 18:00:01 UTC | #6

Since scripting is not the mandatory part of the engine, you could hack script binding code and just remove all the singletones here, and all unwanted members. If you unbind everything except what you need, your scripts won't get any unwanted access.

Search for `RegisterGlobalFunction` and get rid of suspicious things like `get_ui`, leaving all simple functions like math, logging, etc.

-------------------------

primem0ver | 2018-10-02 18:16:56 UTC | #7

@Eugene
Thanks for your suggestion. Since you are a developer, perhaps you can answer this.  I was hoping to be able to fork/hack your project as you suggest.  I was hoping to do something a bit different though, depending on how object lookup is done in your library.

Do scripts result in looking up objects by name?  Is there a "central" hash table for 3d and ui objects? Or is it too complicated to mess with that aspect of the engine? If not, I could supply a base class to inherit from.

-------------------------

Eugene | 2018-10-02 18:29:51 UTC | #8

There are two really different types of script usage in Urho.
You could use script as entry point, and in this case it would be able to access things you directly exposed via global function bindings and objects declared in main script itself (it's pretty much everything).
OR you could attach you script to scene node. In this case, you will be able to get any other script bound to the _same_ scene.
There are no central hash table for everything, but you could access UI tree (from any script) and scene tree (from script belong to this scene) and iterate/cache all the information you need. Scene itself has hash table for all nodes and things you have in the scene too.
If you provide more specific task description, I'd suggest more specific solution.

-------------------------

primem0ver | 2018-10-04 17:41:53 UTC | #9

@Eugene
From what you are saying, I am guessing I should disable the “native” or embedded scripting altogether.  My application is not supposed to allow that approach.  Instead, it accesses objects by name and then allows certain things to be done with them.  What is allowed would be enirely up to the application's published functionality. Let me give you some specifics on what my software would do with scripting.

Much of what happens in a scene is supposed to be script-able.  In fact, that will usually be the basis for much of the animation and action that occurs as a scene progresses.  However, let’s say the script supplied with a mod or add-on wants to impose a tutorial mode where at a particular point in the scene, other functionality is temporarily disabled.  The DLC based add-on has a higher “level of access” than the user and disables the UI and other access until the user accomplishes a specific task.  The user then tries to circumvent this “lockout” by another custom addon/script.  The objective is to not allow the user (with a lower level of access) to accomplish this circumvention.  However, now let’s say that the user gets stuck on something later and needs help from a person with technical support access.  This support person’s level of access would be higher than the script.  So they would be able to disable the lockout or at least access an appropriate object in the scene.

At the core of the engine are two low level (not quite base) classes that represent this lock and key mechanism: a KeyedObject and an AccessAgent.  3D and UI objects inherit from KeyedObject while users and scripts inherit from AccessAgent.

-------------------------

Eugene | 2018-10-04 14:53:10 UTC | #10

[quote="primem0ver, post:9, topic:4574"]
From what you are saying, I am guessing I should disable the “native” or embedded scripting altogether
[/quote]

I suggest you to disable all parts of the scripting that you consider malicious.
As I understand, you want multiple levels of access. Some scripts are able to do certain things, some are not. Is it correct?

-------------------------

primem0ver | 2018-10-04 17:40:14 UTC | #11

More or less.  Though, the source of the script is more important than the content.  Example: In general, many or most activities are set in motion by a script provided by a published DLC/module.  Official scripts should always trump user mods.

-------------------------

Sinoid | 2018-10-05 01:27:06 UTC | #12

If you wish to use scripts for your own purposes but have them realistically impossible to mess with in release you could add CryptoPP as a dependency and just using one of it's asymmetric encryption methods so that as part of the release process you encrypt your scripts with your private-key and tweak the runtime to decrypt with your public-key.

That isn't perfect, but it's generally not viable for someone (especially in a small sample set like your program would have - you're not Facebook) to manage to do a one-way dupe. It won't protect your scripts strongly from inspection (you have to have the key), but will protect them from a fair bit beyond the layman ... what you say above is kind of dodgy about that specific bit.

You would have to go into the scripting bindings though and disable anything that accesses files (well, at least script-files). It's certainly doable that way, I think your biggest hassle would be making sure that you don't turn script-based development on your end into a nightmare for the sake of your release-end.

The `asymmetric-encryption == military-weapon` from the Wassenar thing hasn't been enforced for a long time and also never applied to any case where you could claim it as a copyright protection - which you could do here.

---

I'm not intimate with Lua, but now that I think about it since it was born for the power-generation industry it might actually have some sand-boxing capability built-in. I vaguely remember the subject, but it could've been that *what you choose to bind* **is** the sandbox.

-------------------------

Modanung | 2018-10-05 16:07:14 UTC | #13

@Sinoid Would that then come down to forking the engine to create custom script bindings?

-------------------------

Sinoid | 2018-10-06 20:40:20 UTC | #14

It'd mean forking, but I would think the best way to do it would be as an additional feature of the existing PAK loading stuff, which would just mean locking down script bindings. Tying it into PAK record reading would probably be pretty simple (CryptoPP is super easy to use, not sure if there are better libs nowadays though).

Although AS can compile to ASC which would be about as much of a hassle to reverse as C - you'd still have to lock everything down though so that an additional script can't be attached to a `template scene` or whatever to trick it into loading.

All that using CryptoPP would get you is it just being extremely impractical for anyone to tamper with files (they'd need your private key), it'd still be fairly easy to actually read them as if you can read them, they can read them with some effort.

-------------------------

