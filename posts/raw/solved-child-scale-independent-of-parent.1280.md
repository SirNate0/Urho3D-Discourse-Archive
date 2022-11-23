George | 2017-01-02 01:06:34 UTC | #1

Hello, I'm stuck on this one.

Anyone know how do I scale the parent node without affecting the child nodes. 
I want the child node to stay the same regardless of parent node scale.

Thanks for helping,
George

-------------------------

thebluefish | 2017-01-02 01:06:34 UTC | #2

With how the node heirarchy works, this may not be possible.

One solution is to not have the child node as an actual child, but rather another node in the scene. Then use a custom component to mirror the desired transforms.

Another might be to apply an inverse scale through a custom component on the child node. Though with large scales, floating point errors may make this undesirable.

-------------------------

George | 2017-01-02 01:06:34 UTC | #3

Ah! 
I hope there is an efficient way to not loose size precision.
It would be great to have a parameter or some settings so that we can have a control over this.

-------------------------

cadaver | 2017-01-02 01:06:34 UTC | #4

This is not supported by the scene graph.

You should be able to work around it by having an unscaled parent chain for attaching nodes, and a separate child node for displaying e.g. a mesh which need to be scaled. You never parent anything to the scaled child node.

-------------------------

George | 2017-01-02 01:06:34 UTC | #5

That could be the option. 
But would double the nodes.
Also if the parent is not scale. Do I need to compute it's bounding box for selection? Otherwise it would select the first child node.

If my parent is a conveyor, then it can be a problem.

-------------------------

cadaver | 2017-01-02 01:06:34 UTC | #6

I don't think the performance impact would be bad; it's typical for example for Unity to always create one extra node when you import a skinned character.

Note that in Urho there is no concept of a node's bounding box, it's always either a drawable or physics component's property. It's also these components that a raycast will return. Just be aware of the hierarchy you're creating and adjust your logic accordingly, for example when raycast hits an object, knowing you have to go either 1 or 2 parents backward to get the "root" object.

-------------------------

George | 2017-01-02 01:06:34 UTC | #7

Thanks for clarification mate.

I have created 15k conveyors and 10k boxes with the single node method and the performance is wonderful. That was 25ks of objects. Uh! not sure how you guys manage the ram but it is incredible.

Now I will try the method you suggested when I get home tonight to see if I get any performance degeneration.

Thanks for great support,
George

-------------------------

thebluefish | 2017-01-02 01:06:35 UTC | #8

Performance at that scale isn't going to be an issue. Nodes are extremely cheap, it's the components that you need to worry about. So go free and use as many nodes as it takes to get your idea down :slight_smile:

-------------------------

George | 2017-01-02 01:06:36 UTC | #9

Thanks cadaver works well.

Regards
George

-------------------------

