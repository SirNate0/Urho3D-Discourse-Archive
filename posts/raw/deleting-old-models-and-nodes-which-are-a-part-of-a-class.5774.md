spenland | 2019-12-18 19:18:11 UTC | #1

I have a class called BasicTree which has a node and a model. I want to be able to put these trees all over the map. I have achieved that but now I want to clear the map and put them all in new positions. 

How do I delete the node and model and (maybe?) the entire class instance so that if the world repopulates many times, these tree instances don't get left and cause a problem later?

New to c++ and new to Urho3d...

Thanks!

-------------------------

Dave82 | 2019-12-18 20:11:32 UTC | #2

[quote="spenland, post:1, topic:5774"]
How do I delete the node and model and (maybe?) the entire class instance so that if the world repopulates many times, these tree instances don’t get left and cause a problem later?
[/quote]

You can simply use 
[code]yourNode->Remove();[/code]
This call will remove the node and all it's children and all components in the hierarchy.
If you want to remove just components from the node but keep the node "alive" , use 

[code]yourNode->RemoveComponent(yourModel);[/code]
Technically if you frequently remove/add nodes and components to the scene it is recommended to add a root node to the scene adn add everything removable stuff there so you can remove everything with just one call. Something like :
[code] 
Node* forestRootNode = scene->CreateChild();
// populate forestRootNode with what ever you want and if you want to remove everything from the scene
//just call
forestRootNode->RemoveAllChildren(true); // the true value indicates to remove all children recursively
[/code]

-------------------------

Modanung | 2019-12-18 22:21:49 UTC | #3

If your trees consist only of `StaticModel`s you may want to consider using a `StaticModelGroup` as demonstrated in sample 20.

-------------------------

