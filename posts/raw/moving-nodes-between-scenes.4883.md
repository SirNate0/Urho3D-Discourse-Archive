Bananaft | 2019-01-30 09:56:40 UTC | #1

Is it legal?

I found this thread from 2015, where @cadaver says that it is not, is it still true?
[quote="cadaver, post:2, topic:943"]
Moving nodes from scene to another is not supported. The reason is that they would need to let go and re-acquire of global components like Octree &amp; PhysicsWorld.

If you want to load prefabs, use Scene::InstantiateXML() function to load a node hierarchy you want directly into the correct scene.
[/quote]

I was able to do it with this angelscript code:

			Scene@ tempscene = Scene();
			tempscene.CreateComponent("Octree");
			
			PlayerNode.parent = tempscene;
			scene_.LoadXML(cache.GetFile(currentmap.name));
			
			PlayerNode.parent = scene_;
			tempscene.Remove();

PlayerNode have a bunch of nodes and components attached to it, everything seems to be working except for the camera (and my handwritten component). Camera can be fixed by setting it again to a viewport in the next update (scene switch is done in pre-render).

So, am I fine, or is it a hacky mess and I should't rely on it? What is the good practice of moving a bunch of stuff from one scene to another? In future, I want to be able to move any number of entities from one scene to another. Not just the player.

-------------------------

Modanung | 2019-01-31 14:06:14 UTC | #2

`scene->AddChild(node_)` seems to works fine for me.

-------------------------

Bananaft | 2019-01-30 12:04:38 UTC | #3

This removes camera component. :confused:

-------------------------

Modanung | 2019-01-30 12:49:35 UTC | #4

It _removes_ the component? Or does the _viewport_ stop working?
The latter would make more sense to me. In [Edddy](https://gitlab.com/luckeyproductions/Edddy/blob/master/view3d.cpp#L143) I simply create a _new_ `Viewport` after changing the camera node's parent scene.

-------------------------

Bananaft | 2019-01-30 12:26:59 UTC | #5

[quote="Modanung, post:4, topic:4883"]
It *removes* the component? Or does the *viewport* stop working?
[/quote]

I'm not sure. But:
1) viewport works if I switch it to another camera.
2) getting camera component returns null.

-------------------------

lezak | 2019-01-30 13:19:32 UTC | #6

[quote="Modanung, post:2, topic:4883"]
if (node_-&gt;GetScene()) node_-&gt;SetParent(nullptr);
[/quote]

This is unnecessary and it does nothing (there is a null check in SetParent). Node::ResetScene() should be used to clear node's scene, but this is only side node, because when node is being reparented there's also check if scene changed and if so, all logic behind cleaning up old scene and assigning new one is fired. 
In my project I move nodes between scenes very often and everything works fine, I've implemented my code long time ago but I don't recall having any issues there. 
One thing that I remember being problematic is creating node outside of any scene, adding components to it and placing it in a scene after that. This leads to ids conflicts (ids are cleaned when node is removed from a scene) and Urho delas with them by removing old component with same id which can be a problem. 

[quote="Bananaft, post:5, topic:4883"]
getting camera component returns null.
[/quote]
Getiing camera from where? Scene, owner node, viewport?

-------------------------

Bananaft | 2019-01-30 15:21:45 UTC | #7

owner's parent node.

I also tried loading scene next to an active one, attaching player to it, and then replacing one with another.

			Scene@ tempscene = Scene();
			tempscene.CreateComponent("Octree");
			tempscene.LoadXML(cache.GetFile(currentmap.name));
			PlayerNode.parent = tempscene;
			
			scene_ = tempscene;

This breaks stuff in different way.

So far, the method I posted at the start of this thread gives me fewest glitches.

-------------------------

Modanung | 2019-01-31 19:08:41 UTC | #8

Ah, thanks for clearing that up. I assumed I put it there because it fixed something. :palm_tree:

-------------------------

Bananaft | 2019-01-31 13:46:20 UTC | #9

switching scene of a node with rigid body component sets its linear and angular damping to 0.

I also noticed more bugs the nature of which I just can't understand. I'm now considering avoiding node scene switching and somehow hacking my way around. :frowning:

-------------------------

Leith | 2019-02-08 12:46:23 UTC | #10

Happy to help with these issues, my current project creates a scene in code, saves it, and then loads it (throwing out the old scene), so if anything needs fixing up, I'm probably going to notice real soon, as saving snapshots of a scene is how I intend to save gamestate.

