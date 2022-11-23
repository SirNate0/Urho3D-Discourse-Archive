vivienneanthony | 2017-05-08 00:19:24 UTC | #1

What is the best way to deal with the viewport on Android? Considering that a app can run on a small phone 480x853 or a full Android tablet around 1280 width view. I seen about a dozen different size standards.

The biggest issue is with font. My thoughts was make a window 480x853 then scale up.

-------------------------

rasteron | 2017-05-08 02:06:32 UTC | #2

That would be the same solution with responsive websites and web apps which is having a separate UI design for mobile or smaller screens. If your UI is simple enough then you would just worry about scaling and screen ratio.

-------------------------

vivienneanthony | 2017-05-08 04:25:57 UTC | #3

I was thinking the same thing. The easiest and I guess the less complicated is to have maybe 3 screen designs. Then select size of UI to use depending on the screen resolutions.

It's not the best solution but the UI is not complicated, and complicated solution for something minor is time consuming and might over complicated something that literally take minutes to do.

-------------------------

johnnycable | 2017-05-08 08:18:57 UTC | #4

In mobile you can have very different screens / aspect ratio. It is common to create assets at the highest resolution possible (uhd, 2048x1536 ipad like / android xxxhdpi screen) and then SCALE DOWN to intermediate screens (hd, 1920x1080) and low density screens (800x640 android or iphone 5 something). This is about 2d assets. About 3d... you probably end up choosing a favorite / design resolution and following the same route...
NEVER scale up...

-------------------------

SirNate0 | 2017-05-08 22:30:47 UTC | #5

I would not take such a hard position on scaling up. Scaling up should work fine (and is probably the best/only choice) for certain retro-style projects (pixel art, arcade style games, for example). Other than that, I agree, scaling down is always the way you should go, or your assets will likely end up looking blurry on higher resolution devices.

-------------------------

