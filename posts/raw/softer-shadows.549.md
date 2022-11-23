rogerdv | 2017-01-02 01:01:18 UTC | #1

Is it possible to make shadows a bit transparent? I have been using shadows in my test project and they are too dark, in contrast, shadows in Wasteland 2 are gray and doesnt disturb the scene.

-------------------------

cadaver | 2017-01-02 01:01:18 UTC | #2

Two basic ways: either increase the ambient light level in your scene (through Zone) or set the shadow intensity in lights higher than 0 (Light::SetShadowIntensity)

-------------------------

rogerdv | 2017-01-02 01:01:19 UTC | #3

Thanks! Solved now.

-------------------------

