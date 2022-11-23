atai | 2017-01-02 01:09:17 UTC | #1

On some devices or machines, more than one type of OpenGL or OpenGLES is supported.  For exmple,l latest iphone supports OpenGLES 2 and 3, while on the GNU/Linux desktop OpenGLES 2 works as well (although one would normally use OpenGL instead of GLES there).

Is there a way to select the type of OpenGL (ES) used in Urho3d?   One thing I know is that OpenGL ES 2 seems the most widely supported OpenGL variant from mobile to the desktop, and using the same GL can mean the most common platform-which can be useful for development purposes, developing on the desktop and thing would work the same way on devices.

-------------------------

cadaver | 2017-01-02 01:09:17 UTC | #2

Currently when it's a GLES platform, it will always be GLES2. On desktop code for both GL2 & GL3 is compiled in and it detects it at runtime (GL3 will be used if available, but you can configure Graphics to not do that - see the -gl2 commandline switch)

We have a pull request for SDL2.0.4 which will bring GLES3 support too. I haven't studied yet how it configures what to use.

-------------------------

atai | 2017-01-02 01:09:18 UTC | #3

Thanks for the reply.

For what I mean, this page [mepem.com/pemcode/?p=35](http://mepem.com/pemcode/?p=35) is a good example.  It shows how to use OpenGL ES 2 from SDL.  Since Urho3d is built on top of SDL, I may try the setup as described in that page applying to Urho3d. I would think everything should just work on desktop platforms that support OpenGL ES 2 (the current GNU/Linux and Mac OSX, for example) if somewhat less optimally than using Open GL 2 or 3 (but for my purpose that is OK)

-------------------------

atai | 2017-01-02 01:09:20 UTC | #4

This works; I can use OpenGLES 2.0 on the desktop and the examples work the same (or at least look the same)

-------------------------

