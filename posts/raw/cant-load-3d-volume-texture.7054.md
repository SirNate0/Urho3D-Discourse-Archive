GodMan | 2021-11-14 00:02:41 UTC | #1

So I am working a water shader. I am using a noise texture that is straight from DirectX media. I set my texture xml file, and link that to the .dds texture. 

In the console window I see. Unsupported dds pixel byte size. The texture loads fine in other 3d applications. 

NoiseVolume.xml

```
<texture3d>
    <volume name="NoiseVolume.dds" />
	<mipmap enable="false" />
    <quality low="0" />
</texture3d>
```
Am I overlooking something?

-------------------------

Eugene | 2021-11-14 07:15:03 UTC | #2

What is the format of your DDS texture?

-------------------------

GodMan | 2021-11-14 18:17:10 UTC | #3

Compressed DXT3 8 bit L8 128 x 128 x128

According to AMD tool.

-------------------------

Eugene | 2021-11-15 09:18:41 UTC | #4

[quote="GodMan, post:1, topic:7054"]
Unsupported dds pixel byte size
[/quote]

Image can be extended [here](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Resource/Image.cpp#L502) and [here](https://github.com/urho3d/Urho3D/blob/f861a10a61c473b16b941df96db20d514862f87c/Source/Urho3D/Resource/Image.cpp#L338) to support 8-bit images. Or you can just use anything but 8-bit images.

-------------------------

GodMan | 2021-11-15 16:43:40 UTC | #5

okay thanks @Eugene. I could just find some 3D volume textures that are not 8 bit like you suggested. I just can't find anything using Google.

-------------------------

