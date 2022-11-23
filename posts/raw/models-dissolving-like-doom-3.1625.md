1vanK | 2017-01-02 01:09:03 UTC | #1

For now without burning edges

[github.com/1vanK/Urho3DModelsDissolving](https://github.com/1vanK/Urho3DModelsDissolving)

Use slider to dissolve

[url=http://savepic.ru/8145082.htm][img]http://savepic.ru/8145082m.png[/img][/url]

-------------------------

1vanK | 2017-01-02 01:09:03 UTC | #2

Added burning edges

[url=http://savepic.ru/8177867.htm][img]http://savepic.ru/8177867m.png[/img][/url]

-------------------------

codingmonkey | 2017-01-02 01:09:03 UTC | #3

nice) but how about dissolving from top to bottom?
and you probably better turn off cull to see back faces also

-------------------------

1vanK | 2017-01-02 01:09:03 UTC | #4

> but how about dissolving from top to bottom?

Dissolution is applied to the material, rather than the model. I do not quite understand how to find the top of the material :) Probably it can be done with dissolving map, individually designed for each model (currently it used clouds texture generated in Photoshop).

> and you probably better turn off cull to see back faces also

Then it will be seen that the objects are hollow. It is strangely, when the living creatures are empty inside :) 
Anyway, it is possible to turn off cull in material

-------------------------

1vanK | 2017-01-02 01:09:03 UTC | #5

Added from top to bottom burning (gradient over model painted in Blender)

[url=http://savepic.ru/8144096.htm][img]http://savepic.ru/8144096m.png[/img][/url]

-------------------------

rasteron | 2017-01-02 01:09:03 UTC | #6

nice!

-------------------------

codingmonkey | 2017-01-02 01:09:04 UTC | #7

>Added from top to bottom burning
very good) 
let's say we hited this character into: leg, ass, head, arm... and we want for dissolving starts from point of impact and process to whole body from this impact point. Is it possible to implement?

-------------------------

1vanK | 2017-01-02 01:09:04 UTC | #8

[quote="codingmonkey"]>Added from top to bottom burning
very good) 
let's say we hited this character into: leg, ass, head, arm... and we want for dissolving starts from point of impact and process to whole body from this impact point. Is it possible to implement?[/quote]

Perhaps it can be done as follows:
1) send to the vertex shader coordinates of the point of impact
2) calculate distance from current vertex to point  of impact
3) use it in pixel shader as coefficient

In other words, we need a spherical gradient centered at the point of impact

-------------------------

Kyle00 | 2017-01-02 01:09:04 UTC | #9

This is great! Thank you for this!

-------------------------

sabotage3d | 2017-01-02 01:09:05 UTC | #10

This is really cool. Thanks for sharing. It reminds me of a disintegration fx that we are doing for a feature film.

-------------------------

Bluemoon | 2017-01-02 01:09:05 UTC | #11

Wow... This is really awesome

-------------------------

Modanung | 2018-07-05 11:20:35 UTC | #12

This shader is now put to work scraping pilots off the ceiling in heXon. 
https://vimeo.com/157520969
[b][ WARNING: Fake Blood ][/b]
I slightly edited the [url=https://github.com/LucKeyProductions/heXon/blob/master/Resources/Techniques/DissolveDiffEmissiveAlphaMask.xml]technique[/url] to add emission and alpha. Instead of the [url=https://github.com/LucKeyProductions/heXon/blob/master/Resources/Shaders/GLSL/DissolveLitSolid.glsl]shader[/url] using the emission map for the dissolve rate this is now controlled by the spec map, since I don't need specularity in this case. I guess adding a dedicated dissolve texture would be better.
Thanks again 1vanK! :slight_smile:

-------------------------

weitjong | 2017-01-02 01:10:33 UTC | #13

You should probably warn that your video has mature rating content due to the blood.  :laughing:

-------------------------

Modanung | 2017-01-02 01:10:33 UTC | #14

[quote="weitjong"]You should probably warn that your video has mature rating content due to the blood.  :laughing:[/quote]
Better? :slight_smile:

-------------------------

codingmonkey | 2017-01-02 01:10:33 UTC | #15

the last man almoust was happy what will be still alive :slight_smile:

-------------------------

thebluefish | 2017-01-02 01:10:34 UTC | #16

[quote="Modanung"]This shader is now put to work scraping pilots off the ceiling in heXon. [url=https://vimeo.com/157520969][video][/url] [b][color=#DF0000][ WARNING: Fake Blood ][/color][/b]
I slightly edited the [url=https://github.com/LucKeyProductions/heXon/blob/master/Resources/Techniques/DissolveDiffEmissiveAlphaMask.xml]technique[/url] to add emission and alpha.
Thanks again 1vanK! :slight_smile:[/quote]

That's cool dude!

-------------------------

Modanung | 2017-01-02 01:12:54 UTC | #17

On [url=https://vimeo.com/171174842]ejecting[/url] the ships in heXon phase out using this shader too.

-------------------------

