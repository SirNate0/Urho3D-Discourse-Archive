Bananaft | 2017-01-02 01:12:12 UTC | #1

Hi.

I have a huge scene, and I want to place some very far individual dynamic objects on background, like sun, moon, stars(individual quads), and maybe some far away terrain(this one should be depth sorted).
My first approach was to mess with vertex shader. But then I need to make bounding boxes infinitely large. I know, some engines have a feature of adding a second scene(with much smaller world scale) as a background, or draw sky scene with second pass using game scene depth as a stencil.

Is there an out of the box solution for this in Urho i missed, what is the best way in your opinion? I'm using deferred, b.t.w.

-------------------------

Enhex | 2017-01-02 01:12:13 UTC | #2

you could attach them to the camera node and somehow make their rotation independant (A quick hack would be to reset it every frame).

Try to look at how the skybox is implemented.

-------------------------

rku | 2017-01-02 01:12:13 UTC | #3

[gamasutra.com/view/feature/1 ... hp?print=1](http://www.gamasutra.com/view/feature/131393/a_realtime_procedural_universe_.php?print=1)

-------------------------

