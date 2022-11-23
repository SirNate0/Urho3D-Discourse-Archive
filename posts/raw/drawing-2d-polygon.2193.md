dgp | 2017-01-02 01:13:48 UTC | #1

I am newbie and looking forward fro some direction on accomplishing the following using Urho2D namespace.

1)How do I set my ortho to -100,100,-50,50 ,I use glOrtho in Opengl
2)How to draw  polygons,lines and points 
3)Is it possible to modify Urho2DSprite sample to accomplish above to? If so, what should be used in place of StaticSprite2D
4) Is there a self contained sample with main(0 as entry point ?

-------------------------

rku | 2017-01-02 01:13:48 UTC | #2

You should really check samples: [github.com/urho3d/Urho3D/tree/m ... e/Samples/](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/)

1) [url=https://github.com/urho3d/Urho3D/blob/master/Source/Samples/24_Urho2DSprite/Urho2DSprite.cpp#L91]Like this[/url]
2) [url=https://github.com/urho3d/Urho3D/blob/master/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp]Dynamic geometry sample[/url], but likely you do not want this at all.
3) You are not clear enough what your goal is.
4) See definition of [url=https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Engine/Application.h#L73]URHO3D_DEFINE_APPLICATION_MAIN[/url]

Yeah docs are bit lacking, but code of engine is very clean and clear so reading it can answer your questions most of the time.

-------------------------

