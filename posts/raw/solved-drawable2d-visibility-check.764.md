Mike | 2017-01-02 01:02:44 UTC | #1

I'd like to check visibility of 2D drawables (AnimatedSprite2D and StaticSprite2D) to limit the udpate calls when drawables are not visible.
Something like Drawable::IsInView() performs.
Renderer2D class has a CheckVisibility() method and Drawable2D has a visibility_ variable that is not used.

EDIT: as Drawable2D derives from Drawable, IsInView() should work for 2D either, but it always returns false (I've tried in C++, AS and lua).
IsInView() works fine for 3D drawables (AnimatedModel and StaticModel).

-------------------------

