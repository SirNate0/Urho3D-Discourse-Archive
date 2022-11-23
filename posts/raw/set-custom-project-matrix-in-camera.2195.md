godan | 2017-01-02 01:13:50 UTC | #1

Small request: implement a SetCustomProjectMatrix(Matrix4 mat) function in the Camera class. From what I can see, only various SetFOV and SetNearClip methods are exposed. 

For my recent investigations in VR, this is would be a pretty handy function to have.

-------------------------

godan | 2017-01-02 01:13:50 UTC | #2

To clarify, the use case here is for reading the left and right eye projection matrices from the device and forcing them on to the cameras. So this function would be called during Update.

-------------------------

Egorbo | 2017-01-02 01:13:50 UTC | #3

You can extract FOV, FarClip, NearClip, aspectRatio from your custom projection matrix and feed them to Camera without that additional method.

-------------------------

godan | 2017-01-02 01:13:50 UTC | #4

Yep, but it's a hassle :slight_smile:

Since in my case, I'm getting a Matrix4 directly from the device, it seems much easier to simply set the private variable "projectionMatrix_" via a SetProjectMatrix method. No math needed.... Don't get me wrong, I can certainly find a work around for now. However, I think it's simple enough fix that would make this sort of application a lot easier.

-------------------------

Egorbo | 2017-01-02 01:13:50 UTC | #5

Make sure your matrix is left-handed :wink:
PS: you will have to extract those values anyway in that SetProjectMatrix method, otherwise other components/code with some logic based on camera->GetFOV\camera->GetFarClip etc will get wrong values (default).

-------------------------

cadaver | 2017-01-02 01:13:50 UTC | #6

This can be done, but IMO it should be done in a raw way, no new state or "useCustomProjection" flag but you simply set it, and if you change any of the standard parameters like FOV or near clip, your custom matrix is lost. Also you must take care yourself of D3D / OpenGL differences, since the final matrix would be different for both of them due to different depth range.

-------------------------

cadaver | 2017-01-02 01:13:50 UTC | #7

Hm, now that I think of this more, it has potential to make some things not work so well, so I lean on not adding it after all. I also remember that I've possibly thought of it before. :slight_smile: For example OpenGL texture rendering needs to flip the projection vertically, which would under the simple scheme I outlined in the last post, just overwrite the custom set matrix. Also screen ray calculation and occlusion software rendering need the projection matrix too, but it's always for the D3D-like depth (from 0 to 1) so an OpenGL matrix would produce incorrect results there, and then you might wonder why screen picking or occlusion doesn't work as you expect.

In short I don't plan to spend energy on this now. A cleanly implemented PR that avoids these shortcomings would be welcome though, as usual.

-------------------------

Egorbo | 2017-01-02 01:13:50 UTC | #8

I guess we can add a method smth like this:

[code]void Camera::SetProjection(const Matrix4& projection)
{
  //TODO: calculate values
  //calculation depends on DX\GL and LH\RH coordinate systems

  //for example, this is how fovY is calculated:
  float fovY = 360 * atanf(1 / projection.m11_) / M_PI;

  SetAspectRatio(apect);
  SetFov(fovY);
  SetNearClip(nearClip);
  SetFarClip(farClip);
}[/code]

-------------------------

cadaver | 2017-01-02 01:13:50 UTC | #9

Doing it that way would also ensure the frustum is kept correct.

-------------------------

Egorbo | 2017-01-02 01:13:51 UTC | #10

BTW, in my case a device returns me a projection matrix with some fields that Urho3D Camera doesn't use. For example - skew (m01).

-------------------------

godan | 2017-01-02 01:13:51 UTC | #11

Interesting. @Ergobo, I hadn't thought about the case where another component would call GetFov(). So yes, good point that those values need to be split out anyway.

I'll take a stab at recovering the various values - basically writing the inverse function to GetProjectMatric(bool apiSpecific).

-------------------------

cadaver | 2017-01-02 01:13:51 UTC | #12

We could support arbitrary custom projection matrices by extracting the view frustum from it (ie. inverse transform the clip space corner points)

However to be a friendly and useful feature, we should only require the user to pass the projection matrix in one format. Preferably the D3D one as that is used internally by occlusion rendering & screen rays.

But when using OpenGL, we'd need to be able to convert it to OpenGL format for the actual rendering. Ogre had code for conversion (it was rather doing OpenGL to D3D) but I'm not convinced that it was correct. As it stands now the formulas for D3D & OpenGL projection matrices are quite different.

-------------------------

cadaver | 2017-01-02 01:13:52 UTC | #13

I dug up the original post on the Ogre forum (where projection matrix conversion was being proposed)
[ogre3d.org/forums/viewtopic.php?f=4&t=13357](http://www.ogre3d.org/forums/viewtopic.php?f=4&t=13357)

and the formulation appears to be working, at least for a typical perspective and ortho matrix.

Need to test the frustum definition from the matrix, but if that works too, then it's worth implementing the ability to supply an arbitrary projection matrix, since it would then work without any shortcomings / bugs.

-------------------------

weitjong | 2017-01-02 01:13:52 UTC | #14

Thanks Lasse, I am also looking forward to this one.

-------------------------

cadaver | 2017-01-02 01:13:56 UTC | #15

Custom matrix code has been merged to master. It's not mega-accurately tested, but we'll then see if it causes any issues.

-------------------------

godan | 2017-01-02 01:13:56 UTC | #16

Amazing! Thanks cadaver.

-------------------------

