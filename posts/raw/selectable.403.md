friesencr | 2017-01-02 01:00:11 UTC | #1

I was thinking about adding a 32 bit uint Selection Mask attribute to node.  It would be kind of like unity tags.  A legend could be associated to each bit to give it stringiness.  We could suggest the first half dozen bits like unity:

?Respawn?
?Finish?
?EditorOnly?
?MainCamera?
?Player?
?GameController?

This would allow a more generic component for script components to target nodes.  Node#FindBySelectionMask would be appropriate as well.

I have been thinking about adding a much more robust node selector/filterer to the editor and this would be a natural fit.

Any thoughts?

Thanks,
Chris

-------------------------

cadaver | 2017-01-02 01:00:11 UTC | #2

I believe this is mostly a good idea, my concern is that when you're finding nodes and not Drawables / RigidBodies, you have no acceleration structure to help you. Therefore it's going to be a brute-force search through the node graph. This is fine as long as users are reminded that it's a slow operation, just like finding a node by name.

-------------------------

friesencr | 2017-01-02 01:00:12 UTC | #3

It could be a StringHash instead and an index could be made.  Is it worth the memory trade?

-------------------------

cadaver | 2017-01-02 01:00:12 UTC | #4

In any case it will need a string list in the scene root node to serialize the tags, so it's quite the same to me if it's a bitmask or something else. In any case we're likely looking at an extra 32 bits in each scene node. Mainly the question is whether you want the scene node to have multiple tags or not. If multiple, then a bitmask is most appropriate.

-------------------------

szamq | 2017-01-02 01:00:12 UTC | #5

Right now I'm just using Variants inside the node for that. Just boolean variable set to true, and then you can check if the object has certain tag just by:
if(otherNode.vars["ladder"]==true)

-------------------------

friesencr | 2017-01-02 01:00:12 UTC | #6

[quote="szamq"]Right now I'm just using Variants inside the node for that. Just boolean variable set to true, and then you can check if the object has certain tag just by:
if(otherNode.vars["ladder"]==true)[/quote]

That is what I am doing too.  I was simpling thinking that a reserved worthless integer could have shared existiential meaning for the sake of sharing code :slight_smile:

-------------------------

vivienneanthony | 2017-01-02 01:00:13 UTC | #7

[quote="friesencr"]I was thinking about adding a 32 bit uint Selection Mask attribute to node.  It would be kind of like unity tags.  A legend could be associated to each bit to give it stringiness.  We could suggest the first half dozen bits like unity:

?Respawn?
?Finish?
?EditorOnly?
?MainCamera?
?Player?
?GameController?

This would allow a more generic component for script components to target nodes.  Node#FindBySelectionMask would be appropriate as well.

I have been thinking about adding a much more robust node selector/filterer to the editor and this would be a natural fit.

Any thoughts?

Thanks,
Chris[/quote]

Good idea.

-------------------------

thebluefish | 2017-01-02 01:00:14 UTC | #8

I'd personally prefer to keep the Node as a generic template.

Unless I'm missing something, this is no different than having a bunch of sub-components. Except with the case of components, you still have the ability to maintain component-specific attributes and logic. I'll have a "SpawnPoint" component with attributes such as type, weighting, team, etc... or a Player that handles inventory and player logic.

What benefit do we gain by adding "tags" to a component? We can specify "this node should be a Player", but we cannot act on the Node until we find its Player component. At that point we might as well have called Node#GetChildrenWithComponent (Alternatively we could keep the logic and associated information outside of the Node, but that would break the entire point of the component system).

-------------------------

