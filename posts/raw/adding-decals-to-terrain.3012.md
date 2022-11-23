slapin | 2017-04-16 14:07:24 UTC | #1

Hi, all!

I need to add decal to terrain at [i]Vector3 pos[/i] location and [i]Vector3 normal[/i].
How can I
1. Find closest terrain patch to [b]pos[/b] and use it as drawable. is there some way?
I don't want to use raycast as I already know the location.

2. Find the rotation from normal vector.

-------------------------

George1 | 2017-04-16 15:09:55 UTC | #2

I think you need to use the search function. I think most of the questions you raised existed in the forum.
There is a decal example in the lib.
I remember there are a few other solutions including a car wheel trace mark kindly shared by a member a year or two ago.
Also see the basic effect posted by Lumak. I believed it has decal effect in there.

Best

-------------------------

slapin | 2017-04-16 18:18:58 UTC | #3

Decal example use Raycast which provides the Drawable.
And there's no decal examples I am aware of on the forum.

as for Lumak's code, he creates geometry, not uses decals in offroad vehicle demo.

-------------------------

jmiller | 2017-04-17 02:11:51 UTC | #4

George1 refers to a decal example in the lib, here:
  https://github.com/urho3d/Urho3D/tree/master/Source/Samples/08_Decals

If you only want to find the nearest TerrainPatch, you could calc that using the Terrain API (*possibly, depending; or other Drawable methods):
  https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Terrain.h

-------------------------

slapin | 2017-04-17 05:30:47 UTC | #5

@jmiller would you please read what I write before answering? :)

I wrote exactly about 08_Decals and that it uses Raycast to get Drawable.

About terrain API - it is not obvoius how to get TerrainPatch closest to a point,
so I still wait for help with this.

-------------------------

jmiller | 2017-04-17 14:27:13 UTC | #6

My bad -- I was tired and completely missed your first sentence. :)

As an example of 'other Drawable methods': could iterate patches and use their Drawable::GetWorldBoundingBox().Center() perhaps?

By 'calc', I was thinking of a simpler 2D method that may or may not be suitable. by analogy: "given the position of a grid (terrain), and the grid square (patch) size, find which grid coord a point falls in".

-------------------------

Dave82 | 2017-04-17 15:16:09 UTC | #7

[quote="slapin, post:1, topic:3012"]
Find the rotation from normal vector
[/quote]

If you know the normal vector and the position , you can get a rotation vector using a vector function from irrlicht : 
[CODE] 
Vector3 Vector3::EulerFromNormal()
{
    Vector3 angle;
    angle.y_ = (atan2(x_ , z_) * :M_RADTODEG);
    if (angle.y_ < 0)  angle.y_ += 360;
    if (angle.y_ >= 360)  angle.y_ -= 360;

    float z1 = sqrt(x_ * x_ + z_ * z_);
        angle.x_ = (atan2(z1, y_) * M_RADTODEG - 90.0f);
    
        if (angle.x_ < 0)  angle.x_ += 360;
        if (angle.x_ >= 360) angle.x_ -= 360;

        return angle;
}[/CODE]

Please note : Depending on your culling (CW , CCW) you may need to negate the normal to get the correct rotation.
Build a Quaternion using the returned vector (Quaternion rot(returned.x_ , returned,y_ , returned.z_);

-------------------------

slapin | 2017-04-17 15:13:37 UTC | #8

@jmiller - I know I can get height on the terrein in any point, can't this be converted to patch somehow?
the iteratiom method is last resort, it is very, very slow.
About 2D - one can get texture coordinate too. I don't understand why there's no easy Drawable access :(

-------------------------

