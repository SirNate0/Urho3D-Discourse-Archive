Bluemoon | 2017-01-02 00:59:21 UTC | #1

I'm really sorry if this question has been asked before, but what exactly are the image formats/compression supported by Urho3d.
I have a blender model I exported to .mdl but the texture for the model which is a jpg file fails to load when i try loading the model, leaving me with a black shape  :frowning: . The log message depicting the error is
 [code][Mon May 26 19:47:23 2014] ERROR: Could not load image Textures/DIFFUSE_Character.jpg: progressive jpeg[/code]

I even tried using the included Mushroom.dds texture as the models texture and it showed   :confused:  , next i took my image to GIMP and tried exporting to .dds with no compression level and it still failed to load. But on trying with compression level BC1 /DXT1 it loaded in Urho3D :smiley: . Now all these got me wondering, are there particular image format/compressions that are only supported? if there are then I will be so pleased if someone can list them out for me or at least direct me to where I can read them up.

-------------------------

cadaver | 2017-01-02 00:59:21 UTC | #2

For non-block compressed image loading, Urho uses the minimal image loader library STB_Image, which says the following in its header file:

[code]
      JPEG baseline (no JPEG progressive)
      PNG 8-bit only

      TGA (not sure what subset, if a subset)
      BMP non-1bpp, non-RLE
      PSD (composited view only, no extra channels)

      GIF (*comp always reports as 4-channel)
      HDR (radiance rgbE format)
      PIC (Softimage PIC)
[/code]
Block compressed images don't go through STB_Image, for those the DXT1/3/5 (inside DDS, PVR or KTX files) and PVRTC RGB/RGBA 2 or 4 bit (inside KTX or PVR files) compression modes are supported.

My basic recommendation is DDS for DXT1 or DXT5, and PNG for any non-block compressed images.

-------------------------

szamq | 2017-01-02 00:59:21 UTC | #3

I had same problem some time ago. It was jpg file downloaded from some website. I just opened this image in paint and saved again(overwrite) in jpg and then it worked. It looks like there are various types of jpg's and urho can import only the standard one.

-------------------------

Bluemoon | 2017-01-02 00:59:21 UTC | #4

[quote="cadaver"]For non-block compressed image loading, Urho uses the minimal image loader library STB_Image, which says the following in its header file:

[code]
      JPEG baseline (no JPEG progressive)
      PNG 8-bit only

      TGA (not sure what subset, if a subset)
      BMP non-1bpp, non-RLE
      PSD (composited view only, no extra channels)

      GIF (*comp always reports as 4-channel)
      HDR (radiance rgbE format)
      PIC (Softimage PIC)
[/code]
Block compressed images don't go through STB_Image, for those the DXT1/3/5 (inside DDS, PVR or KTX files) and PVRTC RGB/RGBA 2 or 4 bit (inside KTX or PVR files) compression modes are supported.

My basic recommendation is DDS for DXT1 or DXT5, and PNG for any non-block compressed images.[/quote]

 :smiley: Thanks alot for the information, that solved my problem.

-------------------------

