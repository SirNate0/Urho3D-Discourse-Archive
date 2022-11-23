dragonCASTjosh | 2017-01-02 01:10:20 UTC | #1

Due to my recent work on PBR i have needed support for .HDR image formats, something that Urho3D doesn't currently support but i understand that the latest version of STB support .HDR and other new formats that could be useful to the engine. My Current priority is currently OpenGL support for PBR so i do not have the time to work on this just yet, and as expected a simple drag and drop job didnt work :slight_smile: . Some assistance on Updating it, or even just a guide to speed up work when i get round to it would be helpful.

-------------------------

cadaver | 2017-01-02 01:10:20 UTC | #2

Updating STB is mostly just about overwriting the relevant files. However you may need to do changes to the Image or Texture classes, since all Image knows at this point is to store 8-bit images of 1 to 4 components, or block-compressed images (DXT etc.)

-------------------------

dragonCASTjosh | 2017-01-02 01:10:22 UTC | #3

I had a quick go at updating STB but ran into  many errors all of them are link errors in the executables (player, tools and samples). You can find the error report for the player below, im not sure how to fix this error.
[img]http://i.imgur.com/fowMwwb.png[/img]

Im assuming its something to do with the stb function calls failing but my logic says they must be usable or the lib wouldn't of compiled. Not just that the player shouldnt link to stb and i havent touched the cmake files

-------------------------

friesencr | 2017-01-02 01:10:23 UTC | #4

Did you add the define?

