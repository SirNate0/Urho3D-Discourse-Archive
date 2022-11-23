JTippetts | 2017-10-06 02:09:05 UTC | #1

How do you ensure that a custom UI widget generates drag events? I inherit a widget type from UI::Button. UI::Button generates drag events just fine if I use a Button, but if I use the custom widget type instead, no drag events are generated; instead, it just moves the parent window that owns the widget buttons.

-------------------------

JTippetts | 2017-10-06 02:50:09 UTC | #2

Nevermind on this. I had the widget set enabled=false by default. Sorry.

-------------------------

