najak3d | 2020-12-23 21:26:04 UTC | #1

This code works fine on Windows.  But for Android, it does not work if I have multiple LOD's:

Here's the code that creates the Texture and sets NumLevels to 3:
_texture = new Texture2D(_cache.AppContext.UrhoContext);
_texture.SetNumLevels(3);
UrhoUtil.TextureSetSize(_texture, TILE_IMAGESIZE, TILE_IMAGESIZE, ImgFormat, TxtUsage.Static);

Here's the code that sets the Texture Data to an UrhoImage.   On Windows, this works fine, and sets all of the LODs:

Urho.Resources.Image img2 = Tile._cache.UtilityImage;
_texture.SetData(img2, false);

===
The end result on Android is that my PixelShader TextureSampler returns "opaque Black" for every pixel.

To fix the "black pixel" issue, all I have to do is change NumLevels to "1" (instead of 3).

_texture.SetNumLevels(1);

But now I only have 1 LOD and when you zoom out, it shows the flickering/dither effect, which looks horrible.

Is this a known bug, and is there a good work around?   I need 3 LOD's to function on Android too.

-------------------------

Eugene | 2020-12-23 23:11:27 UTC | #2

On GLES you must either have all the LODs or one, you can't just have "some".

-------------------------

najak3d | 2020-12-23 23:13:00 UTC | #3

Eugene, THANK YOU!..   That worked for me.  If I just omit "SetNumLevels(...)" and use the default, it works just fine.

-------------------------

