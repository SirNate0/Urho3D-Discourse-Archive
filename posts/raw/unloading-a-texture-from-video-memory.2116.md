Denthor | 2017-01-02 01:13:13 UTC | #1

Hi there, I was just wondering if there is a best practice for doing this, such as releasing the memory for a splash screen texture? From what I understand even after the component is gone the texture is still available on the video card via the resource cache?

Regards,

-------------------------

1vanK | 2017-01-02 01:13:14 UTC | #2

[quote="Denthor"]Hi there, I was just wondering if there is a best practice for doing this, such as releasing the memory for a splash screen texture? From what I understand even after the component is gone the texture is still available on the video card via the resource cache?

Regards,[/quote]

I found it in code:
[code]
Texture2D::Release()
{
    ...
    glDeleteTextures(...);
}

Texture2D::~Texture2D()
{
    Release();
}
[/code]

-------------------------

cadaver | 2017-01-02 01:13:14 UTC | #3

Using the various overloads of ResourceCache::ReleaseResource() is the recommended solution; this removes both the CPU/GPU memory use. Note that Materials may hold strong refs to textures and therefore keep a texture alive even if it was removed from the cache, so you may also need to Release the material from the resource cache.

-------------------------

