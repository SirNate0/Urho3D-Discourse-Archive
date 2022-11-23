Taymindis | 2017-11-30 09:03:06 UTC | #1

Hi, 

I'm having difficulty to understand the logic kinematics and static rigid body2d, did anyone have any simple explanation ?

-------------------------

Eugene | 2017-11-30 08:20:27 UTC | #2

Static rigid body isn't allowed to move, Kinematic body is.

-------------------------

Taymindis | 2017-11-30 15:16:33 UTC | #3

Hi Eugene, 

Normally I use static RigidBody by using setPosition for moving in PhysicalWorld, How do I use Kenematic body to move?

Do you have some snippet code of it? or you have any Video guide about this ?

-------------------------

Eugene | 2017-11-30 15:37:57 UTC | #4

[quote="Taymindis, post:3, topic:3802"]
or you have any Video guide about this ?
[/quote]

Well, I doubt there is a lot of video guides for Urho... :frowning:

[quote="Taymindis, post:3, topic:3802"]
Normally I use static RigidBody by using setPosition for moving in PhysicalWorld, How do I use Kenematic body to move?
[/quote]
Kinematic body is moved the same way.
The difference is that kinematic body _is allowed_ to be moved at all. It is guaranteed that such body would properly interact with _dynamic_ environment.
The static rigid body is not allowed to be moved and behavior is not defined. AFAIK, it's ok to _reposition_ (aka teleport) static stuff.

-------------------------

