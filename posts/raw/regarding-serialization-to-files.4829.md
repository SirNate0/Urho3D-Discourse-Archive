Leith | 2019-01-17 02:38:54 UTC | #1

I've written a small StateManager, deriving from Object, and a baseclass for GameStates, deriving from Component.

That all works fine, I then tried experimenting with serializing component properties (aka Attributes) to disk.
Following the docs as best I could understand them, I have some code in a derived GameState class that looks like this:
	public:
        float myValue=666.0f;

        static void RegisterObject(Context* context){
            context->RegisterFactory<GameMainMenuState>();
            URHO3D_ATTRIBUTE("My Value",float,myValue,666.0f,AM_DEFAULT);
        }

Later, I attempt to serialize the entire scene to an XML file as follows:
            Urho3D::File serializer(context_, "testscene.xml", FILE_WRITE);
            GetNode()->GetScene()->SaveXML(serializer);

I should mention that I am manually calling the static method to register factory and attribute early in the application startup code.

The problem is that during serialization, my custom attribute is never written to disk: the built-in attributes are showing up for Nodes, but not for any Component, including my custom component.

What am I doing wrong? I assume that since Component derives from Serializable, and can hold Attributes, that these would be Serialized too.

PS - I just checked, I can successfully query the attribute variant using GetAttribute, and I can also successfully query the Context directly for the same. So my attribute is definitely registered with the Context, it's just failing to be Serialized, despite having AM_DEFAULT mode.
The only thing that appears to be different about my implementation with respect to the Samples is that my Component is a Derived class (correctly registered as such, and playing well with Urho in every other respect, including custom events). GameStateX derives from IGameState, which in turn derives from Component... with this arrangement, Serialization appears to be failing!

-------------------------

Leith | 2019-01-17 04:10:56 UTC | #2

Digging into the Serialization code beginning with Node::SaveXML( ), and drilling all the way down to Serializable::SaveXML( ), I could see no reason why my attribute would *not* be saved.
The only way to know for sure, would be to trace Urho, which I'm currently pulling in as a static library built in Release mode. I'm really not inclined to set up a special project for tracing Urho internals just for this one issue, and really hoping that somebody can spot my mistake :)

Examining the SceneLoadExample.xml file, I can see that, under certain conditions, component attributes are indeed serialized - but what are the conditions? Must we set an attribute *via its accessor* before it will be serialized? I notice in that example, one instance of StaticModel Component has two attribute serialized, while another instance has three attributes serialized - this indicates to me that they must have somehow been marked as 'dirty' prior to serialization - am I on the right track?

-------------------------

Leith | 2019-01-17 04:16:12 UTC | #3

![MyOutput|416x500](upload://zbb2m3Q0GCaebR7xyEKhlueNXUf.png)

-------------------------

Leith | 2019-01-17 06:10:16 UTC | #4

Never mind, I trudged back through the Serialization code a second time, and this time I noticed that there is an early-out if the attribute's value, at the time of serialization, equals its default value (as specified via the URHO3D_ATTRIBUTE macro).

I've since checked - it does not matter if you modify an attribute manually, or via SetAttribute, it will serialize correctly, but ONLY if the current value has changed from the default value - otherwise, it will be silently dropped from the output. This makes perfect sense to me, as it is assumed that our attributes are preset to the same values as those specified in our macro - but there is no actual CHECK for this, which gets me to thinking - why do we need to specify a default value for an attribute at all, when the "default" value (at the time we registered our attribute) can be determined via its accessor at runtime? It smells a little redundant to specify a default value at all, given it can be queried via the accessor, given the type is known. Just a thought that we might be able to eliminate one argument from that macro...

Oh well, just happy that my issue was resolved :)

-------------------------

weitjong | 2019-01-17 07:07:49 UTC | #5

The idea of having attributes is to allow the components to be editable via editor. The default value is a way for the editor to reset the value back.

-------------------------

Leith | 2019-01-17 09:02:07 UTC | #6

Thanks weitjong!, yes I appreciate that attributes are mainly about working with the Editor. I don't use the editor at this point, I was focused solely on serialization with respect to loading and saving stateful components. 

Your reply does help me understand the reason for a default value to be provided - initially I still could not see a reason why the macro expansion could not access the existing member value, but when I tried to write a macro that could do so, I realized the problem: we're meant to be registering our class from a static method, prior to any instantiation of the class... the AttributeAccessor requires an object instance to query, and we don't (and should not) have any instance to query at this stage - silly me :blush:

Well, now that I have serialization working, I think I'll rewrite my state manager to take full advantage of it. The current stack-based implementation can't take full advantage, because it can add and remove entire gamestates arbitrarily, meaning that they may not be around during serialization - I might have to rework it to just disable inactive states via their container node.

Questions: #1, can Components be disabled? and #2, if a node (or component) is disabled, will it still be serialized? I'm sick of looking at the serializer code, but I don't recall seeing anything about inactive nodes/components.

-------------------------

weitjong | 2019-01-17 09:10:45 UTC | #7

They both can be disabled separately. They should still be serialized regardless.

-------------------------

Leith | 2019-01-17 09:22:37 UTC | #8

Thanks weitjong - exactly what I wanted to hear! This makes me feel better about tearing up my current stack-based state manager, before I go anywhere near writing my first game under Urho.

Can nodes/components OPT OUT of serialization without being removed from a scene?
I can think of cases where I want to omit certain objects from serialization without having to tear the scene apart...

-------------------------

lezak | 2019-01-17 10:36:57 UTC | #9

Mark any node/component as temporary if You don't want to save it.

-------------------------

Leith | 2019-01-17 10:43:45 UTC | #10

You guys are a great help, thanks so much for helping me with the learn curve !!:fist_left:

-------------------------

