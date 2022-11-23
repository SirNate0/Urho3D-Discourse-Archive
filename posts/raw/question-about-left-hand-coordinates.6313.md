btschumy | 2020-08-11 14:23:06 UTC | #1

This is probably a newbie misunderstanding, but I have a question about the default Urho3D coordinates.  In the Conventions section of the documentation it says:

* Left-handed coordinates. Positive X, Y & Z axes point to the right, up, and forward, and positive rotation is clockwise.

However, when using the UrhoSharp implementation I see positive X pointing to the left.  Positive Y & Z do indeed point up and forward.  

This is driving me crazy because I am trying to port code from an iOS SceneKit implementation and there the coordinates are left handed as described in the above conventions.

Here is the code that is setting the scene up:

			scene = new Scene();
			octree = scene.CreateComponent<Octree>();

			universeNode = scene.CreateChild();
			universeNode.SetScale(Const.SCENE_SCALE);

			cameraPanNode = scene.CreateChild();
			CameraNode = cameraPanNode.CreateChild();
			camera = CameraNode.CreateComponent<Camera>();
			CameraNode.Position = new Vector3(0, 0, Const.DEFAULT_POV_DISTANCE * Const.SCENE_SCALE);

Can someone help me understand what is going on here?  I don't have any code anywhere (to my knowledge) that would flip the coordinate system.

-------------------------

Modanung | 2020-08-11 16:32:14 UTC | #2

[quote="btschumy, post:1, topic:6313"]
I have a question about the default Urho3D coordinates. In the Conventions section of the documentation it says: [...]
However, when using the UrhoSharp implementation I see positive X pointing to the left.
[/quote]

UrhoSharp is not Urho3D, and as such Urho3D documentation is not UrhoSharp documentation.

If UrhoSharp drives you nuts, try Urho3D. :doughnut:

-------------------------

btschumy | 2020-08-11 17:29:35 UTC | #3

Microsoft sure implies UrhoSharp is Urho3D with C# bindings.  Can you point me to something that says otherwise?  There really is not substantive UrhoSharp documentation because they assume you will use the Urho3D docs.

As far as I know I can't use Urho3D in a Xamarin app.

-------------------------

Modanung | 2020-08-11 17:39:49 UTC | #4

I'm no sharpie, and *certainly* no fan of Microsoft (what parts of [Sategllib](http://www.azillionmonkeys.com/qed/dosalot1.html)'s body this means to describe, I shall never know). In my view UrhoSharp is a - deceased - per*version*.

https://forums.xamarin.com/discussion/141631/urhosharp-is-dead-should-we-fork-it

-------------------------

Eugene | 2020-08-11 18:40:06 UTC | #5

[quote="btschumy, post:1, topic:6313"]
However, when using the UrhoSharp implementation I see positive X pointing to the left. Positive Y & Z do indeed point up and forward.
[/quote]
I wonder how do you check that.
It's really weird, axes shall not be filpped under any circumstances.

-------------------------

throwawayerino | 2020-08-11 19:59:11 UTC | #6

Are you working with local or world coordinates? As far as I know, Y is up, Z is forward, and X is Right(?). Check the Vector3 constants `Vector3::UP`, `Vector3::Right`, etc.

-------------------------

btschumy | 2020-08-11 20:37:06 UTC | #7

So I distilled the creation of my scene to the bare minimum that shows the problem.  In this code I have positioned the camera 10 units along the z axis.  I have created a sphere at (3, 0, 0).  I have called LookAt to look down at the origin.

On the screen, the ball appears to the left of center when I would assume it should appear to the right (positive x).

The only thing that might appear suspect is LookAt.  I wasn't totally sure what to specify for the "up" vector but all the example code used Vector3.UnitY so I did as well.

Here is the code:

        private void CreateTestScene()
		{
			scene = new Scene();
			octree = scene.CreateComponent<Octree>();

			universeNode = scene.CreateChild();
			
			cameraNode = universeNode.CreateChild();
			camera = cameraNode.CreateComponent<Camera>();
			cameraNode.Position = new Vector3(0, 0, 10);
			cameraNode.LookAt(new Vector3(0, 0, 0), Vector3.UnitY);

			sunNode = universeNode.CreateChild();
			sunNode.Position = new Vector3(3f, 0, 0);

			var sphere = sunNode.CreateComponent<StaticModel>();
			sphere.Model = CoreAssets.Models.Sphere;

			var sunMaterial = ResourceCache.GetMaterial("Materials/Sun.xml");
			sphere.SetMaterial(sunMaterial);
		}

