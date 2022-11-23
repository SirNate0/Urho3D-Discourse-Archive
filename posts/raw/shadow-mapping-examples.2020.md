namic | 2017-01-02 01:12:20 UTC | #1

Are there any shadow mapping examples for Urho? I'm looking for PCF, hard, VSM?

-------------------------

rasteron | 2017-01-02 01:12:21 UTC | #2

If I'm not mistaken, NSW already has PCF shadows as an example. Check the combined shaders.xml file:

[github.com/urho3d/Urho3D/blob/m ... rs.xml#L11](https://github.com/urho3d/Urho3D/blob/master/bin/Data/NinjaSnowWarShaders.xml#L11)

-------------------------

1vanK | 2017-01-02 01:12:21 UTC | #3

Any exaple in Urho uses PCF shadows. It is default option:

[code]Renderer::Renderer(Context* context) :
    ...
    shadowMapFilterInstance_(0),
    shadowMapFilter_(0),
    ....
    shadowMapSize_(1024),
    shadowQuality_(SHADOWQUALITY_PCF_16BIT),[/code]

u can shange it through Renderer subsystem:

[code]
GetSubsystem<Renderer>()->SetShadowMapSize(2048);
GetSubsystem<Renderer>()->SetShadowQuality();
and other (see Renderer.h)
[/code]

Also some settings of shadows there are in Light component

-------------------------

hunkalloc | 2022-11-16 04:58:54 UTC | #4

Shadows tend to be very low quality still. Any other tricks to increase resolution?

-------------------------

