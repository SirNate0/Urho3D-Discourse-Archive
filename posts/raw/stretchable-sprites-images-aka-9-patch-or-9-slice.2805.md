ricab | 2017-02-20 16:03:01 UTC | #1

Hi,

Does Urho3D support stretchable sprites, either with [nine patch](https://developer.android.com/guide/topics/graphics/2d-graphics.html#nine-patch)/9-slice images, or some other way? 

Otherwise, any suggestions on how to do a 2D platform that can grow and shrink? I thought of using plain images for different parts of the intended sprite (repeatable and static) and then arrange the corresponding multiple sprites spatially so they would look like a single object. But I guess such a "platform" would have to be composed of several scene nodes and would be quite heavy. And I suppose that could have negative impacts on GPU acceleration. Besides, resource creation would be cumbersome.

Is there a better way to non-uniformly scale a source image at run-time, to dynamically obtain an image that can be used as a sprite?

-------------------------

1vanK | 2017-02-20 16:44:33 UTC | #2

BorderImage uses this approach, but it only for UI

-------------------------

ricab | 2017-02-20 19:00:58 UTC | #3

Thanks, indeed this does not seem to be usable for purposes other than UI. Any other suggestions?

-------------------------

Modanung | 2017-02-21 20:52:07 UTC | #4

- AnimatedModel with *key shapes / morphs*
- Dynamic geometry

Either wrapped in a custom class.

-------------------------

ricab | 2017-02-24 16:24:56 UTC | #5

Thanks @Modanung. Your suggestions got me thinking. If I understand properly, they both involve 3d mesh manipulation though. I would rather avoid that in a 2D-only context. 

I am not familiar with dynamic geometries and I have the impression they would be too complex for this case. As for an animation approach, I suppose I could use AnimatedSprite2D. I will keep that in mind, but I think I will try a different approach first, one that does not require bones or keyframes:

1. Define a "stretchable entity resource" with
    * sprite (image, rectangle, hotspot, etc.)
    * stretchable rectangle (can be reduced to horizontal or vertical line if only one dimension can be stretched)
    * collision polygon
2. Have a stretchable entity class that reads this and provides a stretch(x, y) by
    * creating a node with 9 subnodes, one for each cardinal point (N, S, E, W, NE, ...) plus one for the center (C) [only create 3 subnodes if only 1 dimension can be stretched]
    * assigning a sprite to each of the nodes, based on the same image but with different rectangles (derived from the original rectangle and the stretchable rectangle<sup>[1](#myfootnote1)</sup>)
    * scaling nodes N, C, and S horizontally to stretch horizontally
    * scaling nodes W, C, and E vertically to stretch vertically
    * changing collision polygon vertices accordingly
3. other details from the top of my head:
    * override necessary methods (e.g. flip)
    * flip for negative stretching amounts
    * stretching below a ZERO stretch rectangle falls back to scalling corner nodes; scalling back up reverts that

Stretching could then be animated with a ValueAnimation.

What do you think? Do you see important downsides to this approach? More suggestions/discussion welcome!

---
<a name="myfootnote1"><sup>1</sup></a> e.g.:
    * NE.left_ = orig_rect.left_
    * NE.right_ = stretch_rect.left_
    * NE.top_ = orig_rect.top_
    * NE.bottom_ = stretch_rect.top_

-------------------------

Taymindis | 2017-11-17 08:11:50 UTC | #6

Hi Ricab, 

has this feature available now? Do you have any suggestion or reference to create a Patch9Sprite?

-------------------------

ricab | 2017-11-17 16:05:42 UTC | #7

I don't think so, I am afraid I never got around to it.

-------------------------

Lumak | 2017-11-17 16:33:26 UTC | #8

I recall Torque Engine having this, prior to being called Torque3D.

-------------------------

Modanung | 2017-11-17 18:00:29 UTC | #9

I guess you could use a UIComponent to render a BorderImage to a plane. Like in the [Hello3DGUI](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/48_Hello3DUI) sample.

-------------------------

Eugene | 2017-11-17 18:50:03 UTC | #10

[quote="Modanung, post:9, topic:2805"]
I guess you could use a UIComponent to render a BorderImage to a plane.
[/quote]

It sounds a bit overkill.

-------------------------

Modanung | 2017-11-17 18:51:24 UTC | #11

Agreed, but maybe less so then my previous suggestions. ;)

-------------------------

Lumak | 2017-11-17 21:56:05 UTC | #12

this: https://github.com/urho3d/Urho3D/pull/2168/files#diff-957a3aa78761fe8f659474aacf99975aR2322 is probably what you'll need once merged with the main branch.

-------------------------

ricab | 2017-11-18 02:25:48 UTC | #13

Thanks for the link. How exactly do you envision using this? Perhaps having a StretchableSprite2D class that would resize and overwrite the underlying image data in [UpdateSourceBatches](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_drawable2_d.html#aaa3ee2dfe5f37c32ed8fd11a3b169e6e), according to the world scale? And how would the new image data be loaded into the GPU? Wouldn't it be problematic to do that each frame?

-------------------------

Lumak | 2017-11-18 17:04:57 UTC | #14

The setsubimage() fn is designed more for a static copy, you'll have to modify it to accommodate stretch. I don't know the requirement specification so I couldn't say how frequently you should resize the image, but I definitely wouldn't resize it every frame.  There should be some kind of world scale range which indicate when image resizing and stretching should occur.

-------------------------

ricab | 2017-11-22 19:57:43 UTC | #15

> I don’t know the requirement specification 

Considering "stretch" here to be just what 9-patch images do, ideally what I see is:
1. for the client, stretching should be as trivial as scaling; perhaps just using the same Node::Scale API (see below)
2. stretch should be "animatable", with no significant penalty (in performance or ease-of-use) relative to scaling

Perhaps stretching could be encapsulated in a component of the `Drawable2D` family. The client would just call `Node::Scale` normally and stretchable components would react by stretching (falling back to scale if below minimum stretch). Some additional API could be provided by the stretchable component to allow for regular scaling (useful mainly for scene setup).

A basic _use-case_ would be growing/shrinking platforms.

I am not sure how something like this could be implemented though... Input still very much welcome

---
EDIT: just saw [this](https://discourse.urho3d.io/t/does-urho3d-have-patch9imagesprite/3748) other topic. Will have a look at what Eugene suggests there.

-------------------------

Lumak | 2017-11-23 16:33:56 UTC | #16

Should just start with static stretch and onto dynamic once you got static working. This might help you get started: https://github.com/GarageGames/Torque3D/blob/development/Engine/source/gfx/gfxDrawUtil.cpp#L353

edit: I was looking for the 9-patch source code but couldn't find it, and instead, found the drawBitmapStretch fn linked above. I have no idea if that's what you're looking for or whether it actually works because I just found the function while browsing and it sounded like it's something that you're looking to do.

-------------------------

ricab | 2017-11-23 18:29:44 UTC | #17

OK, thanks. I'll need to find some quality time to look at this properly, but the algorithmic part of it is clearer in my mind, at least in the `Drawable2D` component approach I mentioned. Still not perfectly sure about the wisdom of such a design though...

Let's say we do `class StretchableSprite2D : public Drawable2D`. Note the following implications:

* the feature would be limited to 2D -- due to separation between Renderer and Renderer2D, using `StretchableSprite2D` in 3D would be convoluted at best
* no easy way to do regular scale -- the component could provide additional API, like `ActivateNormalScale(bool)` or something, but doesn't sound very elegant
* has the potential to break client expectations -- someone who scales a node might expect internal similarity to be maintained. For instance, today you can work at any scale as long as everything is scaled by the same amount (ignoring precision issues); with stretchable sprites, that would no longer be true (different aspect at different scales).

-------------------------

Lumak | 2017-11-23 19:10:10 UTC | #18

It might be more versatile if you have a function, such as:
[code]
void SetBitmapAutoScaleFactor(const Vector2 &scaleFactor)
{
   autoScaleFactor_ = scaleFactor;
}
[/code]

and say that the auto-scaling required to scale must be whole value:
[code]
IntVector2 newUnitScale = node_->GetWorldScale() * autoScaleFactor_; // don't know if world scale returns float or vec3

if (newUnitScale.x_ != unitScale_.x_)
  ** scale bitmap
[/code]

-------------------------

ricab | 2017-11-23 23:19:09 UTC | #19

Right, so basically providing a way to set the *intrinsic* scale in the sprite directly, correct? I agree that would be a natural way to address the second item above.

-------------------------

Lumak | 2017-11-24 15:09:28 UTC | #20

Oh, I thought specifying the limitations of the other bullet list item was actually a solution. But, let's bounce off some ideas.

*I'm going to imagine that this feature is targeted to something akin to a builder-kit and will reference examples from such.*

> the feature would be limited to 2D – due to separation between Renderer and Renderer2D, using StretchableSprite2D in 3D would be convoluted at best

I agree the 2D texture stretching cannot be applied to 3 dimensions.  But this might be circumvented by how your 3D model is UV mapped. Imagine a wall structure for a building: 10x5x1 (WxHxD). You can uv map the model in a such way that all 9-patches are covered by WxH, but the Depths skip the center patch and only map the edges of the patch.  And by limiting the scaling to only WxH, I imagine it'd look pretty good and not convoluted.

[quote]
has the potential to break client expectations – someone who scales a node might expect internal similarity to be maintained. For instance, today you can work at any scale as long as everything is scaled by the same amount (ignoring precision issues); with stretchable sprites, that would no longer be true (different aspect at different scales).
[/quote]

Same as before. Certain 3D model templates would have restriction on which axis it can be scaled.  But isn't it true that the purpose of the 9-patch image is designed so that when stretched, it'd still look ok?

-------------------------

ricab | 2017-11-28 00:31:12 UTC | #21

Sorry for the delay. Right, all that you say makes sense. I am basically trying to anticipate possible criticism to find an approach that sounds sensible to other people.

You see, for my particular purposes I could cut corners (probably just wrap 9 nodes in a class, with a static sprite each, and scale the central ones as needed). But I would like to contribute something more general back, so better to bounce some ideas as you say and then start on the right track :slight_smile:

-------------------------

