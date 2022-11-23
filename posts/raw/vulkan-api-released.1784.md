dragonCASTjosh | 2017-01-02 01:10:07 UTC | #1

As many of you likely know the Vulkan API was released today and it is looking good, so i thought i would start a post here for people to discus it and maybe even work on adding a Vulkan renderer into Urho. I personally would love to work as part of a joint effort to get vulkan into Urho as i feel it would help bring light to Urho and would also improve the capability of the renderer to people who wish to use it. If you have not stumbled across the Vulkan news they i will point you to the website where you can get the drivers and SDK along with some samples : [url]https://www.khronos.org/vulkan/[/url]

-------------------------

1vanK | 2017-01-02 01:10:07 UTC | #2

[github.com/SaschaWillems/Vulkan](https://github.com/SaschaWillems/Vulkan)

-------------------------

boberfly | 2017-01-02 01:10:14 UTC | #3

I'm not sure if Cadaver has the time or plans to implement this, but I'm giving it a go in a side-branch... :slight_smile:

So far, it's been easier to take the DX11 code and convert it to Vulkan rather than OpenGL, they match a lot more (fill out structs then pass it to a function). The first plan is to just get it to work in a single thread, rebuilding the command buffer each time. But then places like the View/Batch/Renderer classes will need to be retooled to allow throwing onto the threadpool and a way to cache the calls and just make a dirty flag to update it when needed. Then a whole bunch of sync/fence stuff here and there.

One thing, my Geforce GTX 765m is very buggy with Vulkan, I can only display a triangle as the other examples just segfault instantly. I'll need to wait for Nvidia to refine their driver and get out of beta (or I enable my Intel GPU), but for now I can work by just the header and how the examples work. SDL is just there to make a an OS window handle, as the WSI stuff can take over from there so no need to patch SDL for now.

The SPIR-V stuff should be straightforward if I just embed that gslang library or just make it make bytecode, similar to how the DX backends work with fxc I'd imagine.

-------------------------

cadaver | 2017-01-02 01:10:15 UTC | #4

I don't have immediate plans for the recent API's (though I'm interested), so please go ahead.

I have some skepticism though if Urho will benefit from the modern "to the metal" APIs without a lot more extensive reworks. The Graphics API is still based on D3D9 concepts at its base.

-------------------------

boberfly | 2017-01-02 01:10:15 UTC | #5

[quote="cadaver"]I don't have immediate plans for the recent API's (though I'm interested), so please go ahead.

I have some skepticism though if Urho will benefit from the modern "to the metal" APIs without a lot more extensive reworks. The Graphics API is still based on D3D9 concepts at its base.[/quote]

Yeah it is tricky to utilise the closer to the metal APIs without a lot of reworking (and not breaking D3D9 in the process) like using compute instead of the CPU to do culling as one example, or approaching the art data in a fundamentally different way when you don't have older limits (bone counts, texture units, that kind of stuff). If you look towards UnrealEngine4 it's a very DX11 deferred rendering engine, but it also supports OpenGL ES 2.0 forward rendering on the side for mobile. I guess different implementations of Urho's drawables could be made to really take advantage of the lower-level advantages you could have, and you just need to be mindful about your art assets and their intended platform (like not use some gee-whiz compute-based particle system for a D3D9/GLES2.0 target, or your new way of drawing some geometry which uses tessellation).

Some immediate big wins without too many changes would be if someone wants to do texture streaming, there's a lot more sync control here to not cause drastic pipeline stalls, or the reduction of CPU usage alone for mobile. My naive look at RenderPath/View/Renderer/Batch classes looks like I could potentially make some of their command building as worker items, and just make them strictly on the main thread when Vulkan is not the backend (this might cause some performance loss on the other backends?). I'll see how I go.

-------------------------