-------------------------

Bananaft | 2019-02-08 12:46:24 UTC | #11

Yeah, that's the solution I end up using. I save all nodes I want to teleport, then load them into next scene. I had to fix a bunch of things, turn lots of object parameters to not serializable. I don't have a save system yet, but I guess it will help me in future.

Also, my prefab system helps me to ensure certain game objects will always stay the same even if they were changed by game logic.

https://discourse.urho3d.io/t/poor-mans-prefab-system/4681

-------------------------

Leith | 2019-02-08 13:28:40 UTC | #12

I noticed some specific issues with factory method not setting default values as we defined them - it seems there is a kind of placement new, with no guarantees about initial values unless you be professional and initialize everything yourself, even though you told the engine the default values, and even if the engine is the one making them - I am talking about deserialization, and what got serialized in the first place, and what was not initialized properly
The engine will not serialize things whose current value agrees with the default we provided - it only serializes them if the value has changed from the default we provided, and that ignores the current value - basically, defining the default value for something is just limiting what is serialized, and is not used during construction. Serializable things are not always serialized, and no engine code sets default values on your object properties. It all feels a bit unsafe, even for a seasoned coder.

-------------------------

Modanung | 2019-02-08 13:32:10 UTC | #13

Are you using `URHO3D_ATTRIBUTE`?
[details=Excerpt from Serializable.h]
```
// The following macros need to be used within a class member function such as ClassName::RegisterObject().
// A variable called "context" needs to exist in the current scope and point to a valid Context object.

/// Copy attributes from a base class.
#define URHO3D_COPY_BASE_ATTRIBUTES(sourceClassName) context->CopyBaseAttributes<sourceClassName, ClassName>()
/// Update the default value of an already registered attribute.
#define URHO3D_UPDATE_ATTRIBUTE_DEFAULT_VALUE(name, defaultValue) context->UpdateAttributeDefaultValue<ClassName>(name, defaultValue)
/// Remove attribute by name.
#define URHO3D_REMOVE_ATTRIBUTE(name) context->RemoveAttribute<ClassName>(name)

/// Define an object member attribute.
#define URHO3D_ATTRIBUTE(name, typeName, variable, defaultValue, mode) context->RegisterAttribute<ClassName>(Urho3D::AttributeInfo( \
    Urho3D::GetVariantType<typeName >(), name, URHO3D_MAKE_MEMBER_ATTRIBUTE_ACCESSOR(typeName, variable), nullptr, defaultValue, mode))
/// Define an object member attribute. Post-set member function callback is called when attribute set.
#define URHO3D_ATTRIBUTE_EX(name, typeName, variable, postSetCallback, defaultValue, mode) context->RegisterAttribute<ClassName>(Urho3D::AttributeInfo( \
    Urho3D::GetVariantType<typeName >(), name, URHO3D_MAKE_MEMBER_ATTRIBUTE_ACCESSOR_EX(typeName, variable, postSetCallback), nullptr, defaultValue, mode))
/// Define an attribute that uses get and set functions.
#define URHO3D_ACCESSOR_ATTRIBUTE(name, getFunction, setFunction, typeName, defaultValue, mode) context->RegisterAttribute<ClassName>(Urho3D::AttributeInfo( \
    Urho3D::GetVariantType<typeName >(), name, URHO3D_MAKE_GET_SET_ATTRIBUTE_ACCESSOR(getFunction, setFunction, typeName), nullptr, defaultValue, mode))

/// Define an object member attribute. Zero-based enum values are mapped to names through an array of C string pointers.
#define URHO3D_ENUM_ATTRIBUTE(name, variable, enumNames, defaultValue, mode) context->RegisterAttribute<ClassName>(Urho3D::AttributeInfo( \
    Urho3D::VAR_INT, name, URHO3D_MAKE_MEMBER_ENUM_ATTRIBUTE_ACCESSOR(variable), enumNames, static_cast<int>(defaultValue), mode))
/// Define an object member attribute. Zero-based enum values are mapped to names through an array of C string pointers. Post-set member function callback is called when attribute set.
#define URHO3D_ENUM_ATTRIBUTE_EX(name, variable, postSetCallback, enumNames, defaultValue, mode) context->RegisterAttribute<ClassName>(Urho3D::AttributeInfo( \
    Urho3D::VAR_INT, name, URHO3D_MAKE_MEMBER_ENUM_ATTRIBUTE_ACCESSOR_EX(variable, postSetCallback), enumNames, static_cast<int>(defaultValue), mode))
/// Define an attribute that uses get and set functions. Zero-based enum values are mapped to names through an array of C string pointers.
#define URHO3D_ENUM_ACCESSOR_ATTRIBUTE(name, getFunction, setFunction, typeName, enumNames, defaultValue, mode) context->RegisterAttribute<ClassName>(Urho3D::AttributeInfo( \
    Urho3D::VAR_INT, name, URHO3D_MAKE_GET_SET_ENUM_ATTRIBUTE_ACCESSOR(getFunction, setFunction, typeName), enumNames, static_cast<int>(defaultValue), mode))

/// Define an attribute with custom setter and getter.
#define URHO3D_CUSTOM_ATTRIBUTE(name, getFunction, setFunction, typeName, defaultValue, mode) context->RegisterAttribute<ClassName>(Urho3D::AttributeInfo( \
    Urho3D::GetVariantType<typeName >(), name, Urho3D::MakeVariantAttributeAccessor<ClassName>(getFunction, setFunction), nullptr, defaultValue, mode))
/// Define an enum attribute with custom setter and getter. Zero-based enum values are mapped to names through an array of C string pointers.
#define URHO3D_CUSTOM_ENUM_ATTRIBUTE(name, getFunction, setFunction, enumNames, defaultValue, mode) context->RegisterAttribute<ClassName>(Urho3D::AttributeInfo( \
    Urho3D::VAR_INT, name, Urho3D::MakeVariantAttributeAccessor<ClassName>(getFunction, setFunction), enumNames, static_cast<int>(defaultValue), mode))
```
[/details]

