Elendil | 2019-09-17 18:48:14 UTC | #1

I obtain Data from another renderer as unsigned char * Data and I create Texture and display it. Problem is, colors are not ok, blue text is red and green is blue.

Here is my code how I create texture

    void WG::WGUI::mf_GetRender(unsigned char *& data, double width, double height)
    {
    	IntPtr pdata = static_cast<IntPtr>(data);
    	mainWindow->UserC->mf_RenderControl(width, height, pdata);
    }

---

    // Inside urho Start();

            image = new Urho3D::Image(context_);
    		double width = 1024;
    		double height = 512;
    		int RGBA = 4;
    		image->SetSize((int)width, (int)height, 4);
    		
    		DATA = (unsigned char *)malloc(width * height * RGBA);

    		WG::WGUI::wgui->mf_GetRender(DATA, width, height);
    		image->SetData(DATA);
    		
    		texture = new Urho3D::Texture2D(context_);
    		texture->SetFilterMode(Urho3D::TextureFilterMode::FILTER_BILINEAR);
    		texture->SetNumLevels(1);
    		texture->SetSize(image->GetWidth(), image->GetHeight(), Urho3D::Graphics::GetRGBAFormat(), Urho3D::TEXTURE_DYNAMIC);
    		texture->SetData(0, 0, 0, image->GetWidth(), image->GetHeight(), image->GetData());

    		Urho3D::Sprite * sprite = GetSubsystem<Urho3D::UI>()->GetRoot()->CreateChild<Urho3D::Sprite>();
    		sprite->SetTexture(texture);
    		sprite->SetSize(image->GetWidth(), image->GetHeight());
    		sprite->SetBlendMode(Urho3D::BlendMode::BLEND_ALPHA);

-------------------------

Teknologicus | 2019-09-17 04:55:24 UTC | #2

Just a guess, but the function mf_GetRender may be acquiring the RGB data in a different byte order for the RGB channels.  In such cases one can write code to swap the bytes to the correct order before calling image->SetData(DATA);

P.S.  The fact that the data pointer in the mf_GetRender function is cast to an int pointer means it's most likely a little-endian (https://en.wikipedia.org/wiki/Endianness) issue.  If you want the code to be cross platform, you'll need a endianess check and not run the byte swap (RGBA byte order reversal) code on big-endian architectures.

-------------------------

Leith | 2019-09-17 05:18:49 UTC | #3

Yep, this is a case of RGBA meets BGRA. Who knows, it could have been worse, ARGB. Still, you noticed a clean switching of colour channels, so the solution is simple. You know what to do, right?

-------------------------

Elendil | 2019-09-17 09:47:04 UTC | #4

Thanks, I am self taught programmer, I think I know what to do from your descriptions. I search for conversion from BGRA to RGBA and now it display right colors. (btw outside renderer make Pbgra32 pixel format)

            unsigned char* rgba = (unsigned char *)malloc(width * height * RGBA);

    		int w = (int)width;
    		for (int _y = (int)height - 1; _y >= 0; _y--)
    		{
    			for (int _x = 0; _x < w; _x++)
    			{
    				rgba[(_x + _y * w) * 4] = DATA[((_x + _y * w) * 4) + 2];
    				rgba[((_x + _y * w) * 4) + 1] = DATA[((_x + _y * w) * 4) + 1];
    				rgba[((_x + _y * w) * 4) + 2] = DATA[(_x + _y * w) * 4];
    				rgba[((_x + _y * w) * 4) + 3] = DATA[((_x + _y * w) * 4) + 3];
    			}
    		}
    		image->SetData(rgba);

code taken from https://stackoverflow.com/questions/15262855/bgra-rgba-and-vertical-flip-optix
now the question is, can Urho provide some conversion? I found method `ConvertToRGBA()` from Image class, but this does nothing.

-------------------------

Elendil | 2019-09-17 13:17:43 UTC | #5

I have problem with conversion code. It make arond 20 - 30 FPS down if I render it realtime. (without conversion code FPS is ok)
are there faster possibilities in conversion? If yes how?

