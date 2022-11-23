sabotage3d | 2017-01-02 01:08:18 UTC | #1

Hi what would be the correct way of parenting moving nodes? I am trying to parent the player to another moving node but it doesn't work. It either explodes or some weird scales start to stretch the player. I am doing the test with the character controller from the example [b]18_CharacterDemo[/b] .

-------------------------

cadaver | 2017-01-02 01:08:18 UTC | #2

You should not have scaling in the parent chain at all if you want to do that. (Rather add a separate mesh scaling node if a parent needs to both display a scaled mesh and hold children -- in this case you scale only the mesh node)

The 3D physics should support moving parented objects (apply world transforms in correct parent -> child order) but in general it's not recommended; rigid bodies represent freestanding objects and constraints should rather be used to tie them together.

For something like player riding in a car I'd recommend disabling the rigidbody when parenting to the vehicle, then re-enabling when exiting, to make sure the player's motion doesn't interfere. Particularly if the player collision interpenetrates the vehicle collision, the simulation is quite sure to explode.

-------------------------

sabotage3d | 2017-01-02 01:08:18 UTC | #3

Thanks cadaver. The player needs to still move while on the node for example a platform. In unity the same thing is achieved without exploding the simulation. For example this works like a charm and it is stable with moving rigid body: [url]https://github.com/mzijewel/Unity3D_StayOnMovingPlatform/blob/master/Assets/Scripts/Move.cs[/url]

-------------------------

cadaver | 2017-01-02 01:08:18 UTC | #4

Tested quickly implementing moving platforms to CharacterDemo and using player parenting. You're right that something odd happens; it's possible the parented rigidbody transform applying has been broken, as it's rarely tested.

-------------------------

cadaver | 2017-01-02 01:08:18 UTC | #5

Tested this, and came to the conclusion that there's some deep magic going on with Bullet bodies' interpolation-transform. When a parent object moves, RigidBody::SetPosition() & RigidBody::SetRotation() end up being called, which reset both the actual & the interpolation-transform of the child Bullet body.

It seems that this is bad to do outside of FixedUpdate(), which means, outside the actual physics steps.

When I changed my moving platforms to move inside FixedUpdate(), strange things no longer happened.

I don't want to make changes to the code, because for all other cases the correct thing to do is to set also the interpolation-transform if a rigidbody is moved manually. Otherwise there could be visual jitter.

However, instead of reparenting player when on a platform, I would rather recommend keep tracking of the last platform you're standing on, for example via a raycast, and adding its position changes to the player manually. This way when e.g. should the platform ever be destroyed, the player is not destroyed along with it.

If anyone else comes up with a solid solution to this (of course it would be nice to never have strange physics things happening), a PR would be welcome. But it seems my Bullet understanding is not enough for this.

-------------------------

sabotage3d | 2017-01-02 01:08:19 UTC | #6

Thanks for looking into it. I am trying to update the transform in FixedUpdate but it still not working as exepcted. Please look at my sample code here: [url]https://github.com/sabotage3d/MovingPlatforms/blob/master/Source/Character.cpp#L129[/url]. I am switching between the normal parenting and computing the parent transform myself. They both have issues. Would you mind sharing your sample to check what I am doing wrong?

-------------------------

1vanK | 2017-01-02 01:08:19 UTC | #7

I worked with the physics and concluded, that manually manipulating nodes with RigidBodies is VERY bad idea. Try to moving platforms only with applaing impulses. Also try increase friction when character is stay and decrease, when charakter is moving. Then reparenting is not need.

-------------------------

sabotage3d | 2017-01-02 01:08:19 UTC | #8

Well the same thing works perfectly in Unity and other engines. For hybrid character controllers it is mandatory to have the option to transform the rigid body manually. Look at any Unity game using platforms they all are using parenting.

-------------------------

szamq | 2017-01-02 01:08:19 UTC | #9

I managed to implement moving with platforms in my game.
If you are using rigidbody player be sure to set position not on the node but on the rigidbody. It is different than setting the position of node.

RigidBody@ rb=node.GetComponent("RigidBody");
rb.position=rb.position+posDiff;

-------------------------

sabotage3d | 2017-01-02 01:08:20 UTC | #10

During my tests I can't see any real difference between moving the rigid body and the node. The platform is kinematic but there is still a small disconnection between the rigid body and the node visible in the debug draw it looks like they are out of sync. If I do simple position difference we can parent the character but we cannot move while on the platform: [url]https://github.com/sabotage3d/MovingPlatforms/blob/master/Source/Character.cpp#L129[/url]

-------------------------

