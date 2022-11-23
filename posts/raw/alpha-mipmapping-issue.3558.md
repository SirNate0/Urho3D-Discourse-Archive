Don | 2017-09-12 04:08:47 UTC | #1

Hey all,

I am working with some vegetation at the moment, and trying to get the alpha looking correct. As of now, I am using the alpha to coverage method. One thing I noticed was that the alpha tends to fade as the vegetation gets farther away.
![Screenshot from 2017-09-11 21-05-01|250x500](upload://5qCDF83bbVkMkpqd7OcXuGRTsC4.png)

This seems to be similar to what is described here. http://the-witness.net/news/2010/09/computing-alpha-mipmaps/
(I verified this by disabling mip-maps for the texture, and the alpha was fine)

Has anyone else had this issue or know a way to fix it? i have looked through the code for mipmap generation, but it seems to be handled by OpenGL.

Best,
-Don

-------------------------

Eugene | 2017-09-12 08:40:29 UTC | #2

You have to generate mipmaps on your own and tweak alpha channel for each level. E.g. multiply alpha value on some constant.

**Upd:** You could tweak alpha of already generated mip levels

-------------------------

Bananaft | 2017-09-13 04:59:41 UTC | #3

First of all, from your screenshot it seems to me that alpha to coverage does not work. It requiers MSAA to work, make sure you have MSAA turned on.

Second, both Photoshop and Gimp dds plugin have a settings of mip generation you can play with.
Here is Gimp plugin: 
https://code.google.com/archive/p/gimp-dds/downloads

The last parameter seems like what you need:
![image|324x500](upload://yWaOeWKP1eTI2SLOhdZbi7YQuuU.png)

-------------------------

Don | 2017-09-13 05:01:43 UTC | #4

Thank you! This is exactly the sort of thing I was looking for.

I think MSAA was still on when I took that screenshot, but it does look strange compared to other screenshots I have. Maybe I accidentally changed something.

EDIT:

I tried using the plugin and despite using different levels of alpha test coverage preserving. Unfortunately, it does not seems to have an effect.
![Screenshot from 2017-09-12 21-56-19|329x490](upload://tRbATOF4GDpHqbliCYy6bd2WNvX.png)

Anything else that I could try?

-------------------------

Eugene | 2017-09-13 07:10:43 UTC | #5

[quote="Don, post:4, topic:3558"]
Anything else that I could try?
[/quote]

I solved the problem, so you can too.

[quote="Eugene, post:2, topic:3558"]
You could tweak alpha of already generated mip levels
[/quote]

1. Save image to RGBA with lods. Premultipled alpha off.
2. Load the Image in Urho
3. For each mipmap for each pixel `alpha = alpha * k^mipmap` where k in (1, 2)
4. Save the Image if you want to do smth else with it.

**Update:**
[details="I've even found my code!"]
```
void AdjustImageLevelsAlpha(Image& image, float factor)
{
    const unsigned numLevels = GetNumImageLevels(image);
    if (numLevels <= 1)
    {
        return;
    }

    SharedPtr<Image> level = image.GetNextLevel();
    float k = factor;
    for (unsigned i = 1; i < numLevels; ++i)
    {
        for (int y = 0; y < level->GetHeight(); ++y)
        {
            for (int x = 0; x < level->GetWidth(); ++x)
            {
                Color color = level->GetPixel(x, y);
                color.a_ *= k;
                level->SetPixel(x, y, color);
            }
        }
        k *= factor;
        level = level->GetNextLevel();
    }
}
```
[/details]

-------------------------

jackie2009 | 2020-09-07 05:53:28 UTC | #6

You can try sdf alphatest.I found 3 ways to fix it.https://zhuanlan.zhihu.com/p/218635002

-------------------------

