Hevedy | 2017-01-02 01:11:05 UTC | #1

I just making an scene and even using 8k shadows the shadows looks bad.

Why no use some of the render system from Ogre or something ?

[img]https://dl.dropboxusercontent.com/u/28070491/URho3D/Forums/2016-03-15_20-53-28.png[/img]

-------------------------

1vanK | 2017-01-02 01:11:05 UTC | #2

renderer->SetShadowQuality(SHADOWQUALITY_PCF_24BIT);

-------------------------

1vanK | 2017-01-02 01:11:05 UTC | #3

but shadows look fine, you need use FXaa3 for antialiasing

-------------------------

cadaver | 2017-01-02 01:11:06 UTC | #4

There's also SHADOWQUALITY_BLUR_VSM in master branch nowadays, though it may need tweaking for individual needs. Also, experiment with cascade split distances for directional lights.

-------------------------

1vanK | 2017-01-02 01:11:06 UTC | #5

also you can tuning bias and cascade
[github.com/1vanK/Urho3DModelsDi ... ain.as#L67](https://github.com/1vanK/Urho3DModelsDissolving/blob/master/MyData/Scripts/Main.as#L67)

-------------------------

1vanK | 2017-01-02 01:11:06 UTC | #6

[quote="cadaver"]There's also SHADOWQUALITY_BLUR_VSM in master branch nowadays, though it may need tweaking for individual needs. Also, experiment with cascade split distances for directional lights.[/quote]

vsm so buggy :( [gamedev.ru/community/urho3d/ ... page=2#m21](http://www.gamedev.ru/community/urho3d/forum/?id=204980&page=2#m21)

VSM:
[savepic.ru/8327277.htm](http://savepic.ru/8327277.htm)

PCF:
[savepic.ru/8377444.htm](http://savepic.ru/8377444.htm)

-------------------------

Hevedy | 2017-01-02 01:11:06 UTC | #7

Oh wow guys thanks for the fast replies ^^

-------------------------

Hevedy | 2017-01-02 01:11:13 UTC | #8

Okay I just downloaded the last master version that looks got so many more feature than the one I got and the new shadows PCF looks better, the VSM got problems or that looks like, but the Blurred version looks better

[img]https://dl.dropboxusercontent.com/u/28070491/URho3D/Forums/2016-03-17_15-14-15.png[/img]

As you can see the new versions got some problems too in corners

-------------------------

dragonCASTjosh | 2017-01-02 01:11:13 UTC | #9

somewhere in my list of things to do on the renderer is experiment with new shadowing tech, something along the quality of unreal distance field shadows although likely not the same effect as i dont think we can justify all the raytracing in urho

-------------------------

sabotage3d | 2017-01-02 01:11:17 UTC | #10

Here is an article on how they solved some of the issues with PCF in The Witness: [url]http://the-witness.net/news/2013/09/shadow-mapping-summary-part-1/[/url] .
For more complex details something like Directional Ambient Occlusion can help, but it might be too expensive: [url]http://kayru.org/articles/dssdo[/url] .

-------------------------

Hevedy | 2017-01-02 01:11:18 UTC | #11

[quote="dragonCASTjosh"]somewhere in my list of things to do on the renderer is experiment with new shadowing tech, something along the quality of unreal distance field shadows although likely not the same effect as i dont think we can justify all the raytracing in urho[/quote]

That is nice, but well I don't think you need raytracing to improve this, the non raytracing shadows in UE4 and realtime got less problem than this ones in corners.

-------------------------

