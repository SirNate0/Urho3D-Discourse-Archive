hvince95 | 2018-03-16 22:50:15 UTC | #1

I've been trying to include Alchemy ambient occlusion by reattiva ([https://discourse.urho3d.io/t/alchemy-ambient-occlusion/662](https://discourse.urho3d.io/t/alchemy-ambient-occlusion/662)) in my project but upon porting the Angelscript code to C++ I get these warnings/errors in the log file:

    [Sat Mar 17 09:02:54 2018] WARNING: Deprecated rtsizedivisor mode used in rendertarget definition
    [Sat Mar 17 09:02:54 2018] WARNING: Deprecated rtsizedivisor mode used in rendertarget definition
    [Sat Mar 17 09:02:54 2018] WARNING: Deprecated rtsizedivisor mode used in rendertarget definition

    [Sat Mar 17 09:02:54 2018] ERROR: Failed to compile pixel shader SAO_main(NORMAL_MAP):
    D:\Ares\Shaders\HLSL\SAO_main.hlsl(111,20-51): error X3004: undeclared identifier 'Sample'

The error corresponds to this line in the shader: Sample(sDepthBuffer, iScreenPos). This SAO implementation is quite old, is it possible that this method was removed in an older version DirectX?

If this SAO implementation is outdated, is there another option for me? (please let me know if you would like to see my ported code, I am just unsure where to host it)

-------------------------

Sinoid | 2018-03-17 02:43:46 UTC | #2

`Sample` is the old name, it's `Sample2D` now.

> is it possible that this method was removed in an older version DirectX?

No, it's an Urho3D specific macro that's used to conceal the differences between DX9 tex2D and DX11's SRVObject.Sample2D.

>  I am just unsure where to host it

When you need to do that use pastebin or hastebin.

-------------------------

hvince95 | 2018-03-17 02:06:18 UTC | #3

Thanks very much I think that solved the problem. Is there anywhere where these sort of things are documented? I get a similar error in the same file with
`undeclared identifier 'ssDepthBuffer'`
now and it would be great if I had some sort of reference to go to.

-------------------------

hvince95 | 2018-03-17 02:46:00 UTC | #4

okay, sDepthBuffer = DepthBuffer. this sovled the issue :slight_smile: Thanks again for your help. My aim now is to make it a little less grainy!![grain|690x484](upload://cnxbA98sW6AJMdtdU9kPZrDW8op.png)
Other than that, the positions look correct!! YAY!

-------------------------

Sinoid | 2018-03-17 03:02:59 UTC | #5

> My aim now is to make it a little less grainy!

Isn't that what the blur passes/shaders are for in the render-path?

-------------------------

hvince95 | 2018-03-17 03:42:51 UTC | #6

Yes, all is working well now

-------------------------

