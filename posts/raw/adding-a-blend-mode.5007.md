ab4daa | 2019-03-08 01:49:01 UTC | #1

I want to add a blend mode equivalent to `self.gl.blendFuncSeparate(self.gl.SRC_ALPHA, self.gl.ONE_MINUS_SRC_ALPHA, self.gl.ZERO, self.gl.ONE);`

In OGLGraphics.cpp::SetBlendMode() and D3D11Graphics.cpp::PrepareDraw(), it can have custom alpha factor, which is fine.

But can D3D9 do this?
Read a bit [M$ doc](https://docs.microsoft.com/en-us/windows/desktop/direct3d9/d3dblend), still not certain.

-------------------------

Leith | 2019-03-08 01:59:49 UTC | #2

Should not be a problem - blend modes have been with us for a very long time, and not much has changed over the years. I remember using them on DX8, I think you have nothing to worry about.

-------------------------

ab4daa | 2019-03-08 04:04:16 UTC | #3

I mean, I don't know how to combine those D3D9 blend modes to do said blend mode.
Unlike opengl and D3D11, seems I cannot set independent factor on alpha channel in D3D9?

Thank you.

-------------------------

Leith | 2019-03-08 06:07:02 UTC | #4

I'm sorry, I can't answer your question directly, as I have little experience in Urho3D render pipeline - I note that blend mode is set in the renderpath per command, as documented (vaguely) in https://urho3d.github.io/documentation/1.6/_render_paths.html

-------------------------

Leith | 2019-03-08 12:04:45 UTC | #5

this part may be useful : 
[quote]
Direct3D 9Ex has improved text rendering capabilities. Rendering clear-type fonts would normally require two passes. To eliminate the second pass, a pixel shader can be used to output two colors, which we can call PSOutColor[0] and PSOutColor[1]. The first color would contain the standard 3 color components (RGB). The second color would contain 3 alpha components (one for each component of the first color).
[/quote]

-------------------------

