simonsch | 2018-03-21 15:12:04 UTC | #1

Hello community, 

some of you already know, i use Urho3D for mobile devices. This mean OpenGL ES, more specific OpenGL ES 2.0. I came from the pure OpenGL ES 3.0 world and i wrote all my shader code for the corresponding shader versions. I am now making everything downwards compatible (Using varyings again, etc...).

At one function i am not sure how to proof if this would work the modulo function. In my GLES 3 shader code (#version 300 es) i was able to call 'a%b'. I saw this will not work with GLES 2 so i wanted to implement it myself.
    
    int mod(int a, int b)
    {
       return a - (b * floor(a/b));
    }

But there is no 'floor' or 'round' function as well so i did 
    
    int mod(int a, int b)
    {
       return a - (b * int(a/b));
    }

Now i don't know if this is valid shader code and i cannot test it in a fast way cause it is used in a very complex shader, maybe someone can tell me if this is valid and if not what are the alternatives?

-------------------------

Eugene | 2018-03-27 11:30:34 UTC | #2

[quote="simonsch, post:1, topic:4113"]
Now i don’t know if this is valid shader code
[/quote]
It doesn't do what you wish, so it's not.

I suppose that GLES2 hardware may not have integer ops.
If you are sure that only small ints are used (<1kk), you could use float division and then `floor` it. Or just use float `mod`.
Or maybe you have some hashing stuff and this is impossible?

This is quite offtopic, but have you tried to make GLES 3 context in Urho?

-------------------------

simonsch | 2018-03-22 08:21:08 UTC | #3

> This is quite offtopic, but have you tried to make GLES 3 context in Urho?

I would wish to but i thought the engine is not capable of GLES 3. I will try to enable it via AndroidManifest and will see what happens. Maybe this will work with SDLSurfaceView or not. Do i need to change the version anywhere else as in the manifest?

I think modulo is not the only function i am missing. Can you recommend any good comparison for GLES 2 and 3?

I set
    
    <uses-feature 
        android:glEsVersion="0x00030000"
        android:required="true" />

when i try to change my glsl shader version to

    #version 300 es
i get

    ERROR: Invalid #version

-------------------------

Eugene | 2018-03-22 08:27:18 UTC | #4

[quote="simonsch, post:3, topic:4113"]
I think modulo is not the only function i am missing. Can you recommend any good comparison for GLES 2 and 3?
[/quote]

If I understood you correctly...
I usually use official specs to check things
https://www.khronos.org/registry/OpenGL-Refpages/es3.0/

It's pretty clear what's supported, e.g. [cos](https://www.khronos.org/registry/OpenGL-Refpages/es3.0/html/cos.xhtml) and [cosh](https://www.khronos.org/registry/OpenGL-Refpages/es3.0/html/cosh.xhtml)

[quote="simonsch, post:3, topic:4113"]
I would wish to but i thought the engine is not capable of GLES 3
[/quote]
Well, GLES version is just a number. Engine could be capable or not to support certain features of GLES 3 tho, but shader language shan't be the case.

[quote="simonsch, post:3, topic:4113"]
Do i need to change the version anywhere else as in the manifest?
[/quote]
IDK, will check it.

**Update:**
At least there
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/OpenGL/OGLGraphics.cpp#L382

-------------------------

simonsch | 2018-03-22 08:46:02 UTC | #5

Did change the SDL_GL_CONTEXT_MAJOR_VERSION to  as well no success. Sry, i am not that experienced with computer graphics. (One of the reasons i am here using urho3d) :smiley:

But i thought there is a direct correspondence between the GLES version and the version of the shader language.

The
> #version 300 es

is working with my old stringified shader which i load via cpp and used with opengl. So it can work on Android and on this specific device.

> If I understood you correctly…
I usually use official specs to check things
https://www.khronos.org/registry/OpenGL-Refpages/es3.0/

I thought there is maybe a site where i can see 'This feature only gles3 -> not gles2'. E.g.: idk if it is supporter by the actual shader version to use:
    
    void func(in vec4 a, in vec4 b, out vec4 c, out int n)

-------------------------

Eugene | 2018-03-22 09:09:40 UTC | #6

[quote="simonsch, post:5, topic:4113"]
Did change the SDL_GL_CONTEXT_MAJOR_VERSION to  as well no success
[/quote]

So, the shader still doesn't compile because of wrong version?

[quote="simonsch, post:5, topic:4113"]
is working with my old stringified shader which i load via cpp and used with opengl. So it can work on Android and on this specific device.
[/quote]
Do you mean that you have some sample GLES application to check things?

[quote="simonsch, post:5, topic:4113"]
I thought there is maybe a site where i can see ‘This feature only gles3 -&gt; not gles2’.
[/quote]
For me this is enough...
![image|690x88](upload://6kcK0gp5GKNNSbpVB1VhAXdOHDS.png)

**UPDATE**
One more thought... Try to add this line too
`SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_ES);`

-------------------------

simonsch | 2018-03-22 09:23:46 UTC | #7

The issue with the shader version persists, does i need to call     
     
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 3);
from OGLGraphics.cpp and rebuild the whole engine? Or can i set it from outside, eg. int the jni cpp callbacks of sdl?

> Do you mean that you have some sample GLES application to check things?

So i will try to describe where i come from. I created a mobile application with Android NDK and JNI as my glue between java and cpp code. My first attempt to render output was using a GLSurfaceView which define my egl context in combination with c++ opengl bindings and stringified glsl shader code. To make things more simple and robust i decided to use urho3d. 
So i started to port my rendering pipeline to urho3d, which made it necessary to change my GLSurfaceView to a SDLActivity with its own surface view, which inherits from a SurfaceView. The shader code which was working with the first approach seems to be not supported due to the described version issues of the GL Shading Language.

-------------------------

Eugene | 2018-03-22 09:29:59 UTC | #8

[quote="simonsch, post:7, topic:4113"]
from OGLGraphics.cpp and rebuild the whole engine?
[/quote]

This. Set `SDL_GL_CONTEXT_MAJOR_VERSION` where it's set now. Probably, it's better to set `SDL_GL_CONTEXT_PROFILE_MASK` too, in the same place. And build Urho, yes.

-------------------------

simonsch | 2018-03-22 10:44:32 UTC | #9

I changed the lines in OGLGraphics but i still get the error. :confused:

-------------------------

Eugene | 2018-03-22 10:51:34 UTC | #10

That sucks -_-
Maybe it's more tricky to make SDL create GLES 3 context than I thought.
I used this code as reference
 https://github.com/josh43/SDL2-GLES-3-Demo/blob/master/SDL2-GLES-3-Demo-testing/main.cpp#L315

-------------------------

simonsch | 2018-03-22 11:50:44 UTC | #11

Okay, i think i will just try changing my code from 3.0 to 1.0 Shading Language. You suggestion with the 'floor' function works now, will have to figure out some other issues as well. 

Thx for the support!

-------------------------

simonsch | 2018-03-22 15:34:37 UTC | #12

It is me again, didn't want to create an additional thread. My shader code is running now, it only remains one crucial problem.

I have to block interpolation of some variables from my VertexShader to my PixelShader. Normally this would be really easy i would use the qualifier 'flat', which prevents the interpolation after rasterization for those values. Any suggestion how to workaround in this lower version of the Shading Language?

-------------------------

Eugene | 2018-03-22 16:21:49 UTC | #13

There's no generic way to workaround `flat` modifier.
It was asked before to add GLES3 support, so I'll look into this direction. Will try something this weekend. IDK why you weren't able to create GLES3 context tho.

-------------------------

Sinoid | 2018-03-27 11:30:35 UTC | #14

@Eugene in case you missed it:

https://github.com/urho3d/Urho3D/issues/1545 

Towards the end there's some commits for GLES3, I don't believe it's usable as-is looked like he went a little nuclear with it instead of coexisting with GLES2. All-in-all though looked pretty simple ... I was going to get to it eventually in wrapping up GS/HS/DS once I was testing on mobile.

-------------------------

Eugene | 2018-03-25 12:42:20 UTC | #15

Have you tried commits mentioned by @Sinoid?
These changes look both small and legit so I wonder if it helps to make gles3 work.

-------------------------

Sinoid | 2018-03-25 18:23:55 UTC | #16

Not yet, haven't made a droid build for like 2 years - dreading it.

You're right though, just looks like the shader version stuff (pushing the #300) that's nuke. There's probably some other GLES ifdefs that need some tweaks, the depth texture stuff being the big one I can think of that might.

-------------------------

Eugene | 2018-03-25 18:27:10 UTC | #17

[quote="Sinoid, post:16, topic:4113"]
dreading it.
[/quote]
Hah, the same thing. Don’t know why, just don’t want to go through this pipeline.

-------------------------

simonsch | 2018-03-27 09:27:50 UTC | #18

So what does that mean? Any updates so far? Would be still a huge plus for me if i can use latest language features of shading language.

As far as i know ES3 i very common on mobile devices these days, isn't it?

(In the mean time i will try the referenced commits)

-------------------------

simonsch | 2018-03-27 11:30:11 UTC | #19

I can confirm it is working for me with the mentioned commits, thy you all for your effort :). Hope to see it by default enabled in the engine in the future.

-------------------------

Eugene | 2018-03-27 11:57:02 UTC | #20

[quote="simonsch, post:19, topic:4113"]
I can confirm it is working for me with the mentioned commits
[/quote]
Thanks! Since you confirmed that it works, I'll try to pick these commits and somehow integrate them into Urho3D core.

-------------------------

