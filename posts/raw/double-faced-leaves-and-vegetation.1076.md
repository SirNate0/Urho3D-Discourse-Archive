DanteZ | 2017-01-02 01:05:16 UTC | #1

Ok, apologies if this question is already asked somewhere in this forum. Though I did not found it.
The very basic question - leaves of trees. Needs to be rendered from both sides. I understand, that face normally has one visible side. Some techniques propose to apply two sided in real time. But some say it is expensive. 
The second option is duplicate and revert the faces in Blender. Which is suggested to be cheaper in realtime, but a little overhead on modelling time.

What can you suggest (few words) to get proper two sided rendered leaves and vegetation in Urho? :slight_smile:

-------------------------

weitjong | 2017-01-02 01:05:16 UTC | #2

Have you tried to use "none" cull value in the material setting?

-------------------------

Bananaft | 2017-01-02 01:05:17 UTC | #3

Duplicating all faces can't be cheaper than switching off culling. It's that some engines don't allow you to mess with culling, making it the only option. Luckily, Urho does.

-------------------------

