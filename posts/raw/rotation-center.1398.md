exessuz | 2017-01-02 01:07:29 UTC | #1

I have been playing around with Urho3D for quite sometime now and I think its just amazing, I would like to thanks the team, the engine is just awesome.

I would like to know if there is a way to change an object's rotation pivot. In 3d max I didnt center the object, but i want in Urho to be able to rotate on the object's center. I tried in 3d max to change the pivot and it works in the program but after exporting, the pivot resets to the center. I tried in Urho with SetGeometry Center but that didnt seems to work, also tried to translate the object back to origin, rotate and the translate it back to the position.

-------------------------

TikariSakari | 2017-01-02 01:07:29 UTC | #2

You can add a node to your object, and put offset to the node. Then you can rotate the node, which would work as a new "center"  point.

-------------------------

exessuz | 2017-01-02 01:07:29 UTC | #3

[quote="TikariSakari"]You can add a node to your object, and put offset to the node. Then you can rotate the node, which would work as a new "center"  point.[/quote]

Thx thats a good idea, but if i have many objects which are going to be childs of empty nodes, wouldnt that be a burden? or affect performance if I have many objects?

-------------------------

codingmonkey | 2017-01-02 01:07:29 UTC | #4

Your's models may do this offset by it vertexes position in geometry.
In blender you just reset pos transformation (bring model to world's origin), then enter to edit mode and do this offset as you wish. 
Then you just export this model with offset and use in engine. this is most cheapest way I guess )

-------------------------

thebluefish | 2017-01-02 01:07:29 UTC | #5

[quote="exessuz"]Thx thats a good idea, but if i have many objects which are going to be childs of empty nodes, wouldnt that be a burden? or affect performance if I have many objects?[/quote]

Not really. Nodes are very cheap, and primarily just store the transform which is what you would be doing in any other solution without baking the center into your assets.

-------------------------

exessuz | 2017-01-02 01:07:30 UTC | #6

[quote="thebluefish"]

Not really. Nodes are very cheap, and primarily just store the transform which is what you would be doing in any other solution without baking the center into your assets.[/quote]

codingmonkey: but then I will not be able to change it at runtime or at the end I will have to use the empty node, which now that i know nodes are not a burden (thanks bluesfish) i will use them, is a better solution for what  i am trying to accomplish.

Thank you.

-------------------------

