megapunchself | 2018-08-13 23:34:53 UTC | #1

reading a post here, a doubt is in my head

for curiosity:
is possible to change the opengl api to opengl 1.4 or 1.3 and gles 1.0? is hard to do this? more or less how?

i know that ogl 1.4 and gles 1.0 won't use shaders, shaders are created by u coding, and the code is "super" different comparing to the current
with 1.4 we create games like a ps1 and ps2 game
i know that this graphics are deprecateds, but using this in good computers and a good game project manager, programmer and artist
we have a huge performance to a good game

as i know, the differences occurs between:
- 1.4 - more or less compared to directx8 and 8.1
- 2.1 - more or less compared to directx9 and 10
- 3.3 - more or less compared to directx11 and 11.2
- 4.5 - more or less compared to directx12 - more or less compared to vulkan

if we got 2.0 and 3.2, gles 2.0 and webgl, why not?

-------------------------

cadaver | 2018-08-14 07:49:59 UTC | #2

All of the rendering code assumes use of DX9 / GL2-level of shaders at minimum. So you'd be looking at a large rewrite of the rendering code.

It's certainly possible, but I doubt it's worth it. In high-spec machines using fixed function is unlikely to gain you much, and for actual low-spec hardware you should also check whether Urho's CPU level algorithms (like culling) are suitable.

Also fairly sure the project itself isn't interested in that direction, so you'd be on your own.

-------------------------

