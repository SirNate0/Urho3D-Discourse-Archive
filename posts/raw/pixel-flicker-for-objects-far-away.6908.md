najak3d | 2021-07-04 23:42:58 UTC | #1

We depict aircraft far away in our App, and represent them with a static 3D model.   But these slow-moving 3D objects have severe pixel flicker, especially with the parts of the mesh that are "thin" from far away.  Attached is an image of an aircraft slowly flying away from us.   As it moves, the pixels the wing flicker madly between transparent, blue, and black.

For the slow moving objects as they get further away and smaller, what are the best ways to get rid of this pixel flickering?    See image below... it shows two near successive frames of the aircraft... note the right-wing for example -- see how it's oscillates between black and blue?   This looks horrid when rendered frame-to-frame, and the pixel colors flicker madly.

![image|458x500](upload://soVCPm6GS176AWpcBExh6i7DXRB.png)

And here's another example, very similar -- the wing flicker is the worst part here:

![image|473x500](upload://aQBPRMOG3EVgPuGOtI3YyGOG9vZ.png)

-------------------------

najak3d | 2021-07-04 23:49:29 UTC | #2

One solution that I've done in the past is the use of "Imposters", where you take a photo of the 3D object from various angles, and then render the image of the imposter frame that is most-facing-the-camera...     All angle-views of the 3D image are rendered as 128x128 images onto a 1024x1024 image (giving you 64 views total).  and the Imposter material just sets the UV coordinates to the sub-image on this larger image.

So we could do this with the aircraft -- create an image for every 15-30 degree viewing angle (in both Yaw and Pitch directions).... then just render a 2D imposter image with Alpha -- and this will eliminate the Pixel flicker/jitter.   This was a trick from 2007!!!..

I was wondering if there is a more modern trick to use now?  (14 years later!)

-------------------------

najak3d | 2021-07-05 00:14:13 UTC | #3

I found this guy's YouTube from Jan 2020 showing "Octahedral" Imposter support from Vitaly Minnahmetov.

https://www.youtube.com/watch?v=1cROTxRlN6s

-------------------------

Rook | 2021-07-08 19:03:13 UTC | #4

The way I think of imposters is through the use of render to texture, the model is rendered once to texture in high detail and a plane with that render is put in place of the actual model and then re-rendered when there is sufficient change in the viewing angle. If necessary you could queue those re-renders.

Is the actual issue you have with the aircraft an aliasing problem though?

-------------------------

najak3d | 2021-07-18 20:17:19 UTC | #5

Imposters is the right solution for this.

But there were two issues going on with this:
1. Thin wing view has anti-aliasing issue with background, as each pixel 100% opaque, so as the wing moves slightly on the screen, the pixels flicker between showing "wing" and "what's behind the wing(background)"...  That's a key issue.

2. Anistrophic filtering, I think, may partially resolve this issue, otherwise, as it might prevent the wing pixels from dithering/flicker between colors.


But in the end, the best solution is probably imposters, as I render these with alpha-blend, and that resolves the issue of pixels flickering between "wing" and "background".

-------------------------

najak3d | 2021-07-18 20:24:50 UTC | #6

I'm also thinking that maybe as the aircraft gets further away, we change the material to "alpha blend" and start fading it out.   How do other games deal with this issue?

-------------------------

Eugene | 2021-07-19 09:06:32 UTC | #7

[quote="najak3d, post:6, topic:6908"]
How do other games deal with this issue?
[/quote]
MSAA, FXAA (these ones are present in Urho in some form), TAA (temporal antialiasing), billboards for far objects...

-------------------------

