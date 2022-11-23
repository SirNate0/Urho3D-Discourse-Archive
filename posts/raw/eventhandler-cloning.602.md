OvermindDL1 | 2017-01-02 01:01:36 UTC | #1

Any chance of getting a virtual Clone function for the EventHandler hierarchy?

-------------------------

cadaver | 2017-01-02 01:01:37 UTC | #2

Can you explain the scenario where you need this? Do you mean that you want to copy the handler function pointer and/or the receiver object pointer from an existing EventHandler object, and use that to subscribe to another event? This is probably an easy addition, just want to make sure that the API will be right for the usecase.

-------------------------

OvermindDL1 | 2017-01-02 01:01:43 UTC | #3

[quote="cadaver"]Can you explain the scenario where you need this? Do you mean that you want to copy the handler function pointer and/or the receiver object pointer from an existing EventHandler object, and use that to subscribe to another event? This is probably an easy addition, just want to make sure that the API will be right for the usecase.[/quote]
I was writing a dynamic system for my Options screen and just wanted to pass around a handle to multiple events through a function, and since it is not a shared pointer (rightfully so) the even system owns it and deletes it itself (which is not safe if it crosses DLL boundaries on Windows do note), thus I need a unique instance for each subscribe call.  Since the handler is abstract and it is a templated subclass then I cannot easily even just memcpy it safely, thus a Clone or so method to safely duplicate the entire EventHandler object would be best.

Have you thought about using std::function (with a fallback to the identically typed boost::function, which can be included in Urho3D while renaming the boost namespace to urho3d using the boost bcp tool to fully embed it) as it handles these usecases properly without needing a clone (as it does it by using a base type that encodes a certain amount of bytes internally else falls back to reinterpreting them to a secondary pointed object for speed reasons, would likely outperform the EventHandler object as well)?

-------------------------

cadaver | 2017-01-02 01:01:44 UTC | #4

Clone() function added to master.

-------------------------

OvermindDL1 | 2017-01-02 01:01:45 UTC | #5

[quote="cadaver"]Clone() function added to master.[/quote]
Thanks much.

-------------------------

