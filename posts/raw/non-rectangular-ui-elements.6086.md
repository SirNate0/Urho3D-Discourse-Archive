SirNate0 | 2020-04-13 20:33:14 UTC | #1

Does Urho's UI support non-rectangular UI elements for things like `void UI::GetElementAt(UIElement*& result, UIElement* current, const IntVector2& position, bool enabledOnly)`? I ask as I'm trying to use the Spline class @godan posted a few years ago (https://discourse.urho3d.io/t/node-graph-with-urho-ui/2048), but it seems to not handle the mouse being over it or not. Checking the source, it looks like the important check is `bool UIElement::IsInside(IntVector2 position, bool isScreen)`, which seems to just check the position vs the size of the element, which I assume would result just a rectangular check. Is there any support for curves like the spline curve I mentioned or a circle, for example?

If it's not already there, what do you think would be the best way to add support? ScreenToElement is already virtual, so it should be possible to map from the element to the screen using some sort of fancy coordinate change (beyond a simple matrix multiply) that would achieve the effect. Alternatively, IsInside could be made virtual.

Any other ideas/information is welcome.

-------------------------

Modanung | 2020-04-13 21:27:54 UTC | #2

[quote="SirNate0, post:1, topic:6086"]
Alternatively, IsInside could be made virtual.
[/quote]

Indeed overriding `IsInside` seems the most logical and semantically correct approach, in my view.

-------------------------

SirNate0 | 2020-04-13 21:30:59 UTC | #3

If this is done, should Sprite/BorderImage/OtherStuff override this to check for transparent pixels as well?

-------------------------

Modanung | 2020-04-13 21:38:44 UTC | #4

_That_ sounds a bit too resource heavy as a default. Although it might be useful enough to implement it as an a `bool` argument that disables the transparency check by default, or something similar.

When it comes to circles, a `UIElement::shape_` might make more sense, which could be `Ellipse`.

-------------------------

SirNate0 | 2020-04-13 22:16:11 UTC | #5

Agreed, a bool argument would probably be better, something like `checkExact` or `detailedCheck`, especially since the present behavior seems to have worked for most people. Maybe even an enum like we have for RayOctreeQuery supporting Axis-Aligned checks (default UIElement behavior), Object-Local behavior (default sprite behavior - supports rotations but is still rectangular), and Detailed (which would perform the texture lookup). I'm leaning towards a boolean, since it's simpler though.

I'm not opposed to a UIElement::shape_, but what shapes would be allowed? Obviously Rectangles and probably Ellipses, but what about RoundedRectangles, Diamonds, etc.? And where exactly would it be used? Just to accelerate a more accurate check of GetElementAt compared to a texture read?

As an aside, is this page in the documentation supposed to have a `Not Found :(` error page in the middle (where the graph would usually be)?
https://urho3d.github.io/documentation/HEAD/_octree_query_8h.html#a87b77f7eab5a2ec750d2541c90e6eae8

-------------------------

Modanung | 2020-04-13 22:25:00 UTC | #6

The `shape_` member _could_ replace the `bool` as well, if it could be set to `Mask`, which would query the texture for non-zero alpha at the provided point.

-------------------------

najak3d | 2021-11-14 06:49:15 UTC | #7

We are now using elix22's fantastic URHO.NET, so we're off UrhoSharp, and now compiling wrappers with an up-to-date Urho3D source code base.

We need to revive this question.  We have non-rectangular UI elements, where the processing is being done by Avalonia (We are rendering Avalonia).   We are rendering an Avalonia Window to an Urho UI Sprite element... so we route input from the Sprite to Avalonia.

BUT -- If there isn't an Avalonia Control under the mouse, Avalonia will set their "MouseEvent.Handled = false" - so that we know it "was NOT handled".    In my experience, this is the right way to handle Input Events -- you can default "Handled = true"... but allow the Input Handler method to set it to "False" -- in which case, the event then passes through to the next control beneath it (or the 3D Scene, if no more controls are beneath it).

**IMO, the ONLY change needed here is to add "bool Handled {get; set; }" property to the Urho.ClickEventArgs structure.**

Then non-rectangular components can simply do their own click-area-detection logic, and set Handled = false, if the click needs to pass through it.

**Is there any chance of getting this change implemented in URHO3D soon?**  If not, then we'll need to Hack-around this deficiency with some add-on code.

-------------------------

najak3d | 2021-11-14 06:54:28 UTC | #8

We're in the infancy stages of making it so that Avalonia can render 100% to an in-game URHO.NET GUI, without restrictions/issues.    In order to make this work 100%, we need this type of non-rectangular-transparency support.

Here's a current screenshot of an Avalonia Window rendering with transparency to an URHO Sprite.  But since the Sprite is treated like a solid-rectangle, you CANNOT currently click-into-the-3d-Scene except for outside the outer bounds of this AvaloniaWindow (Urho Sprite).

We gotta fix this deficiency to achieve this objective.

![image|690x427](upload://7DaRJN2UI2c1ICJfpDHwrOQ9tWs.jpeg)

-------------------------

najak3d | 2021-11-18 07:23:57 UTC | #9

FYI, when we're done, this will be released as MIT Open-Source.  Our goal is to create a pattern for making Avalonia render in any .NET-based-Game, starting with Urho.Net.   Elix22 basically did most of the heavy-lifting here.  We're just taking it the rest of the way to the hoop.  We are ecstatic about this capability.

ALSO - as of now, we have hacked-around the Urho UI deficiency of not having a "eventArgs.Handled" property.   So there is not dire need for this fix, but it would be nice.

===
EDIT/UPDATE: so far, we've just implemented our own kludge to get it working.  It wasn't complex.  We're just doing "check alpha channel" for the pixel under the mouse cursor to determine if we have Avalonia consume the mouse event.

Our boolean logic looks like this, for MouseDown (or TouchDown) event:

If (Avalonia.Handled = true || Avalonia.UIPixelAlpha != 0)
 {
       Avalonia Consumes the MouseDown -- and owns the other events until Mouse is released...
}
else
{
      MouseDown event gets processed by Urho Scene, as does all other events until Mouse is released...
}


This is working just fine, but just isn't as clean as it probably should be.

-------------------------

