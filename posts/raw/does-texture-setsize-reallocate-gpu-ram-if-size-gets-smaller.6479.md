najak3d | 2020-10-30 19:56:22 UTC | #1

Most of our App renders dynamically created textures and meshes. 

Currently we've modified our Raster map rendering shader to incorporate the "Height Map", so that it can highlight various parts of the raster map because on contour lines.

The issue we have is that our raster tiles are not aligned to our height map (and can't be).  Each part of the world employs slightly different tile sizes (due to Mercator projection math).

Therefore, dynamically, we're calling two methods repeatedly on the same "heightmap" texture.

_elevTexture.SetSize(newSize....)
_elevTexture.SetData(newdata...)

If SetSize changes the #pixels by a few pixels (e.g. from 200x200 to 199x198), what happens in GPU memory (or CPU RAM)?  Does it keep the previous memory allocation for the 200x200, and simply make it work as a 199x198?  (wasting the extra pixels)...   Or does it discard the 200x200 texture allocation and allocate a whole new block sized at 199x198?

We hope it's not re-allocating the whole texture in GPU RAM unless the SetSize *increases* the size required (above the last Maximum).    

If it re-allocates all new GPU RAM each time for the resized texture (even if shrunk), then we're going to instead create our own "larger than needed texture" to start with, and then just set up the UV coordinates to ignore the unused pixels.

-------------------------

Eugene | 2020-10-30 20:56:34 UTC | #2

There is no such thing as "texture working area" for GPU.
GPU always maps allocated texture dimensions onto 0-1 UV range in shader, unconditionally.
So, Urho has no way to reuse bigger texture when you request smaller one -- there's no way to separate valid data from invalid padding.

However, you can implement it as user if you adjust UV properly in your shader

-------------------------

najak3d | 2020-10-30 23:09:40 UTC | #3

Eugene, thanks!  To make sure you understand my question,  what does the following code do:

_texture.SetSize(200, 200 size....)
_texture.SetSize(199, 198 size...)

Does this cause any issues with GPU RAM thrashing for that texture (does it end up doing two allocations)?

-------------------------

Eugene | 2020-11-01 00:19:41 UTC | #4

Yes, Urho will allocate new texture after each size change, due to inability of “partial use” on GPU side.

-------------------------

najak3d | 2020-10-31 00:41:38 UTC | #5

Thanks!   Then we'll just hard code the size to largest size, and dynamically set the UV coordinates to make it only use the portion of the texture that has data.

-------------------------

najak3d | 2020-10-31 18:56:16 UTC | #6

Just to confirm one more thing.   I assume that Texture.SetData(....) does NOT create an new texture, but simply overwrites the old texture data with new data, "in place".  (No memory allocation/deallocation thrashing.)

Our scheme is to have a single RAM memory block to where we write our Pixel data for the texture, and once complete, we call Texture.SetData(...) so that this data is transmitted to the GPU.

Our assumption is that since we have consistent buffer sizes from start to finish, we are doing one allocation up front, and then re-using from then on.

-------------------------

Eugene | 2020-11-01 00:19:41 UTC | #7

SetData doesn’t do any reallocation, only data copy.

-------------------------

