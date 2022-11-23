zedraken | 2017-11-18 05:57:22 UTC | #1

Hello all folks,

I am writing that support request in the frame of my experiments on Urho3D through the design of a small space simulation game:
[https://discourse.urho3d.io/t/spacegates-simulation-preview/3620/13](https://discourse.urho3d.io/t/spacegates-simulation-preview/3620/13)

I recently added a head down display in the spaceship cockpit in order to display what is seen from a front camera that is looking forward. Moreover, such camera is able to track a selected target whatever the spaceship movements are.

Here is a first screenshot…
![SpaceGate003|625x500](upload://xpBmHqqDZVbtfnA7tWg17A14kio.jpg)

On that screenshot, the head down display shows what is in front of the spaceship, with a zoom factor less than 1.0 to have a wide view. Such zoom can be configured on the fly.

Every thing seems to be ok, however…

Now, I activate the tracking system on another spaceship…

![SpaceGate004|625x500](upload://1MQR8BaNqYbMmhaebIVhJxauRte.jpg)

You can see that the big spaceship is oriented from left to right (and it is moving in that way), however on the head down display, it is displayed like if it has been horizontally flipped (left => right, and right => left). No vertical flip at all !

Here is another screenshot…

![SpaceGate005|625x500](upload://oMpf2hteRwSmv68de3Jf5o0lwR0.jpg)

I do not know if it is relevant to show the code snippet I wrote but it is largely inspired from the "10_RenderToTexture" sample coming along with Urho3D engine.

For the front camera, I create it in a regular way, like this:

> ...
> mFrontCameraNode = mModelNode->CreateChild("Front Camera");
> mFrontCameraNode->SetPosition(CAMPOSFRONT);
> mFrontCamera = mFrontCameraNode->CreateComponent<Camera>();
> mFrontCamera->SetViewOverrideFlags(VO_DISABLE_OCCLUSION);
> mFrontCamera->SetZoom(mDisplayZoom);
> mFrontCamera->SetFarClip(10000.0);
> ...

Then I get the rendering surface from the previously created rendering texture…
> RenderSurface *renderSurface = renderTexture->GetRenderSurface();

I create a view port…
> SharedPtr<Viewport> displayViewport(new Viewport(context_, mScene, mFrontCamera));

I assign the viewport to the rendering surface…
> renderSurface->SetViewport(0, displayViewport);

There is nothing strange in that code, but for the moment, I cannot figure out why is there such horizontal flip.
Maybe this has something to deal with how the camera view is rendered on the rendering surface ? Or maybe I forgot to configure something ?
Well, if you have some ideas or tips, I would be very pleased to hear from you.

Thanks !

Charles

-------------------------

Modanung | 2017-11-18 14:59:30 UTC | #2

Is the screen part of the ship's model? You should probably mirror its UVs.

-------------------------

zedraken | 2017-11-18 14:59:28 UTC | #3

The screen is part of the instrument panel model. I did not think at the UV mapping and as you suggested, I flipped the UV map under Blender, then exported again the screen and now, the orientation is fine.
Now that the issue is solved, it seems quite obvious !
Thanks a lot for your help, this has been very efficient.
Charles

-------------------------

Modanung | 2017-11-18 15:23:09 UTC | #4

I'm glad I could help! :)

-------------------------

