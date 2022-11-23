ricab | 2017-12-13 00:28:46 UTC | #1

Following the discussion [here](https://discourse.urho3d.io/t/stretchable-sprites-images-aka-9-patch-or-9-slice/2805) I had a go at _stretchable sprites_. 

Here is an example that shows a regular `StaticSprite2D` (left) and a `StretchableSprite2D` (right). The latter handles scaling differently: it tries to leave the borders untouched, scaling only the "inside", if possible. When the scale goes below the border size, the "inside" is completely removed and the borders are scaled instead. Negative scales are also handled the same way.

Note that this is done on X and Y axis independently, so there are "different levels" of "inside" and "borders". 

![stretch_example_optimized2|643x500](upload://n1bHsyEpgUQm2fNH2NQq9XsCaVi.gif)

Just like `BorderImage`, a `StretchableSprite2D` is specified with 4 independent borders (left, top, right, bottom), so it can be asymmetric on both axis. Each border is specified as an integer corresponding to the number of pixels from the edge (>= 0).

I implemented this `StretchableSprite2D` type by inheriting from `StaticSprite2D` and overriding `UpdateSourceBatches`, to render it as a set of 4, 6, or 9 square patches:

- 9 patches if both X and Y scales determine a size that is larger than the border size
- 6 patches if either X or Y scales (but not both) determine a size that is below the corresponding border size (left+right or top+bottom)
- 4 patches if both are below border size

Inheriting `StaticSprite2D`'s interface means dealing with a bunch of special cases though (e.g. manual draw rect, hotspot, spritesheets, flips). These can be combined in many ways that I still didn't have the chance to test. Some hands on testing would be greatly appreciated. I hope to have a PR coming soon.

-------------------------

ricab | 2017-12-13 00:30:28 UTC | #2

I wonder if there is something that could be done about the way the inside is _dissolved_ when approaching the threshold, but the same happens to the left image, only later, because it has more space before it gets crammed. I suppose it is just an unavoidable consequence of scaling a lot of information into very few pixels.

-------------------------

SirNate0 | 2017-12-13 02:51:23 UTC | #3

Are you talking about this effect (the horizontal rectangle with blurred colors on the right sprite) when you say the "way the inside is *dissolved*"? To me, it looks kind of like the texture coordinates are set up wrong on the middle part at this point, though I can't say this for certain. Perhaps also using a different filtering on the texture would help here, as it is downsizing the texture at that point, but I'm really not familiar with these things.
![1s|643x500](upload://tuA0t1ehgWsYFqNUZumaNbyz49G.gif)

-------------------------

ricab | 2017-12-13 03:19:24 UTC | #4

> Are you talking about this effect

Yes, that is exactly what I meant.

> To me, it looks kind of like the texture coordinates are set up wrong on the middle part at this point

It looks like it at first, but I don't think that is it. It is just that a lot of "pixels" are crammed into a tight space and in the uv mapping somehow neighbour pixels seem to get more weight in the blend in. Notice that, _when the left sprite is scaled to a size that is comparable to the middle part of the right sprite, the same thing happens to it_. It is harder to see because it is not next to an intact part of the sprite to contrast with, but I think it is the same.

> Perhaps also using a different filtering on the texture would help here

I hope so, but that is also beyond me ATM.

-------------------------

ricab | 2017-12-13 03:16:59 UTC | #5

Here is what I mean

![cramm_stretch|643x500](upload://oqrRapKQtQGHCoXDIPnAvKrycCB.gif)

Maybe a better approach would be to cut when scaling down and repeating when scaling up...

-------------------------

Eugene | 2017-12-13 09:02:28 UTC | #6

IMO it could be fixed with smaller inner image area. Maybe anisotropy filtering. It's not a problem of stretchable sprite.

-------------------------

johnnycable | 2017-12-13 09:21:01 UTC | #7

I guess @Eugene is right. It is common to have bleeding in UV mapping sometimes.
Possibly setting up a "margin" value to texture mapping could solve the issue... anyway just guessing...

-------------------------

ricab | 2017-12-13 15:45:46 UTC | #8

> smaller inner image area

Do you mean cutting the inner part, rather than scaling it? 

I though of that, but I am not so sure: currently the inside can be heterogeneous in the chosen axis (e.g. gradient) and I don't think it is worth restricting that.

> Maybe anisotropy filtering

Not sure how to do that... For now I want to get the current hacked code into a reasonable state to submit. Perhaps then people can play with it and hopefully someone will find a way to improve it. 

Meanwhile, I suppose the client should just take this "dissolving" effect into account (just as with normal sprites).

-------------------------

ricab | 2017-12-13 15:48:28 UTC | #9

> Possibly setting up a “margin” value to texture mapping

Sorry, I don't follow. What do you mean?

-------------------------

johnnycable | 2017-12-13 20:29:40 UTC | #10

I mean... could be an [edge padding](http://wiki.polycount.com/wiki/Edge_padding) issue...?

-------------------------

ricab | 2017-12-14 01:55:02 UTC | #11

Oh I see, very interesting. I don't know if that is what is happening here, but it does look something like the problem described there. 

I don't know, perhaps some padding outside could help with the borders a bit. On the other hand, the middle seam shows the same (or similar) problem and it has the rest of the image as padding, so I don't know.

-------------------------

SirNate0 | 2017-12-14 17:40:38 UTC | #12

Could it be a mipmapping issue, possibly?

-------------------------

ricab | 2017-12-22 01:03:15 UTC | #13

Sorry for the late reply. Indeed, disabling mipmapping fixes it!

-------------------------

ricab | 2017-12-22 03:50:50 UTC | #14

https://github.com/urho3d/Urho3D/pull/2214

-------------------------

