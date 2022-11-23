Wobling | 2017-01-02 01:10:25 UTC | #1

Hi All, looking at using Urho3D and I found the xamarin implementation which is certainly a great feature.
I'm curious if someone could answer a question I have.

Xamarin explains that you can have non-fullscreen applications for iOS and Androud using Surface Views.
Can this be done without Xamarin using just the Urho3D Engine?

My aim is to be able to render a 3D scene whilst still having a section of the screen filled with native content like buttons and such to control said screen.

Thanks,
Rob.

-------------------------

weitjong | 2017-01-02 01:10:25 UTC | #2

I don't see why not. The game engine is definitely able to render to a smaller viewport than the whole device screen. On Android I have experimented with "layering" native UI on top. I haven't tried that on iOS yet.

-------------------------

