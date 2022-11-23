btschumy | 2020-09-18 20:51:06 UTC | #1

Although I have my galaxy simulation working reasonably well, I was adding some functionality to switch the view to look at it face-on and edge-on.

the face-on works as expected.

		public void OrientToFace()
		{
			cameraNode.Position = new Vector3(0, 0, 160000);
			cameraNode.LookAt(new Vector3(0, 0, 0), Vector3.Up, TransformSpace.Parent);
		}

In the face-on view, the Sun is to the left of the galactic core

However, the edge-on face is flipping something around so the Sun is to the right.

		public void OrientToEdge()
		{
			cameraNode.Position = new Vector3(0, 160000, 0);
			cameraNode.LookAt(new Vector3(0, 0, 0), Vector3.Up, TransformSpace.Parent);
		}

What is strange is if I set the z coordinate of the camera to something like 200 rather than 0 (so I'm not exactly edge-on) then the Sun is on the left as expected.  However setting z to anything between 100 (approx.) and 0 causes the flipped view to be shown.

Note: Vector3.Up is (0, 1, 0)

Anyone have any thoughts on what is going on here?

-------------------------

btschumy | 2020-09-19 03:32:24 UTC | #2

OK, I think I understand why it is flipping, at least I understand why it would flip when past edge-on.  When looking faced on, the y direction is towards the top of the screen.  The y direction will still point to the top as you move the camera towards edge on.  When you get past edge on the y vector will be directed towards the bottom of the screen and so specifying Vector3.UP as up will case the camera to rotate 180 degrees.

So what I really want is for the up direction of the camera to always be the top of the screen.  Surely this is a common case, but I’m not sure how to accomplish this.

-------------------------

Modanung | 2020-09-19 09:25:16 UTC | #3

Doesn't the "top of the screen" depend on the orientation of the camera? I'm not sure I follow your exact problem, but I think understanding transform spaces might solve it.

From Scene/Node.h:
```
/// Look at a target position in the chosen transform space.
/// Note that the up vector is always specified in world space.
/// Return true if successful, or false if resulted in an illegal rotation,
/// in which case the current rotation remains.
bool LookAt(const Vector3& target, const Vector3& up = Vector3::UP,
            TransformSpace space = TS_WORLD);
```

To keep a node's up the same, you could do `node->LookAt(target, node->GetWorldUp());`.

`Node`s also come with a set of functions to convert orientations from one transform space to another:
```
/// Convert a local space position to world space.
Vector3 LocalToWorld(const Vector3& position) const;
/// Convert a local space position or rotation to world space.
Vector3 LocalToWorld(const Vector4& vector) const;
/// Convert a local space position or rotation to world space (for Urho2D).
Vector2 LocalToWorld2D(const Vector2& vector) const;
/// Convert a world space position to local space.
Vector3 WorldToLocal(const Vector3& position) const;
/// Convert a world space position or rotation to local space.
Vector3 WorldToLocal(const Vector4& vector) const;
/// Convert a world space position or rotation to local space (for Urho2D).
Vector2 WorldToLocal2D(const Vector2& vector) const;
```

-------------------------

George1 | 2020-09-22 01:07:32 UTC | #4

Because the forward and right view vector changes,  the up is no longer (0, 1, 0)
Up = ForwardXRight   (L.H. Rule)

You could approximate it by:
Right = (0,1,0)XForward
NewUp = ForwardXRight

But using Modanung solution for simplicity.

-------------------------

btschumy | 2020-09-21 17:23:30 UTC | #5

I've tried various options using the WorldUp of either the camera node or the target node I'm looking at.  Nothing seems to work.

I have made a video from my old SceneKit app showing what I'm trying to do.  As I pan around on the screen, I'm changing the camera's location relative to the galaxy.  At the start I am at (0, 0, 160000).  When edge on, I am at (0, -160000, 0).  After a move of the camera location, I'm doing a 

LookAt(Vector3.Zero, up, TransformSpace.Parent)

to keep looking at the target (in this case, the galactic center).

The question is what to specify for "up" to yield what you see in this video from my SceneKit app.

www.otherwise.com/movies/Rotation_UP.MP4

If I specify Vector3.Up (which is 0, 1, 0), the view flips 180º as I get close to edge on and the Sun appears on the right as opposed to the left.  I don't know why it happens when I get close as opposed to (say) exactly.

It almost seems to work to convert the camera's location to spherical coordinates with phi in [0, π].  Then I change "up" based upon where it is in the range.

			if (phi < Math.PI / 4)
			{
				up = Vector3.Up;
			}
			else if (phi <= Math.PI / 2)
			{
				up = Vector3.Forward;
			}
			else if (phi < 3 * Math.PI / 4)
			{
				up = Vector3.Forward;
			}
			else
			{
				up = Vector3.Down;
			}


However, I've seen some weirdness with this rule as well.

Surely this must be a straightforward thing to do.  How to I accomplish it?

Thanks, Bill

-------------------------

JTippetts1 | 2020-09-21 19:37:05 UTC | #6

Instead of always using the global world Up vector, try using the camera's last up vector. As the camerrotates, eventually the global up vector becomes parallel to the view vector and weirdness happens. But if at each camera movement you use the last camera up vector, you won't have that problem.

-------------------------

btschumy | 2020-09-24 22:15:46 UTC | #7

Just to follow up and to provide some closure, I ended up having to calculate the up vector myself based upon where the camera was and what I was looking at.  It ended up being a moderately involved solution because there were a number of edge cases that had to be handled correctly.

Thanks for all the suggestions, they did help me arrive at the final solutions.

-------------------------

