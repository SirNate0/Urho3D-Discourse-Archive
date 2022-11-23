dprandle | 2018-12-13 19:36:31 UTC | #1

Hello - I'm trying to understand if script object attributes are replicated to clients. I would think by default they are - as AM_DEFAULT includes AM_FILE and AM_NET. However, the wiki says the following:

"Network replication of the script object variables must be handled manually by implementing WriteNetworkUpdate() and ReadNetworkUpdate() methods, that also write and read a binary buffer. These methods should write/read all replicated of variables of the object. Additionally, the [ScriptInstance](https://urho3d.github.io/documentation/1.7/class_urho3_d_1_1_script_instance.html) must be marked for network replication by calling MarkNetworkUpdate() whenever the replicated data changes. Because this replication mechanism can not sync per variable, but always sends the whole binary buffer if even one bit of the data changes, also consider using the automatically replicated node user variables."

From my understanding the member variables of an angelscript class that inherits from ScriptObject will have all of its members that can be converted to a Variant and that don't start with an underscore automatically registered as attributes.

So... are these attributes replicated to clients when the ScriptObject and owning node are created in REPLICATED mode?

Also.. out of curiosity, what happens if a node is created in LOCAL mode and components for it are created in REPLICATED mode?

Thanks for your time

-------------------------

Sinoid | 2018-12-12 02:50:42 UTC | #2

[quote="dprandle, post:1, topic:4732"]
From my understanding the member variables of an angelscript class that inherits from ScriptObject will have all of its members that can be converted to a Variant and that don’t start with an underscore automatically registered as attributes.
[/quote]

They are, but the automatic attributes are created with AM_FILE mode. 

> So… are these attributes replicated to clients when the ScriptObject and owning node are created in REPLICATED mode?

They are not replicated automatically.

[quote="dprandle, post:1, topic:4732"]
Also… out of curiosity, what happens if a node is created in LOCAL mode and components for it are created in REPLICATED mode?
[/quote]

A component can not be created in replicated mode on a local node, the `CreateMode` will be ignored if you try to do so. 

If you somehow trick it into doing so then network updates will be mangled between server and client because components will add their nodes as network state dependencies (by ID) and they will not be able to correctly mapped to nodes on the other end as local IDs are in a different range than network IDs and may or may not match between clients.

-------------------------

dprandle | 2018-12-12 07:07:43 UTC | #3

Thanks for the quick reply!

[quote="Sinoid, post:2, topic:4732"]
They are, but the automatic attributes are created with AM_FILE mode.
[/quote]

I see - do you know why it is they are created with AM_FILE only? Also, I'm wondering if there is sort of a no brainer way to get these attributes to replicate (or some way that people usually do this without requiring the user to add it in their script)?

The project I am currently working on allows users to build maps - the editor is a sort of dumbed down version of the urho editor and its done in Qt to provide the user with GUI elements they are very familiar with on their OS. The user can create scripts - however since they are typically VERY simple scripts and the users won't really be coders - I am trying to get any vars the user makes to automatically replicate over the network. I have a couple of ideas on how to do this - but

If there is a sort of shortcut way - or maybe someone has done this already - I would love to hear.

Thanks!

-------------------------

Sinoid | 2018-12-12 19:21:05 UTC | #4

It's all handled in `ScriptInstance::GetScriptAttributes()`, you could rely on a naming convention and attach the appropriate mode to the attribute-info. It should *just work*^TM as long as you have AM_NET on the attribute and you're calling MarkNetworkUpdate.

Realistically, you'd **always** have to use virtual accessors (`int myProperty { get; set; }`) in the script-classes and call `MarkNetworkUpdate()` from in the setter since C++ side doesn't see member changes. Though that would help to hide obnoxious naming conventions like `sync_MyField` - in which case you might want to say ok to private+protected members if they pass your naming convention so they can be hidden behind the virtual properties AngelScript side.

Under the hood virtual properties aren't exposed like regular properties, they're actually java-bean like functions internally so they're not part of the binding to attributes - that comes with consequences if you should choose to use AttributeInfo to populate a GUI or something and expect networked fields to cause dirty marking.

---

**Side-note**: local filewatcher changes aren't synchronized over the network (that'd be *evil*) so editing a script with resource hotloading enabled on your end while using client-server will send synchronization to hell.

