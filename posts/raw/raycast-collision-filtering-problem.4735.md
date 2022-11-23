Yatsomi | 2018-12-12 07:54:08 UTC | #1

Hi to all, im using [RayCastSingle()](https://urho3d.github.io/documentation/1.7/class_urho3_d_1_1_physics_world2_d.html#a941235284b5d5ef127a24e0b4abebbdc) in PhysicsWorld2D.cpp, but i have problem with collision filtering, here is my code:

define categories:
>enum GAMELAYERS : const unsigned {
		None = 0,
		Character = 0x0002	,
		Platforms = 0x0004,
	};
>
set character category bits:
>boxCollider_ = GetNode()->CreateComponent<CollisionBox2D>();
boxCollider_->SetCategoryBits(GAMELAYERS::Character);
rigidbody_ = GetNode()->CreateComponent<RigidBody2D>();
>
and raycast:
>physicsWorld_->RaycastSingle(results, startPos, endPos, GAMELAYERS::Platforms);
>
i send platform bits as raycast collisionmask, but it still hit my character. i dont get it.
box2D collision filtering use this method:
>uint16 catA = fixtureA.filter.categoryBits;
uint16 maskA = fixtureA.filter.maskBits;
uint16 catB = fixtureB.filter.categoryBits;
uint16 maskB = fixtureB.filter.maskBits;
if ((catA & maskB) != 0 && (catB & maskA) != 0)
{
// fixtures can collide
}
>

0x0002 & 0x0004 == 0
so whats the problem?
am i misunderstood how Category/Mask collision filtering works?

-------------------------

Sinoid | 2018-12-12 19:40:39 UTC | #2

It's a bug.

`CollisionShape2D::CreateFixture()` needs to set the filter data on the fixture, it currently doesn't. So you can only set those category/mask bits if you follow the sequence of `Create Rigidbody -> Create shape -> setup shapes size and physical traits -> set category/mask bits`

-------------------------

Yatsomi | 2018-12-13 07:13:07 UTC | #3

Hi Siniod, i submit an issue on git, lets see what they say about it.

-------------------------

Sinoid | 2018-12-13 17:06:39 UTC | #4

Well I'm probably wrong. I don't use Urho2D - that's just the suspect stuff I see. I wouldn't be surprised if deep down it's a Box2D problem.

-------------------------

