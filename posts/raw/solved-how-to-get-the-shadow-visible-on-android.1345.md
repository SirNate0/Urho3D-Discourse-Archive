victorfence | 2017-01-02 01:07:01 UTC | #1

Hello, I found shadow in my demo invisible on android, but visible on pc,
are there something special to do to get shadows visible on android?

Here's some of my codes:
[code]
String platform = GetPlatform();
renderer.reuseShadowMaps = false;
if (platform == "Android") {
  renderer.shadowQuality = SHADOWQUALITY_LOW_16BIT;
}
...
// the light
Node@ lightNode = scene_.CreateChild("DirectionalLight");
lightNode.direction = Vector3(-15.0f, 15.0f, 30.0f);
Light@ light = lightNode.CreateComponent("Light");
light.lightType = LIGHT_DIRECTIONAL;
light.color = Color(1.0f, 1.0f, 1.0f);
light.castShadows = true;
light.shadowBias = BiasParameters(0.00025f, 0.5f);
light.shadowCascade = CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f);
light.specularIntensity = 0.5f;
light.shadowIntensity = 0.3;

[/code]

-------------------------

victorfence | 2017-01-02 01:07:04 UTC | #2

Yeah, I found I can see the shadow if I move the camera very near to the object, can this be changed? 

thanks

-------------------------

Bananaft | 2017-01-02 01:07:04 UTC | #3

I assume, there is only one shadow map available, so only very first shadow split is visible. And you only can stretch first split further.
light.shadowCascade = CascadeParameters(100.0f, 0.0f, 0.0f, 0.0f, 0.8f);

-------------------------

victorfence | 2017-01-02 01:07:05 UTC | #4

Thanks a lot for reply,

Now, I can see the shadow when the camera far away the oject, by these codes:

[code]
renderer.shadowMapSize=2048; //changed from 512 to 2048
...
light.shadowBias = BiasParameters(0.00025f, 0.95f);
light.shadowCascade = CascadeParameters(100.0f, 0.0f, 0.0f, 0.0f, 0.8f);
[/code]

The only problem is the shodow seems incomplete, here's my screenshots:

Shadow on android
[url]http://www.tiikoni.com/tis/view/?id=888684d[/url]

Shadow on pc is ok
[url]http://www.tiikoni.com/tis/view/?id=905710a[/url]

-------------------------

Bananaft | 2017-01-02 01:07:07 UTC | #5

No idea. Try tweaking every parameter (including bias and shadowMapSize) to see if anything affects this gap.

-------------------------

