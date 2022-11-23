George1 | 2017-10-25 10:39:40 UTC | #1

Hi I have added multi select by dragging a rectangle on the rendering window in my work. 

Method
-----------
It's pretty simple with the built in function like GetMousePosition and WorldToScreenPoint. 
But WorldToScreenPoint returns 0...1, while GetMousePosition return relative windows coordinate respect to the resolution. We need to convert one unit into the other to use it.

Suggestion for improvement
----------------------------------------
 *  Suggestion to add an overwrite WorldToScreenPoint function that return a relative mouse coordinate. This way I don't need to get graphic object and calling graphic.GetWidth()  and graphic.GetHeight() to convert them into the same unit.


My Question
-------------------
How to draw and simple 2D rectangle on screen space.

Is there a 2D line or rectangle primitive that preserved line width regardless of zoom scale (e.g. like the 3d debug drawer.)

Or is there a simple way of doing it? Please guide or show me a simple solution.

Thanks,

-------------------------

Modanung | 2017-10-25 16:25:47 UTC | #2

As for the first part you could do with something like:
```
IntVector2 pixel{ VectorRoundToInt(
           Vector2(graphics->GetSize()) * camera->WorldToScreenPoint(mousePos)) };
```

For the rectangle, I guess you could use a `BorderImage` UI element?

-------------------------

George1 | 2017-10-25 12:43:57 UTC | #3

Thanks Modanung,
I'm currently doing that for rectangle selection. After conversion I just use Rect and check if point isInside.

I will look at BorderImage UI element. Do you have a simple example to show it as a rectangle?

Thanks

-------------------------

George1 | 2017-10-25 13:26:00 UTC | #4

Got it to work.
Just create an instance.

nodeSelection = new BorderImage(context_);
		nodeSelection->SetSize(0, 0);
		nodeSelection->SetPosition(0, 0);
		nodeSelection->SetOpacity(0.6);
		nodeSelection->SetColor(Color::GREEN);
		uiRoot_->AddChild(nodeSelection);

Then vary the size and position on mouse click to display the rectangle.

One question about Urho3D
----------------------------------------
Do we have  MouseUp event?   E.g. LeftMouseUp event?

Thanks

-------------------------

jmiller | 2017-10-25 14:49:58 UTC | #5

[quote="George1, post:4, topic:3685"]
Do we have  MouseUp event?   E.g. LeftMouseUp event?
[/quote]

Hi George1
The input events and constants:
  https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Input/InputEvents.h
Sample 32_Urho2DConstraints has an example use.
 
FYI, there is also an 'on demand' method used in several samples.
```
    /// Check if a mouse button has been pressed on this frame.
    Input::GetMouseButtonPress(int buttons)
```

-------------------------

