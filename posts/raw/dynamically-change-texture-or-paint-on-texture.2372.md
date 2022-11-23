Marcin | 2017-01-02 01:15:01 UTC | #1

Hi,
How to dynamically change texture of object or paint on texture? I have a box with texture on all faces, but one face has a texture that looks like a colored height map. I would like to dynamically change colors of this texture, as if appeared new "valleys" and "mountains" on the colored height map. What is the best way to do it?
Thanks in advance.

-------------------------

cadaver | 2017-01-02 01:15:01 UTC | #2

See Texture2D::SetData(), the overload which takes x,y,width,height parameters allows to set new data partially if you need that. Note that if your texture has mips, you will have to update all mips so that the texture looks correct from all distances.

If you update the texture frequently (every frame) it's best to create as dynamic.

-------------------------

Victor | 2017-01-02 01:15:01 UTC | #3

Going off of what cadaver said, making sure you have it set to dynamic is really good, however it did take me a while to figure out where to set that at. Here's some code that may help:

[code]
// Note the TEXTURE_DYNAMIC
texture_->SetSize(heightmapImg_->GetWidth(), heightmapImg_->GetHeight(), Graphics::GetRGBAFormat(), TEXTURE_DYNAMIC);

// As cadaver suggested, it's best to set partial data and not do it this way... But this is just an example.
texture_->SetData(textureImage_);
[/code]

You can use the SetPixel/GetPixel methods of the image to set the color based on the 0-255 value you get from the heightmap.

[code]
Color pixel = textureImage_->GetPixel(x, y)
if (pixel.r_ > 200) { textureImage_->SetPixel(x, y, Color::WHITE) }
[/code]

Example here:
[i.imgur.com/nPgqaYq.png](http://i.imgur.com/nPgqaYq.png)

-------------------------

Marcin | 2017-01-02 01:15:09 UTC | #4

Thanks! It works ok. 
In the examples I've seen use a displacement map with component "Terrain". Is it just this object (Terrain) can be deform using the displacement map? Or can I import from Blender any object with a dense mesh and deform it?

-------------------------

cadaver | 2017-01-02 01:15:09 UTC | #5

Terrain reads heightmap from the image and constructs the geometry programmatically. In contrast StaticModel et al. just display the geometry according to the model resource they've been assigned, so displacing them doesn't work similarly out of the box. I suppose you could do displacement on any geometry with customized shaders, though.

-------------------------

namic | 2017-01-02 01:15:10 UTC | #6

How do you get the mouse point position and transform into a 3D position?

-------------------------

Victor | 2017-01-02 01:15:11 UTC | #7

[quote="namic"]How do you get the mouse point position and transform into a 3D position?[/quote]

The sample project for Urho dealing with Navigation may be of some help to you:
[github.com/urho3d/Urho3D/blob/m ... n.cpp#L356](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/15_Navigation/Navigation.cpp#L356)

-------------------------

