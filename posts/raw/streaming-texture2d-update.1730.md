dakilla | 2017-01-02 01:09:45 UTC | #1

Hi

First, I'm new to Urho3D, and I want to say that is a really great engine, so nice work guys. I finally chose this engine after months of testing most of actual 3d engines to get the best that fit my needs for building my project.

In a part of my tool, I'm using a procedural texture generator and I need to upload texture data in streaming to get result in realtime. I'm actually using the Texture2D::SetData to update my texture, I don't know if there is another way to update texture data in Urho, but like this, it is a bit slow for streaming. Is there a better way ?

After looking code in this function (opengl part), I think it may be usefull to have an additional lock/unlock mechanism (like in VertexBuffer) to map pixel buffer. If yout want, I can work on this feature for opengl part (I don't know directx framework). 

Any advice or better idea ?

-------------------------

codingmonkey | 2017-01-02 01:09:45 UTC | #2

>Is there a better way ?
use in-shader computation for procedural textures (I mean do not use textures for this in some cases)
also you may use low-res textures from CPU filled side as parameterization for GPU-generated texture (something like - guidelines, or map for generation in shader)

-------------------------

Enhex | 2017-01-02 01:09:47 UTC | #3

What do you mean by streaming?
There's no need to update more than once every frame.

-------------------------

dakilla | 2017-01-02 01:09:48 UTC | #4

> use in-shader computation
Yes it is planned, but I already have a library that use cpu texture generation and I'd like to use it too.
This library has been already used in others frameworks and it is enough fast. However I encountered some slow-down in Urho when using Texture2D::SetData (I used it max once per frame). 
glTexSubImage2D seems to block, I going to debug it today to see where is the problem.

> What do you mean by streaming?
I think about something like that : [songho.ca/opengl/gl_pbo.html#unpack](http://www.songho.ca/opengl/gl_pbo.html#unpack)

-------------------------

thebluefish | 2017-01-02 01:09:48 UTC | #5

glTexSubImage2D shouldn't be causing those kinds of slowdowns. Maybe there's something messed up with the pixel format? If the format doesn't match, the driver has to block while it converts (AFAIK) which can cause some slow-downs. I've had great success in the past with sub-ms updates in a standalone OGL app, so this is worth investigating.

Several posts on gamedev.net reference the following "golden rule":

internalformal: GL_RGBA
format: GL_BGRA
type: GL_UNSIGNED_INT_8_8_8_8_REV

-------------------------

dakilla | 2017-01-02 01:09:48 UTC | #6

I solved my problem. This was a fu... bug with Qt 5.5.1. 
My editor use Qt and I migrate from 5.4 to 5.5.1 since few days, same as I started to port my tool to Urho.... 
It seems that the new 5.5.1 version is bugged somewhere with the connect slot/signal on linux (it's ok on windows).. The slot that update my texture started to slow down at some point in the event queue. I restored 5.4 version and all is fine now.

So during my debug I tested some stuff, I didn't benchmark but I didn't see any major speed gain by using :

- internalformal: GL_RGBA | format: GL_BGRA | type: GL_UNSIGNED_INT_8_8_8_8_REV
- glTexImage2D instead of glTexSubImage2D
- GL_PIXEL_UNPACK_BUFFER and glMapBuffer

-------------------------

Enhex | 2017-01-02 01:09:52 UTC | #7

Qt's slot/signal system is a hack.

-------------------------

