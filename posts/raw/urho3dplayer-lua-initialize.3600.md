zakk | 2017-09-23 15:25:55 UTC | #1

Hello,

[According to the documention of main loop](https://urho3d.github.io/documentation/1.4/_main_loop.html), _Initialize()_ is a class called when Urho3d is started, before entering the main loop.

[Clicking on _Initialize()_ on the above link lead here](https://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_engine.html). I don't see functions related to _RenderPath_ changing. I'm confused from the start :/ .

`Urho3dPlayer` has a number of parameters which are obviously related to _Initialize()_ class.

Not everything is possible from the command line parameters. For example, you cannot change the default RenderPath, which is by default _RenderPaths/Forward.xml_ .

So what if i want to use _Initialize()_ functions in a Lua script run by `Urho3dPlayer` ?

At first, i tried a sort of overriding of _Initialize()_, with putting this in my script:

> function Initialize()
>   print("Initialize has been called.")
> end

When running the script, the above code is obviously not called.

I've grepped *RenderPath* from the Lua samples scripts, and found reference in *09_MultipleViewports.lua*.

>    local effectRenderPath = viewport:GetRenderPath():Clone()
    effectRenderPath:Append(cache:GetResource("XMLFile", "PostProcess/Bloom.xml"))
    (…)
    effectRenderPath:SetEnabled("FXAA2", false)
    viewport:SetRenderPath(effectRenderPath)

I understand the code above, but is doesn't seem related to an _Initialize()_ class or function.


Is _Initialize()_ a function, and not a class ? How can i use it from a script ?
Should i use _Viewport_ global object for changing parameters at start, and forget about _Initialize()_ ?

Thank you for reading :)
Zakk.

-------------------------

Eugene | 2017-09-23 16:38:36 UTC | #2

What's your use case? What do you want to do?

-------------------------

zakk | 2017-09-23 16:44:59 UTC | #3

I want to understand how to use Urho3D with Lua and the script player (`Urho3DPlayer`).

That's why i'm reading all i can find, and try to understand from the beginning : i don't want to include _Sample.lua_ , i rather like to understand a bit what's behind the Lua curtains.

Urho3D is quite mysterious for me, so i try to solve questions one by one.

-------------------------

Eugene | 2017-09-23 18:46:54 UTC | #4

https://urho3d.github.io/documentation/HEAD/_running.html

> An application script is required to have the function void Start(), which will be executed before starting the engine main loop.

-------------------------

JTippetts | 2017-09-24 10:25:03 UTC | #5

Initialize is a method in the Engine class. It's just a huge pile of boilerplate code, and nothing in there is controllable directly from the Lua scripting system, or really concerns the Lua system in any direct way. Various defaults, such as default renderpath, are set (not directly from Initialize, but usually within the related subsystem(s)) but most can be overridden or changed through command-line args or code. For example, you can change the renderpath using one of 3 command-line args: -deferred, -prepass, or -renderpath with a path argument to a renderpath descriptor. Additionally, you can specify a renderpath manually in code as in the examples you have already looked at.

I don't really recommend modifying the library to change the defaults; they're default for a reason (usually, because it's the simplest/most widely supportable option) and it's easy enough to change on an application basis.

It's reasonable to not want to use Sample.lua, but it's still a good idea to at least peek at it and get an idea for what's expected. While a lot of boilerplate initialization is done behind the scenes, there are still tasks that you need to perform for your own situation such as setting a cursor if needed, constructing a UI (the Sample sets up a very basic one, but in real use you'll need to get a bit more elaborate) and building a scene. Sample.lua is just a simple framework that handles certain tasks that repeat across all the various examples. It's suitable for examples, and that's it. Still, it does show the basic outline of what you have to do. (At the very least, provide a Start() function and put some stuff in it.)

As far as using Urho3D with Lua, it's very similar to using it with AngelScript. The Lua glue code tries very hard to keep the 2 paradigms at least superficially similar, and in fact it is easier to use the two scripting systems than it is to use C++, due to the fact that you don't need to manually write the various boilerplate required for creating a custom C++ component (RegisterFactory, etc...), and you don't need to touch the code in Application as you might need to if you are writing a C++ program. The ScriptObject functionality works pretty well out of the box.

There are some wrinkles with the Lua system that don't occur with the AngelScript system, however, due to the nature of the Lua garbage-collection system and the tolua binding generator used to build the binding boilerplate code. There are certain situations you really need to steer clear of. For example, creating Urho3D objects inside nested loops is usually Bad(TM). I'm talking about situations such as this:

    for x=0,img.width-1,1 do
        for y=0,img.height-1,1 do
            img:SetPixel(x,y,Color(1,1,1,1))
        end
    end

This kind of thing is bad, and the larger that the image is the worse it gets. (Naturally, this exact example isn't likely something you'll be doing, but it is feasible that you might be building images in some fashion. I procedurally generate a lot of various images/maps/buffers, so I run into it a LOT.) The reason this is bad is that tolua keeps various behind-the-scenes tables to hold the objects that are created (Color objects, in this example). Inside a nested loop like this, the count of objects grows quite large, and thus the table they are stored in grows quite large. When the objects are garbage-collected they go away, but those large tables that they were stored in remain, and will remain large and unwieldy, for the duration of your program execution time. Some periodic processing is done on these tables during garbage collection phases. Do this enough, with large enough object counts, and you will see some pretty nasty performance consequences.

This doesn't occur with the AngelScript system; it's purely an artifact of the creaky and aging tolua++ binding generator. However, as long as you steer clear of this kind of situation, it should work well. (I get around it in my own projects by writing custom C++ code and building a custom Urho3DPlayer.exe with the custom bits exposed to Lua script.)

There are other weirdnesses related to the fact that Lua garbage-collects everything, and the GC doesn't mesh perfectly with Urho3D's SharedPtr memory management system, not as nicely as AngelScript does at any rate. I love Lua, and I use it pretty much exclusively since I find AngelScript kind of awkward to use in many respects. Nevertheless, there is a pretty strong argument that can be made in favor of using AngelScript, since its integration with Urho3D is significantly less quirky.

-------------------------

zakk | 2017-09-24 13:21:29 UTC | #6

Thank you  for your answer, it was really informative.

My biggest problem with Urho3D is maybe that i'm not sure on how to understand the concepts involved so i peek here and i poke there. For example , some days ago, i wasn't aware of what is a _renderpath_. I finally understood reading the documentation that it's a sort of state machine with predefined steps for drawing a scene.

It's just an example, because the whole Urho3d seems big for me. I know that _renderpath_ is not specific to Urho3d, it's just to mention that i surely lack some basic notions in modern videogame world.

For a more specific Urho3d notion, i must admit that `VariantMap` are obscure for me. Parsing the doc, i've seen it is a template for defining a dictionary of `Variant` types (the basic objects of Urho3d, i guess). Fine, but what about Lua ? Is this existing directly ? Or may be it has to be implemented with a table of `Variant` maybe ? You see, just an example, but questions like these raise often these days.

That said, of course i've looked what _Sample.lua_ was doing , as it does a lot and as it will be something to be done in my own code , one way or another. But i don't want to blindly call boilerplate code, that's why i'm trying to do things myself without helpers (even if i end up using helpers when i have understand the basic principles)

I'm using Lua for quite a long time (discovered with the game Naev, and never left since). I am not very interested in Angel Script, even if it's more suit to use with Urho3d, because of it's narrow audience (i don't know the language itself, except it is statically typed, which is uncommun for a script language).

