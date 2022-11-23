ghidra | 2017-01-02 01:14:34 UTC | #1

This post is not about getting custom components in the editor. I managed that, thanks to all the other posts....
It's quite ingenious actually (not my method of getting custom components in, but how Urho3D works in allowing it, a testament to the Authors).

I stole the basic code from Urho3DPlayer.cpp to use the arguments to throw a switch in my app to load the editor script. Since my main.cpp already did all the work of registering all the components, it just "works" (assuming the components are script ready).

Anyway...

I am at a point now... where I want to be able to debug my components while i am messing with the in the editor.
If I change an attribute for example, I am running a method in code that does some stuff. But so far I have not been able to output anything with URHO3D_LOGWARNING. Normally if I am just running the base app, all that behaves as expected. In the editor, it doesnt. Probably by design, but I am unsure how to work around that.

How might i print things to the console? Or what is the best method to get some feedback from what is happening in code?

Another question... is there a key that brings up that script console? I didnt find a entry in the menu bar? Maybe I am missing something?
Because maybe it is printing to that... but not opening it?

Thanks for any clarity.

-------------------------

cadaver | 2017-01-02 01:14:34 UTC | #2

F1 should bring up the console in editor. Make sure you have built Urho + your application with logging enabled (build option URHO3D_LOGGING=1).

-------------------------

