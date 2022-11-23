sabotage3d | 2017-01-02 01:07:22 UTC | #1

Hi, 
I I couldn't find in the documentation what are the supported texture compressions for Mobile. In older post it was mentioned that Urho3D is using stb_image but its a bit vague in terms of supported compressions. Where should we start if we want to add additional compressions like ASTC ? There is a also an open-source encoder and decoder for ASTC : [github.com/ARM-software/astc-encoder](https://github.com/ARM-software/astc-encoder) . In general I don't have a lot of experience with textures for mobile. If anyone can recommend me what would be the best compression to use would be great.

-------------------------

cadaver | 2017-01-02 01:07:23 UTC | #2

Mobile compressed texture loading bypasses stb_image and handles the formats directly. From the documentation:

"ETC1 (Android) and PVRTC (iOS) compressed textures are supported through the .ktx and .pvr file formats."

The tools you may find that are able to generate these files may be sucky, so your mileage may vary.

If you want to support additional formats, just start hacking the Image.h / Image.cpp files.

-------------------------

sabotage3d | 2017-01-02 01:07:23 UTC | #3

Thank you very much cadaver. Would you recommend ASTC as the best from both worlds ?

-------------------------

cadaver | 2017-01-02 01:07:23 UTC | #4

It's probably quite well covered by recent Android devices. I couldn't get a clear answer of the iOS devices that support it, but not all do.

-------------------------

jmiller | 2017-01-02 01:07:23 UTC | #5

Just to throw in some references..

PNG/PVR comparison (slightly older)
[stackoverflow.com/questions/5019 ... -opengl-es](http://stackoverflow.com/questions/501956/pvr-textures-versus-png-in-opengl-es)

Not a recommendation for PNG in your scenario but FYI: they can be compressed significantly more than imaging apps like GIMP do (maybe 10%, depends) using a utility like PNGOUT. It's available for Linux/Win/Mac - [advsys.net/ken/utils.htm](http://advsys.net/ken/utils.htm) - and as a plugin for [url=http://www.irfanview.com/]IrfanView[/url] (MSWin). Of course as important, you'd want to select optimal bit depths.

-------------------------

rasteron | 2017-01-02 01:07:24 UTC | #6

[quote="carnalis"]
Not a recommendation for PNG in your scenario but FYI: they can be compressed significantly more than imaging apps like GIMP do (maybe 10%, depends) using a utility like PNGOUT. It's available for Linux/Win/Mac - [advsys.net/ken/utils.htm](http://advsys.net/ken/utils.htm) - and as a plugin for [url=http://www.irfanview.com/]IrfanView[/url] (MSWin). Of course as important, you'd want to select optimal bit depths.[/quote]

I use PNGGauntlet (Windows) for PNG compression. It combines PNGOUT, OptiPNG, and DeflOpt to create the smallest PNGs..

[pnggauntlet.com/](http://pnggauntlet.com/)

-------------------------

