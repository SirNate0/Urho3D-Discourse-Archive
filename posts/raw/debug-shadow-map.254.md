ucupumar | 2017-01-02 00:59:10 UTC | #1

Is there any way to view shadow map in Urho? I tried to render shadow map texture on UI using Sprite, but I got only white texture.

Here's my result, white rectangle in bottom left is shadow map sprite:
[img]https://dl.dropboxusercontent.com/u/17547612/ImagesForForum/white-shadowmap.jpg[/img]
Here's the code:
[code]Renderer* renderer = GetSubsystem<Renderer>();
Light* mainLight = scene_->GetChild("MainLight")->GetComponent<Light>();
Camera* mainCamera = scene_->GetChild("MainCamera")->GetComponent<Camera>();

Texture* shadow = renderer->GetShadowMap(mainLight, mainCamera, 1024, 768);

UI* ui = GetSubsystem<UI>();
Sprite* debugSprite = ui->GetRoot()->CreateChild<Sprite>();
debugSprite->SetTexture(shadow);
int textureWidth = shadow->GetWidth();
int textureHeight = shadow->GetHeight();
debugSprite->SetScale(256.0f / textureWidth);
debugSprite->SetSize(textureWidth, textureHeight);
debugSprite->SetHotSpot(0, textureHeight);
debugSprite->SetAlignment(HA_LEFT, VA_BOTTOM);
debugSprite->SetPriority(-100);[/code]

Am I doing something wrong?

-------------------------

cadaver | 2017-01-02 00:59:10 UTC | #2

The problem with the shadow maps is that they're specially setup depth textures, and sampling them actually does only the "in shadow" comparision, instead of returning the depth value. Long ago when Urho didn't use hardware shadow compare, but plain R32F textures for the shadows, the maps were easily debuggable.

If you're on Windows / D3D9, you may have luck with using PIX to debug the shadow maps while they're being rendered.

-------------------------

ucupumar | 2017-01-02 00:59:13 UTC | #3

Thanks for your explanation.
I already use GPU Perfstudio from AMD to debug the shadow, but sometimes it crashed, maybe because I use Nvidia card. But at least it showed up.  :smiley:

-------------------------

