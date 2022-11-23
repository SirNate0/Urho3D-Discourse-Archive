vivienneanthony | 2017-01-02 00:59:10 UTC | #1

Hello

1. Is this a normal scene? I mean the nodes.    I think starting at 16mil + node number is odd.

[img]http://averyanthony.com/priv/normalscene.jpg[/img]

2. Once you put two static models in a node how do you move each one individually?

Vivienne Anthony

-------------------------

friesencr | 2017-01-02 00:59:10 UTC | #2

This is by design.  If you read the bit of documentation on scene replication you will see that urho reserves the first block of ids for 'replicated' nodes and the latter block is for local nodes.

[urho3d.github.io/documentation/a00036.html](http://urho3d.github.io/documentation/a00036.html)

-------------------------

weitjong | 2017-01-02 00:59:11 UTC | #3

The confusion to newcomer is understandable. The starting number (16777216) may seem very odd in decimal, but the segregation is clear when the number is represented in hexadecimal 1000000.

For your second question. If you need to manipulate individual static model component then I think you are better off with having two nodes instead of just one. With each node having its own component, you can then freely transform the node without worrying about the other node. You can also put the two nodes in one parent node, if you want to. So, moving the parent node will move both the child nodes (and their components) in tandem.

-------------------------

cadaver | 2017-01-02 00:59:11 UTC | #4

Yes, exactly like that. The only situation in which you actually need to put multiple model components in the same Node is when you have full-body clothing attachments (AnimatedModels) for a character (also AnimatedModel) and want them to be skinned/animated with the same bones as the character itself.

-------------------------

vivienneanthony | 2017-01-02 00:59:11 UTC | #5

[quote="weitjong"]The confusion to newcomer is understandable. The starting number (16777216) may seem very odd in decimal, but the segregation is clear when the number is represented in hexadecimal 1000000.

For your second question. If you need to manipulate individual static model component then I think you are better off with having two nodes instead of just one. With each node having its own component, you can then freely transform the node without worrying about the other node. You can also put the two nodes in one parent node, if you want to. So, moving the parent node will move both the child nodes (and their components) in tandem.[/quote]

Thanks. I went with this method. It's a lot easier. The task is still tedious which is my strong point.

In Blender, you can  take a group of mesh and simply place SHIFT-D and move a copy. which might be useful in this case. So, objects can be moved while moving across the same hierarchy level.

-------------------------

vivienneanthony | 2017-01-02 00:59:11 UTC | #6

[quote="cadaver"]Yes, exactly like that. The only situation in which you actually need to put multiple model components in the same Node is when you have full-body clothing attachments (AnimatedModels) for a character (also AnimatedModel) and want them to be skinned/animated with the same bones as the character itself.[/quote]

Agreed

-------------------------

