GoogleBot42 | 2017-01-03 07:35:19 UTC | #1

The title says it all.  Can we add support for Add support for WebGL 2 and OpenGL ES 3.0?  I particularly want this because I want to use texture arrays on the web and smart phones.  Thanks!

-------------------------

artgolf1000 | 2017-01-04 00:21:56 UTC | #2

I noticed the discussion on the issue report block of Github, developers tend to keep OpenGL ES 2.0 at present. 

You can use a big texture to simulate texture arrays in OpenGL ES 2.0, it's not difficult, you just need to add offsets to get sub-textures.

-------------------------

boberfly | 2017-01-06 23:02:39 UTC | #3

I've got ES 3.0 to work with Urho in an old branch from last year, I'll see if I can resurrect. It's quite straightforward, pretty much all the GL3 checks already present in the codebase to compare with GL2 are the checks you'd want when going from GLES2 to GLES3 from what I remember, same for the shaders (this can be dynamic also as GLES3 is pretty much an extension to GLES2). You also need to re-enable multiple render targets with a check as GLES3 can do these now, using the same GL3 check but wrapped in a pre-processor define.

SDL needed patching as the EGL backend wasn't working at least on Android and I needed to hard-code it to get the right context, but this was SDL 2.0.3 at the time? Might be fixed now.

-------------------------

GoogleBot42 | 2017-01-08 01:45:53 UTC | #4

I probably will just do as artgolf suggested.  Thanks though.

-------------------------

godan | 2017-04-21 00:10:58 UTC | #5

So, I've just run up against this - what is the status with ES 3.0? Since it is kind of urgent for me, I'm happy to do the work. @boberfly Would it be possible to outline the steps you took in more detail?

Just wrote a bunch of shaders with [fwidth](https://www.khronos.org/registry/OpenGL-Refpages/es3.0/html/fwidth.xhtml), and found out that they are not supported :frowning:

-------------------------

boberfly | 2017-04-28 18:27:26 UTC | #6

Ahh just noticed this tag @godan

Basically the easiest approach was to use the already existing runtime-tested GL3 conditionals in the codebase for the desktop and apply them to the mobile/GLES2-only parts also, as many of the changes from GLES2 to GLES3 are similar for desktop GL2 to GL3 give or take. This goes for the shaders also with some pre-processor defines. SDL2 at the time didn't make a GLES3 context properly with extensions so I had to hack that to make one for me on Android, but maybe that's fixed now?

All in all it wasn't too difficult actually, due to the groundwork for the GL3+ port, although the Android SDK wasn't all there then to debug...

-------------------------