In the actual app, I have an image of the Galaxy with lots of objects around it (star clusters, globular clusters, etc).  They are in the wrong position unless I negate the x coordinate.  I know the actually position is correct because I am porting from an iOS SceneKit app and the coordinates uses there are identical.

-------------------------

JTippetts1 | 2020-08-11 21:20:11 UTC | #8

Your camera is looking backwards. If it were located at -10, and looking forward along +Z, then the ball would appear to the right, but since you're looking backwards along -Z, it appears to the left.
![image|535x500](upload://edWXp8hRhUUQK0RzAJDKbdYmN2d.png)

-------------------------

btschumy | 2020-08-11 22:26:57 UTC | #9

I appreciate your taking the time to help me out.

Is that really how this works?   That seems bizarre to me and is not the way Apple's SceneKit works.  You have to look at it from behind to see the axes running in the correct direction?  

If I'm looking in real life at an x-axis, I expect to see it increasing to he right.  To say that I need to view it from behind to have it increased to the right just seems very strange.

I'm not saying that you're wrong.  Apple's SceneKit is the only other 3D programming I've done and as I said, it works differently.

Almost all the sample code I've seen has the camera positioned at positive x, y, z.  So in the case, when looking at the scene, the x coordinate is increasing to the left?

If this is the way it works, then I will live with it.  Is there some simple call I can make to change it to what I'm familiar with?  I have a lot of code I'm porting over and it would be much easier if the coordinate systems worked the same way.

-------------------------

JTippetts1 | 2020-08-13 17:23:32 UTC | #10

In a left-handed system, a camera with no transformation will sit at the point (0,0,0), and look along the +Z axis, with up being the +Y axis. The -Z axis is behind the camera. X will increase to the right, Y will increase up. If you place the camera somewhere on the +Z axis, then look at the origin, the camera is now looking directly backwards. Now, X will appear to increase to the left, because you have essentially applied a 180 degree rotation around the up axis.

I did a quick google about Apple SceneKit, and apparently it uses a right-handed coordinate system, so that is most likely the cause of your issues. If you're coming from a right-hand coordinate system, then yes the simplest method is to invert the X axis to convert to left-handed.

-------------------------

vmost | 2020-08-11 23:59:55 UTC | #11

[Here](https://developer.apple.com/documentation/scenekit/organizing_a_scene_with_nodes) it says SceneKit uses a right-handed system, while the documentation for Urho3D you cited says Urho3D uses a left-handed system. I'd say it's fairly self-explanatory.

-------------------------

Eugene | 2020-08-12 10:06:12 UTC | #12

[quote="btschumy, post:9, topic:6313"]
Is there some simple call I can make to change it to what I’m familiar with?
[/quote]
Check this:
https://github.com/urho3d/Urho3D/issues/2642

However, UrhoSharp doesn't have the latest patch, so you will have to constantly enable this flag if you decide to use it.

-------------------------

glebedev | 2020-08-12 11:34:13 UTC | #13

Urhosharp isn't supported anymore. On other hand rbfx looks promising.

-------------------------

btschumy | 2020-08-12 14:16:46 UTC | #14

Thanks for confirming that  SceneKit and Urho3D use a different handedness for their coordinate systems.  That makes sense.  Now I just need to decide whether to try to flip it or just live with it and change my code as needed.

With regards to whether or nor UrhoSharp is supported or not...  If it is indeed no longer supported, I wish Microsoft would remove it from the Xamarin docs which say this is the way to do 3D graphics in Xamarin.  I figure if I really need to I can switch to rbfx, but right now it appears UrhoSharp does what I need.

-------------------------

throwawayerino | 2020-08-12 15:26:33 UTC | #15

UrhoSharp is just a bindings generator. Unless Urho3D 2.0 happens you could always build it yourself in an hour

-------------------------

Eugene | 2020-08-12 18:51:37 UTC | #16

[quote="throwawayerino, post:15, topic:6313"]
you could always build it yourself in an hour
[/quote]
... if you have Mac. If you don't, it's bad to be you.
![image|690x279, 50%](upload://cQ27eSxL8AvzfTwpXdNw15MvWkc.png)

-------------------------

