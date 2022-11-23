stark7 | 2017-10-02 23:10:26 UTC | #1

Hello, 

The use case is within HugeObjectCount example to remove the huge amount of nodes created by adding this as line 154

> 	for (int i = 0; i < boxNodes_.Size(); i++)
	{
		boxNodes_[i]->Remove();
	}

I am observing a significant amount of time to remove those nodes. I also tried disabling the nodes first.

If I create an intermediary parent node to which I add all these nodes, and then remove the parent, then the operation is instantaneous.

Can someone please explain the reason behind this behavior? 

My real use case is a pseudo-destructible environment in which my world elements also consist of a significant number of nodes.

-------------------------

Eugene | 2017-10-02 17:13:31 UTC | #2

[quote="stark7, post:1, topic:3626"]
Can someone please explain the reason behind this behavior?
[/quote]
Every `Remove` call performs linear search over all siblings and then performs linear element removing from vector, so you have O(n^2) complexity when removing nodes one-by-one.

-------------------------

Victor | 2017-10-02 16:12:58 UTC | #3

In general, my understanding has always been that new/delete operations can be slow overall, so avoiding them is always best. I'm not quite sure why Remove is slower, however, my guess is that it has to do a lot more checks to remove a child (who owns the child, traverse any children it may have, etc), than it does for when it's adding the child. That doesn't mean there isn't room for improvement, just that it (possibly) has more checks along the way.

**Possible Solution**
Lumak has a Foliage example which handles updating a lot of foliage nodes at once. One particular issue he addresses is how to quickly update all of them without slowing down the process. If I remember correctly, the solution was to update a set number of nodes each 'Update' frame until you've updated them all, and then repeat the process. 

With that in mind, one solution you can do is to set the Visibility of all nodes you want to delete to "false" while sending them to a "Delete Queue". On each 'PostUpdate', delete a set number inside the queue to prevent the heavy delete operation from slowing down your app. Or, if you can (and if it makes sense in your application), create a 'pool' so you can reuse the nodes later.

-------------------------

ext1 | 2017-10-02 16:27:49 UTC | #4

I have very little experience with Urho3D, but maybe the performance is also being affect due to also having to send change events: [Remove()](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/Node.cpp#L1111) >> [RemoveChild()](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/Node.cpp#L2100)?

-------------------------

stark7 | 2017-10-02 17:21:25 UTC | #5

Thank you @Victor and @ext1 - I think you both have valid points, and all of that is compounded by what @Eugene is saying about the O(n*n) complexity which explains my observations.

If i were to choose between fast create and fast destroy, I would always want fast create/recreate.

I think I will be making extensive use of nodes with the StaticModelGroup component moving forward so my problem is not really a problem anymore.

-------------------------

