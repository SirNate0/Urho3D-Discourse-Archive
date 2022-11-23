zedraken | 2017-10-29 16:08:20 UTC | #1

Hello all,

I am experimenting various features of Urho3D through the development of a light space simulation game.
I just wanted to post a short video showing a preview.

It is here:
[http://ingels.me/~charles/videos/hud.mp4](http://ingels.me/~charles/videos/hud.mp4)

Another cool video (with soundtrack) : 
[http://ingels.me/~charles/videos/blackswann_final.mp4](http://ingels.me/~charles/videos/blackswann_final.mp4) 

The last feature I added is the HUD which displays various symbols on a transparent plane that is in front of the pilot. I played with 3D geometry and using Urho3D various classes, it was quite touchy but funny.

The space ship (the black one) can be controlled using a joystick (this is really recommended) and it is possible to go through the gates that have flashing lights.

There are many features that I would like to add in that game, and for the moment, I detect collision between the spaceship and the gates. However, I am thinking at a good way to detect if the spaceship goes through the gates (without colliding them). For that, I have thought to add an invisible cube inside each gate and detect collision between those cubes and the spaceship but I do not want any action on the ship trajectory due to the collision (no physical reaction). Any better idea and feedback is welcome.

I hope you enjoy that short video.

Regards !

-------------------------

Modanung | 2017-09-30 14:27:37 UTC | #2

For the gates you could add a trigger node, add a `RigidBody` and `CollisionShape` to it and then call `SetTrigger(true)` and `SetKinematic(true)` on this `RigidBody`.
It will then not be influenced by physics and not collide physically. All it will do is trigger an event and move with its parent. The `CollisionShape` could be any shape.

-------------------------

zedraken | 2017-09-30 14:35:03 UTC | #3

Thanks for the tip, I did not know about the function "SetTrigger". I had a look at the documentation and it seems quite useful for what I am trying to do.

So, if I summarize:
1. I create a new node that is a child on the gate node
2. under that node, I create a rigid body for which I activate kinematic and trigger modes (for detection only)
3. still under that node, I create a collision shape (a cube for example)
4. I handle the collisions

It seems to be clear. 

Thanks !

-------------------------

Modanung | 2017-09-30 14:56:58 UTC | #4

That is assuming these gates will have some physical parts you _do_ want ships to bump into. If they are more like wormholes or starlanes (without hardware) you can leave out the child node.

-------------------------

zedraken | 2017-09-30 15:03:09 UTC | #5

Exactly, the gates have a physical solid part (the border). If the spaceship collides with that part, it bumps and is thrown away in the opposite direction depending on its speed. For that, the collision shape is the gate model itself.
The trigger node is just here to detect if the spaceship goes through the gate and I plan to have a cube shape.
Thanks !

-------------------------

zedraken | 2017-09-30 15:26:36 UTC | #6

I added a trigger node as you suggested, and after configuring the rigid body, the collisions are correctly detected (several collision events are generated).
The screenshot below shows the debug geometries.

![gates_collision|654x499](upload://10Podah6e8BEUyGr8mJ9XbWn6Om.png)

In green is the collision shape for the gate. With that shape, the space ship bumps.
In red is the collision shape for the inside of the gate. It is only used for gate traversal detection with no bump effects on the space ship.
And in white is the bounding box of the space ship that is used as a collision shape.

Now that it seems to work, I have to manage the fact that the space ship crosses the gates in the correct order :grin:

Thanks a lot for your help !

-------------------------

Modanung | 2017-09-30 15:35:06 UTC | #7

[quote="zedraken, post:6, topic:3620"]
Now that it seems to work, I have to manage the fact that the space ship crosses the gates in the correct order
[/quote]

Ah, they're like checkpoints!
This will check whether the ship is going in the right direction:
`shipDirection.ProjectAlongAxis(Vector3 gateDirection) > 0.0f`

You could store the gate sequence in a `Vector<Gate*>` as part of a `RaceTrack` that also keeps track of the currently active gate.

-------------------------

zedraken | 2017-09-30 15:48:12 UTC | #8

Yes, the goal is to fly through the gates in the right order, as fast as possible.
The gates are stored in a Vector<Gates> so it won't very difficult to check what is the current active gate to detect if the pilot is not going through a wrong gate.
I think that I have to check the first collision event to check if the space ship goes in the same direction as the gate direction, maybe by computing the dot product. It should be easy I hope…

-------------------------

zedraken | 2017-09-30 17:27:37 UTC | #9

I connected the E_NODECOLLISIONSTART event to a callback function in which I get pointers on the rigid bodies that are involved in the collision:

> RigidBody \*p1 = static_cast<RigidBody*>(eventData[P_BODY].GetPtr());
> RigidBody \*p2 = static_cast<RigidBody*>(eventData[P_OTHERBODY].GetPtr());

Then, I can get the name of the objects:

> String n1 = p1->GetNode()->GetName();
> String n2 = p2->GetNode()->GetName();

And one of the names contains the gate name. Since I numbered the gates starting from 0 ("Gate0", "Gate1", "Gate2", …), I can get the gate number that is traversed by the spaceship. So I am able to know if the traversal sequence is the correct one.

I also noticed that there are two events generated:
1. first object collides with the second
2. second object collides with the first one

-------------------------

Modanung | 2017-10-01 02:27:52 UTC | #10

If you haven't already, I would suggest creating a custom `Gate` component. You could then call `GetComponent<Gate>()` on the colliding node and compare it with a `Gate*` from Vector<Gate*> to check whether it is the right one.

-------------------------

zedraken | 2017-10-02 18:27:08 UTC | #11

Here is another short video showing movements of the main spaceship in its space environment, with a quiet soundtrack.

[http://ingels.me/~charles/videos/blackswann_final.mp4](http://ingels.me/~charles/videos/blackswann_final.mp4)

-------------------------

zedraken | 2017-10-08 14:47:46 UTC | #12

The game is now fully playable and the time required to cross all gates (19 gates) is now recorded, and displayed at the end. My time is 175 seconds, for the moment.
I added a function that detects that the spaceship enters the gate from the right side, and not from the opposite one. This is simply achieved by computing the dot product between the gate node direction vector with the spaceship node direction vector at the start of the collision.
Another addition is that the next gate to cross is indicated by a big visible green 3D arrow so it becomes easier to find the next gate (it is quite easy to be lost in a 3D environment).
Here are some screenshots:

![SpaceGates001|690x421](upload://krxO7Rhbzp0Qk23xaA3lsPuEjBD.jpg)

![SpaceGates002|612x500](upload://nW0iPmsCp7BdsWYQnTz1xMx2A34.jpg)

There are still some graphics and sound improvements, and if some are interested to try, I can prepare an archive file.

-------------------------

zedraken | 2017-10-29 16:00:59 UTC | #13

Here are some other screenshots taken on the fly…
--
![spacegate_screenshot001|604x500](upload://lEoflDp8kA0VB3JwvhG3nhzvnOD.jpg)
--
![spacegate_screenshot002|605x500](upload://aCQzLGlfRcNO2Aji9iMzk2NgaSK.jpg)
--
![spacegate_screenshot003|603x500](upload://pnSJ4C8Lb0tL4OWwbxzRlke2Yw7.jpg)
--
![spacegate_screenshot004|605x500](upload://t51xEteSnKyDX33E1OAl8xCFxKS.jpg)

-------------------------

