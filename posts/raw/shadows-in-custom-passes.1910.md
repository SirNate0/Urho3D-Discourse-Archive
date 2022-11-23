TEDERIs | 2017-01-02 01:11:25 UTC | #1

I'm working on own render path and faced with the one question. Why is access to the shadows is only possible in the first "base" pass? And is it possible to access to the shadows via GetShadow() function in the following passes?

-------------------------

cadaver | 2017-01-02 01:11:25 UTC | #2

Welcome to the forums.

In general, access to a shadow map is possible in a pass that is applying a per-pixel light additively. Note the "litbase" optimization pass is applying the first per-pixel light and the base color in one go.

If you want shadows for transparent forward passes, which are rendered after all opaque geometry, you must disable shadow map reuse: Renderer::SetReuseShadowMaps(false). Otherwise the shadow maps have been reused at that point already and the shadow information is no longer available, in which case engine automatically disables shadowing from the transparent passes.

When you're using custom passes, read [urho3d.github.io/documentation/H ... paths.html](http://urho3d.github.io/documentation/HEAD/_render_paths.html) carefully. There's some properties (metadata, lighting mode) that the engine can only "guess" for the default pass names.

-------------------------

TEDERIs | 2017-01-02 01:11:25 UTC | #3

Thanks for the prompt help!

-------------------------

