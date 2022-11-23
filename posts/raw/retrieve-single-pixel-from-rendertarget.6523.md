Haukinger | 2020-11-13 15:33:43 UTC | #1

Is there a way to retrieve a single pixel from a rendertarget? I can retrieve the whole rendertarget, but it's prohibitively slow on a (slower) machine that can otherwise render the scene just fine. open gl's readpixels allows to specify an area that's not the whole screen, and I expect it to be faster if the area is smaller (i.e. only one pixel), but urho's getdata always fetches the whole screen.

My ray casting fragment shader creates a lookup from screen space to world space that I want to use to get the world coordinates at the mouse pointer.

-------------------------

Eugene | 2020-11-13 16:24:29 UTC | #2

[quote="Haukinger, post:1, topic:6523"]
and I expect it to be faster if the area is smaller (i.e. only one pixel)
[/quote]
This assumption may be incorrect. Or only partially correct.

First of all, you can try to do just that — get one pixel via GL commands and see if it’s faster.

Or you can render one pixel of your texture to 1x1 render target using custom shader and then read whole 1x1 texture .

-------------------------

JSandusky | 2020-11-15 04:47:57 UTC | #3

Eh? You can't fetch one pixel any faster than the whole target, it has to transition to a CPU readable state or blit over to another source that is readable. 

There is no "cheap 1 pixel read." Not in GL, not in DX9, not in DX11, not in DX12, not in Vulkan, etc. You have to use compute to isolate your target and write that to your target read back and if you're not doing it on the transfer queue you stall everything. You accept latency and just use the transfer queue with your code sitting on the fence you have.

WTF does a read of an unresolved MSAA target even look like?

-------------------------

