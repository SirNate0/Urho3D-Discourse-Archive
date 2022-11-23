galileolajara | 2018-05-15 13:04:48 UTC | #1

Hi,

Does anyone had success using PVRTC on 1.7? I always see black textures both on Apple's texturetool and PVRTexToolCLI with all mipmaps generated. I'm also using

glTexParameteri(target_, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST);
glTexParameteri(target_, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

Tried different sizes, 4096x4096, 2048x 2048, 1024x1024 all with no luck.

PVRTC works on Urho3D 1.5 but not on 1.7, anyone knows a patch?

Thanks for your help!

-------------------------

