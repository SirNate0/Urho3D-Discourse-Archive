szamq | 2017-01-02 01:13:07 UTC | #1

Since Oculus changed it's runtime several times through past year I would like to update my previous implementation [topic1000.html](http://discourse.urho3d.io/t/oculus-rift-support-renderer-and-input/974/1) to work with the newest runtime by using OpenVR( which works with Steam Vive out of box too).
I found cool minimal sample how to use openVR, here is the source code for OpenGL (only 400 lines which is optimistic) 

[g3d.cs.williams.edu/websvn/filed ... 2Fmain.cpp](http://g3d.cs.williams.edu/websvn/filedetails.php?repname=g3d&path=%2FG3D10%2Fsamples%2FminimalOpenGL%2Fmain.cpp)

In the newest oculus runtime as also openVR we don't need to care about distortion and rendering, all we need to to is to send two framebuffers to the sdk and that's it.

If you look in the sample there are two framebuffers which are bind for each eye -> rendered -> and submitted. That's quite straightforward.
I would like to make implementation in urho style with maximum use of urho's features, as high level as possible. So the question is: how to do that properly?

Could I use renderpath to render the scene first time for the one eye then subscribe for finished render command to submit to the openvr sdk, clear the framebuffer and then render the same scene same for the second eye? Is this possible? how the renderpath should look like when rendering twice?(doubling all render commands?)

-------------------------

cadaver | 2017-01-02 01:13:07 UTC | #2

Seems fairly sane. You need 2 rendertarget textures to which you define a viewport (see RenderToTexture sample). The renderpath doesn't need to know that stereo rendering is happening, it's just executed once for each viewport. If you want to optimize culling and view preparation use Viewport::SetCullCamera() in both viewports and pass to it a "fake" camera which has its FOV widened so that it sees the combined view of both eyes.

When it's time to submit, use Texture::GetGPUObject() to get the OpenGL integer name of the rendertarget texture. This will change slightly in the api-agnostic-headers branch, but only the function name changes and idea is the same.

-------------------------

yushli | 2017-01-02 01:13:08 UTC | #3

@cadaver, would you like to make an official VR sample? VR is now quite hot and Urho3d's excellent performance suits it really well. It is good to see Urho3d has official VR support and can show off immediately with an official sample demo.

-------------------------

cadaver | 2017-01-02 01:13:08 UTC | #4

I have no VR hardware to test on, so the sample and integration has to come from someone else.

This will obviously be something that will (very likely) need continuous improvement, so it would need a contributor who is interested in maintaining it, instead of just a one-off contribution.

Otherwise it's a good idea.

-------------------------

larsonmattr | 2017-01-02 01:13:08 UTC | #5

@cadaver:

 I have access to both a Oculus DK2 and a HTC Vive system.  I'm trying to find a cross platform engine that can work on one or more of these systems.  I'd also be interested in helping with the development and testing.

 Is there a public branch started for incorporating OpenVR and trying to make an example?

-------------------------

cadaver | 2017-01-02 01:13:08 UTC | #6

I haven't kept track of others' forks, but at least not in the Urho main repo. (Others can fill in)

-------------------------

godan | 2017-01-02 01:13:08 UTC | #7

I also have an Occulus DK2 and have been meaning to test out VR on Urho for a while. I'd be very interested in helping out.

For me, it would be most helpful if someone could write a bit more about the implementation. Some pseudocode maybe? After that, I could probably hack together a test.

-------------------------

yushli | 2017-01-02 01:13:09 UTC | #8

I think cadaver would be the best one to write the pseudo code to show the implementation.  VR demo is really performance critical. Only cadaver can get the most out of Urho3D...
Better yet he can have access to the test device so that he can fine tune the performance.

-------------------------

SeanV | 2017-08-30 05:28:26 UTC | #9

I have gotten OpenVR working in Urho3D and have put up a fork at https://github.com/seanvolt/Urho3D_VR in order to get things moving further. I would love input and some help with things like CMake!

-------------------------

majhong | 2022-01-28 08:27:12 UTC | #10

Looking forward to an openxr implementation！ :+1:

-------------------------

