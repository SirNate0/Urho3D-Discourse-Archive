suppagam | 2019-11-08 23:10:43 UTC | #1

What's the proper way of creating full-screen shaders in Urho? I'm trying to apply a shader to the whole screen to create some camera effects (nightvision, VHS effect, etc).

-------------------------

SirNate0 | 2019-11-08 19:21:24 UTC | #2

Look at the existing post processing effects like Bloom. That sounds similar to what you want to achieve, they would probably be a decent starting point/example, though someone else may be able to provide more concrete help.

-------------------------

suppagam | 2019-11-08 20:47:03 UTC | #3

You mean this? https://github.com/xamarin/urho/blob/master/Urho3D/CoreData/Shaders/GLSL/Bloom.glsl

-------------------------

SirNate0 | 2019-11-09 02:40:55 UTC | #4

Yes, along with some of the others. Combine that with [bin/Data/PostProcess/Bloom.xml](https://github.com/urho3d/Urho3D/blob/master/bin/Data/PostProcess/Bloom.xml) and look at some of the samples for how to add the effect to the render path.

-------------------------

