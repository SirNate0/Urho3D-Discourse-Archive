dwlcj | 2017-01-02 01:13:06 UTC | #1

All hi, I noticed urh3d support HTML5,on windows Google chrome  run the official website example is fine, but on iPhone OS Safari browser is running not successful.
urh3d emscripten support Safari?
sorry, my English is not well.

-------------------------

Modanung | 2017-01-02 01:13:06 UTC | #2

Do you have [url=http://get.webgl.org/]WebGL support[/url]?

-------------------------

dwlcj | 2017-01-02 01:13:07 UTC | #3

Hello Modanung. Safari work it,the return value "Your browser supports WebGL".

-------------------------

Sir_Nate | 2017-01-02 01:13:08 UTC | #4

It is possible that it is too large for mobile. When I try running, e.g. the Physics Stress Test Sample (12), my (android) phone (with Chrome) gives "Aw, Snap! Something went wrong while displaying this webpage", I assume (though I'm not certain) because it tries to use too much memory (as it crashes after downloading for a while). webglsamples.org's aquarium works fine for me, though.

Consider just building for iPhone/Android directly (my project does not crash when built as an Android app). I would strongly recommend against using Emscripten to target a mobile platform. You're already dealing with more limited specifications in terms of processors and RAM, the additional slowdown caused by interpreting JS instead of running native code seems inadvisable.

Has anyone tested with desktop Safari?

-------------------------

dwlcj | 2017-01-02 01:13:08 UTC | #5

Hello Sir Nate:
in OSX May not be successful, but I have not tested.
and in My iPhone return "Exception thrown, see JavaScript console".

-------------------------

Sir_Nate | 2017-01-02 01:13:16 UTC | #6

I tested with a virtual machine -- Emscripten seems to work on Safari, as [url]http://www.iforce2d.net/embox2d/testbed.html[/url] worked fine. However, the Urho Physics Sample (11) failed (and it's a release build on the website with Exception Catching disabled, so I've no idea what from). Another site ([url]sol.gfxile.net/ocornut_demo/imgui.html[/url]) also failed, as it was unable to create a canvas, with an error thrown with GLctx.getParameter, so it could be with the webGL with Emscripten.

One thing to note is that for at least desktop Safari, WebGL is disabled by default (which I would count as supporting, especially if the site you checked on only looks at the User Agent string).
Once I enabled WebGL, it half worked -- it displayed o a black screen with white boxes for the text -- "WebGL: drawElements: texture bound to texture unit 0 is not renderable. It maybe non-power-of-2 and have incompatible texture filtering or is not 'texture complete' and earlier "WebGL: INVALID_ENUM: texImage2D: depth texture formats not enabled" followed by Urho's "ERROR: Failed to create texture" (earlier still: "WebGL: INVALID_ENUM: compressedTexImage2D: invalid internalformat"). The WebGL errors are in native code, so I would assume it is actually a compatibility issue with Safari's WebGL implementation.

-------------------------

