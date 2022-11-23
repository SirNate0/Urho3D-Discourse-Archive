Enhex | 2017-01-02 01:11:21 UTC | #1

I noticed that point light's shadow has less peter panning the further away it is from the end of the light's range.
That means that if I have shadow casting point lights with huge range, I can avoid peter panning, but that' really expensive since they won't be culled(?).

100m range, light slipping under the door:
[img]http://i.imgur.com/Xzip8Cp.jpg[/img]
300m range, same light, more accurate shadows:
[img]http://i.imgur.com/KABmUa6.jpg[/img]

Is there a way to avoid peter panning without huge light range?

-------------------------

1vanK | 2017-01-02 01:11:21 UTC | #2

try
    light.shadowBias = BiasParameters(0.0002f, 0.5f);
    light.shadowCascade = CascadeParameters(10.0f, 50.0f, 100.0f, 0.0f, 0.8f);

-------------------------

Enhex | 2017-01-02 01:11:21 UTC | #3

[quote="1vanK"]try
    light.shadowBias = BiasParameters(0.0002f, 0.5f);
    light.shadowCascade = CascadeParameters(10.0f, 50.0f, 100.0f, 0.0f, 0.8f);[/quote]
ShadowBias is for self shadowing.
shadowCascade is for directional light, I'm using point light.

-------------------------

1vanK | 2017-01-02 01:11:21 UTC | #4

[quote="Enhex"]
ShadowBias is for self shadowing.
[/quote]

it is offset of shadow

-------------------------

Enhex | 2017-01-02 01:11:22 UTC | #5

Ok but I'm already using those values since they're the defaults:
[code]
static const float DEFAULT_CONSTANTBIAS = 0.0002f;
static const float DEFAULT_SLOPESCALEDBIAS = 0.5f;
[/code]

-------------------------

1vanK | 2017-01-02 01:11:22 UTC | #6

[quote="Enhex"]Ok but I'm already using those values since they're the defaults:
[code]
static const float DEFAULT_CONSTANTBIAS = 0.0002f;
static const float DEFAULT_SLOPESCALEDBIAS = 0.5f;
[/code][/quote]

set bias to (0, 0.5), this can cause artifacts, but can solve problem :)

-------------------------

Enhex | 2017-01-02 01:11:22 UTC | #7

Why is it more accurate with bigger range?

-------------------------

1vanK | 2017-01-02 01:11:22 UTC | #8

Maybe when you move the light source parallel to the floor the angle of the shadow to the object is changed

-------------------------

