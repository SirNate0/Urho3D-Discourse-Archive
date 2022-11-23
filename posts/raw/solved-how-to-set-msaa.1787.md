imxqliu | 2017-01-02 01:10:08 UTC | #1

In the sample multiple viewports, I find urho use postprocess Fxaa to AntiAliasing, while I want to use Msaa to get a high quality  render result such as ogre'samples, any suggestion?
    Thanks.

-------------------------

thebluefish | 2017-01-02 01:10:08 UTC | #2

Multisampling is handled by Graphics, not by shader. You can enable this in your engine initialization as so:

[code]
engineParameters_["Multisample"] = 2;
[/code]

Alternatively, you can use the following to set it on the fly:

[code]
// (int width, int height, bool fullscreen, bool borderless, bool resizable, bool vsync, bool tripleBuffer, int multiSample);

auto graphics = GetSubsystem<Urho3D::Graphics>();

graphics->SetMode(graphics->GetWidth(), graphics->GetHeight(), graphics->GetFullscreen(), graphics->GetBorderless(), graphics->GetResizable(), graphics->GetVSync(), graphics->GetTripleBuffer(), true);
[/code]

-------------------------

imxqliu | 2017-01-02 01:10:09 UTC | #3

thanks,  now it's works well.

-------------------------