-------------------------

Leith | 2019-02-08 13:33:28 UTC | #14

yeah that is what I am using

-------------------------

Leith | 2019-02-08 13:33:57 UTC | #15

and I am saying its unreliable and that the values we define are not implemented on new objects

-------------------------

Leith | 2019-02-08 14:14:35 UTC | #16

sure we can save our files, but when we load them back, the values we defined as default, wont be applied - only values which changed from the default are serialized, and deserialized correctly - values that were not serialized (because they happen to equal the default value we described, ie have not changed), are not initialized to default values correctly
I also noticed that when I reload my scene from xml, the nodes are all marked as replicated, even though I have not touched networking yet.

OK so say I go out of my way to define the serialized members, and their default values, why the hell are my default values not applied to new objects, other than that the value is not changed, so we didn't bother to record it, because we know it, and still didnt apply it on a new object? the factory should be able to return a new object with all the default values we defined!

I'm lazy, I should not need to manually initialize every member of everything if its serialized already, grumble grumble

-------------------------

weitjong | 2019-02-08 15:32:53 UTC | #17

The attributes of node/component are editable in the editor. The attribute default is used by editor’s attribute inspector to reset an attribute. It is also used by the engine when the engine serializes a scene or a prefab or what have you, by only saving non-default attribute values in order to minimize the I/O. Thus when the engine deserializes the objects, it expects the constructor has initialized the member variables to the same “default values” that it declares to the engine/editor. There is nothing magic about it. The engine does not auto-magically read those declaration and synthesizes the initialization code for you.

-------------------------

Leith | 2019-02-09 00:09:23 UTC | #18

I'm asking - why not? We're not merely making declarations for the compiler, we're actually registering AttributeInfo structs in our Context, and typically doing so prior to any instantiation via a static method - we're in a pretty good position to "magically" use that information in our factory function.

-------------------------

weitjong | 2019-02-09 05:12:42 UTC | #19

Since it is off-topic in this thread, I will keep it short. I believe if you want a custom component class to always serialize the attributes regardless of their values, you can override this method `SaveDefaultAttributes()` to always return `true`, then you don’t have any issues if you are lazy to implement a ctor properly. I am fine with your idea to improve how attribute default value could be initialized, as long as it works consistently with all the existing components whether they are created via factory class or directly.

-------------------------

Leith | 2019-02-09 09:28:26 UTC | #20

Thanks, sorry to throw a hammer, but it seems like something we could do, as a kindness, and at low cost. We don't create new objects often, so setting their default values the way we described them, hardly sounds like it will break anything. I hope.User would still be free to declare members (public or not) that are not serialized (and so not safely initialized) and deal with those outside their serialization declarations. Sounds like a win.

-------------------------