Thank also for mentionning traps with objects use in Lua.
I was thinking gullibly that something like img:SetPixel was just a thin wrapper to a `SetPixel` function, applied to its `self` object. I'm using Lua this way, when i come to C API. But here of course, we are talking about C++ and `tolua`.
So i keep this in mind.

I guess the correct way for texture generation would be to generate the pixel buffer with Lua, without Urho3D objects call, and then passing the whole buffer to an Urho3D texture. Of course, i would avoid doing this each frame, as in this case, we are hitting Lua limitations :slight_smile:

Another annoying thing i have encountered with Lua in Urho3FD is its intensive use of userdata. I know it's the pillar of exchanges between C and Lua , but for something like `function handle_update(eventType,eventData)` , i'd rather like to have two tables for _eventType_ and _eventData_, rather than an userdata, which i cannot explore with it's associated metatable (only standards fields in the metatable). I think doing this way (with userdate) is surely better for performances. And as i've found [this](https://urho3d.github.io/documentation/HEAD/_event_list.html) , there is no problem with events ;)

About the Lua documentation, i believe i can use the Angel Script documention. As stated somewhere in the documention, Lua and AngelScript have transitive functions implementation. So i guess i can use [this reference](https://urho3d.github.io/documentation/1.4/_script_a_p_i.html) with trust.

Thank you for reading,
Zakk.

-------------------------

weitjong | 2017-09-24 13:33:50 UTC | #7

We also have generated page for Lua scripting API. https://urho3d.github.io/documentation/HEAD/_lua_script_a_p_i.html

Also, note the document version on the top right corner of the documentation page. You may want to switch to the version you are currently using or HEAD when you are tracking the master branch.

-------------------------

JTippetts | 2017-09-24 16:29:39 UTC | #8

A Variant isn't necessarily a basic Urho3D object, so much as it is a sort of catch-all datatype that can _hold_ basic Urho3D objects. In a way, Variants are redundant for Lua, since in Lua, which is dynamically typed, any variable or reference or table member can hold any type, be it a string, a number, a function, or whatever. Such things are not possible in native C++, without using an intermediary such as Variant.

Consider the Lua code:

    local thingy=4.0
    thingy="thingy"

In Lua, that is no big deal. Happens all the time. thingy is not declared with any particular type, because it's not necessary to do so. However, in C++, you need to declare your thingy with a particular type:

    float thingy=4.0;

You can't then override thingy with a string type:

    thingy="thingy";   // Doesn't work in C++

Since C++ is statically typed, you can't just assign different types of values to a variable willy-nilly. Most of the time, that's not an issue. However, one case in which it is nice to be able to do so is in ad-hoc message passing schemes.

In message passing, you have a centralized dispatcher that sends messages from objects to other objects. What, exactly, the content of these messages is is irrelevant. It just takes a message from object A and sends it to object B, and lets B worry about what the message content is. In order to facilitate such a system, you need a data type that can hold an object of any other data type. In order for the body of the message to be generic and flexible, you need an _any_ data type. So that object A could send the message {type="ReduceHitPoints", damage=14} to object B, while object B sends the message {type="ImDead", whokilledme=objectA} to object C, and the message-passing infrastructure doesn't need to know the particulars of these messages. You don't need to come up with dozens of different message structures to facilitate each one; you can just populate a VariantMap with the various data that particular message needs and send it along.

It's a lot like simply populating a Lua table with the various data you need and sending it along. Same principle, it's just that Lua was designed from the start to be dynamically typed, while C++ was not. Variant and VariantMap (along with VariantVector) provide a certain amount of dynamic typing to facilitate the passing of ad hoc messages. And even in Lua, since you are interacting with the C++ library, you need to use Variant and VariantMap to pass your messages, since the C++ code expects it. Think of them as a kinda more convoluted Lua table, addressable by string keys, and you'll be fine.

This touches on your desire to have two tables for eventType and eventData, rather than userdata. Lua would be fine with two tables, but since the C++ engine code doesn't know what to do with a Lua table, it expects instead a StringHash and a VariantMap. It would be valid to construct the binding such that on the Lua side of things you create a Lua table, and when it is passed to a function expecting a VariantMap it is converted behind-the-scenes. However, that is not the way these bindings were constructed. Doing it the way it does it now keeps the interface and usages similar among Lua, AngelScript and C++. In each case, you construct a VariantMap and populate it with data; doing it _differently_ in Lua alone would break the paradigm and make it more difficult to maintain the bindings, I think.

In the case of my example with SetPixel, the problematic part of that line is the Color(1,1,1,1) that is passed to SetPixel. This constructs a garbage-collected instance of the Color class and passes it. Since it's garbage-collected (ie, its lifetime is managed by the Lua garbage collector) then it is stashed in an internal table until it is garbage collected. In an inner loop like that, you can end up creating thousands of such objects which cause the table to explode in size. When they are all garbage collected, that internal table isn't resized to a smaller size, causing a performance drain when looking for other objects to collect.

In addition to the Lua script API page that @weitjong pointed out, I find great value in looking at the .pkg files used by tolua++ to generate the binding code, located in Urho3D/Source/Urho3D/LuaScript/pkgs to see exactly how the bindings are structured and what they require.

-------------------------

