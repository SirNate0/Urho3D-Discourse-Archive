rku | 2017-01-02 01:13:46 UTC | #1

[img]https://i.imgur.com/GZ3lTDN.png[/img]

This is what i got now. First picture from blender is to give you idea what i am trying to shade. Cube on the left is what i have achieved with a point light + Diff technique and diffuse texture.

[code]    auto lightNode = _scene->CreateChild("Light");
    lightNode->SetPosition(Vector3(-1, PLAY_FIELD_HEIGHT, -2));
    auto light = lightNode->CreateComponent<Light>();
    light->SetLightType(LIGHT_POINT);
    light->SetCastShadows(true);
    light->SetRange(100);
    light->SetFadeDistance(100);
[/code]

Any idea how i could get it lit so it looks like something like cube on the right? Basically i want each plane to geet same amount of light without taking into account distance from the light.

-------------------------

TheSHEEEP | 2017-01-02 01:13:46 UTC | #2

I don't know much about Urho internals yet, but an effect like that could be achieved in the shader code rather easily.

Usually, a light's influence is calculated "realistically" by the angle difference between light direction and surface normal.
Instead of doing this realistically, you could introduce different angle ranges.

1: Angle is very large - medium: full light influence
2: Angle is medium - small: half light influence
3: Angle is "same direction": no light influence

Not sure if the same could be done by C++ code only, but it would surprise me.

-------------------------

1vanK | 2017-01-02 01:13:46 UTC | #3

Use flat shading in blender for model and directional light in urho.

EDIT : Or you mean cartoon shader?

[url=http://savepic.ru/10985561.htm][img]http://savepic.ru/10985561m.png[/img][/url]

-------------------------

codingmonkey | 2017-01-02 01:13:46 UTC | #4

Ctrl+E - mark sharp

[url=http://savepic.ru/10992710.htm][img]http://savepic.ru/10992710m.png[/img][/url]

and then use EdgeSplit and apply modif

and only then do export

-------------------------

Mike | 2017-01-02 01:13:47 UTC | #5

Did you set Flat Shading in Blender?

-------------------------

rku | 2017-01-02 01:13:47 UTC | #6

Marking faces as flat shading in blender did the trick, thanks guys.
I also reworked mesh a bit, it probably helped as well:
[img]https://i.imgur.com/j55ab7O.png[/img]

-------------------------

rku | 2017-01-02 01:13:49 UTC | #7

Actually there is one more problem i can not wrap my head around. Flat shading causes object to jitter a bit (like by one pixel or so) when moving. Changing it to smooth shading makes it move smoothly. Are there any workarounds?

-------------------------

1vanK | 2017-01-02 01:13:49 UTC | #8

Use FXAA3 postprocess

-------------------------

rku | 2017-01-02 01:13:51 UTC | #9

That changes nothing, that square part in the middle still jitters up/down by 1px when object is going down on the screen..

Edit:
To be more clear i made a [url=https://www.youtube.com/watch?v=t5uI_6JEswM&feature=youtu.be]video[/url].

-------------------------

