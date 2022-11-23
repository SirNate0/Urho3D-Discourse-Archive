Eugene | 2017-01-02 01:12:43 UTC | #1

Hi all.

I have just started working with Urho3D and I am going to migrate my project onto this engine.
The first improtant feature I want to move is smooth model LOD switch.
You know, it looks like in any other engine. It could be fade through transparency for FR or dithering for DS renderer.

Is there any investigation about?
If it is not, where and how could I start?

Smooth LOD switch forces model to be rendered twice with different geometries when LOD is switching.
How does it better to do?

Thank you.

-------------------------

TheComet | 2017-01-02 01:12:44 UTC | #2

TL;DR: Urho3D doesn't support this feature natively.

Fading through transparency will not look good. Both models will be transparent and you will be able to see what's behind them. The way modern engines achieve smooth LOD transitions is by using a mesh simplification algorithm. If you have been following Overgrowth, they showed this feature in their game at one point @0:36:

[video]https://youtu.be/6PtrFnrk-dY?t=36[/video]

I think it would be very cool if Urho3D could generate lower LOD models automatically.

-------------------------

rasteron | 2017-01-02 01:12:44 UTC | #3

There's already an implementation in Ogre3D MIT
[ogre3d.org/tikiwiki/MeshLod](http://www.ogre3d.org/tikiwiki/MeshLod)

..not sure how much you can derive from it, maybe start from the older versions just to make it work.

-------------------------

Eugene | 2017-01-02 01:12:46 UTC | #4

[quote="TheComet"]TL;DR: Urho3D doesn't support this feature natively.

Fading through transparency will not look good. Both models will be transparent and you will be able to see what's behind them. The way modern engines achieve smooth LOD transitions is by using a mesh simplification algorithm. If you have been following Overgrowth, they showed this feature in their game at one point @0:36:

I think it would be very cool if Urho3D could generate lower LOD models automatically.[/quote]

Oh, it looks cool. How does it work?
Is it a kind of morping animation when you morph model from fake [b]high-poly-that-looks-like-low-poly[/b] to real [b]low-poly[/b]?
If I am right, this algorithm is need to be integrated into LOD generation and couldn't be applied to simple lodded models.

I want to implement at least dithering fade that is used in e.g. UE4 (or my own engine).
It looks quite noisy but anyway it is much better than current hard lod swithc.

-------------------------

TheComet | 2017-01-02 01:12:46 UTC | #5

[quote="rasteron"]Oh, it looks cool. How does it work?
Is it a kind of morping animation when you morph model from fake high-poly-that-looks-like-low-poly to real low-poly?[/quote]

No. You'll have to do some research on some of the existing algorithms for mesh decimation.
[url]http://graphics.stanford.edu/courses/cs468-10-fall/LectureSlides/08_Simplification.pdf[/url]
[url]http://www.cs.mtu.edu/~shene/COURSES/cs3621/SLIDES/Simplification.pdf[/url]

-------------------------

sabotage3d | 2017-01-02 01:12:47 UTC | #6

I think the Overgrowth mesh simplification algorithm is based on the one from Ogre3D: [url]http://www.ogre3d.org/forums/viewtopic.php?f=13&t=77319[/url]

-------------------------

Eugene | 2017-01-02 01:12:47 UTC | #7

[quote="TheComet"][quote="rasteron"]Oh, it looks cool. How does it work?
Is it a kind of morping animation when you morph model from fake high-poly-that-looks-like-low-poly to real low-poly?[/quote]

No. You'll have to do some research on some of the existing algorithms for mesh decimation.
[url]http://graphics.stanford.edu/courses/cs468-10-fall/LectureSlides/08_Simplification.pdf[/url]
[url]http://www.cs.mtu.edu/~shene/COURSES/cs3621/SLIDES/Simplification.pdf[/url][/quote]

These papers explain nothing.
I mean, I am not interested in algorithms of mesh simlification and this is not the subject.
How do they [i]render [/i]smooth LODs?
It looks as smooth as tessellation, but it can't be tessellation.

-------------------------

Eugene | 2017-01-02 01:12:49 UTC | #8

I maked these!

[video]https://youtu.be/73FjrrF_IW8[/video]

-------------------------

