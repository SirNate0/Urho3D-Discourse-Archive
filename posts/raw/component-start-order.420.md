setzer22 | 2017-01-02 01:00:17 UTC | #1

Is there a way to control the start order of the various components in a scene?

I've found that in the editor, whithin the same node, the components get usually started from top to bottom (I don't really know if this is consistent). Do nodes also get initialized (all of its components) in a top-to-bottom fashion?

Is there a way I can reliably control that? I've got some components that rely on other components being already initialized.

Thank you very much!  :smiley:

-------------------------

cadaver | 2017-01-02 01:00:17 UTC | #2

The component that has been added first will be initialized first. When child nodes are involved, the order should be: all components in first child in order, then all components from second child.. The order is preserved in load/save.

When event subscription is involved (for example update events) then there are no guarantees for the order.

Generally relying on order will lead to fragile code though. I'd recommend for example looking up other components the first time you actually need to perform some operation on them, and then cache the component pointer for faster access later.

-------------------------

setzer22 | 2017-01-02 01:00:17 UTC | #3

Well, as I thought relying on order is not really robust.

[quote="cadaver"]I'd recommend for example looking up other components the first time you actually need to perform some operation on them, and then cache the component pointer for faster access later.[/quote]

The thing is, that I have a component that reads and parses and XML file, which is set as an attribute through a resource pointer. Then, other components need to query that main component for some data at initialisation time. 

To clarify let's say component A is the one that reads the XML file, and component B requires a value stored in A that gets correctly added after A has parsed the file (i.e. after A::ApplyAttributes() has been called).

I don't see a way to do this besides calling a custom method for B instead of apply attributes at A::ApplyAttributes. But this seems more like a design issue, components should be independent enough to not require each other's data during initialisation. How is this usually solved?

-------------------------

friesencr | 2017-01-02 01:00:17 UTC | #4

[quote="setzer22"]Well, as I thought relying on order is not really robust.
I don't see a way to do this besides calling a custom method for B instead of apply attributes at A::ApplyAttributes. But this seems more like a design issue, components should be independent enough to not require each other's data during initialisation. How is this usually solved?[/quote]

Components don't require other components.  The node composes the components.  It seems like a smell to me.  Does a component require a StaticModel or something?

-------------------------

setzer22 | 2017-01-02 01:00:17 UTC | #5

[quote="friesencr"]Components don't require other components.  The node composes the components.  It seems like a smell to me.  Does a component require a StaticModel or something?[/quote]

Well, sometimes components have to interact. That's what I understand by requiring. Component X needs Y to be present in the node/scene. That's the case for most scripts, which rely on a particular scene configuration, isn't it?

Although I feel like this one is a bad design choice. The thing is I've got a config file from which multiple components in the same node need to take info. I thought: "Why would them all need to query the same XML file over and over? Instead I could make a component that parses the config file (the properties component) and then make other components in that node look for the properties in the properties component". The problem is most of those properties are needed at initialization time, and if I can't ensure the properties component is loaded before the others, it won't work. But this doesn't feel like an Urho3D related issue anymore.

-------------------------

szamq | 2017-01-02 01:00:17 UTC | #6

Check out DelayedStart method, it may be helpful for you

[quote="http://urho3d.github.io/documentation/HEAD/_scripting.html"]When a scene node hierarchy with script objects is instantiated (such as when loading a scene) any child nodes may not have been created yet when Start() is executed, and can thus not be relied upon for initialization. The DelayedStart() method can be used in this case instead: if defined, it is called immediately before any of the Update() calls.[/quote]

-------------------------