**Illustration of the above:**
```
class Rotator
{
    private int sync_degrees;
    
    int Degrees {
        get const { return sync_degrees; }
        set { 
            if (sync_degrees != value) { 
                MarkNetworkUpdate(); 
                sync_degress = value; 
            } 
        }
    }
}
```

**Edit**: other options are far more involved, using something like stb_c_lexer to scan for marker comments or such (`///@networked`) when script source code is loaded and storing that metadata somewhere to lookup during attribute filling.

-------------------------

dprandle | 2018-12-13 19:43:11 UTC | #5

Thanks again! Super helpful

[quote="Sinoid, post:4, topic:4732"]
you could rely on a naming convention and attach the appropriate mode to the attribute-info. It should *just work* ^TM as long as you have AM_NET on the attribute and you’re calling MarkNetworkUpdate
[/quote]

This is exactly what I was looking for! 

[quote="Sinoid, post:4, topic:4732"]
Realistically, you’d **always** have to use virtual accessors ( `int myProperty { get; set; }` ) in the script-classes and call `MarkNetworkUpdate()` from in the setter since C++ side doesn’t see member changes.
[/quote]

[quote="Sinoid, post:4, topic:4732"]
that comes with consequences if you should choose to use AttributeInfo to populate a GUI or something and expect networked fields to cause dirty marking.
[/quote]

So - currently in my GUI builder I show all attributes that are not marked AM_NOEDIT and for each attribute there is a widget that sets the attribute to the new value anytime the widget is edited... I couldn't really figure out a general way to detect changes to individual attributes so every frame I basically go through each attribute that has a widget, disable the signal from the widget that sets the attribute, and set the widget value from the attributes value (I'm thinking now I will try to only do this when the network node flag is dirtied instead of every frame).

I am wondering - theoretically - since script attributes are convertible to Variants - what if on the c++ side I checked all attributes with "sync" prefix before the script update runs and again after the update runs - and auto mark the network update flag for the node if any of those values have changed? Your thoughts?

I could require the virtual properties for networked attributes - and just brute force update the widgets associated with the attributes within ScriptInstance the way I am doing it now for everything else - but of course just requiring the "sync" prefix and doing the work for vars with that prefix on the c++ side is ideal.

The brute force thing works because the property editor only allows the user to view/edit attributes of a single node and associated components at a time - so theres never really that many attributes/widgets at a time.

EDIT - The map editor and game itself are two different applications - and once a script (and other resources) from the map editor are loaded in to a package, and that package is used in the game, they cannot be edited in the game. So - there should be no case during game play where a script is edited... The scripting portion is to allow the user to sort of mod the game - and I am currently creating most major gameplay parts of the game with scripting as well

-------------------------

Sinoid | 2018-12-13 21:00:55 UTC | #6

[quote="dprandle, post:5, topic:4732"]
I am wondering - theoretically - since script attributes are convertible to Variants - what if on the c++ side I checked all attributes with “sync” prefix before the script update runs and again after the update runs - and auto mark the network update flag for the node if any of those values have changed? Your thoughts?
[/quote]

I would do it only once, after the script runs - but cache those sync_ members' values after the script loads (when it applies the serialized attributes the very first time during initialization) to check for differences from the last update (swapping the new values for the cached ones so the cache is always up to date of course).

The two problems are going to be script handling of events (ie. a post-update changes sync state) and what to do about script-classes inside of your ScriptInstances that *should* be serialized according to naming - there's a bunch more on working with asIScriptObject and such in [asPEEK debugging server](https://gist.github.com/JSandusky/51f12192f40b90b4a09ee9138820e74c) that might be useful working reference on how arbitrary script classes are inspected (though it's all string printing). Though I think the attribute get/set stuff in Urho3D does cover everything except identifying regular AS classes.

---

Because of those problems you might be better off adding an event that the Network system sends at the very start of `Network::PostUpdate` (like an `E_NETWORK_PREUPDATE` or something). You would have to have the script system loosely track ScriptInstances that have sync attributes so they can report dirtiness (same caching process as above).

Don't be fooled by the `PostUpdate` name, the `Network` subsystem does that when in response to the `RenderUpdate` event which occurs after the real `PostUpdate` event.

-------------------------

