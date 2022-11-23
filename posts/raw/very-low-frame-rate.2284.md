slapin | 2017-01-02 01:14:29 UTC | #1

Hi, all!

I've got to some progress with city as can be seen here:
[youtube.com/watch?v=LJs5hF-FN-g](https://www.youtube.com/watch?v=LJs5hF-FN-g)
[youtube.com/watch?v=_0gOh0LPwU0](https://www.youtube.com/watch?v=_0gOh0LPwU0)
[youtube.com/watch?v=mdix7qwJGuk](https://www.youtube.com/watch?v=mdix7qwJGuk)

Now I need help with the following:
[youtube.com/watch?v=kn-IKxFLlqI](https://www.youtube.com/watch?v=kn-IKxFLlqI)

All cars are low poly and use LODS (600 - 300 - 100 polys in each lod at 0 20 50 units). Each car have its physics initially disabled.
If camera is closer than 10 units, the physics gets enabled. There is only 100 cars in scene spread-out over 1000x1000 units square.
camera farClip is at 200, fog is at 150. The FPS is about 1-10. Any ideas?
(reducing amount of cars to 10 gets frame rate back to 30).
The CPU is i7 2600K, video is gtx660. I can run games which have much more polygon power...
The building are set as occluders.

-------------------------

1vanK | 2017-01-02 01:14:30 UTC | #2

Try to build Release version of engine

-------------------------

slapin | 2017-01-02 01:14:30 UTC | #3

Thanks, I build release version and performance is better, but the load is still at 90% CPU.
is there any idea on how to properly handle large amounts of objects, like in traffic simulations?

-------------------------

Eugene | 2017-01-02 01:14:30 UTC | #4

[quote="slapin"]Thanks, I build release version and performance is better, but the load is still at 90% CPU.
is there any idea on how to properly handle large amounts of objects, like in traffic simulations?[/quote]
I look at your shaking cars and think.. Are they all awoken physical objects? If so, I suppose that such amount of vehicles can't be handled properly by physical engine. Try to use minimum possible amount of such objects.

-------------------------

cadaver | 2017-01-02 01:14:30 UTC | #5

I suspect a large city simulation would typically just have the vehicles "gliding" on paths without physics involved at all. For a game like GTA, you'd likely only have the nearby cars (those that can collide with the player) physical, and cheat so that the faraway cars always behave nicely and don't collide.

The amount of ExecuteMethod and UpdateCollisionShape in your profile seems suspicious. UpdateCollisionShape shouldn't happen each frame when objects just update, and aren't being created/destroyed. For max. performance you can't really have scripts updating 100's of objects each frame, use C++ instead.

-------------------------

slapin | 2017-01-02 01:14:30 UTC | #6

Thanks for the pointers. I fixed collision shape updates (they really happened each frame due to some logic error), but performance is still not right. I currently have physical 5 cars max. This should be fine, but for some reason the frame rate is not great :frowning:
any suggestions where I can cheat?

[youtu.be/RzwbokHZBN8](https://youtu.be/RzwbokHZBN8)

How is car traffic organized when no physics is involved? As I understand I still need physics bodies, as geometry raycasts should be very slow...

-------------------------

slapin | 2017-01-02 01:14:30 UTC | #7

Also I need to ask - can't Urho crowd system help with traffic?

Thanks!

-------------------------

Lumak | 2017-01-02 01:14:30 UTC | #8

Here are some things you can do to optimize performance:
-don't render vehicles in far distance and fade them in when you're getting closer. I haven't look into this and not sure if you'll need to modify the engine.
-use occulders/occuldees - looks like vehicles are rendered even when they're occluded by buildings.
-a viewport for a minimap probably is a huge cost to your performance, consider drawing a map instead. I'd like to hear what the difference is w/o it.
-vehicles w/o using physics are typically moved on a spline.

-------------------------

slapin | 2017-01-02 01:14:31 UTC | #9

Could you please help with vehicles without physics?

I'd like to have the same vehicle controller, i.e.

const int CTRL_FORWARD = 1;
const int CTRL_BACK = 2;
const int CTRL_LEFT = 4;
const int CTRL_RIGHT = 8;

to hide the fact of switching to/from physics. as I understand I can rotate body using node.rotation.yaw and move adding node.direction * speed * timeStep to node.position, right?

-------------------------

Lumak | 2017-01-02 01:14:31 UTC | #10

The whole point of having vehicles move on a spline is that you don't steer them for something like what you're trying to create, a massive traffic system.  Instead you'd have something like a manager that move your vehicles on a spline.  For a racing, it's more ideal to use AI steering and you still wouldn't use any key controls.

Urho3D has a spline component and you can place from the Editor.  I wrote my own spline/spline manager/AI steer, so I don't know how the Urho3D spline component works. I'm sure there's a document on it or maybe someone on the forum could shed some light on its use.

-------------------------

slapin | 2017-01-02 01:14:31 UTC | #11

Well, I want AI steering. Splines can be used with AI steering too with some tweaking without any real problems, which makes controller the same for physics mode and non-physics mode.
I've already implemented half of it, now I can switch off physics and continue motion in realistic way, but I can't steer, for some reason I can't find a way for car to turn.

What I do:
when I switch to non-physics mode:
[code]
(After disable all bodies)
node.worldPosition - body.position;
node.worldRotation = body.rotation;

(for all wheels)
frontLeft.parent = node;
....
fromLeft.worldPosition = node.worldPosition + node.rotation *offset ;
[/code]

and vice versa restoring back all parameters to go back to physics. The criteria is certain raycasts and distance to camera.
with this I can have 400 cars  (probably much less when all be in motion :slight_smile:. The difference in motion between physics and
non-physics is noticeable but acceptable at low speeds. At high speeds I enable physics on collisions (checked by raycasts)
which works perfect (as soon as collision is over physics is off again and continuation works great, very nice effect).
But now I need wheels to turn (easy) and actual car to turn (still could not get it. Changinr rotation.y on the node
produces freaky results. Should it work or I need to calculate it properly?

As for splines - I understand how to do these, I will do it for some distant traffic, it can be done using steer control too, just by checking local x of the transform
which is quick and the result is quite nice and preciese.

-------------------------

Lumak | 2017-01-02 01:14:31 UTC | #12

[quote="slapin"]Splines can be used with AI steering too with some tweaking without any real problems... [/quote]

Yup, here's mine that I implemented a few months ago.
[video]https://www.youtube.com/watch?v=THtkRu9Zrv8[/video]

I thought you were looking for ways to increase your frame rate/performance and hence, my list of things to try.
But I think you're going after something else altogether.  From the sound of it, I think you got a good handle on how to do it.  

Good luck with your implementation, can't wait to see how your traffic turns out.

Edit: there is a distinction between 1) following a spline to 2) moving on a spline (some might call it riding on a spline) - 1 is costly, 2 is not.

-------------------------

slapin | 2017-01-02 01:14:31 UTC | #13

Well, Thanks for advices.

I don't want to sacrifice details until absolutely necessary. I will implement spline motion if absolutely required to handle.
But I hope non-physicsl steering will be sufficient.

-------------------------

