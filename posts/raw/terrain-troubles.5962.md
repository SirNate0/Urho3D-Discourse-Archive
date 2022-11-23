Lys0gen | 2020-03-02 15:21:25 UTC | #1

Hey everyone, just recently started using this engine and liking it a lot so far. I'm rather new to working with 3D stuff though and have encountered two issues when working with terrains.

Specifically, I am trying to imitate a Hexgrid which for the most part is working fine. I am hiding the edges of the map with a masking plane, using materials as described in
https://discourse.urho3d.io/t/cutting-holes-in-the-terrain/3667
And the plane is built pretty much the same as here
https://github.com/urho3d/Urho3D/wiki/How-to-define-3D-object-in-code

The plane is positioned at Y=0.1 while the to-be-hidden terrain pieces have a height of 0. This works fine when the camera is near as seen in this screenshot.
https://i.imgur.com/4EsjfjO.png

However when moving further away the terrain and plane start to flicker and I am not sure how to fix that. At "normal" distance it is only on the edges.
https://i.imgur.com/qSM750v.png

When going very far the even higher places in the terrain start to behave like this.
https://i.imgur.com/DnxPKSP.png

Currently my terrain has the following properties. 
    terrain->SetPatchSize(2);
    terrain->SetSpacing(Vector3(1.0f, 0.1f, 1.0f));
    terrain->SetSmoothing(true);´
    terrain->SetOccluder(true);
    terrain->SetDrawDistance(200000.0f);
    terrain->SetLodBias(200000.0f);

Any ideas on how to fix this? Getting the same issue when using other, "normal", materials and modifying the plane height only slightly changes the camera distance at which this starts to happen.

My second question is a bit simpler: Is it somehow possible to assign multiple materials to a terrain? I see other objects have an index you can pass when doing ->SetMaterial(...) but this seems to be missing on terrains.

Thanks for any help!

-------------------------

Modanung | 2020-03-02 15:59:12 UTC | #2

This looks like [Z-fighting](https://en.wikipedia.org/wiki/Z-fighting) which can be alleviated by setting a depth bias in the material XML:
```
<depthbias constant="-0.0000023" slopescaled="0"/>
```
You may have to play around with those values to find what works best in your situation.
Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

Miegamicis | 2020-03-02 19:06:30 UTC | #3

Also make sure that your camera near clip distance is not 0, that might also cause a lot of issues.

-------------------------

Lys0gen | 2020-03-02 18:53:37 UTC | #4

Thanks guys! Setting a DepthBias reduced the issue and together with SetNearClip it is completely gone.

-------------------------

