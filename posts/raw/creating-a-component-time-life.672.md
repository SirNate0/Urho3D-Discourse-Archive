vivienneanthony | 2017-01-02 01:02:01 UTC | #1

Hello

I revised some code to create a GameObject component so it can hold a object lifetime, creation date/time, and additional information once added. 

The question, I have is  how do test the time between the creation time and the lifetime, based on Urho3d built in timers. I was thinking in the main Postupdate event. It can loop through the nodes and test for a object lifetime.

/// Base code
GameObject::GameObject(Context* context) :
    LogicComponent(context),
    GameObjectType(0),
    GameObjectLifetime(0),
    GameObjectLifetimeCreated(0)

{
/// Only the physics update event is needed: unsubscribe from the rest for optimization
    SetUpdateEventMask(USE_FIXEDUPDATE);
}

Part of the code for the GameObject
[code]/// Registering a object
void GameObject::RegisterObject(Context* context)
{
    context->RegisterFactory<GameObject>();

    /// These macros register the class attributes to the Context for automatic load / save handling.
    // We specify the Default attribute mode which means it will be used both for saving into file, and network replication
    ATTRIBUTE(GameObject, VAR_INT, "Game Object Type", GameObjectType, 0, AM_DEFAULT);
    ATTRIBUTE(GameObject, VAR_INT, "Game Lifetime", GameObjectLifetime, 0, AM_DEFAULT);
    ATTRIBUTE(GameObject, VAR_INT, "Game Lifetime Created", GameObjectLifetimeCreated, 0, AM_DEFAULT);

    return;[/code]
}

Code I can probably move to test lifetime in a eventupdate of either the individual object or the whole scene which I prefer.

[code]/// Get node list
    PODVector <Node *> NodesVector;
    scene_ -> GetChildren (NodesVector, true);

    /// Set necessary objects
    Node * OrphanNode;
    String Nodename;

    /// loop nodes
    for(int i=0; i < NodesVector.Size(); i++)
    {
        /// Do nothing like copy the node vector to a node
        OrphanNode = NodesVector[i];

        /// Add a component
        GameObject * OrphanNodeGameObject = OrphanNode-> CreateComponent <GameObject>();

        OrphanNodeGameObject -> SetLifetime(0);

    }[/code]


Vivienne

-------------------------

JTippetts | 2017-01-02 01:02:01 UTC | #2

I'm kind of uneasy about this "GameObject" approach. What is a GameObject? Is a Treasure Chest a GameObject? The player? Is a tree? Why is it named so generically? It seems to me like a GameObject would tend to accumulate all sorts of useless cruft in the same manner that traditional deep object hierarchies did; and, in fact, you can see it with this lifetime counter. Do all GameObjects need a lifetime counter? What if a type of GameObject is intended to exist perpetually and not track its lifetime? In such a case you have waste.

My approach has so far been to break GameObjects down into components, which is how the library itself is structured. GameObjects are Nodes, aggregated from components and child nodes. Really, that's the heart and soul of a component system. So instead of including time life counter in some general-purpose GameObject, I would instead include it in a special-case component or script object. ie (in Lua):

[code]
TimedLifeComponent=ScriptObject()
function TimedLifeComponent:Start()
     self.life=0
    self.timeToLive=10
end

function TimedLifeComponent:Update(dt)
    self.life=self.life+dt
    if self.life>self.timeToLive then
        self.node:SendEvent("TimeToLiveEnded")  -- Or some other means of telling the game this object needs to end
    end
end

function TimedLifeComponent:SetTimeToLive(ttl)
    self.timeToLive=ttl
end
[/code]

Now, any game object that needs to have a life counter can just add a TimedLifeComponent script instance:

[code]
timer=gameobject:CreateScriptObject(TimedLifeComponent)
timer:SetTimeToLive(43)
[/code]

This way, the game at large doesn't really need to know or care about which objects have a timed life. There is no need to loop through all nodes (and there can be a great many nodes in some games, so this really isn't that practical). You just need to figure out what to do with an object when it passes the"TimeToLiveEnded" event. (And sane object despawning is a problem all fair-sized games need to handle gracefully.)

Really, any time you start finding yourself writing overly general classes like GameObject, you ought to step back and take a look at your design. Large god-objects like that can ALWAYS be broken down into smaller, more atomicized responsibilities.

-------------------------

vivienneanthony | 2017-01-02 01:02:01 UTC | #3

Game object is a component in a  general term with only a few variables to define the type, parent(s), children(s), time of life.  If anything, It could be used as a postupdate event for that component, nod, or a loop through.

GameObject is a component attached to a node. I'm coding it in C++ so it would be integrated into the actual game.

As for looping, there will be a lot of things going on so at this point. I could put in special-case areas but I'll probably have to loop through objects nodes anyway.

[quote="JTippetts"]I'm kind of uneasy about this "GameObject" approach. What is a GameObject? Is a Treasure Chest a GameObject? The player? Is a tree? Why is it named so generically? It seems to me like a GameObject would tend to accumulate all sorts of useless cruft in the same manner that traditional deep object hierarchies did; and, in fact, you can see it with this lifetime counter. Do all GameObjects need a lifetime counter? What if a type of GameObject is intended to exist perpetually and not track its lifetime? In such a case you have waste.