-------------------------

Modanung | 2019-09-17 19:05:52 UTC | #6

[quote="Elendil, post:4, topic:5588"]
I found method `ConvertToRGBA()` from Image class, but this does nothing.
[/quote]

Did you look into its implementation, or `Urho3D/Resource/`[`Image.cpp`](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Resource/Image.cpp) in general?

[quote="Elendil, post:5, topic:5588"]
are there faster possibilities in conversion? If yes how?
[/quote]

Do you see no way to avoid conversion altogether?  Does WG not have conversion capabilities or options concerning color space?

-------------------------

Elendil | 2019-09-17 19:15:15 UTC | #7



[quote="Modanung, post:6, topic:5588"]
Did you look into its implementation, or `Urho3D/Resource/` [ `Image.cpp` ](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Resource/Image.cpp) in general?
[/quote]

Yes

[quote="Modanung, post:6, topic:5588"]
Do you see no way to avoid conversion altogether? Does WG not have conversion capabilities or options concerning color space?
[/quote]
Unforunately no. And if conversion capabilities are there, I don't think it will be faster because it is managed code. But I wonder how fast it is without conversion, but I tested it with only simple graphics.

-------------------------

Teknologicus | 2019-09-18 12:21:58 UTC | #8

With all due respect, that code from Stackoverflow looks overly computational intensive for the task with all the those variables being accessed, adds and multiplies.  One should be able to do this and achieve the same thing with much fewer machine instructions generated by the compiler and much better performance:

    #include <stdint.h>
    ...
    uint32_t *ptr = (uint32_t*)DATA;
    int size = width * height / sizeof(uint32_t);
    for (int i = 0; i < size; ++i) {
        uint32_t pixel = ptr[i];
        rgba[i    ] = pixel >> 24;
        rgba[i + 1] = (pixel >> 16) & 0xFF;
        rgba[i + 2] = (pixel >> 8) & 0xFF;
        rgba[i + 3] = pixel & 0xFF;
    }
    ...

-------------------------

Elendil | 2019-09-18 13:39:18 UTC | #9

