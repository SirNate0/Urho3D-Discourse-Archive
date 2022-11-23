nergal | 2018-07-09 12:35:23 UTC | #1

I read through the documentation and checked the demo 45_InverseKinematics. And I wonder; If I procedurally generate, say a 2D pixel-art character, can I animate this char (if legs/arms/hands/head are separated meshes) using inverse kinematics?

Or is inverse kinematics just to handle small changes to already animated objects (such as the demo shows)?

-------------------------

TheComet | 2018-07-09 13:56:31 UTC | #2

It depends on the algorithm and how many bones you have.

If your character only has 2 bones per chain, then it is very possible, because 2-bone IK can give you a unique solution if you specify the plane of rotation. This is especially easy in 2D where you can only get 2 solutions at most. You'll just have to choose whether you want the one that bends your knee "left" or "right".

If you want to animate with more than 2 bones, things aren't as easy. The current algorithm used in Urho3D (FABRIK) is not suitable for IK driven animation because it's not based on any physical model and will produce unnatural looking results if the solved tree is far away from the initial tree. It's very fast though and it is suitable for small adjustments.

I am actively working on a new algorithm JSandusky made me aware of which uses masses and springs to find a solution. This algorithm would be suitable for 3-or-more-bone IK driven animation, because it is aware of the distribution of mass within the character, i.e. each joint specifies a "weight" parameter such that the "heavier" joints move slower while the "lighter" joints move faster. It can produce some very natural looking results if you tune the weight parameters correctly.

I have made a little bit of progress but nothing that really works yet. My attention has been more on getting constraints to work. If you want you can help out with implementing MSS for my lib [here](https://github.com/TheComet/ik), or, you can implement it for yourself. Here's the relevant paper: [An Efficient Energy Transfer Inverse Kinematics
Solution](https://pdfs.semanticscholar.org/aac6/cbd168f0e01911edbe564f59d7c1a00b7535.pdf)

But to re-iterate: For 2 bones, there exists a unique solution and you don't need anything fancy beyond a little bit of trigonometry.

-------------------------

