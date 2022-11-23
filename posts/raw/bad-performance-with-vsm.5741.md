GoldenThumbs | 2019-12-01 08:50:19 UTC | #1

So, I'm not sure if this is just an issue I've had, but VSM seems to be very VERY finicky, and half the time causes huge performance drops. This seems very strange to me because (from my understanding) it's supposed to be the more performant method of shadow mapping. Using the blurred version of it changes it from a *chance* of running bad to a guarantee of running slow. I've tried this on plenty of different PCs, with GPUs ranging from literally nothing to a GTX 1660 TI. The results are always the same. Anyone else having this issue? Is it only with the OpenGL renderer? I haven't tested this with DirectX yet, but I feel the result won't be much different.

-------------------------

Modanung | 2019-12-02 18:57:17 UTC | #3

Setting the `Renderer`'s shadow quality to `SHADOWQUALITY_BLUR_VSM` indeed does drop the frame rate quite significantly.

-------------------------

Sinoid | 2019-12-09 05:08:15 UTC | #4

IIRC VSM is platform dependent in implementation to be decent since you're cheating to begin with. DX11 should be faster here since this is about FBOs and OpenGL sucks there due to fallback after fallback after fallback but it's still going to be bad because the VSM code is done through the Urho3D graphics abstraction rather than being and internal part of it.

The DX11 renderer is always faster than the OpenGL one, sometimes by a massive margin.

I'd grab a known good VSM demo and run both it and your Urho3D project through RenderDoc and check the states when shadows are processed to see if there's anything peculiar standing out regarding the FBO or the final stage when the shadows are being rendered to shadowmaps.

Note: VSM uses R32G32+z so it's going to be much much slower than regular shadowmaps, it's a fat 128-bits after your driver touches it IIRC. You could try changing that to R16G16 to see if it helps in `Renderer::GetShadowMap`.

-------------------------

