smellymumbler | 2017-05-30 14:02:22 UTC | #1

I called that method on my DebugRenderer, but the lines are still jaggy. Is there any special step needed?

-------------------------

jmiller | 2017-06-02 17:08:39 UTC | #2

SetLineAntiAlias() should take effect immediately.
It is hardware-dependent and I think it's ignored on OpenGL ES 2.

Apparently, hardware-drawing very nice lines (in OpenGL at least) is not as simple as we might expect.
  https://www.codeproject.com/articles/199525/drawing-nearly-perfect-d-line-segments-in-opengl
(*I tried adding the glHint(GL_LINE_SMOOTH_HINT,  GL_NICEST) to OGLGraphics, but did not notice a difference.)

Urho's FXAA does pretty well, but is not exactly fine-grained.

I seem to recall the 'lines' subject popping up before, so maybe someone has made a share.

-------------------------

smellymumbler | 2017-06-03 15:10:29 UTC | #3

I tried on more powerful hardware, but still had the same issue. I'll try on a Windows machine later and post the results.

-------------------------

smellymumbler | 2017-06-06 13:52:28 UTC | #4

Also happens on Windows. Has anyone successfully used this feature?

-------------------------

1vanK | 2017-06-06 16:05:31 UTC | #5


<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/5c627b223b91ffa9fd5523ecbdbee790862d7c69.png" width="690" height="339">
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/90791bf39f3ac71f37158aa8e62a950c0e4aed5a.png" width="690" height="292">

-------------------------

