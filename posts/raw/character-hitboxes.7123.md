GodMan | 2022-01-10 19:34:24 UTC | #1

Is it possible to use more accurate physics shapes for characters? Currently I'm just using a capsule shape, but this obviously does not work very well. 

Example:
https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9egmZDglKf2HVQbAYQc4jSh_kEzVWsl9IFw&usqp=CAU

-------------------------

SirNate0 | 2022-01-10 20:02:09 UTC | #2

Yes. Without knowing what you want to achieve it's hard to provide more detailed suggestions, but I can explain what I do.

The physics in terms of character control are kept very simple (capsule or sure l sphere combined with a sphere cast and some custom logic to keep the sphere off the ground except when crouching). Hitboxes to check damage are all set as kinematic (maybe triggers) and are attached to the bone nodes.

-------------------------

GodMan | 2022-01-10 20:41:17 UTC | #3

Okay so is it possible to have lets say smaller box shapes for each bone, for better collision results?

-------------------------

Eugene | 2022-01-10 21:55:47 UTC | #4

[quote="GodMan, post:3, topic:7123"]
for better collision results
[/quote]
You have to manage object masks.
I mean, you still have to use capsule for the character movement itself.
If you want to add more details, you have to do in in "second layer" which doesn't interact with capsule and with important world objects, but interacts with bullets and non-important debris.

-------------------------

GodMan | 2022-01-10 21:59:21 UTC | #5

So I still need an overall capsule shape around the character, but can I use lets say small capsule shapes for each bone just for projectile physics.

-------------------------

Modanung | 2022-01-10 23:07:39 UTC | #6

[quote="GodMan, post:5, topic:7123"]
So I still need an overall capsule shape around the character [...]
[/quote]

Unless you're making a learning-to-walk simulator, yes.

-------------------------

GodMan | 2022-01-11 05:03:58 UTC | #7

Are their any post on the forums of anyone trying this idea? I thought I saw someone trying this in the past.

-------------------------

Modanung | 2022-01-11 13:51:16 UTC | #8

