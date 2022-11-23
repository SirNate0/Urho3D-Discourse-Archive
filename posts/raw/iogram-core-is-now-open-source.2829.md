godan | 2017-03-01 03:26:39 UTC | #1

Yep, as of this release, [the entire Node Graph and Geometry libraries are now totally open source](https://github.com/MeshGeometry/IogramSource). Also, we've released all the 150+ core components that are accessible via the Editor.

There is also a brand new Iogram release for [Windows, OSX, and Linux available here](https://github.com/MeshGeometry/Iogram/releases/tag/v0.0.5-wip).

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/5eb363be4ed8dd7084bf460042c668e196fc6dc2.png" width="690" height="388">

https://youtu.be/hdOY9ktaWtQ

-------------------------

hdunderscore | 2017-03-01 04:11:21 UTC | #2

The library looks like a real gem, big thanks for sharing the source ! I was recently looking for something similar to the geometry library you've shared, and I had trouble finding anything similar.

-------------------------

Eugene | 2017-03-01 13:53:03 UTC | #3

Great work!
However, your Iogram really, really, _really_ needs detailed text documentation and lessons. It is very puzzled and videos almost don't help.

-------------------------

godan | 2017-03-01 14:30:28 UTC | #4

@Eugene Yes, it certainly does! In fact, this week we are making a big push with the documentation/tutorials.

-------------------------

rku | 2017-03-01 16:33:57 UTC | #5

What is the practical application of this? It looks cool and all but i have no idea what it could be used for.

-------------------------

godan | 2017-03-01 18:05:09 UTC | #6

@rku I guess the main goal with Iogram is to make the best possible prototyping environment for 3d models, apps, and games. To me, this means a few things:

1. **No black boxes. Open source only please.** There is nothing worse than getting a great prototype working with 3rd party code, and then not being able to actually bring the project to market do to licenses, cost, lack of support, lack of features, etc...

2. **Levels of Abstraction**. Sure, sometimes I want to dig in to the guts of the rendering system, or deal with issues arising from floating point precision (boolean operations, I'm looking at you!). Most of the time, however, I just want to test my idea as fast as possible. I want to work with a rich set of components that let me figure out if what I want to do is easy/hard/impossible.

3. **Explore families of solutions, rather than single instances** I personally find it very difficult to start with a blank text file and code up exactly what I want perfectly, the first time. Instead, I find it far more effective to write modular systems and tweak their parameters, and find that perfect mix of values through exploration. There is actually a bunch of literature on this stuff ([check out this talk by Brett Victor](https://vimeo.com/115154289)).

So, that's the plan! We certainly have a ways to go, but I think this latest release is a pretty good step in the this direction. Would love to hear any thoughts on this!

-------------------------

hdunderscore | 2017-03-01 20:43:53 UTC | #7

The tool kind of reminds me of Houdini, and probably is useful to a similar audience. It might help to use similar terms as Houdini when describing Iogram.

Just playing with it a little -- I definitely need to see those tutorials :D

-------------------------

sabotage3d | 2017-03-02 00:05:09 UTC | #8

It looks like Houdini SOPs but in realtime context. Looks pretty cool. Thanks for sharing.

-------------------------

smellymumbler | 2017-03-02 14:01:13 UTC | #9

I'm so curious about how you handled the architecture behind this! I was working on something similar a few weeks ago, but more inspired by Houdini. Of course, my implementation was very naive and i started with a small noise texture generator created with nodes. 

The way i did it was, basically, a tree of nodes that i walked from the root. The root was always one output. From that, i walked to all leaves, checking if the node was runnable (by checking if all required ports were connected), and ran an execute() method on the nodes. Each node implemented the execute() method differently. My actual execute() code was just building a virtual shader, literally by copying shader code strings to a buffer. When i was finished with all nodes, i just executed the shader code.

Could you elaborate on your approach? It would be very enlightening to see other approaches on this. My approach seems very hackish, but i never found a better way of doing it.

-------------------------

godan | 2017-03-02 14:31:41 UTC | #10

@smellymumbler Hey, for sure. In fact, I can refer you directly to [the source!](https://github.com/MeshGeometry/IogramSource/tree/master/Core)

In our approach, we have three main classes for the Node Graph:

1. IoGraph - handles node add/delete, link add/delete, and solving the graph.
2. IoComponentBase - the base class for inheriting nodes that do particular things. There are a bunch of important functions in this class, but by far the most important is the SolveInstance. This handles what exactly the node does.
3. IoInputSlot and IoOutputSlot - these classes handle what kind of data is passed to SolveInstance, and the level of DataAccess (i.e. Item, List, Tree).

So, to interact with the NodeGraph, you would create some custom nodes from IoComponentBase and then add them to the graph, along with some connections, and add some data at the _exposed_ input slots. Here is an example from one of the tests:

```
	Context* myContext = new Context();

    //the data
	Vector<Variant> someFloats;
	someFloats.Push(7.0f);
	someFloats.Push(9.0f);
	someFloats.Push(11.0f);
	someFloats.Push(13.0f);
	someFloats.Push(15.0f);
	someFloats.Push(17.0f);

    //push data to data tree
	IoDataTree tree0(myContext, someFloats);

    //create graph object
 	IoGraph g(myContext);

    //create the Mass Average component
	SharedPtr<IoComponentBase> averager(new Maths_MassAverage(myContext));
	g.AddNewComponent(averager);

    //add the data tree input at component index 0, input slot index 0
	g.SetInputIoDataTree(0, 0, tree0);

    //solve using topological sorting
	g.TopoSolveGraph();

   //collect data
	IoDataTree outTree(myContext);
	g.GetOutputIoDataTree(0, 0, outTree);
```

We use a [topological sorting algorithm](https://github.com/MeshGeometry/IogramSource/blob/master/Core/IoGraph.cpp#L41) that orders that orders the nodes by their rank (i.e. how many edges away from being a root node). Then, you can loop through the nodes and call the Solve methods.

-------------------------

smellymumbler | 2017-03-02 15:38:38 UTC | #11

Very interesting! Thank you so much for the detailed explanation. I'll dedicate some time to read and understand the codebase, it's really well written.

I've noticed that you're passing the scene to the graph: https://github.com/MeshGeometry/IogramSource/blob/master/Player/IogramPlayer.cpp#L159

Is that how the components manipulate textures and geometry? You pass the scene and then, on the solve method, each component manipulates a part of the scene?

Also, what is the purpose of the PreLocalSolve() methods?

-------------------------

godan | 2017-03-02 17:39:43 UTC | #12

Hmm, I think passing the scene to graph is deprecated. Rather, I use the context variable (i.e. GetGlobalVar) "Scene" to get an active scene. This is probably not great.

PreLocalSolve() is an interesting one. The problem is that some graph nodes create state. For instance, the AddNode component adds a (scene) node when it is run. But without any other handling, this would very quickly create lots and lots of nodes. So, the PreLocalSolve() function is there so that components can implement a way to handle their state. [In the AddNode case, PreLocalSolve()](https://github.com/MeshGeometry/IogramSource/blob/master/Components/Scene_AddNode.cpp#L119) deletes all the nodes it created during the last TopoSolveGraph().

-------------------------

ghidra | 2017-03-07 22:29:04 UTC | #13

@godan this is super cool stuff.
Looking at the code, i noticed that the license at the top of each file seems to mirror urhos.
To be clear, is it MIT?

-------------------------

godan | 2017-03-07 22:36:02 UTC | #14

Yes, it is MIT. I guess we could probably state that somewhere, but I think the terms of the license are pretty clear (and more important than the name of the license). Also yes, the goal was to mimic Urho's license. Please let me know if I messed it up somehow!

-------------------------

slapin | 2017-03-08 00:13:48 UTC | #15

Can you please provide build instructions? I don's see root CMakeLists.txt, so I wonder...

-------------------------

godan | 2017-03-08 13:58:39 UTC | #16

Ah right. I suppose you will need that :slight_smile: I think each folder (i.e. Geometry, Core, etc) has it's own CMakeList, but I will create one that builds everything.

-------------------------

godan | 2017-03-08 15:35:41 UTC | #17

@Eugene @hdunderscore We now have some [documentation](https://iogram.gitbooks.io/iogram-documentation/content/getting-started-with-iogram.html) and some [tutorials](https://www.youtube.com/watch?v=E4jmdwry8Lk&list=PL_1hCYCSHdNQb6VmRNUkzYx7UW-WFD2i7)! There is more to come, but it would be great to know if this is helpful.

-------------------------

hdunderscore | 2017-03-11 07:32:54 UTC | #18

I have read through some of the getting started documentation, it definitely helps !

I think there are some things that you might be able to look into UI-wise, eg: Highlighting things should give visual feedback, dragging the nodes from the list to the graph should give some visual feedback (easiest thing might be to dim all the windows except for the graph and/or change the mouse icon).

I didn't realise before I read the documentation that you could right click on the node inputs/outputs.

Nice work :D

-------------------------

