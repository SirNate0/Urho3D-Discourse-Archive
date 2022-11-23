KatekovAnton | 2020-06-09 17:16:01 UTC | #1

Hi. I am trying to convert hdr backgrounds int urho zone cubemap but I cannot figure out what parameters should I use.

Urho have an example of such image that I am trying to receive - output_pmrem_***.dds which works great and contains mipmaps, contains radiance and irradiance maps and everything we need. So Im trying to find a way how to create our custom skyboxes + environment maps.

I did a few attempts with cmft and https://hdrihaven.com/hdri/?c=skies&h=kiara_4_mid-morning . I work on MacOS.

1. > I was trying to convert initial .hdr file

it constantly freezes my mac, I have to restart it (tried 3 times). It also looks dangerous because mac become very (very) hot and cooling system was not triggered...

2. > tried to convert tonemap JPG with cmft

cmft cannot recognize the format (cannot read the file - no idea why)

Using GIMP I converted tonemap JPG into a tga (kiara_4_mid-morning.tga) and tried few times with it

3. > --output2 "kiara_4_mid-morning"  \
--output2params dds,RGBA8,facelist    \  

This gave me the following error:
*File type DDS does not support RGBA8 texture format. Valid internal formats for DDS are: BGR8 BGRA8 RGBA16 RGBA16F RGBA32F. Choose one of the valid internal formats or a different file type.*

4. > --output2 "kiara_4_mid-morning"  \
              --output2params dds,BGRA8,facelist    \

This parameters game me 350kb dds images that I can at least open and see in preview. But unfortunately urho cannot read it: 
> **[Wed Jun 10 00:48:57 2020] ERROR: Unrecognized DDS image format**
**[Wed Jun 10 00:48:57 2020] ERROR: Null image, can not set face data**

Can anyone give me an example of how to convert that images? I feel I do smth completely wrong... Thank you.

-------------------------

lezak | 2020-06-09 22:28:50 UTC | #2

Can You give more details what's causing this freezing/on what stage it occurs? What is Your setup etc? Side note: I'm on windows, so if it's something related to macOS, I won't be able to help.

[quote="KatekovAnton, post:1, topic:6196"]
**[Wed Jun 10 00:48:57 2020] ERROR: Unrecognized DDS image format**
**[Wed Jun 10 00:48:57 2020] ERROR: Null image, can not set face data**
[/quote]
Just like it's stated in error: wrong dds format. You need to use other, for sure BC1/DXT1, BC2/DXT3 and BC3/DXT5 are supported.

-------------------------

KatekovAnton | 2020-06-10 00:53:10 UTC | #3

Hi.

[quote="lezak, post:2, topic:6196"]
Can You give more details what’s causing this freezing/on what stage it occurs?
[/quote]

I have no idea unfortunately... It is happening in the middle of conversion process... I was trying to build it from source but I got some compiler errors so I decided to try prebuilt binary. I will try from windows today later.

[quote="lezak, post:2, topic:6196"]
What is Your setup etc?
[/quote]

MacBook Pro (16-inch, 2019), Catalina. 

[quote="lezak, post:2, topic:6196"]
Just like it’s stated in error: wrong dds format. You need to use other, for sure BC1/DXT1, BC2/DXT3 and BC3/DXT5 are supported.
[/quote]

Yeah I saw the source code... CMFT exporting it into dds DX10, I dont see any options to modify dds format... Can you show the parameters that you pass to CMFT? Here is what I was trying to do:

> eval $CMFT $@ --input "kiara_6_afternoon.tga"           \
              ::Filter options                  \
              --filter radiance                 \
              --srcFaceSize 256                 \
              --excludeBase false               \
              --mipCount 7                      \
              --glossScale 10                   \
              --glossBias 3                     \
              --lightingModel blinnbrdf         \
              --edgeFixup none                  \
              --dstFaceSize 256                 \
              ::Processing devices              \
              --numCpuProcessingThreads 4       \
              --useOpenCL false                  \
              --clVendor anyGpuVendor           \
              --deviceType gpu                  \
              --deviceIndex 0                   \
              ::Aditional operations            \
              --inputGammaNumerator 2.2         \
              --inputGammaDenominator 1.0       \
              --outputGammaNumerator 1.0        \
              --outputGammaDenominator 2.2      \
              --generateMipChain true           \
              ::Output                          \
              --outputNum 3                     \
              --output0 "kiara"       \
              --output0params dds,bgra8,cubemap \
              --output1 "kiara"       \
              --output1params ktx,rgba8,cubemap \
              --output2 "kiara"  \
              --output2params dds,BGRA8,facelist    \

Thank you for your help!

-------------------------

lezak | 2020-06-10 12:49:52 UTC | #4

[quote="KatekovAnton, post:3, topic:6196"]
Can you show the parameters that you pass to CMFT?
[/quote]

I use gui version <a href="https://github.com/dariomanesku/cmftStudio"> from here </a> and I don't use same paramters for all maps.
As for You setup, besides obvious reducing resolution, increasing gloss scale (this one You have rather high already) and bias should speed up processing.

[quote="KatekovAnton, post:3, topic:6196"]
–excludeBase false
[/quote]

This option should be turned on. Not only this will increase processing speed a lot, but also You don't want to have level 0 filtered for two reasons: 
- You'll be able to use the same cubemap with skybox;
- For low roughness surfaces, You'd probably  want sharp and clear reflections. Now, as a side note, there's one thing about Urho's pbr shader - roughness is never 0 in it, so it still never samples 0 level in IBL, to get clean and sharp reflections it's necessary to make small changes in the shader.
As for dds, i don't think that cmft can export to format supported in Urho, so You'll need to use some other software to convert (i use GIMP with some plugin, but I've installed it so long ago that I don't remember which one was it). Just keep in mind that You'll need to import images with mipmaps and export with the same ones, so for example nvidia texture tool plugin for photoshop won't do the trick.

-------------------------

