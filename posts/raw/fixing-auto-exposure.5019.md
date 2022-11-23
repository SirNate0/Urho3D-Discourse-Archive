Bananaft | 2019-03-18 09:41:32 UTC | #1

Auto exposure post-effect does not utilize the whole range it given. One can see it by setting AutoExposureLumRange parameter to extreme numbers, or removing the Clamp from shader code completiley. And looking at very dark or bright objects.

I was able to work around this by:
1) dividing result by 4 in LUMINANCE64
2) removing division by 16 in LUMINANCE1
3) setting AutoExposureMiddleGrey to 0.05

Now it works great. And can pull exposure to any extreme numbers. Does anyone know what this code is based on? My fix gives perfect rersults, but It's probably not the way it was intended to be (esp. middle grey 0.05 :smile: )

full [ **AutoExposure.glsl** ](https://gist.github.com/Bananaft/ea515040f116d19665ecbf8c3df013a6#file-autoexposure-glsl). Commented out, is the debugging output of luminance value.

-------------------------

Leith | 2019-03-19 08:13:05 UTC | #2

I like the way you didn't explain how your lighting hack works in theory - some people get caught up in that, while just tweaking is, in my opinion, more valid than explaining why the tweak is effective.
I'll test your stuff out shortly - I'm planning on using positive and negative lights (aka darklights) - I have been assured that the sign of the brightness will be observed by Urho's default shaders.

-------------------------

GodMan | 2019-03-22 15:41:37 UTC | #3

I tried your changes, and I only noticed a darker scene. If I change the 0.05 to a different number the scene begins to brighten up. I change it back to the default values, and my results in my op is better looking. I am also on the DX9 side, not OpenGL.

-------------------------

