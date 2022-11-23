projector | 2017-11-20 09:47:18 UTC | #1

Urho3D supports KTX compressed image file,  I would like to ask if I can use ETC2 compressed format on ETC2 supported devices? Urho3D is currently using OpenGL ES2 for mobile platform, I'm not sure If it does affect the ETC2 compressed image format support.

-------------------------

jmiller | 2017-11-20 14:35:32 UTC | #2

Hello,

Looking into this, it is my impression that ETC2 format requires OpenGL ES 3, which Urho does not yet support.

Reference.dox says "ETC1 (Android) and PVRTC (iOS/tvOS) compressed textures are supported through the .ktx and .pvr file formats." and I do not see ETC2 here..  https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Resource/Decompress.cpp#L272

GLES3.1 may not be too far ahead. boberfly has mentioned a branch in the forum...

HTH

-------------------------

projector | 2017-11-20 16:23:59 UTC | #3

Thanks for your information and good to know that there is plan for to support GLES3.1.

As far as I know ETC2 is mandatory to be supported by OpenGL ES3 devices, not sure if we still can ETC2 compressed format if we run it on OpenGL ES3 devices with OpenGL ES2 API. I hope to use ETC2 in my coming project, majority of mobile devices that released within these 2-3 years support OpenGL ES3.

The code you linked contains ETC1 and PVRTC decompress functions, isn't the ETC/PVRTC compressed texture format should stay compressed in memory? Are those functions used fo decompress in case users run it on platforms that do not support the compressed format, for example loading PVRTC on Windows PC?

-------------------------

jmiller | 2017-11-20 18:01:06 UTC | #4

You're welcome!

I assume that ETC1/PVRTC/DXT textures do remain compressed in VRAM... at least, that was a primary reason to support them and I do not recall reports otherwise.

Maybe someone can elucidate, or a bit of trial or digging in source.. :)

-------------------------

projector | 2017-11-21 03:13:33 UTC | #5

I have just tested to load ETC2 image with Urho, it printed error "Unsupported texture format in KTX file".

looking at image.h, looks like ETC2 compressed format is not defined
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Resource/Image.h

-------------------------

projector | 2017-11-21 09:17:59 UTC | #6

I have tried to get opengl es extension list with Urho running in ES3 capable mobile devices, it could not find the ETC2 extension, it is pretty clearly that ETC2 is not supported in OpenGL ES2 context regardless running in OpenGL ES3 capable devices. 

looks like the only option to use ETC2 is to switch to OpenGL ES3. ETC2 is the only compressed format that is widely supported nowadays by both iOS and Android devices, I hope to use it in my project.

What is the status of ES3 implementation in Urho?

-------------------------

Eugene | 2017-11-21 09:42:20 UTC | #7

[quote="projector, post:6, topic:3762"]
What is the status of ES3 implementation in Urho?
[/quote]

If you want to have some feature, make an issue on GitHub tracker.
Or bettter, implement it on your own and make PR.

-------------------------

projector | 2017-11-21 10:15:19 UTC | #8

Thank you, i will check with GitHub tracker. Btw, could I know if there is anyone in the team working with ES3? I got the impression someone is working with ES3, I'm happy to help,  that's also the reason I asked about the status of ES3 implementation.

-------------------------

