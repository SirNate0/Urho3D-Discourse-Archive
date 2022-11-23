talos | 2021-01-16 16:56:37 UTC | #1

Greetings and salutations! 

I am completely new to Urho3D, but after extensive research of alternatives, this engine appears to fit my needs perfectly. I have big plans, hopefully you will be seeing me here often, asking questions!

Asides from the official Documentation, Demos and Wiki, are there any other great resources I should be aware? I plan to be working with C++, making extensive use of instancing, texture-arrays, physics and networking. 

Any advise for a beginner like me will be appreciated. Any additional resources for learning the libraries will also be appreciated.

-------------------------

throwawayerino | 2021-01-16 19:31:55 UTC | #2

Urho3D is a very hands-on engine unlike the others out here. It's centered more around the library rather than the editor and I believe that is what makes it give faster results as it never tries to slow you down.
I'd say that 99% of everything you'll ever ask may have been asked before in the forum archives, but don't hesitate to ask here if you feel lost. There's a terrain editor and a nice skeleton constraint editor made by the people here that are worth looking at.
Learn how to use attributes and events in Urho3D efficiently. Attributes are really nice as everything uses them and you can animate them quickly and integrate any variable into the editor with 1 macro + get/set functions. Events are really powerful and you can let components communicate with each other with little setup (despite the risk of code spaghetti).
The engine is completely usable without the editor, but learning to use it is very worthwhile especially if you plan to work with UI.
And grab a copy from master branch, not the 1.7 release!

-------------------------

JSandusky | 2021-01-18 05:59:41 UTC | #3

Make yourself aware of API limits and how Urho uses those limited things. From my own experience blowing the D3D11 SamplerState limit before with scores of tiny 16x16 textures before I fixed it as a table in a fork.

View, Renderer, and RenderPath are your danger-zone classes. Everything you touch there is likely to have serious consequences or balloon in the scale of changes required beyond what you might imagine.

Code search for the `WorkQueue` so you know what's already jobified so you don't do something stupid trying to jobify things that are already jobified in some fashion elsewhere.

Balance your script and C++ code usage. Some tasks like those that touch crowds and physics events are better suited for C++ than Angelscript/Lua.

There's a handy-dandy `WriteDrawablesToOBJ` capability that you can use to dump your scene/geometries to OBJ so you can use it as a reference in other tools (or for other purposes like static-batching). This is useful when you need to generate geometry in other tools like Houdini or just fitting some spline generated extrusions in Blender.

Beware that the async loading is actually brittle as hell. If there's a pending async load you have to force it to finish before queueing a new async load. You can quickly tweak that to pump asyncs into a vector though and cycle through them for each step of the async load. If you intend to use async load, then you **MUST** modify the function to accept a destination Node. It's borderline unusable without it as you can't dump async things out if you don't have a holder for them.

Edit: Urho is also not setup for texture streaming. If you need that you need setup your own file scheme for how you load mips from bottom to top instead of the usual top to bottom and setup the sampler LODs appropriately to cap the miplevel.

-------------------------

talos | 2021-01-22 03:25:56 UTC | #4

Thank you a lot for your amazing answer. Much appreciated.

-------------------------

talos | 2021-01-22 03:27:21 UTC | #5

Thank you a lot for your amazing answer. I plan to be working with textures a lot so these details are very valuable to me. Much appreciated.

-------------------------

