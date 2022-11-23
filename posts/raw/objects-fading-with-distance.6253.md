btschumy | 2020-07-09 22:20:53 UTC | #1

I have no lights in my scene.  All techniques specify "unlit" shaders.  I just implemented zooming in and out of the scene and am finding my objects fade out as I get further aways from them.

In the documentation I only see reference to fading when using lights (which I don't have).

How can I disable this behavior?

-------------------------

JTippetts1 | 2020-07-09 23:22:26 UTC | #2

It's probably getting fog from the Zone. If you haven't set a Zone specifically, then it is using the default Zone which defines a black fog with Fog Start at 250 units and Fog End (maximum visible distance) at 1000 units. You can modify the fog values to push the fog boundary out further than your furthest objects to disable fog completely.

-------------------------

btschumy | 2020-07-10 13:52:41 UTC | #3

Thanks for the tip.  Yes it was the default Zone.  I have added the following code where I set up the scene.  Does this seem like a reasonable way to disable this feature?

            var zoneNode = scene.CreateChild("Zone");
            Zone zone = zoneNode.CreateComponent<Zone>();
            zone.SetBoundingBox(new BoundingBox(-float.MaxValue, float.MaxValue));
            zone.AmbientColor = new Color(0f, 0f, 0f);
            zone.FogStart = float.MaxValue;
            zone.FogEnd = float.MaxValue;

-------------------------

SplinterGU | 2020-07-15 20:55:09 UTC | #4

you can define a normal region and move it when you are moving... a huge zone will take lot of processing...

-------------------------

btschumy | 2020-07-15 22:56:37 UTC | #5

That probably wouldn't work in my case.  This is a galaxy visualization and I show things as close as 0.5 light-years out to maybe 100,000,000 light-years.  They pretty much all have to be visible at the same time.

I haven't seen a performance problem yet, but I don't yet have objects throughout the complete volume.

-------------------------

JTippetts1 | 2020-07-16 00:13:22 UTC | #6

Yikes. That might play hell with your depth buffer.

-------------------------

btschumy | 2020-07-16 03:02:59 UTC | #7

How would that be manifest?  What should I watch out for?

-------------------------

JTippetts1 | 2020-07-16 04:07:15 UTC | #8

Z fighting. Depth buffer only has so much range. Having an extremely far far plane and an extremely near near plane is the worst-case scenario for it. If a lot of bits are eaten up handling near Z-depth precision, then far objects can end up Z-fighting a lot. See https://developer.nvidia.com/content/depth-precision-visualized for some graphs of what happens. You end up with a very fine resolution near-space, and a much coarser resolution of values further away, leading to distant objects that might be quite far apart, but which end up z-fighting with one another due to the precision loss.

-------------------------

jmiller | 2020-07-16 04:36:42 UTC | #9

https://outerra.blogspot.com/2012/11/maximizing-depth-buffer-range-and.html

  https://ogrecave.github.io/ogre/api/latest/reversed-depth.html

-------------------------

Modanung | 2020-07-18 22:16:44 UTC | #10

Since you may want stars to switch from being spheres to billboards anyway, you might as well split the universe into two scenes and overlay them; one for near and one for faraway objects. You could also cheat with the distance of objects, since you'd mainly want to vary a star's *magnitude* beyond a certain point.

-------------------------

Modanung | 2020-07-20 09:39:27 UTC | #11

Another thing that comes to mind is merging distant stars into a single piece of custom geometry that uses a _point_ rendered vertex color material.

-------------------------

