najak3d | 2021-07-18 05:33:44 UTC | #1

Our Urho app renders very simple runways, comprised of One quad, with a texture that is repeated along the V-axis, but not along the U-Axis.    This is so that we can repeat the runway lines as many times as is appropriate for the runway length.

However, when you are taking off or landing (looking parallel to the runway), the runway lines smear terribly on the parts of this quad that are further away from you, and it's not subtle.   It's awful looking.

Is there some simple fix for this?  This is using the simple Diffuse texture shader (nothing else).  It only happens when we tile the texture across this one quad in V-axis (while U-axis is non-repeating, as it's just the runway from side-to-side).

![image|336x377](upload://p7T0SzlHpdwjsZ2GuFD15ZEVF6J.png)

Our Diffuse texture looks like this:

![image|278x274](upload://qhfGjtMqbeclAdV6SvxIG4dBIfF.png)


If this behavior is "normal" (inescapable), then I supposed we can just complexify-the-mesh, giving every runway segment it's own Quad.

-------------------------

najak3d | 2021-07-18 05:57:11 UTC | #2

This type of defect also happens when not repeating...    I think I understand why this is working this way... as it gets further way, the pixel-size in the V-direction gets miniscule, while the U-direction pixel size really hasn't shrunk much.   But since the V-direction is so compressed, this is what triggers the graphics card to use a very low rez texture LOD, and therefore it blurs it just as badly along the U-direction as well.

So I'm guessing this is a common defect for many situations where you are looking at a ground texture.  As the ground is eye-level but further from the camera, texture will blur not just in the Up/down-direction, but also equally as blurred along the side-to-side direction.

I'd like to avoid this, and not sure if there is a special trick that can be used.

Note, when looking at the runway more perpendicular (e.g. a top view) - it works just fine.  This only happens when you are landing or taking off, and your view is parallel to the runway itself.

Here's another view of the runway, after we got rid of the V-Repeating -- here I have one Quad for each Line Segment -- there is no texture tiling here, yet we're still facing nearly the same defect.

![image|690x339](upload://knqFd1JxvzoDvJcZ6urGHNBvuWf.png)

-------------------------

WangKai | 2021-07-18 06:03:44 UTC | #3

You could try to enable this -
https://www.pcgamer.com/pc-graphics-options-explained/3/

As an example, create a xml file with the same name of your diffuse texture, and to add extra filter information to the texture. You can copy and paste these lines to the created xml file -
```xml
<texture>
    <quality low="0" />
    <filter mode="anisotropic" anisotropy="8"/>
    <mipmap enable="true" />
</texture>

```

-------------------------

najak3d | 2021-07-18 17:06:35 UTC | #4

Thank you, Anistrophy looks like the answer.   Similarly I found this other recent thread which addresses the same issue, with better explanations than I provided.

https://discourse.urho3d.io/t/textures-blurring-in-short-distance-anisotropy/6888/6

-------------------------

najak3d | 2021-07-18 20:28:13 UTC | #5

I'm embarrassed that I had long forgotten about anistrophy!   Thank you for setting me back on the track.

We're probably going to set Anistropic to 16, looks the best, and hopefully is performant enough.

The current result with this set to 16 looks like this  (much better):

![image|230x430](upload://p4t6vKcOZZ95SYSoWWS2E8ABaeM.png)

-------------------------

