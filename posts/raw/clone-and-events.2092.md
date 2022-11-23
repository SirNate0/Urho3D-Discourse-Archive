dakilla | 2017-01-02 01:13:00 UTC | #1

Any way to also clone subscribed events for components and nodes when cloning ?

I have some components and nodes that subscribes to events, when cloning them, clones have lost events.
Thanks.

-------------------------

cadaver | 2017-01-02 01:13:00 UTC | #2

Cloning uses the exact same method as load/save, attribute serialization. Event subscription status is separate from this.

If possible, I'd just recommend making the event connections in OnNodeSet() or Start() / DelayedStart() functions, as appropriate.

-------------------------

dakilla | 2017-01-02 01:13:00 UTC | #3

ok.
And what about to send a cloned event with the clone ptr in map to trigger actions for clones when a object is cloned ? maybe usefull for lot of things like auto registering to some other events  :confused: 

I added :

[code]/// A component has been cloned.
URHO3D_EVENT(E_COMPONENTCLONED, ComponentCloned)
{
    URHO3D_PARAM(P_SCENE, Scene);                  // Scene pointer
    URHO3D_PARAM(P_NODE, Node);                    // Node pointer
    URHO3D_PARAM(P_COMPONENT, Component);          // Component pointer
}[/code]

and at end of Node::CloneComponent()

[code]
    // Send component cloned event
    using namespace ComponentCloned;

    VariantMap& eventData = GetEventDataMap();
    eventData[P_SCENE] = scene_;
    eventData[P_NODE] = this;
    eventData[P_COMPONENT] = cloneComponent;
    SendEvent(E_COMPONENTCLONED, eventData);[/code]

It works for cloned components, but I'm not sure for cloned Node where to send a similar event.

-------------------------

cadaver | 2017-01-02 01:13:00 UTC | #4

Events are often used for when something happens that you can't directly anticipate. For example screen resize. The scene already sends node and component creation/deletion events, which are used by the editor for keeping the hierarchy window up to date. But that doesn't differentiate between cloning and other methods of creating new nodes.

Since the engine doesn't ever call Clone() on its own, but it's always your application logic and you know when it's called, you could follow with any post-cloning setup imperatively, just by calling some function in the cloned component(s). So I don't see a separate engine-defined event necessary here. Or if you wish, you could send an event yourself at the same time when cloning.

-------------------------

dakilla | 2017-01-02 01:13:00 UTC | #5

ok right. E_COMPONENTADDED should be sufficiant.
however I get some crash using the component ptr from E_COMPONENTADDED after cloning.

When I look the CloneComponent code, SafeCreateComponent (who call addComponent and then trigger the event E_COMPONENTADDED), the sended component does not have yet attributes applied by CloneComponent, this event shouldn't be sended only after ? (when I move the send event code after it fix the crash)

-------------------------

cadaver | 2017-01-02 01:13:00 UTC | #6

The meaning of the event is exactly what it says (component added). It doesn't tell anything of the attribute contents, which could be populated some time after, or possibly never (In case it's a node/component creation outside serialization or cloning.) 

At the time when the component is added, and the event is sent, Node code cannot know what case it is.

-------------------------

cadaver | 2017-01-02 01:13:01 UTC | #7

On second thoughts, the Node::Clone() function knows best when it's done with setting each components' (and its own) attributes, and also the mappings to new and old component. Therefore it could in fact make sense to have events sent from the engine code. Cloning shouldn't be a high-frequency operation (not any more frequent than instantiation of prefabs) and furthermore the events should be cheap performance-wise if no-one is listening to them.

-------------------------

cadaver | 2017-01-02 01:13:01 UTC | #8

Added in master branch.

-------------------------

dakilla | 2017-01-02 01:13:02 UTC | #9

great thanks.

-------------------------

