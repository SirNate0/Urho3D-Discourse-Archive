AGreatFish | 2017-01-02 00:59:15 UTC | #1

Hi, I am a noob when it comes to Urho3D and game development in general, so this is probably a very noobish question  :laughing: 

I am working on a shader which requires me to know the dimensions of the window.

I know that I can pass this information to the shader using a Shader Parameter, but I was wondering if there is a "proper" way to do this (as I would have to update that parameter each time the window size changes). E.g. I thought that cGBufferInvSize was something that I could use for this but it doesn't seem to give me the right results.

If the proper way to do it is to change the value manually from the game code, I would like to know if there is a resize event that I can subscribe to, to do so ?
Currently I know how to set the proper size at startup and how to update it each frame.

Once that stuff works properly, I may have something to show you that may or may not be useful for other Urho3D users  :mrgreen: 

PS:
Thanks for creating such an awesome open source engine  :slight_smile: 

It's really the only engine (that's not dead) I found that offers all of the basic features I expect to need while still being simple to use and understand due to its clean source code and decent documentation.
Being able to develop an application in C++ using the tools that the engine offers in a relatively straightforward manner is something that I have been searching a long time for.
Most engines either don't have enough features, are complicated to use, or make you modify a "template game" in a scripting language.

So keep going ! You have created an awesome and unique engine  :wink:

-------------------------

cadaver | 2017-01-02 00:59:15 UTC | #2

Welcome!

The pixel shader uniform cGBufferInvSize is indeed the inverse size (x & y) of the viewport texture. You can inverse that further if you need the actual size. Note that if you have a viewport that's smaller than window, it's not giving the whole window size, but only the viewport, as you'll never be sampling the actual backbuffer, but a viewport-sized copy of it.

What do you need the window size for? If you need to sample the viewport texture eg. for postprocessing see the shader function GetScreenPos() or GetScreenPosPrediv() for getting the UV coordinates in the vertex shader. For a simple example, see the greyscale postprocess shader (Bin/CoreData/Shaders/HLSL/GreyScale.hlsl). For a more complicated example that uses the viewport inverse size to offset to adjacent pixel samples, see the FXAA shader (Bin/CoreData/Shaders/HLSL/EdgeFilter.hlsl)

If you want to go the other route (manual uniform), the screen resize event is ScreenMode (E_SCREENMODE) defined in Source/Engine/Graphics/GraphicsEvents.h.

-------------------------

AGreatFish | 2017-01-02 00:59:15 UTC | #3

It seems like I was overcomplicating things  :smiley: 

I tried to do all kinds of weird stuff to cGBufferInvSize to make things work, when in truth, I needed cGBufferInvSize itself without any modification  :laughing: 

So things are working decently now, thanks for the help  :wink: 

As for what I am needing it for:
[topic253.html](http://discourse.urho3d.io/t/fxaa-3-11/267/1)

-------------------------

