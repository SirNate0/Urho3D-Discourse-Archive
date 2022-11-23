setzer22 | 2017-01-02 01:00:12 UTC | #1

Hello everyone!

I've already asked a more general version of this but I'm struggling to find out how to make it work, so I'd like to ask for a dummy-proof answer. Here's my question:

How can I make a c++ class o be shown on the editor like a regular component? (No need to have a menu entry for it, just being able to add it and modify its values on the fly is more than fine, just like script objects, but  being c++). I'm asking what should I inherit from, how should I compile it and how should I add it to the editor.

I think this might help other newbies lilke me and I'm willing to write a tutorial / guide / wiki page once I figure this out!

Thank you!

-------------------------

friesencr | 2017-01-02 01:00:12 UTC | #2

Update:  I was wrong.

-------------------------

cadaver | 2017-01-02 01:00:12 UTC | #3

Your class needs to be a subclass of Component.

Look at something like the C++ VehicleDemo sample, where it registers the Vehicle component (factory + attributes). Then, like said in the earlier topic, you must execute the registration code before running the editor script. You can use the form Context::RegisterFactory<MyComponent>("MyCategoryName") to have the component appear in a specific Create -> Component sub-menu in the editor.

-------------------------

setzer22 | 2017-01-02 01:00:12 UTC | #4

Finally I managed to do it!

Your explanation was quite clear but I had a hard time figuring out how to compile my classes and link them against Urho3D without using CMake. In the end I learned cmake as I couldn't find any other way.

For anyone reading I found all the required info to compile in the documentation: [urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html)

Also I had to edit the Urho3DPlayer script in order to make it appear on the menu under a custom category as you explained, no big deal, but would be nice to have a way to define a custom list of classes to  register as components before urho3d player starts a given script.

-------------------------

cadaver | 2017-01-02 01:00:12 UTC | #5

I'm not quite sure of what you're asking. Additional C++ components require them to be linked to the executable, but there's no way for the Urho library/engine, or an unmodified Urho3DPlayer to know of them.

Typical way to solve this would be to load plugins as dynamic libraries. The plugins would have some kind of constructor / initialization function, which registers any subsystems or classes contained within. However, there's no plugin system in Urho (at least so far), instead the assumption is that a C++ application uses it like a library, and from that follows that it's the C++ application's responsibility to register any classes or functionality outside of Urho's builtin ones.

EDIT: note it's also just as valid to "fork" Urho3D and add your own classes directly to it. This fits particularly well if you need to do other engine customization at the same time. Then you'll just have to deal with merging upstream updates.

-------------------------

setzer22 | 2017-01-02 01:00:13 UTC | #6

Yes you're right, there's no easy way to do this. It could always be done setting up a system that modifies Urho3DPlayer's source code and recompiles it dynamically. Anyway, once you get the workflow adding new components isn't that much of a pain. Furthermore the scripting is really well integrated so there's no much need for a lot of C++, I just watned to know for the sake of knowing how to do it and understand the engine before I start using it.

So, Thank you! I'll mark this as solved (Forgot to do it yesterday)

-------------------------

