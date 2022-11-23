UrhoIsTheBest | 2020-07-26 18:50:09 UTC | #1

I was loading a big terrain heightmap data through png image ~270M.

I got the error
> Could not load image XXXXX: too large

I traced down the issue found it's related to ```stb``` image lib that Urho3D is using, see [github issue](https://github.com/nothings/stb/issues/672#issuecomment-580041441).
Generally,
> stb_image uses ints pervasively, including for offset calculations.
> so MAX_IMAGE_SIZE ~256MB max.

I tried a smaller image ~200M but there is still other issue I haven't figured out yet.

**This is unfortunate and I was wondering if there is a quick workaround, e.g. use a different image type?**

Otherwise, I might need to write my own image loader purely for large files.

*I could separate source image into smaller ones and load them one by one, but this would make things nasty given I am going to upload this heightmap to GPU. I don't want to implement "selecting images according to coordinates" nasty logic in the shader.*

**Update:** I also have error when using texture image ~200M for opengl
> Failed to create texture.  

There should be a max size (width, ram) for GPU to resolve too :(

-------------------------

Eugene | 2020-07-25 09:08:11 UTC | #2

Max size of the image is limited, check your GPU specs to find out exact limits. It’s usually varies from 2k to 16k.

-------------------------

Modanung | 2020-07-26 01:41:47 UTC | #4

...or [ImageMagick](https://imagemagick.org/script/command-line-options.php#crop).

-------------------------

UrhoIsTheBest | 2020-07-26 02:32:51 UTC | #5

Thanks.

I did not notice CDLOD cuts large texture into smaller ones. At least it's not obvious from the paper. But I am a little bit disappointed about those papers (CDLDO, geoclipmapping). CDLOD paper mentioned about streamable blocks of terrain data but that's for StreamingCDLOD. I would not expect the author is cutting textures for the BasicCDLOD one. 
I tried to read the source code for that paper, but it's very un-readable as all the academia codes.

If I have to use smaller texture images, things would get tricky.
For my case, I need to show the full terrain in low resolution when the camera zooms out enough. So I might need different LOD texture anyway, and decide which one to use in real time. The idea is simple but would be a pain to implement.
I am not sure how the BasicCDLOD dealing with those exchanging texture images realtime since there is no single word about it in the paper. I probably going to spend sometime reading through that source code no matter how un-readable it is.
If you happened to be familiar with that source code, could you point me where is the code for the shaders to choose the correct smaller texture images?

As for cutting images, I am not worried about it. Since I have my own tool based on GDAL for Geographic terrain data manipulation. I made my terrain with it.

I thought I was close for this implementation but looks like lots of things need to be done if the program is for real application other than a demo.

-------------------------

UrhoIsTheBest | 2020-07-26 18:53:56 UTC | #7

I could make different images for different LODs, but for my case, I have LODs from 0 ~ 8. For example, I could make a low resolution image for the whole map (lod = 8), then maybe 4 with lod = 7. That's the minimum number of images I need but **that would occupy 5 texture units already!** IIUC, we have only 16 texture units for certain. But I still needs other textures (e.g. normal, spec, several terrain details). If we have different images for different lod, we need the same number of image for normal, spec etc too.
I am not sure what's the good solution for this.

**Anyway, I tried to cut my source image into 4 pieces.**
Looks like my computer is okay to load texture image with size <= 8192.
My texture image size is about two times larger. So I divided my image into 4 pieces. A very rough demo code:
```
  const int kMaxSupportedSingleHeightMapSize = 8192;
  for (int i = 0; i < 4; ++i) {
    auto texture = SharedPtr<Texture2D>(new Texture2D(context_));
    int index_x = i % 2;
    int index_y = i / 2;
    int x0 = std::max(0, index_x * kMaxSupportedSingleHeightMapSize);
    int x1 = std::min(heightmap_image_->GetWidth() - 1, (index_x + 1) * kMaxSupportedSingleHeightMapSize);
    int y0 = std::max(0, index_y * kMaxSupportedSingleHeightMapSize);
    int y1 = std::min(heightmap_image_->GetHeight() - 1, (index_y + 1) * kMaxSupportedSingleHeightMapSize);
    SharedPtr<Image> heightmap_test = SharedPtr<Image>(heightmap_image_->GetSubimage(IntRect(x0, y0, x1, y1)));
    texture->SetFilterMode(FILTER_NEAREST);
    texture->SetData(heightmap_test, false);

    // I also changed those values, but does not make difference for my case.
    std::vector<TextureUnit> units{TU_DIFFUSE, TU_NORMAL, TU_SPECULAR, TU_EMISSIVE,};
    batches_[0].material_->SetTexture(/*texture unit*/units[i], texture);
  }
```

And then I get different texture image for vertex displacement in the shader:
```
float GetHeight(vec2 pos) {
    vec2 texCoord;
    vec2 heights;
    if (pos.x <= cMapSize.x && pos.y <= cMapSize.y) {
        texCoord = vec2(pos.x / cMapSize.x, pos.y / cMapSize.y);
        heights = texture(sHeightMap0, texCoord).rg;
    } else if (pos.x > cMapSize.x && pos.y <= cMapSize.y) {
        texCoord = vec2(pos.x / cMapSize.x - 1.0, pos.y / cMapSize.y);
        heights = texture(sHeightMap1, texCoord).rg;
    } else if (pos.x <= cMapSize.x && pos.y > cMapSize.y) {
        texCoord = vec2(pos.x / cMapSize.x, pos.y / cMapSize.y - 1.0);
        heights = texture(sHeightMap2, texCoord).rg;
    } else if (pos.x > cMapSize.x && pos.y > cMapSize.y) {
        texCoord = vec2(pos.x / cMapSize.x - 1.0, pos.y / cMapSize.y - 1.0);
        heights = texture(sHeightMap3, texCoord).rg;
    }
    ...
}
```
with the material definition
```
<material>
    <technique name="Techniques/CdlodTerrain.xml" />
    // units 0 ~ 3 reserved for heightmap images.
    <texture unit="0" name="" />
    <texture unit="1" name="" />
    <texture unit="2" name="" />
    <texture unit="3" name="" />
    <texture unit="4" name="HeightMapsTest/DEM_print.png" />
    <texture unit="5" name="Textures/TerrainDetail1.dds" />
    ...
</material>
```

This cutting-image method works fine for a smaller heightmap. 
**But for my case, some textures do not show. It looks like they are unloaded automatically somehow.**

![image|676x500](upload://kuGKNKvovQr0NvVExoDZzhFQjOa.jpeg) 

If I randomly exchange the order of heightmap in shader, for example:
```
float GetHeight(vec2 pos) {
   ...
        heights = texture(sHeightMap3, texCoord).rg;
   ...
        heights = texture(sHeightMap2, texCoord).rg;
    ...
        heights = texture(sHeightMap1, texCoord).rg;
   ...
        heights = texture(sHeightMap0, texCoord).rg;
    ...
}
```
**Different texture images will be remained.** The bottom-left is a different one.

![image|675x500](upload://x18EcONxSp3rAnIO8VBEn8Je4CV.jpeg)  
*(don't mind the edges, it's not there yet)*

**So I think it's the OpenGL automatically unloading texture if they are taking too much memory?** BTW: my source heightmap texture image is ~170MB in png (size ~ 16k pixels).
But how can I verify that and is there any way from Urho3D API to query which texture is loaded/unloaded in real time?
Or what other way should I address this problem overall?

-------------------------

UrhoIsTheBest | 2020-07-27 03:05:50 UTC | #9

Notice there are two stages for "loading texture images":
1. Load image from disk to memory via Urho3D engine;
2. Load image in GPU video card memory for shader calculations.

I believe all those DEBUG LOGGING is about the 1st stage, while my problem is related to the 2nd stage.
And I can verify the ```[...] DEBUG: Loading resource XXXX.png``` is done successfully. Also, I cannot build QuadTree if the 1st stage is not successful :slight_smile:

As you can see from my first piece of code, I then cut the image into 4 pieces. When I set the material texture, that's the 2nd stage.

**As for compression** 
> PNG can be compressed (like jpeg) I see 9 compression levels.  

If I would like to compromise to lossy compression, I probably would not need those high resolution texture images anyway :) 


**Good question about**
> How big is your landscape?
Maybe it makes sense not to render it entirely?

I wish I could. Unfortunately, the answer is no.
You are the first replier for my original post about [geo clipmapping](https://discourse.urho3d.io/t/anyone-tried-to-implement-geo-clipmapping-for-super-large-terrain/6238/2?u=urho). But I did not describe why I need this at that time. I can elaborate a little bit here. Think about it as a strategy game so play can zoom-out to see the whole map while zoom-in to see state/county level.
> My game needs a terrain, the requirements are:
>1. Freely Zoom in & zoom out, like GoogleEarth. Max resolution when zooming in ~100 meter, Max range when zooming out ~2000km (a whole country scale).
>2. Freely fly over to any direction with any height; Freely rotate camera; 
>3. Support large heightmap data, e.g. real world elevation data from NASA , around 20k * 20k for a whole country.

**Now back to the problem**
As I mentioned in that [geo clipmapping post](https://discourse.urho3d.io/t/anyone-tried-to-implement-geo-clipmapping-for-super-large-terrain/6238/2?u=urho)
> It uses 200k * 100k heightmap (40G compressed to 300M), stores it in video card memory. Very good frame rate even in 2004! 16 years ago! They used the whole US heightmap (1arc resolution, ~30meter).

**The paper did not mention any cutting-image techniques.** It claims "pre-load all 300M heightmap data in the GPU". **So if a video card in 2004 can do that, why not now (in 2020)?**

As for [Fstrugar's paper,](https://github.com/fstrugar/CDLOD/blob/master/cdlod_paper_latest.pdf) **I could not find any cutting-image techniques either in paper or BasicCDLOD source code.**
If I check the [shader source code](https://github.com/fstrugar/CDLOD/blob/master/source/BasicCDLOD/Shaders/CDLODTerrain.vsh), I could only find one texture sampler for the heightmap (variable name ```g_terrainHMVertexTexture```). It is used in the ```sampleHeightmap()``` function.
It's a pity I don't have a windows pc so I cannot run Fstrugar's source code myself to verify everything.

I am not questioning your comment above, but I might miss something important in those papers/projects. 

*Of course we can have different work-around or hack solutions to make things just work.*
**But the key question here is:**
If in 2004 we can preload 200k * 100k heightmap (compressed to 300M) into video card memory, 
**or** preload 
>carlifmtns_large: 48897 x 30465 heightmap with a normal map and a simple texture splatting technique;

in 2010.

**Why is it not even a piece of cake to do the same thing in 2020 ten years later?** :thinking: :thinking: :thinking:

-------------------------

jmiller | 2020-07-27 07:19:17 UTC | #11

PNG was intended to be lossless and this is true for most encoders+options but I see not all. Compression speed and ratios vary a lot with the encoding and heuristics, where a huge image can be "compressed small, quickly" or "crushed to a crystal, with CPU in flames for a week".

A guide to PNG optimization also covering a variety of programs including the newer `optipng`: http://optipng.sourceforge.net/pngtech/optipng.html

-------------------------

UrhoIsTheBest | 2020-08-09 08:05:19 UTC | #12

FYI, I haven't fully solved my problem but had a temporary workaround.

For reading large png into memory, I use a very lightweighted [lodepng](https://lodev.org/lodepng/) lib. It uses ```std::vector<unsigned char>``` to represent image so the length is > ```int_max```. Luckily, Urho3D Image API is flexible enough I can directly use the vector data to construct a new image.

For processing the whole heightmap in GPU, I did split it into 4 pieces. But this time I use ```TEXTURE_DYNAMIC``` instead of ```TEXTURE_STATIC```. Now it seems work, although I don't know why static does not work.

The code & shader is a mess with this hack, it's definitely not a scalable solution. But I would take a deeper look later. I am going to move forward to deal with shadow etc.

-------------------------

