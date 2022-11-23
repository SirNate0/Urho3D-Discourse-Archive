rku | 2017-01-02 01:14:26 UTC | #1

I noticed that Camera::WorldToScreenPoint() returns Vector3() with normalized screen coordinates. However UI elements are positioned using pixels. I can not find any methods for UI positioning using normalized coordinates. So what is the right way to position UI element using WorldToScreenPoint()? Converting normalized position to pixels is simple, however i find it surprising there is no such basic API already which leads me to think i simply can not find it.

I am basically looking for something like:
[code]
UIElement::SetPositionNormalized(Vector2 pos);
Camera::WorldToScreenPointPixels(Vector3 pos);
[/code]

Or no such thing exists and i should implement them and make PR?

P.S. In case i should make PR i assume it would not be a good idea to overload SetPosition() since Vector2 and IntVector2 are kind of interchangeable and would likely lead to confusion and unwanted bugs. Correct me if im wrong.

-------------------------

cadaver | 2017-01-02 01:14:27 UTC | #2

Camera does not know the viewport it's being rendered to. It could be rendered to multiple viewports with different sizes too. IMO it should not assume whole screen size and it's in the end simpler if you convert to the desired viewport size yourself.

The "Screen" in the function name is somewhat misleading, though.

-------------------------

cadaver | 2017-01-02 01:14:27 UTC | #3

Forgot that Viewport::WorldToScreenPoint() should already do what you're after.

-------------------------

rku | 2017-01-02 01:14:27 UTC | #4

Oh, this was exactly what i was looking for, thank you

Edit:
By the way i can not stop admiring design choices of engine. It really is by far best (to me personally) of all these opensource community driven engines out there, probably one of the best in general as well.

-------------------------

