coldev | 2017-08-11 11:41:07 UTC | #1

Nice day for everyone..

I am newbie in urho3d..

i have any questions ...

1. set resolution and fullscreen in runtime (game in pause, or running)

2. i am working in a wrapper for other language called bennugd , uses sdl 1.3 , i pass window handle to urho3d and all work ok.. but ... when urho3d finished destroy current window context handle... is possible not destroy this ..how ?  i use sdl to restore window , but is possible not destroy window handle / context to finish? 

2. in skeletal animation example is possible instancing all models to best performance ?

3. somebody haves a gpu skinned mesh example in urho3d?
[https://www.youtube.com/watch?v=GjNNiw8oJ50](https://www.youtube.com/watch?v=GjNNiw8oJ50)

4. using imposter with animated billboards ... exists any example?

 Thank you very very much

Cheers

-------------------------

1vanK | 2017-08-11 11:39:21 UTC | #2

[quote="coldev, post:1, topic:3439"]
set resolution and fullscreen in runtime (game in pause, or running)
[/quote]

Graphics::SetMode()

> when urho3d finished destroy current window context handle

try Graphics::SetExternalWindow()

-------------------------

cadaver | 2017-08-11 14:50:27 UTC | #3

Not sure if you can even destroy the context in SDL below 2.0. Was a long time since I used it. If Urho is used in Direct3D9/11 mode, it will destroy the D3D context even if it uses an external window handle, but in OpenGL mode with external handle, it expects to be passed a functioning GL context along with the window, and it doesn't attempt to destroy it, since that would be OS-specific.

https://stackoverflow.com/questions/12050234/closing-an-sdl-window-without-quitting-sdl

-------------------------

coldev | 2017-08-11 14:56:36 UTC | #4

Thanks 4 your reply..  

Last Question,

Is possible in URHO3D  instancing  "Skeletal Animation Example" in urho3d
to show more models , how this ..

[https://www.youtube.com/watch?v=GjNNiw8oJ50](https://www.youtube.com/watch?v=GjNNiw8oJ50)

exists a example for that?  

Thanks

-------------------------

SirNate0 | 2017-08-11 15:35:00 UTC | #5

Presently, no, I don't think that form of instanced animation is supported, as the example in question uses a compute shader to calculate the needed buffers, yet presently I don't think Urho supports compute shaders, though some forks may have integrated them (see, for example, the discussion [here](https://discourse.urho3d.io/t/rasterized-voxel-based-global-illumination/2115/13)).

-------------------------

coldev | 2017-08-11 22:37:35 UTC | #6

Use ogre3d instancing code is possible ?  port ogre3d instancing code to urho3d ?

urho3d  grass example use hardware static instancing?

-------------------------

