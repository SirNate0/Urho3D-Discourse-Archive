namic | 2017-01-02 01:08:38 UTC | #1

What's the technique used for terrain LOD in Urho3D?

-------------------------

cadaver | 2017-01-02 01:08:38 UTC | #2

Simple geomipmapping. 3 decreased LOD levels max. (in addition to the maximum resolution level) if I remember right.

-------------------------

namic | 2017-01-02 01:08:41 UTC | #3

Are there any plans on improving the current terrain support? Geomipmapping is not powerful as CDLOD and might not handle 4k heightmaps with more than 2 meter per pixel.

-------------------------

cadaver | 2017-01-02 01:08:41 UTC | #4

Anyone is free to work on it and contribute a PR. And also you can always create a custom terrain component in your application. Otherwise I can speak for myself that I haven't planned improvements to it.

-------------------------

namic | 2017-01-02 01:08:41 UTC | #5

Sorry if i sounded like a customer demanding something, i just wanted to know if the guys who know more about the engine are planning to improve the terrain parts of it. I understand it's a libre project and people can do stuff on their own, but i'm not really in that league. :frowning:

-------------------------

Bananaft | 2017-01-02 01:08:42 UTC | #6

In my project I have a 3072x3072 terrain with 5 meter step and draw distance at 12 000. Looks great, runs great. I really don't see why it may need any improvements.

-------------------------

