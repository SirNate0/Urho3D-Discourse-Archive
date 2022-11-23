rbnpontes | 2017-04-03 00:30:18 UTC | #1

Hello guys, i'm here again, i need to get render Target but is not working, i'm follow the sample but not working,i'm Using Directx11

-------------------------

jmiller | 2017-01-02 01:13:48 UTC | #2

Hello,

Could you give a little more information or code, or what part of what sample you refer to?

As I understand render targets, you can define them in code, or a RenderPath XML - for example [github.com/urho3d/Urho3D/blob/m ... /Bloom.xml](https://github.com/urho3d/Urho3D/blob/master/bin/Data/PostProcess/Bloom.xml) 
More on 
RenderPaths [urho3d.github.io/documentation/ ... paths.html](https://urho3d.github.io/documentation/HEAD/_render_paths.html)
Rendering [urho3d.github.io/documentation/ ... ering.html](https://urho3d.github.io/documentation/HEAD/_rendering.html)

-------------------------

rbnpontes | 2017-01-02 01:13:49 UTC | #3

Here is my code
[code]
Texture2D* tex =new Texture(context_);
tex->SetSize(500,500,Graphics::GetRGBFormat(),TEXTURE_RENDERTARGET);
RenderSurface* surf = tex->GetRenderSurface();
surf->SetViewport(0,_viewport);

[/code]

-------------------------

jmiller | 2017-01-02 01:13:49 UTC | #4

Is any more information written to the log file*?

* by default on MS Windows, something like %APPDATA%\urho3d\logs\*.log (\Users\user\AppData\Roaming\logs\*.log)

-------------------------

rbnpontes | 2017-01-02 01:13:50 UTC | #5

I solved, but the bug is ocur
I'm changed the RenderSurface to update always
Its working fine,but i m show the Texture in Sprite, Sprite is render Texture normal but the viewport is not rendered, the viewport is rendered Black
Sorry again for my english

-------------------------

jmiller | 2017-01-02 01:13:50 UTC | #6

Maybe a problem in defining the new Viewport?
[github.com/urho3d/Urho3D/blob/m ... e.cpp#L194](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/10_RenderToTexture/RenderToTexture.cpp#L194)

-------------------------