Thanks, but unfotunately it make this (see picture).
And i forgot add discoverty that renderer which make pixel data, his format is Pbgra32 (*Each color channel is pre-multiplied by the alpha value*)
![urhoArtifacts|690x355](upload://2WMQgX1T4TexjLydAXhCq7gpicT.jpeg)

-------------------------

Teknologicus | 2019-09-18 13:47:18 UTC | #10

Try:

    ...
        rgba[i    ] = (pixel >> 16) & 0xFF;
        rgba[i + 1] = (pixel >> 8) & 0xFF;
        rgba[i + 2] = pixel & 0xFF;
        rgba[i + 3] = pixel >> 24;
    ...

-------------------------

Teknologicus | 2019-09-18 14:05:01 UTC | #11

I just realized there's a pointer arithmetic error in the code.  This should correct that:

    #include <stdint.h>
    ...
    uint32_t *ptr = (uint32_t*)DATA;
    int size = width * height / sizeof(uint32_t);
    for (int i = 0; i < size; ++i) {
        uint32_t pixel = ptr[i];
        int j = i * sizeof(uint32_t);
        rgba[j    ] = pixel & 0xFF;
        rgba[j + 1] = (pixel >> 16) & 0xFF;
        rgba[j + 2] = (pixel >> 8) & 0xFF;
        rgba[j + 3] = pixel >> 24;
    }
...

-------------------------

Elendil | 2019-09-18 14:39:31 UTC | #12

Unfortunately it not working, it does something but text on buttons is transparent.

btw this is working after I edit it to this. But it not convert colors

    unsigned char *ptr = (unsigned char *)DATA;
		int size = width * height * 4; // / sizeof(uint32_t);
		for (int i = 0; i < size; ++i) {
			uint32_t pixel = (uint32_t)ptr[i];
			rgba[i] = pixel >> 32;
			rgba[i + 1] = (pixel >> 16) & 0xFF;
			rgba[i + 2] = (pixel >> 8) & 0xFF;
			rgba[i ] = pixel & 0xFF;
		}

---

Aha you edit code little bit. Your last code working with conversion but it not convert all image
![urhoArtifacts2|690x359](upload://5zMIVCm75WYppnM5vhneANV9JYY.jpeg)

-------------------------

Elendil | 2019-09-18 15:00:11 UTC | #13

This is working

    uint32_t *ptr = (uint32_t*)DATA;
		int size = width * height; // / sizeof(uint32_t);
		for (int i = 0; i < size; ++i) {
			uint32_t pixel = ptr[i];
			int j = i * sizeof(uint32_t);

			rgba[j] = (pixel >> 16) & 0xFF;
			rgba[j + 1] = (pixel >> 8) & 0xFF;
			rgba[j + 2] = pixel & 0xFF;
			rgba[j + 3] = pixel >> 24;
		}

but speed is not much increased. Around + 5 or 10  FPS
Anyway thanks for help.

![urhoNGFINISH|690x362](upload://mxFow97muU3WIImraQ622G6xNVU.jpeg)

-------------------------

Pencheff | 2019-09-18 15:09:13 UTC | #14

It is faster if you directly copy data to your texture without swapping or allocating data when you copy.
Asuming you are using DirectX9, you can try this:
[code]
void SetTextureData(Texture2D* texture, int width, int height, int stride, char* data) {
  RECT d3dRect;
  int srcStride = stride;

  d3dRect.left = 0;
  d3dRect.top = 0;
  d3dRect.right = width;
  d3dRect.bottom = height;

  int level = 0;
  DWORD flags = D3DLOCK_DISCARD;

  D3DLOCKED_RECT d3dLockedRect;
  IDirect3DTexture9* object = (IDirect3DTexture9*)texture->GetGPUObject();

  if (!object || FAILED(object->LockRect(level, &d3dLockedRect, (flags & D3DLOCK_DISCARD) ? 0 : &d3dRect, flags)))
    return;

  for (int j = 0; j < height; ++j) {
    unsigned char* dst = (unsigned char*)d3dLockedRect.pBits + j * d3dLockedRect.Pitch;
    memcpy(dst, data, stride);
    data += stride;
  }

  object->UnlockRect(level);
}
[/code]

**NOTE**: Don't forget to set the correct stride (usually width * 4).
I use this for rendering video and CEF browser, there are also versions for OpenGL and DirectX11.

Other technique you can use is reorder colors in the pixel shader, it will be faster than conversion in CPU.

-------------------------

Elendil | 2019-09-18 15:51:49 UTC | #15

Thanks, this looks interesting, unfortunately I use DX11 and I have no experience in it.

-------------------------

Pencheff | 2019-09-18 16:53:52 UTC | #16

In DirectX11 with Urho3D:
[code]
void SetTextureData(Texture2D* texture, int width, int height, int stride, char* data) {
  D3D11_BOX box;
  box.left = 0;
  box.right = width;
  box.top = 0;
  box.bottom = height;
  box.front = 0;
  box.back = 1;

  graphics_->GetImpl()->GetDeviceContext()->UpdateSubresource((ID3D11Resource*)texture_->GetGPUObject(), 0, &box, data, stride, 0);
}
[/code]

-------------------------

Elendil | 2019-09-19 10:34:15 UTC | #17

Thanks, but this is not working for me. Maybe I don't know how to use this function, because when I check Urho source, it looks like virtual function wait for declaration (I am not able find declaration of this function UpdateSubresource( ... )).

-------------------------

Modanung | 2019-09-19 16:01:55 UTC | #18

Maybe try this:
```
#include <d3d11.h>
```

Somewhat of a wild guess.

-------------------------

Elendil | 2019-09-19 17:31:50 UTC | #19

Without that I am unable compile a project. Therefore this is most basic thing.
When I use this function it does nothing. It means if I use it, it doesnt set data in to texture and it doesnt convert DATA to RGBA.

-------------------------

