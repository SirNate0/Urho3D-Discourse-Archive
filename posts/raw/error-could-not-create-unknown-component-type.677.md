vivienneanthony | 2018-09-06 10:04:56 UTC | #1

Hello

Does the line below makes since ? The GameObject is a general name that I will change.

```
[Wed Dec 17 17:58:06 2014] ERROR: Could not create unknown component type 1B71
```


The code that is causing the problem is

```
    /// Loop through the whole scene and get the root Node
    Node * RootNode = scene_ -> GetParent();

    /// Get node list
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
        GameObject * OrphanNodeGameObject = OrphanNode-> CreateComponent<GameObject>();

        OrphanNodeGameObject -> SetLifetime(-1);

    }
```


The header file is 

```
#ifndef GAMEOBJECT_H_INCLUDED
#define GAMEOBJECT_H_INCLUDED


#include "LogicComponent.h"

using namespace Urho3D;

/// Character component, responsible for physical movement according to controls, as well as animation.
class GameObject : public LogicComponent
{
    OBJECT(GameObject)
public:
    /// Construct.
    GameObject (Context* context);
    /// Register object factory and attributes.
    static void RegisterObject(Context* context);
    /// Handle startup. Called by LogicComponent base class.
    virtual void Start();
    /// Handle physics world update. Called by LogicComponent base class.
    virtual void FixedUpdate(float timeStep);

    /// updatelifetime
    float GetLifetime(void);
    void SetLifetime(float lifetime);


private:

    /// Component information
    float GameObjectLifetime;

};

#endif // GAMEOBJECT_H_INCLUDED
```

-------------------------

JTippetts | 2018-09-06 10:05:42 UTC | #2

It will log that error if you try to create a component for which you have not registered an object factory. You can register a factory by [code]context->RegisterFactory<GameObject>()[/code]

-------------------------

vivienneanthony | 2017-01-02 01:02:04 UTC | #3

I will look over the code again because I think the source has it.

-------------------------

vivienneanthony | 2017-01-02 01:02:04 UTC | #4

*smiles*

Thanks for the reminder. The fix was simple. I was overlooking something.

-------------------------

vivienneanthony | 2017-01-02 01:02:05 UTC | #5

Can this thread be deleted.

-------------------------

darkowic | 2018-09-05 19:33:36 UTC | #6

Not remove it :) This is very useful for beginners like me :) Even after 4 years :smiley:

-------------------------

Modanung | 2018-09-06 10:02:56 UTC | #7

Fixed markup of the code blocks.
And welcome to the forums, @darkowic! :confetti_ball: :slight_smile:

-------------------------

