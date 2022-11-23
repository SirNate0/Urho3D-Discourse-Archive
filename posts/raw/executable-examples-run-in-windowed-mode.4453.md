Valdar | 2018-08-10 12:42:56 UTC | #1

Hi All,

Urho noob here. I've just started evaluating Urho 3D and I must say I'm impressed with the functionality of such a lightweight package. I have cloned and compiled the source successfully, but i have an "issue" that I can't seem to find an answer for.

Any of the compiled examples run in what appears to be a 1028x768 window, although my screen resolution is 1920x1080. In the _Engine initialization and main loop_ docs it says _FullScreen (bool) Whether to create a full-screen window. Default true_.

If I run any angelscript example through the Urho3dPlayer, it runs full-screen. I've searched the forum, and had a cursory look at the code for a graphic setting, but no joy in either case. Is this as intended, or do I have something wrong somewhere? Any help appreciated and thanks in advance.

-------------------------

Miegamicis | 2018-08-10 13:11:47 UTC | #2

All samples are launched with fullscreen mode off:
https://github.com/urho3d/Urho3D/blob/master/Source/Samples/Sample.inl#L62

Also 1024x768 is the default resolution for all the graphics interfaces:
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Direct3D9/D3D9Graphics.cpp#L332-L333

-------------------------

Valdar | 2018-08-10 13:34:54 UTC | #3

[quote="Miegamicis, post:2, topic:4453"]
engineParameters_[EP_FULL_SCREEN]
[/quote]

Brilliant! That's exactly what I was looking for (obviously not looking in the right place) :)

Thanks Miegamicis

-------------------------

