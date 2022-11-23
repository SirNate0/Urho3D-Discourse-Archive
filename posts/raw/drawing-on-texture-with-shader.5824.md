Taqer | 2020-01-19 15:20:07 UTC | #1

Hi :smiley:

I wanted to speed up my fog of war code and get it from c++ side to shader code, which is really like drawing alpha on texture. But I have one problem: I can't really permanently draw on texture, it's like on every frame shader resets texture and I can only see something in one frame:
[Video](https://cdn.discordapp.com/attachments/668069542085525507/668248857917915136/2020-01-19_01-06-21.mp4)

Im using DiffAlpha technique. My shader code is just modification of LitSolid with added:
```
	if(diffColor.a > 0.01) //check if that part wasn't cleared yet
{
	//if not, then get square of distances
	float dX = cUnitPos.x - vTexCoord.x;
	float dY = cUnitPos.y - vTexCoord.y;
	float sqrD = dX*dX+dY*dY;
	
	float sqrR = 0.01;
	float sqrR2 = 0.02;
	
	//if square is smaller than first radius clear fully
	if(sqrD < sqrR)
	{
		diffColor.a = 0;
	}
	else if(sqrD < sqrR2) //otherwise if square is smaller than second radius clear partly
	{
		diffColor.a = (sqrD - sqrR)/(sqrR2 - sqrR);
		diffColor.a = diffColor.a + ((rand(vTexCoord) / 4.0) * diffColor.a);
	}
}
```
I have 1 uniform parameter that describes unit position in current frame. First radius describes range of full clear, second describes partly clear + Im adding some randomity.	

From c++ side Im only updating cUnitPos with current mouse position.

-------------------------

Modanung | 2020-01-19 15:26:39 UTC | #2

It does not seem to me like you're _writing_ to a texture at all, but rather setting each fragment's alpha value. Maybe this topic can help you:
https://discourse.urho3d.io/t/dynamically-change-texture-or-paint-on-texture/2372

-------------------------

Taqer | 2020-01-19 15:38:25 UTC | #3

Thanks for reply!

This is actually my old way of doing this... On c++ side, but I want to have this in shader because using only CPU is very slow.

Is it even possible to change texture from shader? :frowning:

-------------------------

Modanung | 2020-01-19 15:56:05 UTC | #4

I'm not sure, but for some reason I doubt it given the notion of a graphics _pipeline_. What happens in the shader occurs further down the line as where textures are prepared, I think.
Someone else may be able to confirm or refute this somewhat baseless claim.

-------------------------

Modanung | 2020-01-19 16:05:11 UTC | #5

Are you taking these words from the other topic into account, btw?
[quote="cadaver, post:2, topic:2372, full:true"]
See Texture2D::SetData(), the overload which takes x,y,width,height parameters allows to set new data partially if you need that. [...] If you update the texture frequently (every frame) it’s best to create as dynamic.
[/quote]

[quote="victor, post:3, topic:2372, full:true"]
`// As cadaver suggested, it's best to set partial data and not do it this way... But this is just an example.`
`texture_->SetData(textureImage_);`
[/quote]

-----

Maybe you could have two textures - a latest and one from the previous "tick" - and crossfade them so you can lower the update frequency of the texture while still having smooth results.

-------------------------

Taqer | 2020-01-19 16:15:50 UTC | #6

I don't know how could I do this, I remove alpha only when units move, the problem is that in higher resolutions many pixels need to be checked, on 1024x1024 its 25600 pixels to check square distance (I check only a square of fog, that unit can see), and then set pixels alpha to appropriate value, and finally swap texture. That lags my game with every move of unit, so I'm stucked with 512x512 which is smooth yet.

-------------------------

Modanung | 2020-01-19 16:52:20 UTC | #7

It would probably be faster to draw another texture (similar to the Spot.png, included with the engine) on the fog map than to  pixel by pixel calculate a circle each frame.
Of course the texture could be generated at run time, but storing it as such should save some CPU.

-------------------------

SirNate0 | 2020-01-19 19:06:29 UTC | #8

If you want to go with updating the texture what I would do is use a texture render target (like the render to texture example) with a render path that does not clear the texture. Clear it once at the beginning, and then after that the only updates are adding/subtracting based on billboards or the like at each of your units (depending on whether 1 or 0 represents fog). This should allow you to relatively easily get your inner and outer radius fading by changing what texture you use as the particle "brush." (I believe the is basically the approach Modanung is suggesting in his latest reply)

-------------------------

Modanung | 2020-01-19 19:32:52 UTC | #9

Similar but not identical to what I had in mind. I think my suggestion is closer to what @Taqer already has, whereas thine approach, @SirNate0, would be a more high-level minimap-like solution using existing building blocks. My suggestion did not mean to diverge from the `SetData(...)` part.

-------------------------

