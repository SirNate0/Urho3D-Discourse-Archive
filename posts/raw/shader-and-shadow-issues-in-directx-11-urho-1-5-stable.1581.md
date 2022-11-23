gawag | 2017-01-02 01:08:40 UTC | #1

Maybe this is already known:
[img]http://i.imgur.com/iyKDi3y.jpg[/img]
Those black lines are only there in DirectX 11. OpenGL and DX9 work fine.

Sometimes this is accompanied by errors such as:
[quote][Mon Dec 14 14:20:25 2015] ERROR: Failed to create input layout for shader Shadow(), missing element mask 8
[Mon Dec 14 14:20:25 2015] ERROR: Failed to create input layout for shader Shadow(SKINNED), missing element mask 8
[Mon Dec 14 14:20:26 2015] ERROR: Failed to create input layout for shader level_1_terrain(DIRLIGHT PERPIXEL SHADOW VERTEXCOLOR), missing element mask 8[/quote]
(these errors are from a different project with custom shaders)

The black line appear in this project: [github.com/gawag/UrhoSampleProject](https://github.com/gawag/UrhoSampleProject)
It only uses default shaders&techniques.
That terrain is the default Urho terrain (same material&textures).

The printed errors seem to depend on the Urho version. Some GitHub pulls have them, some not. There seems to be some activity in that area in the last days.
But what about the lines?

The Urho samples look fine.
The lines are also there when removing the skybox, the planet, the torch (with it's light source and effects), the postprocess effects and the sun billboard.

-------------------------

cadaver | 2017-01-02 01:08:40 UTC | #2

This will need to be documented (I thought it already was), but it's a limitation of D3D11. A model will not render if the shader uses vertex attributes it doesn't have. The error tells you which element is missing.

[code]
static const unsigned MASK_TEXCOORD1 = 0x8;
[/code]

E.g. the LitSolid shader allows the NOUV define to prevent reading texture coords, and this is defined by the NoTexture family of techniques, but the shadow shader presently doesn't have this.

Those lines look like shadow acne, which would point to shadow bias not being strong enough.

EDIT: use of NOUV is added to Shadow & Depth shaders in the master branch.

-------------------------

gawag | 2017-01-02 01:08:41 UTC | #3

Ah the shadow bias again. Didn't think of that due to OpenGL and D3D9 being fine. Me and those shadow parameters... Had a thread about that quite a while ago.
Changed the bias from 0.00000025 to 0.00002 and the stripes are gone.
Is there some kind of rule of thumb how to set those parameters? Now the shadows are starting too far away from the model (peter paning) and that's quite depending on the looking angle and position (flickering).
Currently my parameters are 
light->SetShadowBias(BiasParameters(0.00002f,0.5f));
light->SetShadowCascade(CascadeParameters(10.0f,50.0f,200.0f,400.0f,0.8f));
If the first parameter is higher (like 0.0002) there are no more shadows. If it's lower (like 0.000002) the stripes are there again.
The second bias parameter doesn't seem to change anything.
Found this: [docs.unity3d.com/Manual/ShadowOverview.html](http://docs.unity3d.com/Manual/ShadowOverview.html) Though in my case there are either stripes or peter paning, or both at the same time. Is there still no solution to this?

Looking into the error issue later.

-------------------------

bvanevery | 2017-01-02 01:08:43 UTC | #4

BTW I definitely had a CMake stale build issue on this today, on my cheesiest Intel integrated GPU laptop.  Pulled what I thought was new Urho3D, built and installed it but not cleanly.  Ended up with a log full of errors about read-only depth stencil.  Knew that was impossible for a recent build because my other machine had those demoted to warnings only and rendered fine.  Nuked my Urho3D build and install directories, nuked UrhoSampleProject build directory, built everything from scratch.  Now everything works fine.

Moral of the story is CMake can only handle so much "automatic" adjustment of the build.  I think, especially if the CMake build itself changes much, it'll eventually just barf.  That's why one does out-of-source builds, so it's easy to nuke the build and start over clean.

I'm surprised that both the AMD and Intel integrated GPUs are running at 10 FPS, whether in Debug or Release.  The AMD part has been consistently 2x faster than the Intel on other tests, like Unigine Valley.  I suppose it's possible that Urho3D's shadowing exercises GPU capabilities that are equally crappy on both though.  I will drag out my bigger laptop that has a dedicated NVIDIA GeForce 8600M GT in it, to see if it runs any faster.  All 3 machines have roughly similar CPU-side capabilities.

GeForce does 15+ FPS in Debug and Release.  So, faster, but not fast.  I know this is old HW but I had hoped for better on seemingly such a trivial demo.  I do recall various DirectX SDK demos that choked the crap out of that card back in the day though.  Now I suppose I can learn what all my cheesy old HW can and cannot do.

I don't know if it's related to the performance, but this is all DX10 or DX10.1 class HW, running a DX11 API on top of it.  [url=https://mynameismjp.wordpress.com/2010/11/14/d3d11-features/]This says[/url] read-only depth-stencil views were introduced in DX11, so my HW may not be able to support simultaneous writeable and read-only views.
[quote]
4. Read-only depth-stencil views: D3D10 let you bind depth-stencil buffers as shader resource views so that you could sample them in the pixel shader, but came with the restriction that you couldn?t have them simultaneously bound to the pipeline as both views simultaneously. That?s fine for SSAO or depth of field, but not so fine if you want to do deferred rendering and use depth-stencil culling. D3D10.1 added the ability to let you copy depth buffers asynchronously using the GPU, but that?s still not optimal. D3D11 finally makes everything right in the world by letting you create depth-stencil views with a read-only flag. So basically you can just create two DSV?s for your depth buffer, and switch to the read-only one when you want to do depth readback.[/quote]

-------------------------

