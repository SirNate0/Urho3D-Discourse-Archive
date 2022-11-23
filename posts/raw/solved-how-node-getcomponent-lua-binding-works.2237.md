KonstantTom | 2017-01-02 01:14:08 UTC | #1

[b]How Node::GetComponent lua binding works?[/b]
It works with any types of components. I need to implement this for some my classes. For example I has this function:
[code]StatesEngine::StateObject *Get (Urho3D::String typeName);[/code]
StatesEngine::StateObject is basic class such as Urho3D::Component. 
I can use all Urho3D::NavigationMesh functionality if I call:
[code]local navMesh = scene_:GetComponent ("NavigationMesh")[/code]

But if I call it I can use only StatesEngine::StateObject functions.
[code]local stateObject = myStateObjectsManager:Get ("PlayerController")[/code]

In Node.pkg I see only:
[code]// template <class T> T* GetComponent() const;
Component* GetComponent(const String type, bool recursive = false) const;[/code]

In my StateObjectsManager.pkg:
[code]StateObject *Get (String typeName);[/code]

[b]Is it ancient magic of Urho3D?[/b]

-------------------------

cadaver | 2017-01-02 01:14:08 UTC | #2

The "magic" is the helper function ToluaPushObject, which determines the object's type dynamically through the Object::GetType() type identification system (set up with URHO3D_OBJECT macro).

When bindings are generated, the init code in Source/Urho3D/LuaScripts/pkgs/ToCppHook.lua instructs this function to be used for Component, UIElement and Resource subclasses. In theory it looks like this could be simplified to say that it should be used for all Object subclasses.

As for the base class functions, these should get included as long as your pkg file defines the base class relationship, but I'm not familiar with all the ways how this could go wrong.

-------------------------

KonstantTom | 2017-01-02 01:14:08 UTC | #3

Big thanks! Now all works! :slight_smile:

-------------------------

