Spongeloaf | 2019-08-26 23:12:47 UTC | #1

I have a Component subclass called Planet. It looks like this:

````
class Planet : public Component {
public:
	bool has_gravity = false;
};
````

It's added to the planet's node like this:

````
Planet* rock_planet = rock_node->CreateComponent<Planet>();
rock_planet->has_gravity = true;
````
During each update, I check each planet for gravity:
````
PODVector<RigidBody2D*> all_nodes;
scene_->GetComponents(all_nodes, StringHash::Calculate("RigidBody2D"));

for (PODVector<RigidBody2D*>::Iterator body = all_nodes.Begin(); body != all_nodes.End(); body++)
	{		
		Node* node = (*body)->GetNode();
		Planet* planet = node->GetComponent<Planet>();
		if (planet) 
                {
                      // do stuff
                }
````

However this always returns null. If I swap <Planet> for any other built in component type, it works perfectly:

````
// For debug rendering - this code works just fine.
PhysicsWorld2D* physics_world = scene_->GetComponent<PhysicsWorld2D>();
````

Inside GetComponent<T> is a rabbit hole of templates, typedefs, and string hashes. It is not obvious to me what I need to do to make this work, or more specifically which parts of these templates my Planet is missing.

Other Components have #defined things in their class definitions that I'm not familiar with:
````
class URHO3D_API StaticSprite2D : public Drawable2D
{
    URHO3D_OBJECT(StaticSprite2D, Drawable2D);
````

Straight copying those into my class has not helped:
 `"URHO3D_OBJECT(Planet, Component)")` 
Visual studio doesn't like it, and I don't know what it does anyway, but it's the most obvious difference between my class and other components. 

Any help?

-------------------------

elix22 | 2019-08-26 15:01:39 UTC | #2

You didn't register  your component ,

**Declare in your class** 
static void RegisterObject(Context*); 

**Implement**
`void Planet ::RegisterObject(Context* context){ context->RegisterFactory<Planet>("Planet");}`


**Call once in the beginning :**
Planet::RegisterObject(context);

-------------------------

S.L.C | 2019-08-26 15:23:52 UTC | #3

Also, i hope you don't forget the boilerplate macro:

```cpp
URHO3D_OBJECT(Planet, Component);
```

-------------------------

Spongeloaf | 2019-08-26 15:35:43 UTC | #4

[quote="S.L.C, post:3, topic:5511"]
Also, i hope you don’t forget the boilerplate macro
[/quote]


I mentioned it in the original post; I wasn't sure if I needed it but it did look important. According to visual studio the function definition for 'URHO3D_OBJECT' is not found. I've included object.h, and visual studio can even peek the definition of it. What else am I missing?

````
class Planet : public Component {

	URHO3D_OBJECT(Planet, Component);

public:
	bool has_gravity;
	static void RegisterObject(Context*);
};
````

-------------------------

codexhound | 2019-08-26 20:36:14 UTC | #5

Every custom object which derives from object needs a constructor that takes a context pointer to use the URHO3D_OBJECT macro (it defines a bunch of code Urho objects need to use events and hashing, etc) kind of like the Q_OBJECT macro in qt.
For you it would look like

    class Planet : public Component {
           URHO3D_OBJECT(Planet, Component);
           public:
             Planet(Context * context) : Component(context) {}
	         bool has_gravity;
	         static void RegisterObject(Context*);
    };

Without that constructor, Urho3D has no way of registering the object for lookup from what I've gathered. Given that, in all my implementations so far RegisterObject has not been necessary as I've been using this:

Use GetDerivedComponent() for finding custom unregistered derived objects.

I think with all that in your class it should work with GetComponent as well.

-------------------------

Spongeloaf | 2019-08-27 00:08:16 UTC | #6

It seems to work now. Thanks for the help @elix22, @S.L.C, and @codexhound!

-------------------------