[github.com/nothings/stb/blob/ma ... image.h#L5](https://github.com/nothings/stb/blob/master/stb_image.h#L5)

-------------------------

dragonCASTjosh | 2017-01-02 01:10:23 UTC | #5

[quote="friesencr"]Did you add the define?

[/quote]

I did miss the defines but it has not solved any of the link errors

-------------------------

weitjong | 2017-01-02 01:10:24 UTC | #6

The error means exactly that. The symbols were not found in the Urho3D.lib, which they should if everything went through correctly. You must have accidentally modified the STB's CMakeLists.txt. More specifically this highlighted line. [github.com/urho3d/Urho3D/blob/c ... ts.txt#L30](https://github.com/urho3d/Urho3D/blob/c4f6f315ff5b6ea992340780521d3e5f2e668b11/Source/ThirdParty/STB/CMakeLists.txt#L30). This innocently looking macro does a lot of heavy lifting behind the scene. One of the thing it does is to "register" STB as one of the Urho3D.lib static libraries, so all its objects/symbols are archived (for STATIC lib type) or linked (for SHARED lib type) together into Urho3D library. If you mess that up then you will get the linker error as you observed.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:24 UTC | #7

[quote="weitjong"]The error means exactly that. The symbols were not found in the Urho3D.lib, which they should if everything went through correctly. You must have accidentally modified the STB's CMakeLists.txt. More specifically this highlighted line. <a class="vglnk" href="https://github.com/urho3d/Urho3D/blob/c4f6f315ff5b6ea992340780521d3e5f2e668b11/Source/ThirdParty/STB/CMakeLists.txt#L30" rel="nofollow"><span>https</span><span>://</span><span>github</span><span>.</span><span>com</span><span>/</span><span>urho3d</span><span>/</span><span>Urho3D</span><span>/</span><span>blob</span><span>/</span><span>c4f6f315ff5b6ea992340780521d3e5f2e668b11</span><span>/</span><span>Source</span><span>/</span><span>ThirdParty</span><span>/</span><span>STB</span><span>/</span><span>CMakeLists</span><span>.</span><span>txt</span><span>#</span><span>L30</span></a>. This innocently looking macro does a lot of heavy lifting behind the scene. One of the thing it does is to "register" STB as one of the Urho3D.lib static libraries, so all its objects/symbols are archived (for STATIC lib type) or linked (for SHARED lib type) together into Urho3D library. If you mess that up then you will get the linker error as you observed.[/quote]

I checked the CMakeLists.txt and nothing has changed, you can find the branch im working on here: [url]https://github.com/dragonCASTjosh/Urho3D/tree/STB_Update[/url] currently i have left the extra STB files such as voxel rendering just until i get the branch working then i will clean up what is not needed.

Its worth noting that stb_image.c has become deprecated and functionality was implemented into the header .

-------------------------

weitjong | 2017-01-02 01:10:24 UTC | #8

[quote="dragonCASTjosh"]Its worth noting that stb_image.c has become deprecated and functionality was implemented into the header .[/quote]
Why not you say so earlier  :wink: . It changes everything. If that is the case then the objects do not exist and hence they never get archived/linked into Urho3D library. If they only exist in header-only implementation then on the contrary we must change our CMakeLists.txt to adapt to it. Currently the STB headers are not exposed to Urho3D library users, i.e. they are only used when building Urho3D library and not when using the library. With this change from upstream STB then we have but no choice to expose their headers to Urho3D library users as well. You can see how this is done in CMakeLists.txt from Bullet or Lua/LuaJIT.

-------------------------

hdunderscore | 2017-01-02 01:10:26 UTC | #9

I played with it a bit, looks like it can build if you do this:

[code]#define STB_IMAGE_IMPLEMENTATION
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include <STB/stb_image.h>
#include <STB/stb_image_write.h>

#include "../DebugNew.h"

//extern "C" unsigned char* stbi_write_png_to_mem(unsigned char* pixels, int stride_bytes, int x, int y, int n, int* out_len);[/code]

There was a second define required, and remove the declaration for stbi_write_png_to_mem.

I didn't do any real testing to see if anything broke-- but the editor seemed to work. I suspect like cadaver mentioned, you'll need to do extra things to make the engine/shaders understand HDR. For quick testing purposes, you could decompress HDR in the shader.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:27 UTC | #10

[quote="hd_"]I played with it a bit, looks like it can build if you do this:

[code]#define STB_IMAGE_IMPLEMENTATION
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include <STB/stb_image.h>
#include <STB/stb_image_write.h>

#include "../DebugNew.h"

//extern "C" unsigned char* stbi_write_png_to_mem(unsigned char* pixels, int stride_bytes, int x, int y, int n, int* out_len);[/code]

There was a second define required, and remove the declaration for stbi_write_png_to_mem.

I didn't do any real testing to see if anything broke-- but the editor seemed to work. I suspect like cadaver mentioned, you'll need to do extra things to make the engine/shaders understand HDR. For quick testing purposes, you could decompress HDR in the shader.[/quote]

thanks ill give it a go

-------------------------

dragonCASTjosh | 2017-01-02 01:10:27 UTC | #11

[quote="dragonCASTjosh"] played with it a bit, looks like it can build if you do this[/quote]

Worked a dream, thanks  :smiley: . i will likely make a PR and see what i need to do from there.

-------------------------

hdunderscore | 2017-01-02 01:10:30 UTC | #12

@Cadaver, is it only the Image class that will need significant changes to support 16f/32f textures-- or will the Texture* classes need significant changes too?

If we keep it simple and only support .hdr at the moment, we will need a way to stitch mip levels in the .xml file like we can for faces ([urho3d.github.io/documentation/1 ... rials.html](http://urho3d.github.io/documentation/1.5/_materials.html)).

At a later stage, I see potential in using this to load/save extra formats: [github.com/dariomanesku/cmft/bl ... /image.cpp](https://github.com/dariomanesku/cmft/blob/master/src/cmft/image.cpp)

-------------------------

cadaver | 2017-01-02 01:10:31 UTC | #13

The Texture classes interrogate the Image for the kind of data to be uploaded, currently they wouldn't understand anything else from that than 1-4 component 8bit. So the classes need to be updated in tandem.

The actual support for float textures should already be there, as they can be used as e.g. rendertargets.

-------------------------

