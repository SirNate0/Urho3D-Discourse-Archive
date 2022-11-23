rifai | 2017-01-02 01:00:20 UTC | #1

Where I can find list of all inbuilt angelscript event (update, postupdate, etc) ?  
I can find C++ event in header files xxxxEvents.h. 

Can I "register" my custom C++ event and using it from angelscript?

-------------------------

friesencr | 2017-01-02 01:00:20 UTC | #2

Reference is in the script documentation.
[github.com/urho3d/Urho3D/blob/m ... API.dox#L6](https://github.com/urho3d/Urho3D/blob/master/Docs/ScriptAPI.dox#L6)

You can use your own events.  Events are more or less a stringhash(a 32bit integer) with a stringhashmap of event parameters.  The code in c++ that registeres them in object.h:

[code]
#define EVENT(eventID, eventName) static const Urho3D::StringHash eventID(#eventName); namespace eventName
#define PARAM(paramID, paramName) static const Urho3D::StringHash paramID(#paramName)
[/code]

they reserve and make a constant of the names to minimize memory usage and increase performance.

On the script side you can either give a string or a stringhash. the string will be converted to a stringhash.

-------------------------

weitjong | 2017-01-02 01:00:20 UTC | #3

All the inbuilt events are listed in [urho3d.github.io/documentation/H ... _list.html](http://urho3d.github.io/documentation/HEAD/_event_list.html).

You don't actually "register" your own events in C++ in order to expose them to AngelScript and Lua. Your C++ class just send those custom events in your code at the point where they are desirable. Your script can subscribe to the new custom events just as if they are other inbuilt events.

-------------------------

rifai | 2017-01-02 01:00:20 UTC | #4

Thanks. I got it.

-------------------------

