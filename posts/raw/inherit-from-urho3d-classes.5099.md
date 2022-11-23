Lunarovich | 2019-04-14 19:26:53 UTC | #1

Is it OK to inherit directly from Urho3D classes. For example, I want to have my own customized class derived from Text.

Right now, I'm having a URHO3D_OBJECT based class that functions as a Text class wrapper, i.e. I have an attribute text_ in my class. Is there a better solution?

-------------------------

S.L.C | 2019-04-14 20:37:30 UTC | #2

AFAIK it is something recommended. Otherwise you're just duplicating smart pointers.

Although be aware that there might be more to some than just having the `URHO3D_OBJECT` inside your class. If you get deeper into the subject and reach serialization, components and so on.

-------------------------

Pencheff | 2019-04-15 00:29:30 UTC | #3

Both solutions are fine.
Most of the UI components have other UI components inside - slider is made of scrollbar and a border image, LineEdit is using text inside as element. 
You can inherit text as well and add more functionality to it, expose that as attributes.

-------------------------

Leith | 2019-04-15 08:06:17 UTC | #4

Do you expect to have a high level of script interop? I make data-driven games so in most cases I can avoid the script part, and lose the benefits of hotloading, not that I usually notice. 
My opinion only: generally I would consider/recommend deriving from LogicComponent.
In one special case I derive from Urho3D::Object, but its my gamestate manager top level object, near the application object, and not like the things it controls.

-------------------------

Lunarovich | 2019-04-15 12:38:10 UTC | #5

@Leith, no, I'm just using C++. 

[quote="Pencheff, post:3, topic:5099"]
expose that as attributes.
[/quote]

What does it mean to expose something as an attribute? I was reading docs, and they're explaining how to use URHO3D_ATTRIBUTE for the serialization. What does it mean to **register an attribute**? For now, I know how to register a factory and a subsystem and I understand why we need to do it. However, I'm puzzled when it comes to attributes.

-------------------------

Pencheff | 2019-04-15 13:38:45 UTC | #6

