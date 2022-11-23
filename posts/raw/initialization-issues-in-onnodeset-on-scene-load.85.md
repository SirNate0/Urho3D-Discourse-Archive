Kingsley | 2017-01-02 00:57:52 UTC | #1

Just what it says on the tin! 

I'd like to have a generic initialization function for my components, similar to Start() in unity3d. OnNodeSet seems the best built-in option, but it's not working out as I planned.

Here's the code I'm using:

[code]
void TestComponent::OnNodeSet(Node *node)
{
    //Calling Init here doesn't seem to properly create the rigidbody and/or collisionshape upon loading
    if (node) Init(node);
}

void TestComponent::ApplyAttributes()
{
    //Uncommenting this Init() call and commenting out the OnNodeSet one results in save/load working fine,
    //but initialization of instantiated objects becomes obviously borked.

    //Interestingly it seems to have no effect when both are uncommented

    //Init(node_);
}

void TestComponent::Init(Node* node)
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();

    StaticModel* model = node->GetOrCreateComponent<StaticModel>();
    model->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
    model->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
    model->SetCastShadows(true);

    RigidBody* rigidbody = node->GetOrCreateComponent<RigidBody>();
    rigidbody->SetMass(1.0f);

    CollisionShape* shape = node->GetOrCreateComponent<CollisionShape>();
    shape->SetBox(Vector3::ONE);
}
[/code]

When I create objects, it works fine:
[img]http://i.imgur.com/tMLirmH.png[/img]

However, when I save/load the scene, the collisionshapes seem to become detached from the node, and the model falls through the ground.
[img]http://i.imgur.com/Zn8bj55.png[/img]

My test scene is available [url=https://db.tt/f1lxv51w]here[/url].

Is this a bug, or should I not be using OnNodeSet to call other components' functions? Is there a recommended approach?

Thanks.

-------------------------

friesencr | 2017-01-02 00:57:52 UTC | #2

I have been digging around for a bit.  There isn't a scene start event to subscribe to.  The start event happens on a script instance when the component is created.  What if the node isn't attached to a scene? Should it start?  I haven't gotten very advanced using multiple scenes but I bet there is trouble there. What if you attach a node to a scene that is paused?  There is maybe a difference to "Start" and "The first frame it participates".  Does having a Start and Init event clear up the intent?  I really haven't thought much about this.  The Start method on a ScriptInstance has always done what I have expected and I am just starting to move to c++.

Sorry for not really answering your question and asking more questions.

-------------------------

Kingsley | 2017-01-02 00:57:52 UTC | #3

friesencr, interesting! OnSceneLoad seems like it would make more sense than ApplyAttributes. I suppose currently one could hack an event atop E_CLIENTSCENELOADED to mimic the functionality, but that would be...unpleasant, to be sure. :I

I'm looking for something more along the lines of [url=http://docs.unity3d.com/Documentation/ScriptReference/MonoBehaviour.Awake.html]Awake()[/url] and [url=http://docs.unity3d.com/Documentation/ScriptReference/MonoBehaviour.Start.html]Start()[/url] The idea in that engine is, after an object is instantiated, Awake is first called, and used to assign variables, and Start is then used to do setup work using those variables. Urho has OnNodeSet, which seems to wrap the functionality of Awake with [url=http://docs.unity3d.com/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html]OnDestroy[/url] into one function, eschewing delayed initialization completely. This seems a bit frightening, considering I might check the value of another component's variable and get the wrong result due to race conditions.

I'd take a shot at resolving these issues, but I want to make sure I'm not blatently misunderstanding urho's node constructor style. :smiley:

-------------------------

cadaver | 2017-01-02 00:57:53 UTC | #4

Theoretically it's OK to create components in OnNodeSet(), for example physics components require the existence of the PhysicsWorld component in the root scene node, but the root node should already be loaded at that point. What I believe goes wrong here, while loading, is that you have the logic to GetOrCreate the physics components, and maybe your component will be loaded first, so it detects there are no physics components, and creates them. BUT a second set of physics components will be loaded into the scene node after your component's initialization!

So, I'd phrase it so that when you're going to load and save scenes, do not make your custom components create other components. Instead compose them in higher-level code, or save the scene node (with all its components) as a "prefab" which you can load with Scene::Instantiate() or Scene::InstantiateXML().

Urho's components are a bit lower level compared to Unity. Maybe you could create your own base class for "game components" that implements a Unity-like API, what it could do is that it subscribes to the scene update event, and on the first scene update it would call Start() before Update().

Also, nothing prevents you calling ApplyAttributes() yourself when you have finished spawning a new node + components in your code. The reason why the engine doesn't call it automatically, except when loading scenes, is that it cannot know when you are finished with all possible attribute changes. The editor, for example, calls it after each attribute edit to make sure all the attribute side-effects (such as recreating a CollisionShape's Bullet object when shape parameters change) are applied correctly. For the editor this is acceptable, but the engine itself should not call ApplyAttributes() without reason.

-------------------------