My approach has so far been to break GameObjects down into components, which is how the library itself is structured. GameObjects are Nodes, aggregated from components and child nodes. Really, that's the heart and soul of a component system. So instead of including time life counter in some general-purpose GameObject, I would instead include it in a special-case component or script object. ie (in Lua):

[code]
TimedLifeComponent=ScriptObject()
function TimedLifeComponent:Start()
     self.life=0
    self.timeToLive=10
end

function TimedLifeComponent:Update(dt)
    self.life=self.life+dt
    if self.life>self.timeToLive then
        self.node:SendEvent("TimeToLiveEnded")  -- Or some other means of telling the game this object needs to end
    end
end

function TimedLifeComponent:SetTimeToLive(ttl)
    self.timeToLive=ttl
end
[/code]

Now, any game object that needs to have a life counter can just add a TimedLifeComponent script instance:

[code]
timer=gameobject:CreateScriptObject(TimedLifeComponent)
timer:SetTimeToLive(43)
[/code]

This way, the game at large doesn't really need to know or care about which objects have a timed life. There is no need to loop through all nodes (and there can be a great many nodes in some games, so this really isn't that practical). You just need to figure out what to do with an object when it passes the"TimeToLiveEnded" event. (And sane object despawning is a problem all fair-sized games need to handle gracefully.)

Really, any time you start finding yourself writing overly general classes like GameObject, you ought to step back and take a look at your design. Large god-objects like that can ALWAYS be broken down into smaller, more atomicized responsibilities.[/quote]

-------------------------

vivienneanthony | 2017-01-02 01:02:01 UTC | #4

[quote="JTippetts"]Really, that's the heart and soul of a component system. So instead of including time life counter in some general-purpose GameObject, I would instead include it in a special-case component or script object. ie (in Lua)[/quote]

It's coded as a component.

-------------------------

vivienneanthony | 2017-01-02 01:02:01 UTC | #5

This might work as the component  The main thing the timestep created is important so I have to calculate that.

[code]/// Fix update
void GameObject::FixedUpdate(float timeStep)
{
    // Disappear when duration expired
    if (GameObjectLifetime >= 0)
    {
        GameObjectLifetime -= timeStep;
        if (GameObjectLifetime <= 0)
            node_->Remove();
    }
    return;
}
[/code]


My idea is

[code]/// Fix update
/// Creation of a game object
void GameObject::Start()
{
    // code to set  time created here
    GameObjectLifetimeCreated = (?) GetTimeStep();
    return;
}


void GameObject::FixedUpdate(float timeStep)
{
    // Disappear when duration expired
    if (GameObjectLifetime+GameObjectLifetimeCreated >= GameObjectLifetimeCreated)
    {
        GameObjectLifetime -= timeStep;
        if (GameObjectLifetime <= 0)
            node_->Remove();
            /// Send out a event notice or something
    }
    return;
}
[/code]

-------------------------

JTippetts | 2017-01-02 01:02:02 UTC | #6

[quote="vivienneanthony"][quote="JTippetts"]Really, that's the heart and soul of a component system. So instead of including time life counter in some general-purpose GameObject, I would instead include it in a special-case component or script object. ie (in Lua)[/quote]

It's coded as a component.[/quote]

My objection is that it's coded as part of some kind of nebulously-named, apparently general-case component called GameObject. Ostensibly, GameObject is used by any object in the game, so all objects in the game thus become burdened with this lifetime-limiting functionality whether they need it or not. Sure, you could turn it off for those that don't need it, but it's still waste and cruft. I think that any component needs to hold to the Single Responsibility Principle. A StaticModel is just that: a static model. A Light is just a Light. A GameObject is... what? Some sort of aggregate? Architecturally, the aggregation should take place in Node and the components themselves should be simple.

My proposed solution was a component (I wrote it as a ScriptObject, but it could easily be a C++ component) that ONLY handles lifetime management. It doesn't track parents, children or type. It doesn't have any of this general-purpose GameObject stuff. It only tracks lifetime. You could add such a component to those game objects that need it, and those that don't need it don't get one. No need to special-case or turn off anything in GameObject.

