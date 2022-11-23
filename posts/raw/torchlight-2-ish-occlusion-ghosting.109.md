JTippetts | 2017-01-02 00:58:04 UTC | #1

I'm trying to do an effect like the occlusion ghosting that Torchlight 2 does when a character or enemy is behind a wall or other blocking object. A blue or pink silhouette is drawn so that even if things are not visible from the camera view, you can still see them. Here is an example: [img]http://i.imgur.com/Qn2pWID.png[/img]

My first thought was to render all static level geometry first, then render the ghosts using no depthwrite and depthfunc=greater, then render the normally lit solid passes of the objects. However, I'm not really sure how I would do this.

My second thought was to draw the solid passes normally, then during alpha pass draw the model again using a "ghost" material with depthfunc=greater and a small, arbitrarily chosen negative depth bias to keep the ghost for parts of a character occluded by the character's body from overwriting the solid pass. This works somewhat, although there are weird edge cases, such as when the character is standing very near the occluder, near enough that depth-bias is no longer greater than the depth in the depth buffer.

(One other issue related to this is one I will probably file a bug report for, once I have done some more testing. To do the ghost pass, I create another AnimatedModel component into the node, specifying the ghost material. However, when I do this I notice weird glitches in the animation. 90% of the time, the animation is fine. But, for example, when standing there playing the looping idle animation I will get very rapid, occasional twitches of feet and hands, ad if the underlying skeleton were going haywire then quickly being corrected back to what it should be. I'm unsure what could be causing that.)

At any rate, does anybody have any better ideas for how I might accomplish this?

-------------------------

friesencr | 2017-01-02 00:58:04 UTC | #2

here is an article i found
[developer.valvesoftware.com/wik ... low_Effect](https://developer.valvesoftware.com/wiki/L4D_Glow_Effect)

I am reading through it right now.  Its a bit over my head but and there is like a 5% chance of survival but I think I might try it myself.

-------------------------

JTippetts | 2017-01-02 00:58:05 UTC | #3

I'm thinking I might be able to achieve what I'm looking for using multiple cameras and viewmasks. Let me try a test...

-------------------------

JTippetts | 2017-01-02 00:58:05 UTC | #4

Okay, so I managed to get a pretty good result using multiple cameras and view masks.

I created a copy of the default forward render path and removed the clearing of the depth and color buffers, then set this to the second camera. All solid world geometry and all "ghost" geometry is assigned a view mask compatible with the first camera. All objects that have a ghost are given their correct regular material and assigned a viewmask compatible with the second camera. The ghost material uses a technique that renders during the postopaque pass to draw the silhouette; it is also enabled for the shadow pass, so that correct object shadows are drawn. The ghost material renders with depthfunc=greater and no depth writing.

When the first camera renders, all solid geometry is rendered as normal, then in the postopaque pass all ghosts are rendered. In the second camera, all objects are rendered normally. This works pretty well, but with 2 issues: objects are drawn without shadows, since no shadows are rendered in the second camera, and the animation glitching still occurs, causing Jack to jump and twitch like that caffeinated squirrel from the movie Over The Hedge. The first, I think I can live with, but the second is a problem, so I guess I'll need to try to sort that out if I can.

-------------------------

friesencr | 2017-01-02 00:58:05 UTC | #5

pics or it didn't happen :wink:

-------------------------

JTippetts | 2017-01-02 00:58:05 UTC | #6

[img]http://i.imgur.com/gaSVPGR.png[/img]

With the 2-camera setup, I'm getting some glitchiness, not with the render but with update. With the single-camera setup, movement is silky smooth, but when I switch to the 2-camera setup, movement becomes rough, picking seems to take enough time to case frame-rate hitches, and other weirdness arises. I'm probably doing something wrong. The 1-camera setup with depth-bias works "okay", as long as you properly constrain the camera. Zoom too near, and the depth bias isn't enough to overcome the overwriting, zoom too far and the depth bias is too large, and causes the ghost to disappear if the object is directly behind certain pieces of geometry.

cadaver has been able to reproduce the twitchy animation, so perhaps we'll see a bugfix there soon. (I'm still not really familiar enough with the guts to really diagnose the bug myself.) In the meantime, though, I'm still researching alternative methods.

-------------------------

