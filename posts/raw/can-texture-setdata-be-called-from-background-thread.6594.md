najak3d | 2020-12-03 23:26:15 UTC | #1

We have a map application which loads Map Tiles 512x512 pixel on demand.   We load from disk on a background thread, but then Urho seems to demand that we do the "Texture.SetData(...)" on the Urho Update thread, which means that times spent on this method interrupts the Frame rate.

We load up to 20 tiles at once.   When the user zooms out, we actually load NEW LOWER REZ tiles to fill in the space.   However, while those new tiles are loading, the user is stuck viewing the previous higher rez tiles.   If we don't have LOD's for these tiles, then the user sees "dither" (where pixels flicker madly because the image it's trying to render is too high resolution, and LODS are needed).

So to resolve this, we load the tiles with 3 LODs and that gets rid of the dither.

However, loading 3 LOD's takes 1.2 msec per tile (on a PC, will be slower on mobile devices).  But if we only set 1 LOD (using SetData(x, y, fmt, (void*)dataPointer), it only takes 0.33 msec per tile (almost 4x faster).

20 tiles x 1.2 msec = 24 msec (on a PC).   For mobile devices, we expect this might be much slower (e.g. 3 msec/tile == 60 msec for 20 tiles).   And so this may cause a rendering hiccup, as we call "Texture.SetData()" for 3 LODs.

===
Is there a way to call "Texture.SetData()" on a background thread without crashing Urho?  (when we've tried this, it often results in sporadic application crashes, sudden)   If we can call SetData on the background thread, safely, then we don't have to be concerned about the rendering hiccup.

Our code looks like this:

_textture.SetNumLevels(3);
.....
IntPtr pixelPtr = {points to the pixel buffer}
Urho.Resources.Image img2 = Tile._cache.UtilityImage;  // we re-use this Image for each tile
img2.SetData((byte*)pixelPtr);  // First we send the Pixel Buffer to the Image.  Takes about 0.3 msec
_texture.SetData(img2, false);  /// then we send the Image to the Texture.  This step takes the longest.  Takes about 1 msec

-------------------------

Eugene | 2020-12-04 08:35:36 UTC | #2

TL;DR: No, you cannot and it's quite hard to change.

Longer answer: Unless you create multiple GAPI contexts, you cannot work with GAPI from different threads. You _probably tecnhincally_ can manage multiple contexts and write GPU resource from background thread while using main thread, assuming you don't read and write resource simultaneously from different threads, your platform and GAPI support this stuff and you don't encounter any driver bugs on the way.

The most common solution is to write data chunk by chunk: instead of uploading whole resource do it for small enough region. Bigger engines like Unity do it under the hood and have settings like "main thread resource upload quota". Urho does not implement it on its own, but it's not impossible.

I assume that you have this function exposed in C#:
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Texture2D.h#L65
If you don't... Well, my condolences.

-------------------------

najak3d | 2020-12-04 08:36:37 UTC | #3

Thanks Eugene.   We're probably just going to limit the amount of Data Transfer per frame, and handle it that way.

-------------------------

