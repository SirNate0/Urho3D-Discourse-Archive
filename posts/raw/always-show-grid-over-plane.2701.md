George1 | 2017-01-14 02:28:35 UTC | #1

Hi, I'm drawing a grid at the same location as the plane. How can I  always show the grid in Urho3D without having any y-offset.

In Irrlicht I can disable or enable z buffer or something like that to achieve this.

-------------------------

SirNate0 | 2017-01-14 04:20:31 UTC | #2

You can try messing with the render order for the grid material (see https://urho3d.github.io/documentation/1.6/_materials.html). You could also try creating a new technique with a different depthtest setting (perhaps always or lessequal).

-------------------------

jmiller | 2017-01-14 18:35:40 UTC | #3

When using Material/Technique/shader approaches on a single geometry, the z-buffer is not relevant.
[b]setzer22[/b] renders a white grid on top of Terrain in this older thread:

http://discourse.urho3d.io/t/solved-various-questions-about-shaders/400

The result image seems to no longer exist, but it showed a nice effect which one can still visualize.

-------------------------

George1 | 2017-01-15 16:09:46 UTC | #4

Hi, this problem uses two geometries. A grid node a plane node at the same location.

I can set zwriteenable to false in Irrlicht = false to achieve this. 

I'm not too familiar with Techniques and shader in Urho yet. Will come back to learn this in the future when I'm process further with what I'm doing. At the moment I just use a small offset for the grid as a temporary fix.

Here is a snapshot of what I'm working on atm. 

40k boxes moving on 10k conveyors using discrete event method. I have not create cad for conveyors yet.

https://www.youtube.com/watch?v=uSBMW6o7Uw8

-------------------------

jmiller | 2017-01-15 17:00:32 UTC | #5

Then I think SirNate0's idea is more what you want and easiest.
Another thread describes a couple methods: one that clears depth and adds a custom pass, and one that revisits a multiple camera method.
http://discourse.urho3d.io/t/depthwrite-questions/1255

-------------------------

George1 | 2017-01-16 05:14:28 UTC | #6

Thanks,
I will study this.

Best Regards

-------------------------

