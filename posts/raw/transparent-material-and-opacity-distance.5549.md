Teknologicus | 2019-09-04 12:40:53 UTC | #1

How does one control the distance at which a transparent material (texture with apha channel) becomes opaque vs. maintains transparency?  Here's my material:

    <material>
        <technique name="Techniques/DiffAlpha.xml" />
        <texture unit="diffuse" name="Textures/texture_atlas.dds" />
    </material>

Do I need to define a custom technique for this material, and if so, what parameter(s) would I set?

-------------------------

Modanung | 2019-09-04 19:25:15 UTC | #2

You can add multiple techniques to a single material and assign a `loddistance` to them. This determines the distance (divided by the scale I believe) at which each technique is used.

If you're interested about adding LODs to your models as well; I made a video about that:
https://discourse.urho3d.io/t/information-source-how-to-exporting-lods-with-blender/2083

-------------------------

Teknologicus | 2019-09-05 00:59:56 UTC | #3

I tried the below but it doesn't seem to make any visual difference.  I've attached a screenshot with this material active for the water to show what I'm seeing.  Each terrain cube is 1 unit in size.  I'm not sure what I'm doing wrong. :face_with_raised_eyebrow:

    <material>
        <technique name="Techniques/DiffAlpha.xml" quality="2" loddistance="0" />
        <technique name="Techniques/DiffAlpha.xml" quality="1" loddistance="128" />
        <technique name="Techniques/DiffAlpha.xml" quality="0" loddistance="256" />
        <texture unit="diffuse" name="Textures/texture_atlas.dds" />
    </material>
![Untitled|690x407](upload://2S4Ci77PDtTT82fsMAnJkmPI8m8.png)

P.S.  I also tried the below with same results.

    <material>
        <technique name="Techniques/DiffAlpha.xml" quality="2" loddistance="64" />
        <technique name="Techniques/DiffAlpha.xml" quality="1" loddistance="128" />
        <technique name="Techniques/DiffAlpha.xml" quality="0" loddistance="256" />
        <texture unit="diffuse" name="Textures/texture_atlas.dds" />
    </material>

-------------------------

Modanung | 2019-09-05 22:34:50 UTC | #4

Well yes, you're using the same technique three times. :slightly_smiling_face:
Try something that looks more like:
```
<technique name="Techniques/DiffAlpha.xml" quality="0" loddistance="0"  />
<technique name="Techniques/Diff.xml"      quality="0" loddistance="32" />
```

I'm not sure how the *quality* works, but I guess it allows you to link your material to graphics settings.

-------------------------

SirNate0 | 2019-09-06 00:05:37 UTC | #5

Is there problem that you don't want the water to appear transparent further from the camera? If so, what happens if you disable mip mapping on your texture atlas? 

If I remember correctly (I may be entirely wrong) mip mapping sometimes doesn't play nicely with texture atlases/transparency, though someone else may be able to provide better advice.

-------------------------

restless | 2019-09-07 19:27:11 UTC | #6

I used similar technique for distant foliage. At distance tree leaves and grass would fully disappear due to how mip maps work... So I just made the last mip level part fully opaque :) Worked surprisingly well

-------------------------

Teknologicus | 2019-09-06 01:16:24 UTC | #7

Thank you to everyone that replied.  It was indeed a mipmap issue, and once I eliminated and disabled mipmaps for the water texture, it looks as desired.
![Untitled|690x407](upload://fwTYWbWcbd4JicqgtGcXSIQnja9.jpeg)

P.S.  I got to playing with the code from Urho3D's water sample (23_water) and did this.  It doesn't play nice with my code yet (water at different depths than sea level, no water at sea level, etc.), but looks very cool in a test run!
https://youtu.be/3O1iqVnGzUM

-------------------------

SirNate0 | 2019-09-06 02:35:03 UTC | #8

Since it does seem to be a mipmap problem and you seem to be using a dds file for the texture already you may want to simply edit the higher mipmaps by hand to fix the transparency while retaining the benefits of using mipmaps. I'm pretty sure GIMP can do this if you don't already have tools that will.

-------------------------

Teknologicus | 2019-09-06 03:15:35 UTC | #9

Agreed.  I definitely want to use a texture atlas with mipmap for as much of the terrain as possible to avoid that pixel shimmer one gets without mipmaps.  With water and glass I will use a texture atlas without the mipmaps and see how that goes (I haven't tested the glass texture yet).  For blocks with transparent areas and opaque blocks I will use the texture atlas with mipmaps.

I develop under Linux and do use GIMP for the dds file stuff.  I also wrote a custom mipmap generator for my texture atlases that doesn't blend tiles across each other.  :slight_smile:

-------------------------

Teknologicus | 2019-09-10 07:10:56 UTC | #10

I found a solution for the texture atlas mipmap generation and alpha channel which works both with tiles like leaves and grass which only contain pixel alpha values of 255 or 0 (with the textures I'm using https://github.com/cylgom/freeture) and tiles like water and glass which have pixel alpha values somewhere in between 255 and 0:  When blending four pixels to make one pixel in a lower detail mipmap level, take the highest alpha value from the four pixels and use that as the result alpha value.

Follow up:  Averaging pixels (including alpha channel) for only pixels with alpha greater than zero works better for both partially transparent blocks and fully transparent blocks in my findings when generating mipmaps.  Now everything including water, ice, leaves can use the same texture altlas with mipmaps in my project.

-------------------------

