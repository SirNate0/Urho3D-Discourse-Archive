Lys0gen | 2021-12-15 20:32:37 UTC | #1

Hello,

I am trying to symbolize the relationships between UI elements with some lines.

These lines might be rotated, which necessitates using Urho3D::Sprite elements. I create a Sprite element with the required line width and stretch the texture onto that.
For a "simple" (uniformly colored) line this works perfectly fine.

Now I want to display a different kind of relationship where there is transparency dividing the line continously.

But I just can't get it to wrap the texture properly, instead it always stretches it. I have tried playing around with Sprite->GetTexture()->SetAddressMode(..) and setting U (and V) to Urho3D::TextureAddressMode::ADDRESS_WRAP but it is still stretched.

Here is a visualisation, the horizontal "line" is the problem:

![texwrap|266x500](upload://dlStmUSQpkIB1I5OepwxyR5KxVs.png)

It was strange that the texture is just cut off without BLEND_ALPHA mode. Just like how the colors are somehow different from the actual texture, but both those things are not much of an issue.

But now I am kind of stuck with the stretched texture, and it should somehow be possible to get it to wrap properly?

The only relevant topic I had found is [this](https://discourse.urho3d.io/t/how-to-make-the-texture-image-of-a-2d-sprite-repeat-to-fill-a-rectangle/3980) but that does refer to "regular" sprites, not UI sprites I guess.

Anyone know what the problem might be?

-------------------------

SirNate0 | 2021-12-16 03:06:06 UTC | #2

I don't do much with Urho's UI, so this is just a guess, but I think the issue is that you need to get the UI to use UV coordinates larger than 0-1 for your repeating-line sprite. I think, though I'm not sure, that you might be able to get it to do that using `SetImageRect` with a rectangle larger than the size of the texture.

-------------------------

Lys0gen | 2021-12-16 03:28:29 UTC | #3

Ah yes of course! That fixed it, thanks a ton.

-------------------------

