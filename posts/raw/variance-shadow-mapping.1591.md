darwikey | 2017-01-02 01:08:43 UTC | #1

Hello,
I have implemented Variance Shadow Mapping (VSM). It works with OpenGl, dx9 and dx11.
In order to add softness to shadows, this method allows to post-process the shadow map. 
At the moment, it's a 7x7 gaussian blur, but the user can use his own filter with the function Renderer::SetShadowMapFilter(Object* instance, ShadowMapFilter functionPtr).

Another notable change is the ShadowQuality, now it's an enum :
enum ShadowQuality
{
    SHADOWQUALITY_SIMPLE_16BIT = 0,
    SHADOWQUALITY_SIMPLE_24BIT,
    SHADOWQUALITY_PCF_16BIT,
    SHADOWQUALITY_PCF_24BIT,
    SHADOWQUALITY_VSM,
    SHADOWQUALITY_BLUR_VSM
};


[img]http://s13.postimg.org/4sicfz1qv/shadows.jpg[/img]


The drawback of this technique is the light bleeding, but in the lighting shader, there is a trick to reduce it.

The link to my fork :
github.com/darwikey/Urho3D

I just need to add function in Renderer to set the shadow softness and the light bleeding reduction.

If it's ok, I can propose a PR.

-------------------------

cadaver | 2017-01-02 01:08:43 UTC | #2

On cursory look, changes to engine look solid. Certainly make a PR.

The SHADOWCMP shader define for D3D may be handled incorrectly. It should be used only when Graphics::GetHardwareShadowSupport() returns false, which will only happen on fairly old ATI GPU's.

Also, a stylistic minor thing: when making if statements with only one statement within the block, we usually omit the curly braces:

[code]
if (condition)
    DoSomething();
[/code]

-------------------------

darwikey | 2017-01-02 01:08:44 UTC | #3

I solved the problem and i had functions to set shadow softness and light bleeding reduction.

Here is my PR :
[github.com/urho3d/Urho3D/pull/1098](https://github.com/urho3d/Urho3D/pull/1098)

-------------------------

rikorin | 2017-01-02 01:08:45 UTC | #4

I just thought it would be great to have variance shadows, and here they are. Awesome.

-------------------------

sabotage3d | 2017-01-02 01:08:47 UTC | #5

Nice work! Is VSM faster than PCF for mobile?

-------------------------

darwikey | 2017-01-02 01:08:48 UTC | #6

I haven't tested for mobile. But it will be great if you do some benchmarks :slight_smile:

-------------------------

Bananaft | 2017-01-02 01:08:55 UTC | #7

My wish comes true. Can't wait to play with it.

-------------------------

