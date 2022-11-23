weitjong | 2017-01-02 00:58:40 UTC | #1

Attached is the screenshots from my Galaxy Tab3.
[url]https://www.dropbox.com/s/oye40pmpkcsscoy/CharacterDemo-1.png[/url]
[url]https://www.dropbox.com/s/qsdukqm57r3l0mg/CharacterDemo-2.png[/url]
[url]https://www.dropbox.com/s/z2uk8emxkwjy3ef/NinjaSnowWar-1.png[/url]
[url]https://www.dropbox.com/s/podp8trm08gukcd/NinjaSnowWar-2.png[/url]

I know this has been discussed previously in the forum and I understand that depth bias would need to be adjusted to remove the artifacts. But as it appears to manifest in most of the sample scenes on Android device (at least on my Galaxy S3 and Galaxy Tab3), could the engine adjust the depth bias automatically/adaptively when runs on Android platform?

-------------------------

cadaver | 2017-01-02 00:58:40 UTC | #2

It is already adjusting the depth bias larger on OpenGL ES by quite a large amount (2x if I remember right).

The reasons for the artifacts are at least:
- Lower interpolator (varying) precision
- No slope scale depth bias support
- Worse filtering; on desktops the smooth hardware filtering hides the artifacts partially

Because adjusting the bias higher also causes disconnected shadows ("Peter Panning") we'll have to be careful when the engine is adjusting things behind our backs. Maybe there should be a parameter for the adjust factor.

-------------------------

weitjong | 2017-01-02 00:58:41 UTC | #3

Using CharacterDemo as basis for my test, I have adjusted the depth bias until I can start to visibly see the peter panning side effect but even at such setting I can still see self-shadowing artifacts albeit in a much smaller area. I suppose it is hard to predefine just one adjust factor that would work best for all cases on Android platform then.

-------------------------

cadaver | 2017-01-02 00:58:41 UTC | #4

Yes, in general dynamic shadows on OpenGL ES 2 -level hardware are a bit of a joke, because either you use 1 sample (on/off) sampling, in which case you can get acceptable performance on for example iPad2, or you take 4 samples in which case you are causing dependent texture reads, and still don't get quite good quality. Haven't tested 4 samples with manual bilinear filtering, which would help to hide the artifacts, but I assume the performance hit would be quite large.

One thing that might help would be if all the arithmetic related to the shadow texture coordinates would be in high precision. Will have to test.

EDIT: making the shadow sampler mediump did not change anything. The texture coordinates are already mediump (highest supported by pixel shaders)

-------------------------

