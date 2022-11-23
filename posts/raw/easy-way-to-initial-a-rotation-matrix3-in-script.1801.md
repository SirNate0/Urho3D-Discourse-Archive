victorfence | 2017-01-02 01:10:17 UTC | #1

Hi all,

I want to initial a Matrix4 in script by setting translation and rotation.
[code]
Matrix4 m1;
...
m1.SetTranslation(Vector3(1,1,1));
m1.SetRotation(r);
[/code]
I found r must be passed as Matrix3.

So I plan to initial r by convert a Quaternion to Matrix3.

At last, I found Quaternion::RotationMatrix() was not ported to script interface.

So, I wonder, is there a easy way to initial a rotation Matrix3 in script?

Thanks

-------------------------

thebluefish | 2017-01-02 01:10:17 UTC | #2

[quote="victorfence"]At last, I found Quaternion::RotationMatrix() was not ported to script interface.
[/quote]

I wonder if there's a good reason for this. If not, I don't see a reason why we can't expose this to AS.

-------------------------

cadaver | 2017-01-02 01:10:18 UTC | #3

At one point matrix classes were not exposed to script (while Quaternion was) so that's probably the reason for the omission. Should be simple to add.

EDIT: It's already there, in AngelScript script API tradition getters are transformed into properties where possible. So in this case the Quaternion will have a rotationMatrix read-only property instead of getter. See [urho3d.github.io/documentation/H ... Quaternion](http://urho3d.github.io/documentation/HEAD/_script_a_p_i.html#Class_Quaternion)

-------------------------

victorfence | 2017-01-02 01:10:19 UTC | #4

Thanks for reply, I pulled last version from repo, now I see get_rotationMatrix() exported in
Source/Urho3D/AngelScript/MathAPI.cpp

And not in my old file:
Source/Urho3D/Script/MathAPI.cpp

Sorry for misinformation.

-------------------------

