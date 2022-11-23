k7x | 2018-11-09 17:56:48 UTC | #1

Hello
I have a problem. I am writing a program for artists. The platform is an android. One of the important components of this program is to save the render to a file. That is a picture.
The function to make a screenshot is not suitable. I need a specific size of the picture.
I tried to make an ordinary render to the texture, get a picture from the texture and save it to PNG. Used RGBA
But in the place of the picture I was getting a noise or something like that.

Help please solve this problem.

-------------------------

Sinoid | 2018-11-05 17:36:50 UTC | #2

Post your code. There's too many ways you could be trying to do this.

You should just be using `GetImage()` and `Image::SavePNG`.

-------------------------

k7x | 2018-11-05 19:49:30 UTC | #3

I am using some like this :
```
Node@ renderCameraNode = scene0.CreateChild("RenderCamera");
Camera@ renderCamera = renderCameraNode.CreateComponent("Camera");
renderCamera.orthographics = true;

Texture2D@ renderTexture = Texture2D();
renderTexture.SetSize(512, 512, GetRGBAFormat(), TEXTURE_RENDERTARGET);
Material@ renderMaterial = Material();
renderMaterial.SetTechnique(0, cache.GetResource("Technique", "Techniques/DiffUnlit.xml"));
renderMaterial.SetTexture(TU_DIFFUSE, renderTexture);

RenderSurface@ surface = renderTexture.GetRenderSurface();
Viewport@ rttViewport = Viewport(scene0, renderCamera);
surface.SetViewport(0, rttViewport); 

Texture2D@ texture = surface.parentTexture;
Image@ image = texture.GetImage();

image.SavePNG("data/render.png");
```
this code is running at the end of start() function

I try do engine.RunFrame() before save

-------------------------

Sinoid | 2018-11-05 18:52:57 UTC | #4

Probably need to set the surface update mode to always, the stuff with the image looks fine. 

By default surfaces only render when visible. You're probably getting whatever gobbly-gook your driver gives an uninitialized texture (noise, it's usually a pattern though).

Surfaces do send an event, so you can subscribe to that to save the image when you know it's really there.

-------------------------

k7x | 2018-11-05 18:57:36 UTC | #5

I also tried to render the entire scene with the plane on which the rendering will take place, but all the same could not save the result in png

I try always update

-------------------------

k7x | 2018-11-06 10:57:25 UTC | #6

I try do update always but output still noise

-------------------------

k7x | 2018-11-09 17:56:56 UTC | #7

Finally it happened!
All you need to do is
1) use lines of code not in the Start () function but after
2) Use RGBA texture format
3) Surface.update = update always
4) Before getting the image from the texture, exec engine.RunFrame()
5) After get the image save

I think my mistake was that I used lines of the render code to the texture in the start function. Perhaps this is a specific device error.

Thank for the help!

-------------------------

Sinoid | 2018-11-09 18:16:09 UTC | #8

Yeah, that'd do it. Didn't cross my mind at the time but the cubemap rendering in the editor (`Data/Scripts/Editor/EditorCubeCapture.as`) shows how wonky it can be.

Although you **can** immediately render a view to a render-target, it's not doable outside of C++ and is a raw *not really supported* thing - so you need a really good reason to do it like lightmapping/rendering-cubes/etc.

-------------------------

