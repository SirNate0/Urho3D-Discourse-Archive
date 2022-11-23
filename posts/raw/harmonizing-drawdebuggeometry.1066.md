Mike | 2017-01-02 01:05:10 UTC | #1

Currently some component classes additionally provide the DrawDebugGeometry() method without passing the DebugRenderer as argument.
Is it OK to add this method to every component class?
At the level of the bindings, should we expose the 2 methods, or just one of them?

Edit: maybe adding method without DebugRender to Component class and removing it from children classes would be wise

-------------------------

cadaver | 2017-01-02 01:05:11 UTC | #2

Typically subsystem-like components have offered this function. I don't oppose adding it to every component, considering it's mostly a shortcut and usually you don't want to use any other debug renderer than the one at the scene root.

Easiest would be to add it to the component base class (remember proper lookup from scene with nullchecks along the way) in which case the bindings could also add it to the base class.

-------------------------

Mike | 2017-01-02 01:05:11 UTC | #3

I've just tried to add it to the component base class. As DebugRenderer is a component, I don't know how to access it from component base class.

-------------------------

cadaver | 2017-01-02 01:05:11 UTC | #4

node_ -> GetScene() -> GetComponent() 

(remember, nullchecks along each step) 

Also, because Urho is nowadays one monolithic library, there is no problem to access a Graphics component from the base class, when you just use the correct include path. Graphics classes are always compiled in.

-------------------------

weitjong | 2017-01-02 01:05:11 UTC | #5

Speaking of DebugDraw, I just notice today that UI::DebugDraw() is now broken. It used to be able to debug draw a blue bounding rectangle around the UI element being highlighted/selected. Currently PICK_UIELEMENT mode in the Editor does not display the bounding box because of that. It could have been broken already since a few releases back and it seems nobody has missed it :frowning:.  I have just tried compiling from old releases and it only works in v1.3.

EDIT: I just push a commit to fix it.

-------------------------

Mike | 2017-01-02 01:05:11 UTC | #6

Thanks, I forgot the include  :blush: 
Now it creates some trouble with SceneAPI, I'll try to fix this.

For UI::DebugDraw(), I don't experience this in the Editor. I'll post a screenshot to check if I understand your issue correctly.

-------------------------

Mike | 2017-01-02 01:05:11 UTC | #7

Here is what I get in the Editor when loading the ScreenJoystick UI layout:
[img]http://i.imgur.com/1DXB2CX.png[/img]
Main window is also highlighted as I was hovering when taking screenshot.

-------------------------

cadaver | 2017-01-02 01:05:11 UTC | #8

Yes, that's a nasty and easily overlooked problem related to static initialization: if a static const initializer refers to another static const, it may be garbage at that time since the initialization order is not mandated.

-------------------------

