Enhex | 2017-01-02 01:07:06 UTC | #1

This is really weird.
It only happens in my game when the player dies while the monster attack animation plays, and the scene clears after attack animation ends and a the idle animation starts.
The scene clear is used for a level restart, removing everything and re-creating the scene.

The assertions seems to originate from components deleting things on destruction.
Each time it's one of the following:

[code]delete compoundShape_;[/code] in ~RigidBody()
[spoiler][code]btFreeDefault(void * ptr) Line 29	C++
btAlignedFreeDefault(void * ptr) Line 86	C++
btAlignedFreeInternal(void * ptr) Line 177	C++
btAlignedAllocator<btCompoundShapeChild,16>::deallocate(btCompoundShapeChild * ptr) Line 90	C++
btAlignedObjectArray<btCompoundShapeChild>::deallocate() Line 117	C++
btAlignedObjectArray<btCompoundShapeChild>::clear() Line 190	C++
btAlignedObjectArray<btCompoundShapeChild>::~btAlignedObjectArray<btCompoundShapeChild>() Line 134	C++
btCompoundShape::~btCompoundShape() Line 47	C++
[External Code]	
Urho3D::RigidBody::~RigidBody() Line 97	C++
[/code][/spoiler]

Some HashMap in ~PhysicsWorld()
[code]operator delete[](void * ptr) Line 82	C++
Urho3D::AllocatorUninitialize(Urho3D::AllocatorBlock * allocator) Line 82	C++
Urho3D::HashMap<Urho3D::StringHash,Urho3D::Variant>::~HashMap<Urho3D::StringHash,Urho3D::Variant>() Line 246	C++
Urho3D::PhysicsWorld::~PhysicsWorld() Line 179	C++[/code]

When AnimationController is destroyed, and [code]Vector<AnimationControl> animations_;[/code] is destroyed.

If I don't play the idle animation, the first kind of assertions stop happening (destruction ones), but I still get this assertion in asCContext::CleanReturnObject():
[code]asASSERT( m_regs.objectType != 0 );[/code]
Which originates from  ScriptFile::Execute().
I'm not sure but I think this one doesn't originate from scene->Clear().
It also may happen when the idle animation is enabled but quite rarely.

I use a ScriptInstance on the scene node and have a script entry point "Main" class that derives from ScriptObject.
When the scene clears, the scriptInstance is removed, and when the level is reloaded a new scriptInstance is created. Maybe it causes problems with the script engine state?

I do derive a class from Script to register game level script API, could it cause this problem?

I'm using HEAD version (a2d8f8670e46565b74f1765c369f969c83cdf7c6)
VS2015
Windows 7 64bit

It seems like something went horribly wrong but I have no idea what.
And it only happens in that weird case of player dying while the monster AI is attacking and the scene is cleared after the attack animation is over.
If another animation starts after the attack is over it also changes the kind of error.

-------------------------

Enhex | 2017-01-02 01:07:07 UTC | #2

I tried to change the idle animation to the walk animation and the problem disappeared.
When I tried other animations it still happens, only the walk animation works.

Is it possible that the .ani is corrupted? I exported it from Blender using the Urho addon.

It still doesn't make sense that the asserts only happen when a specific animation is played after the attack animation.
Maybe there's a bug with the animation controller?

-------------------------

rasteron | 2017-01-02 01:07:07 UTC | #3

[quote="Enhex"]
Is it possible that the .ani is corrupted? I exported it from Blender using the Urho addon.
[/quote]

You should probably test your ani files first individually and verify if you have successfully exported them using Blender. The Editor is a good tool for that. Check also if you are using the correct animation layers.

-------------------------

Enhex | 2017-01-02 01:07:07 UTC | #4

[quote="rasteron"]
You should probably test your ani files first individually and verify if you have successfully exported them using Blender. The Editor is a good tool for that. Check also if you are using the correct animation layers.[/quote]

It works, if an animation wouldn't work on its own will be very obvious and trivial.
All the animations are on layer 0.
Like I said the weird part is that it only happens when the attack animation is played and then the other animation is played, and the scene clears.

EDIT:
I just tested it with just a model (no monster AI), and it still happens.

-------------------------

cadaver | 2017-01-02 01:07:07 UTC | #5

I just tested a potentially dangerous operation, clearing the scene from a script object's method in the AnimatingScene sample (which plays animations), but it didn't cause trouble.

My suspicion is on memory / heap corruption, but it's hard to say where that is happening, it could be your code.

See if you can get a short reproduction case with for example only using scripting and the Urho built-in assets, if you manage that then please submit it as an issue.

We should definitely update AngelScript to newer at some point, it has improved a lot in the meanwhile.

-------------------------

Enhex | 2017-01-02 01:07:07 UTC | #6

Managed to replicate it in a project based on modified "04_StaticScene.as" using "Urho3DPlayer_d.exe".

I'm using the same free model, which is this one: [opengameart.org/content/lizardman-0](http://opengameart.org/content/lizardman-0)
It takes two animations, and jack only have walk animation.

I'll pack it up, including the lizardman model and its blender file, and open an issue in a moment.


EDIT:
Issue opened: [github.com/urho3d/Urho3D/issues/885](https://github.com/urho3d/Urho3D/issues/885)

-------------------------

