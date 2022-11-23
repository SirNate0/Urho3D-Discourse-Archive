empirer64 | 2017-01-02 01:06:04 UTC | #1

Hi,

is it possible to create multiple collision shapes in a single node and handle collision of each of them differently ? I have a model and I want it to react differently if the player collides with it from the front and from the back.

Thanks

-------------------------

cadaver | 2017-01-02 01:06:04 UTC | #2

You cannot differentiate collision from shapes in the same node. Rigidbody components are actually the "real" components which get added to the Bullet physics world, and they will aggregate the collision shapes from their owner node (for example you can make a simple "chair" from two box CollisionShapes in the same node).

So to differentiate between collision that way, you would also need two child nodes and two rigidbodies. I don't recommend that as it may not make sense simulation-wise.

Rather I recommend to use math to detect where/how the collision occurred after you receive the collision event. If your character is animated, you can for example test against the bone hitboxes, or just check the direction of the impact in relation to the character.

-------------------------

empirer64 | 2017-01-02 01:06:04 UTC | #3

My model is static, so no hitboxes. I will use the collision direction way. 
Thanks for quick reply :slight_smile:

-------------------------

