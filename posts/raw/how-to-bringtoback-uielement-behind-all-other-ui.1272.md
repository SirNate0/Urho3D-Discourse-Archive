codingmonkey | 2017-01-02 01:06:31 UTC | #1

There is code, but it's no working properly. This UI Text still placed above menus and other windows.
[pastebin]8ttbbKKg[/pastebin]

-------------------------

rasteron | 2017-01-02 01:06:32 UTC | #2

AFAIK, there's only the BringToFront() function and both attributes (front and back) when you focus on the element.

[urho3d.github.io/documentation/1 ... 738aed7ceb](http://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_u_i_element.html#a497ae1d9996a1eeb5d84ae738aed7ceb)

maybe do an iteration excluding the one you want to sort way back

-------------------------