I wonder, too, about your use of GameObject to track things such as parent (which can be obtained through the Node interface instead), type (which can be stored in a Node-level user variable if it's really necessary) or children (which again can be accessed through the Node). Again, this strikes me as a component that is trying to take on too much responsibility. It gets back to the same old mess of polymorphic hierarchies trying to include everything, including the kitchen sink, in order to account for all possible object types; worse, you are deliberately bypassing the wonderful composition framework provided by Urho in order to make it.

-------------------------

vivienneanthony | 2017-01-02 01:02:02 UTC | #7

Hmmm. Maybe GameObject is too broad of a term. I think maybe ObjectLifetime.

I'm thinking every node will have a ObjectLifetime.  I'm going want the ability to change or reset the lifetime, and additionally apply a muiltiple to decrease the lifetime(aging).

As for future coding, I am thinking Nodes might have a one-to-many or many-to-one relationship,  in with some type of Hierarchy component is needed.

For example, two players wearing a suit on a spaceship. The ship would be the parent node. The spacesuit would be a child node and the players inside would be nodes inside of that.

 
[quote="JTippetts"][quote="vivienneanthony"][quote="JTippetts"]Really, that's the heart and soul of a component system. So instead of including time life counter in some general-purpose GameObject, I would instead include it in a special-case component or script object. ie (in Lua)[/quote]

It's coded as a component.[/quote]

My objection is that it's coded as part of some kind of nebulously-named, apparently general-case component called GameObject. Ostensibly, GameObject is used by any object in the game, so all objects in the game thus become burdened with this lifetime-limiting functionality whether they need it or not. Sure, you could turn it off for those that don't need it, but it's still waste and cruft. I think that any component needs to hold to the Single Responsibility Principle. A StaticModel is just that: a static model. A Light is just a Light. A GameObject is... what? Some sort of aggregate? Architecturally, the aggregation should take place in Node and the components themselves should be simple.

My proposed solution was a component (I wrote it as a ScriptObject, but it could easily be a C++ component) that ONLY handles lifetime management. It doesn't track parents, children or type. It doesn't have any of this general-purpose GameObject stuff. It only tracks lifetime. You could add such a component to those game objects that need it, and those that don't need it don't get one. No need to special-case or turn off anything in GameObject.

I wonder, too, about your use of GameObject to track things such as parent (which can be obtained through the Node interface instead), type (which can be stored in a Node-level user variable if it's really necessary) or children (which again can be accessed through the Node). Again, this strikes me as a component that is trying to take on too much responsibility. It gets back to the same old mess of polymorphic hierarchies trying to include everything, including the kitchen sink, in order to account for all possible object types; worse, you are deliberately bypassing the wonderful composition framework provided by Urho in order to make it.[/quote]

-------------------------

vivienneanthony | 2017-01-02 01:02:02 UTC | #8

Does this make sense? I will name GameObject probably to Lifetime (component). This would apply to all objects.

[code]/// Base code
GameObject::GameObject(Context* context) :
    LogicComponent(context),
    GameObjectLifetime(-1.0f)
{
/// Only the physics update event is needed: unsubscribe from the rest for optimization
    SetUpdateEventMask(USE_FIXEDUPDATE);
}

/// Registering a object
void GameObject::RegisterObject(Context* context)
{
    context->RegisterFactory<GameObject>();

    /// These macros register the class attributes to the Context for automatic load / save handling.
    // We specify the Default attribute mode which means it will be used both for saving into file, and network replication
    ATTRIBUTE(GameObject, VAR_FLOAT, "Game Lifetime", GameObjectLifetime, -1.0f, AM_DEFAULT);

    return;
}

/// Creation of a game object
void GameObject::Start()
{
    /// Set
    GameObjectLifetime = -1.0f;

    return;
}

/// Fix update
void GameObject::FixedUpdate(float timeStep)
{
    // Disappear when duration expired
    if (GameObjectLifetime  >= 0)
    {
        GameObjectLifetime -= timeStep;
        if (GameObjectLifetime <= 0)
        {

            node_->Remove();
        }
    }
    return;
}


/// Set Lifetime
void GameObject::SetLifetime(float lifetime)
{
    GameObjectLifetime = lifetime;

    return;
}

/// Set Lifetime
float GameObject::GetLifetime(void)
{

    return GameObjectLifetime;
}
[/code]

My character.h header file is this
[code]

/// Character component, responsible for physical movement according to controls, as well as animation.
class Character : public LogicComponent
{
    OBJECT(Character)

public:
    /// Construct.
    Character(Context* context);

    /// Register object factory and attributes.
    static void RegisterObject(Context* context);

    /// Handle startup. Called by LogicComponent base class.
    virtual void Start();
    /// Handle physics world update. Called by LogicComponent base class.
    virtual void FixedUpdate(float timeStep);
    virtual void WorldCollision(VariantMap& eventData);
    virtual void ArtificialSpaceCollision(VariantMap& eventData);

    /// Set and get the character health
    int SetHealth(int health);
    int GetHealth(void);

    /// Set basic information
    int SetPlayerInfo(playerbasicinfo TempPlayer);
    playerbasicinfo GetPlayerInfo(void);

    playeralliance GetAlliance(void);
    int SetAlliance(playeralliance TempAlliance);

    int SetCharacteristics(playercharacteristics TempCharacteristics);
    playercharacteristics GetCharacteristics(void);

    /// Movement controls. Assigned by the main program each frame.
    Controls controls_;

private:
    /// Handle physics collision event.
    void HandleNodeCollision(StringHash eventType, VariantMap& eventData);

    /// Grounded flag for movement.
    bool onGround_;
    /// Jump flag.
    bool okToJump_;
    /// In air timer. Due to possible physics inaccuracy, character can be off ground for max. 1/10 second and still be allowed to move.
    float inAirTimer_;

    Player CharacterPlayer;
};
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:02:05 UTC | #9

Can this thread be deleted.

-------------------------