You mean something like [this](https://invidious.kavin.rocks/embed/pgaEE27nsQw), right?

I think I've only seen a question or two on the subject over the years; nothing functional or conclusive.

-------------------------

Modanung | 2022-01-11 15:23:57 UTC | #9

...but if you're going down that path, I think a pogo stick would be a good starting point. It's the most basic balanced locomotion I can think of.

-------------------------

GodMan | 2022-01-11 20:10:42 UTC | #10

So I am just looking for a way my characters to have different regions for projectile hits. So for example if I shoot the character in the head play a different death animation. I can't do this if the character physics is just one big capsule. I don't need anything fancy. Just some simple primitives to help distinguish different regions that are hit.

-------------------------

Modanung | 2022-01-11 20:23:05 UTC | #11

Ah, but _then_ you could just make a ghost doll and ray it. *Or* - if you want it to be (or don't mind it being) "pixel-perfect" - use the `Octree` instead of `PhysicsWorld`.
The specifics depend on what you're looking for, but it's perfectly doable.

-------------------------

GodMan | 2022-01-11 22:12:32 UTC | #12

Are their any Urho3d examples on this anywhere? Like I said in the past. I'm trash with the physics part of the API.

-------------------------

Modanung | 2022-01-11 23:03:13 UTC | #13

You could approximately do what the ragdoll sample does, but with a single `RigidBody`, no `Constraint`s, and creating the components along with the character instead of when it faints... and also set the `RigidBody` to being - I believe - both a _trigger_ and _kinematic_. To filter the results beforehand you could assign the bodies a layer and provide the correct mask with the raycast.

But there may be some hurdles I'm not anticipating that might introduce transform syncing.

-------------------------

GodMan | 2022-01-11 23:16:49 UTC | #14

okay. I will look into the ragdoll sample. 

Thanks

-------------------------

Dave82 | 2022-01-12 08:36:15 UTC | #15

For long run physics isn't the best solution unless you're satisfied with a very basic bullet-body collision detection system. If you want blood decals on your enemies on the exact same position as the bullet intersects the mesh itself and keep that decal moving with a skinned mesh or have a blood splash effect at the exact position you have to use the ray-triangle check using the scene's octree and forget about the physics system.

-------------------------

Eugene | 2022-01-12 09:10:50 UTC | #16

[quote="Dave82, post:15, topic:7123"]
and forget about the physics system.
[/quote]
From *gameplay* point of view, raycasts against actual visible triangles are worthless.

* You cannot easily assign damage multipliers to different regions.
* You cannot add padding to balance how hard or how easy it is to hit target, which is especially important for any multiplayer game with more than one avatar model.
* You cannot adjust which parts of the model are important and which parts should be ignored. You don't want to get hits from shooting cloth or hair.
* It's harder to do lag compensation just from tracked data without actually messing with live Urho components.

Basically, you want to cast agains visible geometry for pure visual effects, and you want to cast against some explicit shape (hitboxes) for anything that matters.

-------------------------

Dave82 | 2022-01-12 10:40:52 UTC | #17

Well theoretically (according to documentation) when raycasting an animated model the raycast info contains the closest bone you've hit. So you have a very detailed info of which part of the body was hit. Head shot , shoulder etc. I think you can even set extra bones for more detailed hit detection (top of the head , jaw , eye etc)

-------------------------

Eugene | 2022-01-12 11:07:50 UTC | #18

Even if you get the most important bone from hit triangle, it may be not really whay you need.

You cannot in good faith add redundant bones just for sake of game logic calculations, because it may be a bottleneck for rendering. You already have only about 32..64 bones on mobiles, it's a precious resource.

Moreover, bones don't always match that well with hit model.
It may be okay to distinguish limb from body from head.
But if you want to add specific vulnerable or armored points, like a crack in the body armor... eh.

-------------------------

SirNate0 | 2022-01-12 13:25:12 UTC | #19

[quote="Modanung, post:13, topic:7123"]
both a *trigger* and *kinematic* .
[/quote]

Not 100% sure, but I think I had issues with both of those being set. I think it was impossible to detect trigger-trigger collisions. But I did just wake up, and was working on that several years ago, so I may be completely off. I think with appropriate collision layers and masks you can do it with everything being kinematic only. But again, I may remember that wrong, and it may not matter for you (if the weapon is not a trigger, it wouldn't be a trigger-trigger collision).

-------------------------

Modanung | 2022-01-12 14:22:55 UTC | #20

https://github.com/Lumak/Urho3D-KinematicCharacterController

> added PhysicsWorld to generate collision callback events when two triggers collide. Used when kinematic rigidbody enters moving kinematic volume.

Indeed it depends on the type of check that comes with the projectile whether you'd need this. But since we're talking ghost objects, couldn't the voluminous projectiles simply cast hulls instead of rays, as a bullet would? The implementation would differ less between projectiles and therefor be easier to generalize. It would also take less `Component`s.

-------------------------

Modanung | 2022-01-12 15:25:37 UTC | #21

[quote="Eugene, post:16, topic:7123"]
You cannot adjust which parts of the model are important and which parts should be ignored. You don’t want to get hits from shooting cloth or hair.
[/quote]

They could be separate models. Or you could even have an invisible hit model with skeletal animation for flesh and use the visual parts of any armour covering it. Checking damage to armour and health lost separately with a single cast, ignoring the wavy coat.
I can imagine someone making a sniper game to not settle for blocky targets, or even calculate abrasion versus critical hits, based on the hit normal.

-------------------------

GodMan | 2022-01-12 20:13:59 UTC | #22

Well this thread exploded. On the decals part. I would eventually like the NPC to have blood decals onto the ground or environment, but not on themselves. 

Now I'm not sure which method to go with. Did not expect so many replies.

Thanks everyone.

-------------------------

Dave82 | 2022-01-12 21:38:03 UTC | #23

I like decals on enemies. It gives such extra realism that it just worth it. Bullets can also create bloodstains on walls and even on other enemies if they are close enough to the enemy that was hit. It looks really cool. Also bullets have extra properties in my game. Like on how many enemies can pass through before they  stop. It gives the oportunity of upgradable ammo for the same weapon

Just adding extra ideas that maybe you can use in your game 😁

-------------------------

GodMan | 2022-01-12 22:44:20 UTC | #24

I agree with all that, but my game is something I can't really release to the public. So no need for all the bells and whistles. Just some of them.

-------------------------

