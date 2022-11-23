boberfly | 2017-01-02 01:03:54 UTC | #1

[url]https://www.khronos.org/vulkan[/url]

Discuss :slight_smile:

-------------------------

weitjong | 2017-01-02 01:03:55 UTC | #2

Live long and prosper...

-------------------------

Faizol | 2017-01-02 01:03:55 UTC | #3

[quote="boberfly"][url]https://www.khronos.org/vulkan[/url]

Discuss :slight_smile:[/quote]

PowerVR Rogue GPUs running early Vulkan demo (experimental drivers) 
[youtube.com/watch?v=KdnRI0nquKc](https://www.youtube.com/watch?v=KdnRI0nquKc)

This blog is a very interesting read on Vulkan;
"Trying out the new Vulkan graphics API on PowerVR GPUs"
By Ashley Smith (an Applications Engineer at Imagination)
[blog.imgtec.com/powervr/trying-o ... wervr-gpus](http://blog.imgtec.com/powervr/trying-out-the-new-vulkan-graphics-api-on-powervr-gpus)

Among the highlights from the demo using an alpha driver (from the blog);
    High-quality, physically-based shading
    HDR (High dynamic range) rendering
    20 unique 2K PVRTC textures
    2 GiB of texture data compressed to 266 MiB using Imagination?s PVRTC texture compression standard
    4 x MSAA (Multi-sample anti-aliasing)
    16 x Anisotropic texture filtering
    Physically-correct material parameters
    Low CPU usage, very efficient GPU usage
    Correct specular reflections on reflective materials
    More than 250,000 triangles
    Post processing effects: saturation, exposure and tone mapping

-------------------------

rogerdv | 2017-01-02 01:03:56 UTC | #4

What does this means from the Urho point of view? We will have a new Vulkan based rederer at some future time?

-------------------------

cadaver | 2017-01-02 01:03:56 UTC | #5

Once there are public APIs / SDKs / drivers, it's possible, which I understand will go into the next year. Naturally will also depend on who is / are interested in implementing new graphics APIs support.

-------------------------

Faizol | 2017-01-02 01:03:59 UTC | #6

"GLAVE: A Debug Tool For The New Vulkan Graphics API"

[phoronix.com/scan.php?page=n ... GLAVE-Demo](http://www.phoronix.com/scan.php?page=news_item&px=LunarG-GLAVE-Demo)

Update:
"Valve Developed An Intel Linux Vulkan GPU Driver"
[phoronix.com/scan.php?page=n ... kan-Driver](http://www.phoronix.com/scan.php?page=news_item&px=Valve-Intel-Vulkan-Driver)

and snapshot of Valve's Source 2 on Vulkan API
[youtu.be/0Hth4u65zfc](http://youtu.be/0Hth4u65zfc)

UPDATE 2:
presentation by various companies (AMD, ARM, etc) - "The new Vulkan and SPIR-V specifications"
[youtube.com/watch?v=EUNMrU8uU5M](https://www.youtube.com/watch?v=EUNMrU8uU5M)

-------------------------

