artgolf1000 | 2017-01-02 01:14:00 UTC | #1

Hi,

I want to add logical components to UI elements like it does with nodes, so I can control their behavior flexibly.

For example, I want to add various logical components to Button.

One way is using multi-inherit from both Node and Button, but I haven't tested it;

Another way is creating corresponding nodes for each UI element, then add logical components to the corresponding nodes, it works, but I have to synchronize their status manually.

I don't know if it exists better way to achieve this.

Thank you.

-------------------------

cadaver | 2017-01-02 01:14:00 UTC | #2

Welcome to the forums.

Since the UI hierarchy is not a component hierarchy, not directly. However you can abuse the system a bit. Inherit UIElement, which by itself doesn't draw anything. Add it as a child of the element you wish to affect, and code the logic so that it affects its parent.

If you're using a layout, an additional child element can mess it up, however try setting fixed 0,0 size for the logic child.

In this case you can't use scene update event for per-frame update, or LogicComponent convenience virtual functions Update() or FixedUpdate(), so you just have to subscribe to the application-wide update event. This is actually proper since the UI is a global subsystem.

-------------------------

artgolf1000 | 2017-01-02 01:14:00 UTC | #3

Thanks for your quick reply.

-------------------------

1vanK | 2017-01-02 01:14:00 UTC | #4

If you are not afraid to modify the engine, you can try it: [github.com/urho3d/Urho3D/pull/1 ... b8af9784d5](https://github.com/urho3d/Urho3D/pull/1356/commits/973e1b46f7127903b4de1850a90067b8af9784d5) :)

-------------------------

