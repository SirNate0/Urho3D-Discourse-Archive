receme | 2017-01-02 01:10:29 UTC | #1

Hello, 

I am working on a xamarin project I have to implement a wall collision effect. I am using urhosharp 3d. Problem is my wall is not working as a completely solid object. 
It is working like a elastic wall. When I try to move the object using mouse move, some portion of the object is going through the wall and then bouce back. And also if I move the mouse very quickly, the object completely goes through the wall.

How can I make it completely solid.. so that any portion of the object cannot go through the wall.

-------------------------

receme | 2017-01-02 01:10:29 UTC | #2

This is what it like for now....

[youtube.com/watch?v=S9z6YycPNVk](https://www.youtube.com/watch?v=S9z6YycPNVk)

-------------------------

weitjong | 2017-01-02 01:10:29 UTC | #3

Have you tried to turn on the bullet's CCD? See [urho3d.github.io/documentation/H ... s_Movement](http://urho3d.github.io/documentation/HEAD/_physics.html#Physics_Movement).

-------------------------

Bananaft | 2017-01-02 01:10:29 UTC | #4

Hi, how exactley you are moving your object? What engine function you use for it? Try using RigidBody.ApplyForce(Vector3) or RigidBody.SetLinearVelocity(Vector3).

-------------------------

godan | 2017-01-02 01:10:29 UTC | #5

Are you setting the objects position using a velocity? I can't quite remember how this works in Bullet, but it's usually something like SetKinematicPos or SetKinematicTarget. If you set the object's position directly (i.e. by specifying the objects world transform from mouse position), there is nothing preventing it from being positioned inside the wall. The physics engine will then apply a kick back force to resolve the interpenetration, resulting in the jitter.

Note: this also assume that you have set up the object as a kinematic object in the first place. Using a kinematic object is generally the recommended approach for accurately setting an objects transform in the physics engine. If you really want to use a dynamic object, you'll have to set up some kind of "dragger" function or use a spring constraint.

-------------------------

gawag | 2017-01-02 01:10:30 UTC | #6

To fix fast objects glitching through colliders this may help you: [github.com/urho3d/Urho3D/wiki/H ... h%20things](https://github.com/urho3d/Urho3D/wiki/How%20to%20fix%20a%20fast%20object%20not%20colliding%20with%20things)?

-------------------------

receme | 2017-01-02 01:10:30 UTC | #7

Hi, I used Translate function to move the object. here is my code...

[code]      public void Move3dModel (float angle)
		{
			var input = Application.Current.Input;

			TouchState state = input.GetTouch (0);

			if (state.TouchedElement != null)
				return;

			var dir = state.Position - state.LastPosition;
                        
          //calculate vector if camera angle is changed
			var newDir = Quaternion.FromAxisAngle (Vector3.UnitY, angle) * new Vector3 (dir.X, 0, -dir.Y);		
					
			//UtilMethods.PrintLog ("angle: " + angle);

			modelNode.Translate (newDir * 0.1f, TransformSpace.World);		

		}[/code]


Thank you for your reply. I will try now what you have given.

-------------------------

gawag | 2017-01-02 01:10:32 UTC | #8

Yes using translate should cause the issue as it is "teleporting" the object and not moving it physically.

You can check out my sample game which uses a physical capsule as the player: [github.com/damu/Urho-Sample-Pla ... player.cpp](https://github.com/damu/Urho-Sample-Platformer/blob/master/player.cpp)
It's using ApplyImpulse, which is the proper way, and also SetLinearVelocity which I'm using to limit the speed. Also the player model is independent from the physical capsule, I did that to rotate the player model independent of how the capsule is being rotated through friction and stuff (there may be a better way to do that?).
(The code is a bit messy, was my first time doing that. I'm planning on overhauling the whole project.)

-------------------------

receme | 2017-01-02 01:10:49 UTC | #9

Thank you all for reply. I have solved the issue by calling "applyForce" method to rigidbody instead of translate.

-------------------------

