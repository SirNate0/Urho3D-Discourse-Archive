gkontadakis | 2021-03-18 09:51:37 UTC | #1

Hi all,

I am trying to get MSAA working with post-process effects (e.g. trying something simple like the GreyScale). For example I use some sample like the 42_PBRMaterials:

> engineParameters_["Multisample"] = 4;

If I put any value greater than 1 for "Multisample" I see everything pitch black when applying any post process effect. If it is 1, the post process effect is fine. Dunno how the rendering pipeline works. Any suggestions on what am I missing? Maybe in master branch it behaves differently? (Urho3D 1.7.1, Win10, VS2015, RTX 2080 Ti, DX11)

-------------------------

Avagrande | 2021-03-21 12:06:20 UTC | #2

For MSAA to work ALL further render targets in your renderpath need to have the multisample tag which matches with the setting on your context be it the whole window or a render surface. 

`<rendertarget name="normals"  sizedivisor="1 1" format="rgba" filter="false"  persistent="false" multisample="4"/>`

Its very annoying, and I am not sure why it's not done automatically.

-------------------------

gkontadakis | 2021-03-21 12:06:20 UTC | #3

Thx for the support,

For this specific problem though which I see everything pitch black what worked for me was this:
https://discourse.urho3d.io/t/solved-how-to-set-msaa/1787

Without knowing what happens underneath, this alone didn't work:

> engineParameters_[“Multisample”] = 4;

Also adding it to all post process rendering targets didn't work. I had to also do this:

> graphics->SetMode(graphics->GetWidth(), graphics->GetHeight(), graphics->GetFullscreen(), graphics->GetBorderless(), graphics->GetResizable(), graphics->GetHighDPI(), graphics->GetVSync(), graphics->GetTripleBuffer(), true, graphics->GetMonitor(), graphics->GetRefreshRate());

-------------------------

vmost | 2021-03-21 12:06:08 UTC | #4

Not sure if v1.7.1 is the same, but you can use the following pattern to set screen mode parameters (in master `SetMode()` is deprecated):

```
// copy old params
ScreenModeParams screen_params = GetSubsystem<Graphics>()->GetScreenModeParams();

// update the multisample setting (for example)
screen_params.multiSample_ = 4;

// get screen size
IntVector2 screen_size = GetSubsystem<Graphics>()->GetSize();

// update window modes
GetSubsystem<Graphics>()->SetDefaultWindowModes(screen_size.x_, screen_size.y_, screen_params);
```

You might want to use `SetWindowModes()` instead for better control over the behavior in the context of fullscreen vs windowed (probably need to experiment to get exactly what you want).

-------------------------

gkontadakis | 2021-03-21 12:05:58 UTC | #5

Thx for the info, it is not there in v1.7.1, but good to know for future reference

-------------------------

