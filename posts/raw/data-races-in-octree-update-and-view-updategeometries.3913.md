LuoZHipeng | 2018-01-05 09:54:22 UTC | #1

Hello, I am using Urho3D recently on a little project.
I encountered some data races problems in the below situations:

1. When different drawables from the same node are putted into different WorkItem that  working in different threads.

2. This is kind of rare, when different drawables from different nodes but those nodes have relationships are putted into different WorkItems that working in different threads .

UpdateDrawableGeometriesWork from these different threads may access the same node, sometimes one thread is calling MarkDirty() of that node but another thread is calling UpdateWorldTransform(). When this happens, the precondition in Node::MarkDirty() is broken(MarkDirty() can't mark all children dirty).
Here is a sample picture showing what this problem causes.
![Untitled|690x388](upload://rbGJgpI0dafVGtQbBf7hqZe2qi7.jpg)
I tried to fix this by arrange the workitems , making all drawables from same node always added to the same workitem. This fixed the first situation but not works in situation 2.
I don't really want to have a lock or disable the multithread calculation.
I really need some suggestions.!
Thank you.

-------------------------

ab4daa | 2018-01-05 10:59:28 UTC | #2

Hi, did you read [this](https://urho3d.github.io/documentation/1.7/_multithreading.html)?

> When making your own work functions or threads, observe that the following things are unsafe and will result in undefined behavior and crashes, if done outside the main thread:
    Modifying scene or UI content
    Modifying GPU resources
    Executing script functions
    Pointing SharedPtr's or WeakPtr's to the same RefCounted object from multiple threads simultaneously

For my understanding, one should not modify node/drawable in multi-threading.

-------------------------

LuoZHipeng | 2018-01-06 17:45:34 UTC | #3

I didn't make my own work functions.
My main post was not clear, I meant the 2 funcitons below:
1. void Octree::Update(const FrameInfo& frame)
2. void View::UpdateGeometries()

The multithreaded works in these functions could have data races when same they eventually call same nodes' MarkDirty() and UpdateWorldTransform() function.

-------------------------

Eugene | 2018-01-06 19:32:32 UTC | #4

[quote="LuoZHipeng, post:3, topic:3913"]
The multithreaded works in these functions could have data races when same they eventually call same nodes’ MarkDirty() and UpdateWorldTransform() function.
[/quote]

What `Drawable`s are you talking about?
There is single node, and there are different `Drawable` components with non-trivial `UpdateGeometry` that belong to this node, am I right?
Please provide actual Node layout: what the node is and what components does it contain.

-------------------------

LuoZHipeng | 2018-01-07 12:10:41 UTC | #5

I got some nodes with multiple AnimatedModels like:
node id="2"
	...
	omponent type="AnimatedModel" id="16777216"
            ...
        /component
        component type="AnimatedModel" id="16777216"
            ...
        /component
        ...
/node

-------------------------

Eugene | 2018-01-07 13:20:19 UTC | #6

Haaa, I see..
Maybe the node of the Drawable shall always be un-dirty-ed if it has update job in worker thread.

It’s time to summon some experts...
@cadaver ?

-------------------------

cadaver | 2018-01-08 09:06:39 UTC | #7

I remember the original intention was that MarkDirty / UpdateWorldTransform would be safe even from multiple threads simultaneously, and no dirtyings would be missed. However I believe the update by clb in 2015 has changed that. You could check the version of MarkDirty from before that (hash 7db65a8). It will however perform potentially worse, e.g. for animations.

Manually undirtying before could be another solution.

Actually inserting locks there to add proper safety would likely degrade performance further.

-------------------------

LuoZHipeng | 2018-01-09 07:47:19 UTC | #8

Thank you for your advice, i'll have a look at it.
Any chance we have a fix in the engine?

-------------------------

Eugene | 2018-01-09 12:00:57 UTC | #9

[quote="cadaver, post:7, topic:3913"]
I remember the original intention was that MarkDirty / UpdateWorldTransform would be safe even from multiple threads simultaneously, and no dirtyings would be missed
[/quote]

It doesn't sound like healthy approach.. There is no guarantee that read/write ops are ordered in the intuitive way unless atomics are used. For example, dirty flag may be removed before updating transforms.

There is one suspicious thing... What nodes are you talking about, @LuoZHipeng ?

As I can see, the only threaded code of `AnimatedModel` is `AnimatedModel::UpdateSkinning`. It couldn't call `MarkDirty` in any way because it only grabs transforms from nodes.
How could you get dirtying and undirtying simultaneously?

[quote="LuoZHipeng, post:1, topic:3913"]
sometimes one thread is calling MarkDirty() of that node but another thread is calling UpdateWorldTransform().
[/quote]
In other words, I'm interested in `MarkDirty()` callstack. Any ideas?

My only idea is that some main-threaded `UpdateGeometry` is touching same nodes.. Doesn't sound believable at first glance.

-------------------------

cadaver | 2018-01-09 12:14:05 UTC | #10

Before the update geometry phase (which can be threaded where applicable), there is the animation update itself (kicked off by Octree as the UpdateDrawables profiling block) which *can* move around scene nodes threaded. Though this and the geometry update should be strictly separated, ie. the animation update always finishes first.

-------------------------

Eugene | 2018-01-09 15:58:46 UTC | #11

[quote="cadaver, post:10, topic:3913"]
which can move around scene nodes threaded
[/quote]

Aahh, I missed that `AnimatedModel::ApplyAnimation` is threaded too.

`ApplyAnimation` is dirtying the node. `UpdateBoneBoundingBox` is un-dirty-ing the same node. So, `ApplyAnimation` for two `AnimatedModel`s for single `Node` will likely cause the descibed problem.

Probably `MarkDirty` shall be called only for node's children and `Node` shall be undirtyed for each `Drawable`. It shan't be performance issue because all drawables need world transforms for rendering anyway.

However, it will work only if drawables aren't moved during drawable updates. BUT they are, damn. Drawable could be attached to the bone of `AnimatedModel`

-------------------------

Eugene | 2018-01-19 10:39:36 UTC | #12

Just to make things clear:

I confirm the problem with races. I'm looking for good solution, but it's not so easy.

-------------------------

LuoZHipeng | 2018-01-22 01:15:12 UTC | #13

Thank you. I tried to solve it myself but no luck.

-------------------------

Eugene | 2018-01-22 06:48:25 UTC | #14

You could temporarily disable threading or try to split your node into two until I figure out some good fix.

-------------------------