You can add your own "properties" of an object (a component or UI element) using attributes. When you save your scene or UI layout, attributes of your object are saved too. You can have animated attributes using AttributeAnimation. If you make a multiplayer game for example, attributes are serialized over the network and can be synchronized to every player. You can edit attributes of an object in the Editor:
![attr|690x414](upload://xue31FJMZSknQ5J8INRcaP9Igjo.png) 
Notice the "Attribute inspector" on the right - these are the attributes of a Text UI element. Using URHO3D_ATTRIBUTE macros you register an attribute to call methods of your object (or access a variable directly). For example, when you change "Text" attribute, it calls Text::SetTextAttr() internally, which changes the actual text of the element then does internal things to display the updated string.

-------------------------

Lunarovich | 2019-04-15 13:59:27 UTC | #7

@Pencheff, thank you for this elaborate answer. Besides the use in the editor and for (de)serialization, is there any other need to register attributes? For example, can I animate my custom Object based class attributes without using  URHO3D_ATTRIBUTE?

-------------------------

Pencheff | 2019-04-15 14:07:19 UTC | #8

You probably can, but I don't see a reason you are trying to avoid using URHO3D_ATTRIBUTE :slight_smile:

-------------------------

Lunarovich | 2019-04-15 14:27:02 UTC | #9

I'm not really trying to avoid using it :slight_smile: I just want to see what it is used for. I want to understand better how Urho3D works. So, my next question would be, when and why one should use [RegisterAttribute](https://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_context.html#a05cc4b7fca0d74caf169def5b1ce172c) method?

-------------------------

JTippetts | 2019-04-15 21:50:58 UTC | #10

There are macros to keep you from having to call RegisterAttribute directly. See the macros in [Serializable.h](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/Serializable.h#L240) and consult the various samples for usage.

-------------------------

Lunarovich | 2019-04-16 12:09:00 UTC | #11

Thank you, everyone. I've decided to publically inherit from Text and Window classes. I'm doing a mini-roguelike framework, so my game does not use scene system at all. Sometimes in the future, I'll probably rather inherit from Sprite than from Text, but for now, I'm ok with this solution.

If anyone is interested, I've decided to implement my own "viewport". Basically, my world map is a UI window inside another UI window. The latter behaves as a viewport for the containing window. So far so good :smiley:

-------------------------

JTippetts | 2019-04-16 14:57:11 UTC | #12

In my experience, it is rarely necessary to inherit from the UI leaf classes to accomplish something in Urho3D.

I'm not sure how 'doing a mini-roguelike framework' would preclude using a scene manager and require inheriting from Text and Window. This seems like an ideal candidate for a scene manager, with the Urho2D system sitting on top if it's a 2D roguelike.

As for your world map window, this is a good candidate for a scene that is rendered to texture then displayed as a sprite in a UI element. For example, in this prototype world-map screen shot from my own game:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/f/fbd329b8c8356b49d556ffd38211b48865c8cb4f.png'>

The world map is its own separate scene that renders to a texture. The texture is then drawn as a Sprite inside a Window. No need to inherit from anything to implement it, it works with Urho3D right out of the box. This can of course be done with any scene: a 3D one as in my example, or a 2D one with sprites for a 2D world map, as in this prototype of mine:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/b/be1743ca09075518f040c6a57fdc02c60fc0ce19.jpeg'>

(This had the cool benefit of being able to reuse the rendered texture for the in-world map table graphic.)

Typically, the only Objects I ever need to inherit from are: directly from Object (for subsystem-like systems) and from Component (or, more commonly, LogicComponent). For everything else, basic Urho3D objects are usually sufficient.

-------------------------

Lunarovich | 2019-04-16 15:10:39 UTC | #13

[quote="JTippetts, post:12, topic:5099"]
I’m not sure how ‘doing a mini-roguelike framework’ would preclude using a scene manager and require inheriting from Text and Window. This seems like an ideal candidate for a scene manager, with the Urho2D system sitting on top if it’s a 2D roguelike.
[/quote]

The problem with the Urho2D is that it does not allow me to use text letters as sprites. I know that a possible solution would be to use some kind of texture atlas with letters. However, I wanted to have letters out of the box. I really don't need the  physics system, collision checking, etc. That is why I opted for using only the UI elements.

[quote="JTippetts, post:12, topic:5099"]
Typically, the only Objects I ever need to inherit from are: directly from Object (for subsystem-like systems) and from Component (or, more commonly, LogicComponent). For everything else, basic Urho3D objects are usually sufficient.
[/quote]

Yeah, that's why I've asked this question, cause it seems to me that I've read somewhere that one does not need to inherit from the Urho3D classes, only from Object and LogicComponent, as you say.

-------------------------

JTippetts | 2019-04-16 16:06:34 UTC | #14

You can use the [Text3D](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/UI/Text3D.h) component to handle drawing entities as letters. Text3D puts a bit of text 'into the world' at a specified location by attaching it to a Node. You can see it in action in the [32_Urho2DConstraints](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/32_Urho2DConstraints) sample, as well as in a few of the 3D ones where it is used to put a title above an object in the 3D world. In 2D, it can be used to simply draw text at the location of a scene node.

The reason I recommend using a scene, is you get all of the various scene management stuff (culling, batching, etc...), plus if/when you decide to mix non-letter sprites into it, ie for landscape graphics and such, then it's easy.

-------------------------

Lunarovich | 2019-04-16 16:38:03 UTC | #15

@JTippetts, that's a great suggestion! Thank you very much!

-------------------------

JTippetts | 2019-04-16 17:04:22 UTC | #16

Here is a very quick example using Lua:
https://pastebin.com/5jihwMjg
Image:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/e/eee49f25a27e888c04d28643cbea86a0e4aafa07.png'>

Note, you will have to do some thinking about sizing (viewport, ortho camera, font size) and spacing, but that should be pretty easy to handle. Objects are Nodes, meaning they can have attached components for logic and functionality, etc... You can use Z coordinate of Node position to handle layer draw sorting.

-------------------------

Lunarovich | 2019-04-16 17:37:39 UTC | #17

Thanks! I'm very, very grateful for this one! This looks great. 

Well, I'll have to refactor a lot now :slight_smile:

EDIT: I've just tested it. Looks very nice :slight_smile:

-------------------------

Modanung | 2019-04-17 13:06:01 UTC | #18

As long as you do not inherit from `Node` you should be fine...
https://discourse.urho3d.io/t/node-getscene-return-null/96/5

-------------------------

Lunarovich | 2019-04-17 20:07:05 UTC | #19

While we're at it, what's the recommended way to do the inheritance in Lua scripting? Is this [kind of inheritance](https://www.lua.org/pil/16.2.html) ok, for example?

EDIT: I've just realized that Node is a userdata in Lua, so there's no option to do an inheritance by means of tables. I was wondering how one goes about adding a special purpose functions to game entites. For example, if I have a hammer entity, how do I add some method to this entity? The only thing that comes to my mind is to have a wrapper table and a Urho3D hammer node as a member of this wrapper table and than to add methods to this table. Is this a viable solution? The bonus of this solution is that it allows inheritance via tables.

-------------------------

jmiller | 2019-04-18 15:46:03 UTC | #20

[NinjaSnowWar](https://github.com/urho3d/Urho3D/tree/master/bin/Data/Scripts/NinjaSnowWar) uses inheritance (GameObject as base) and ScriptObjects -- maybe helpful?

-------------------------

JTippetts | 2019-04-19 17:14:31 UTC | #21

A Node provides a mechanism for entity definition via composition. The usual method for adding behavior to it is to add components, either out-of-the box components, custom C++ components, or ScriptObject components.

For example, here is a part of the main player character object definition in my own game, Goblinson Crusoe. (Just a portion, for brevity.)

https://pastebin.com/JWLtzAn9

If you take a look at that definition, you see a straight XML document defining the components that comprise a Goblinson Crusoe combat player object. You'll see some Urho3D components (AnimatedModel, AnimationController) and you'll see a whole bunch of custom components (Highlighter, for setting a shader highlight attribute on mouse hover; FloatingCombatText for reporting damage numbers; CombatActionController, a FSM-based action controller for implementing movement, attacking, etc...)

Entities such as GC, mobs, trees, etc... are all plain vanilla Nodes, no packaging or wrapping. All of the custom behavior and stuff are inside the custom components. Communication among the various components is a mix of events (if more than one component, or an outside entity, is interested in something) and direct component coupling (where it makes sense, like in animation stances and handling).

In the prototype, all of these custom components were implemented in Lua is ScriptObject classes.

I don't believe inheritance to be necessary, outside of the minimal amount required in the Urho3D framework to make the component-based system work. Components with event communication provide everything necessary to make disparate and varying objects possible.

-------------------------

Lunarovich | 2019-04-19 20:52:56 UTC | #22

Thank you for this elaborate answer. I find this discussion very interesting. It is about basic design principles. I find, on the contrary, that inheritance in Lua is rather easy and pleasant to use and does not have the overhead of C++ or Java instancing, at least, when it comes to a mental overhead.

On the other hand, in some instances, inheritance model comes more naturally than the component-based model. Especially if you have some "formal ontologies" in your game like Entity > Item > Tool > Shovel, or like Entity > Actor > Animal > Monkey, etc.

-------------------------

Leith | 2019-04-20 06:10:36 UTC | #23

The main cost with Lua is crossing the boundary between Lua and C++.
Every time a call needs to be made from one language to the other, the arguments need to be carefully wrapped and unwrapped, with type-restrictions enforced, and functions need to be looked up and executed, and possibly return values need to be carefully wrapped and unwrapped. There is overhead, and it compounds quickly when our code is designed without regard to that overhead.
For this reason, in my opinion, it's better not to have a low-level interface on the lua side, but instead to offer a simpler yet richer interface (you have less api to worry about, and so less calls across the language barrier, but more parameters are involved).

One way to optimize performance when using Lua with C++, is to try to do everything in one language or the other, and avoid cross-calling.
Another way to optimize Lua applications is to measure the performance of Lua functions, and consider the slow ones as candidates for promoting to c++ (since the call overhead for calling this function in C++ from Lua is now less than the cost of the function in Lua, given that the cost of the Lua function is likely to be caused by cross-calling to C++ functions, including your math-wrapper functions).

-------------------------

