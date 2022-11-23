eldog | 2017-12-01 17:41:04 UTC | #1

Has anyone had shadows appear correctly when compiling for web/html5? You should be able to reproduce by trying out one of the samples on these devices.

Trying on Android with Chrome and Safari iOS 11.2 (beta), neither a working properly, see attached screenshots.

![IMG-0932|281x500](upload://rbQPCJkHeKXxJrL8ljQzMqG0ffR.PNG)

![2634398549970812361|300x500](upload://hAGZr4AXjDr6e4PzdfSLzic2LO3.jpg)

-------------------------

Eugene | 2017-12-01 19:10:49 UTC | #2

Reproduced on my iPhone. Yeah, it looks awful.
Other samples are broken too. E.g. navigation sample doesn't render Jack and shrooms texture.
Maybe this is caused by light paramters and low shadowmap depth. Try to tweak shadow biases and decrease light area.
Maybe WebGL on mobiles is just broken. Have you tried native demos?

-------------------------

eldog | 2017-12-01 19:26:26 UTC | #3

Can confirm they work correctly on my Desktop browser (chrome and Firefox) and the native (Linux) build. Seems to mobile specific.

Tried tweaking some biases, and light ranges, but seems to not fix it. 

Looking at the light class I can see a define DESKTOP_GRAHPICS which sets the max number of cascades, https://github.com/urho3d/Urho3D/blob/26ff4fce30bcc8f5a9f21e0e938d221cb2a53eaa/Source/Urho3D/Graphics/Light.h#L47

Not sure if it's worth trying to unset that, just don't know how to configure cmake to do it.

-- 

Really enjoying the performance otherwise, compiling with EMSCRIPTEN_WASM=1 gives a massive performance boost, the Physics example is running at 60fps on Nexus 4 and iPhone 5S.

-------------------------

eldog | 2017-12-01 19:53:41 UTC | #4

OK got shadows on iOS safari now (not android chrome though)  thanks @Eugene for pointing to the Light class. I added an `__EMSCRIPTEN__` check to https://github.com/urho3d/Urho3D/blob/460a3a38c0833245b9dd6fa789a18ff4e519d82d/Source/Urho3D/Graphics/GraphicsDefs.h#L34

    #if defined(IOS) || defined(TVOS) || defined(__ANDROID__) || defined(__arm__) || defined(__aarch64__) || defined(__EMSCRIPTEN__)
    #define MOBILE_GRAPHICS
    #else
    #define DESKTOP_GRAPHICS
    #endif

The comment above that line is
    
    /// Graphics capability support level. Web platform (Emscripten) also uses OpenGL ES, but is considered a desktop platform capability-wise

I guess the assumption that the web does not need mobile fixes breaks for mobile browsers. My solution obviously ignores the capabilities of desktop browsers, but I'm not sure how to create a hash define that could use something like the useragent string to decide if we're running in a mobile browser (I don't know if that's possible).

![IMG-0934|281x500](upload://8Y78d2gp8gno2kd5URrhOpvEBzL.jpg)

-------------------------

SirNate0 | 2017-12-02 23:30:10 UTC | #6

Cool that you seem to have it working!

Regarding "how to create a hash define that could use something like the useragent string to decide if we’re running in a mobile browser," my guess is that the best approach is to actually compile it separately -- have two different web builds, one for desktop and one for mobile, and have the server give the client (browser) the appropriate one, like how some sites have separate mobile versions (perhaps [this StackExchange post](https://stackoverflow.com/questions/11381673/detecting-a-mobile-browser) points in the right direction for how to do that).

-------------------------

weitjong | 2017-12-03 02:03:49 UTC | #7

We have similar idea. It means that assumption for mobile/desktop decision needs to be changed to build option. This is where this topic interests me. :)

-------------------------

weitjong | 2017-12-03 13:31:48 UTC | #8

I have raised it as an issue. https://github.com/urho3d/Urho3D/issues/2195

-------------------------

eldog | 2017-12-07 12:25:12 UTC | #9

The problem with the Nexus 4 Android device I'm testing this on is from 2012 and doesn't support `WEBGL_DEPTH_TEXTURE`, so shadow maps are disabled (happens in  `OGLGraphics.cpp`).

three.js renders shadows on this device, my understanding is that you can have shadowmaps without a depth texture by packing a 24 or 32 bit depth value into the RGB(A) channels of a colour texture (I don't know if this is how threejs currently does it, I'm using [this blog](https://blog.tojicode.com/2012/07/using-webgldepthtexture.html) as my source on non-depth-texture shadowmaps). Not sure how feasible this is within Urho.

-------------------------

eldog | 2017-12-07 22:51:40 UTC | #10

OK got something to appear via quick and ugly hacking:

I changed [this line](
https://github.com/urho3d/Urho3D/blob/dbfbda76c3ee05f316d0b5aadf43600e43937158/Source/Urho3D/Graphics/OpenGL/OGLGraphics.cpp#L2840) in `OGLGraphics.cpp`

to be

`shadowMapFormat_ = GetRGBAFormat();`

Basically if it doesn't suppoer `WEBGL_depth_texture` then tell it to use a RGBA one.

Now I get something like a shadow... Closer, warmer.

![3938180754818538491|300x500](upload://kcXrrkkGwcD5FRGXHxTZeSQMr0g.png)

[edit]

OK the above is with VSM shadows, that's why the nonsense code of using an RGBA texture worked. As it wasn't using it all I guess.

I can't get VSM shadows to look right on WebGL desktop and mobile (see above).

-------------------------

