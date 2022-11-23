esak | 2017-01-02 01:04:43 UTC | #1

I added a simple FPS counter to one of the samples. With this visible I got 20 FPS on my Pi 2.
Without it and displaying the debug-hud instead I got 15 FPS.
So my suggestion is to add a simple FPS counter to the samples, maybe enabling it through a special key.

-------------------------

rasteron | 2017-01-02 01:04:49 UTC | #2

Good idea esak but I remember on older versions this was available as a sample afaik..

-------------------------

GoogleBot42 | 2017-01-02 01:04:49 UTC | #3

Here is the code that outputs the fps in the debug renderer: [url]https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Core/Profiler.cpp#L130[/url]
The statement "Min(block->intervalCount_, 99999)" is the value of the fps to be precise.   :wink:   This is not exactly the most helpful but it is a start...  :\

-------------------------

