Lys0gen | 2020-03-27 19:15:57 UTC | #1

Hello,
I was wondering if there is a way to give UI elements a size relative to the window/parent. I see that it is possible to set a relative position with the "Min Anchor"/"Max Anchor"/"Pivot" attributes but for size attributes only absolute pixels seem to work. Of course I could calculate and adjust the size in code after reading the layout, but if in any way possible I would prefer to have it all in the XML layout file.

(And another unrelated question, not sure if it warrants another topic:)
Urho/SDL window creation seems to disable Windows aero designs, which is kind of ugly. Additionally, alt+tabbing causes a brief black screen flash, which is especially annoying if I have set the window to be a borderless fullscreen mode, this seems to be abnormal from the borderless-fullscreen-windowed mode that I know from any games. Any way to change that?

Thanks!

-------------------------

Modanung | 2020-03-28 13:30:00 UTC | #2

Would `UI::SetScale` and `UIElement::SetLayoutFlexScale` work for you?

I personally would love to see SVG support to ensure pixel-perfect results in these cases.

-------------------------

Lys0gen | 2020-03-29 17:15:57 UTC | #3

Hmm, not really I'm afraid. That would still require me to calculate proper ratios in code. Thanks anyway, guess I'll just set a target resolution and scale everything according to the actual resolution in code then.

-------------------------

lezak | 2020-03-29 21:22:59 UTC | #4

[quote="Lys0gen, post:1, topic:6019"]
I see that it is possible to set a relative position with the “Min Anchor”/“Max Anchor”/“Pivot” attributes but for size attributes only absolute pixels seem to work.
[/quote]

Actually anchors should do the trick as they affect size, not sure where You can have a problem - maybe some size setup (min/max/fixed size), that doesn't allow anchors to do their job?

-------------------------

Lys0gen | 2020-03-29 21:22:56 UTC | #5

Huh, you're right! Thanks. I didn't set 
`<attribute name="Enable Anchor" value="true" />`
And while the positioning with anchors still worked, the max anchor apparently doesn't. Weird. I gotta say, the documentation here is also rather lacking, or I just can't find a page explaining the behaviour...

-------------------------

