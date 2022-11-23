najak3d | 2022-02-28 15:02:35 UTC | #1

We're seeing ShadowMap Coverage being skewed to the Left (in the direction that the Directional Light is pointing) in the below screenshot.

We're not doing anything unusual that we know of here.   This error does not happen in the Samples, so not sure why it's happening in our particular scene.   In this case, the ShadowMap is skewed towards the X-Negative Axis, and away from X-Positive.

This shows missing shadows (or partial for the girl) on Right side(X-Positive), but on Left Side (X-negative), the shadows extend very far way.

![image|690x367](upload://eh7fX2dmBSAmWEko9PAJyGYMW7a.jpeg)

It skews the coverage in the direction of the Scene's "Directional Light".   For the above screenshot, the directional light direction is:  new Vector3(-1f, -1f, -0.2f)    and the shadow map coverage is strong towards X-Negative.

If we change the Direction Light to "new Vector3(1f, -1f, -0.2f)", then it skews the coverage towards X-Positive.

Since this does not happen in the "Skeletal Animation" sample, it's definitely some sort of bug with our scene/camera setup.   But I'm using the same code for this as the Skeletal Animation.

**Does anyone have any clues as to where in our setup we should be looking for something that could cause this type of Shadow-Map skew?**

-------------------------

najak3d | 2022-02-28 15:31:12 UTC | #2

One thing that might be peculiar about our scene vs. the Samples is "SCALE".   These buildings are 2000 units tall here... so our scale is about 50x larger than that of the Samples.   Perhaps our scale is triggering some sort of buggish behavior here.

EDIT -- NOPE!  I reduced Shadow Map splits down to 10% of what they were, and still this defect persists:

![image|634x500](upload://90RZmfMV4puuanNNDkmusJfwUs2.jpeg)


I even then scaled up the Skeletal Demo to 100x size -- and still IT WORKS.   So there is something else peculiar about our scene setup or camera.

This screenshot shows it working for the Skeletal Demo scene:
![image|491x500](upload://nJgLRrbkOtdUuKMJj6EhQBwkDq.jpeg)

-------------------------

najak3d | 2022-03-04 08:20:47 UTC | #3

OK, just discovered that this IS a problem in the Urho Samples project as well.   Check out the top image, where we are looking away from the sun -- the shadows are cast for very far away models.

![image|690x273](upload://6cdaOgjt7hl1s6zRvgi3eISdSoF.jpeg)

Then I just rotate the camera 180 to look into the sun, and here the models from VERY CLOSE already have lost their shadows!

![image|690x312](upload://iQgJZWyYYoDxHogg2OnSRlMBZbc.jpeg)

This defect is more obvious the lower-in-sky the sun is.   Directional Light going closer to horizontal (casting long shadows), exhibits this defect the most.

So there appears to be a shadow-map-skew bug, that is responding to the Directional Light's direction, especially as it goes more horizontal.   I'd like to see an Urho maintain reproduce this

NOTE: THIS ONLY HAPPENS WHEN I SCALE UP THE "SkeletalAnimation" demo up to 100x the original size (scale the plane, the models, the Shadow Clip distances, everything)... so the scene "appears the same", but the shadows are messed up, the higher the scale we go.

So this is related to scene Scale.  Higher scales trigger this defect.

**Urho3D Defect:**
The defect is that Shadow-Map get skewed away from the Direction Light, tragically, at higher scale.  This should not be scale-independent.   Scale should have no Visual impact on ShadowMap skew.

-------------------------

najak3d | 2022-03-04 18:41:22 UTC | #4

Here's another screenshot of the Samples Skeletal Animations, with scale set to 1000x... here the shadows become super defective as you look towards the light source:

![image|690x334](upload://uuAUI5Jte92GXIOcp2FWNCIjGca.jpeg)


**WORKAROUND:**
The workaround is to more Urho-Standard scale (e.g Camera Far Clip range between 100 to 10,000) ... but that shouldn't be a requirement of Urho3D for using shadows.   Is there some way to adjust the built-in Shadow Map technique to accommodate larger scales?

Our game world is 10 million units (meters) side-to-side, but will never allow you to get closer than 1000 units from what you are viewing...   Our workaround fix will be to change our standard unit-of-measure from Meters to Kilometers.   And that'll resolve this issue for us.

-------------------------

najak3d | 2022-03-04 17:13:10 UTC | #5

More notes -- if I instead scale SkeletalAnimations to 0.1 (making it smaller) - the shadow suffer a different defect - in that the Cascade don't seem to really be 1, 5, 20...   The result is blurry/close-up shadows (same as if the Cascade ranges were still more like 10, 50, 200).

![image|690x329](upload://4Cbt4YPR9DgO0DPsHmq8878k7a1.jpeg)


So shadow Cascades of that are too small or too large -- seem to trigger an Urho defect, in that it doesn't really let you set these values outside of some built-in optimum range...  such as 10, 50, 200.

So our workaround is to resize our scene to the "Urho supported scene size" (with regards to shadows).

-------------------------

najak3d | 2022-03-04 18:43:08 UTC | #6

The reason we want our scene scale to remain meters, despite the world map being 10 million meters wide -- is that we still want to think in terms of meters.

Due to this defect of Urho, we'll be switching our game units to Kilometers, which means that we'll have human characters that are just "0.002" units tall.

-------------------------

SirNate0 | 2022-03-06 03:09:49 UTC | #7

You may already be dealing with this, but you're probably going to run into other issues if your may is 10^7 character-size units wide. My recollection is that single precision floats have only about a 10^7 precision, so at the edges of the map you'll run into a bunch of floating point rounding errors because the computer can't tell the difference, for example, between 10^7 and 10^7+0.1 (say the width of a characters hand).

If you're looking for suggestions for how to get around that I have a few (though no idea if they're any good), but I don't want to impose if you've already thought through it. And I also don't want to drag the thread too far off topic.

-------------------------

JSandusky | 2022-03-06 04:51:22 UTC | #8

If this is a directional light the problem is probably with how far the directional "*walks backward*" to include things potentially out of view. I can't remember where that's done though and I might be crossing engines in my memory.

-------------------------

