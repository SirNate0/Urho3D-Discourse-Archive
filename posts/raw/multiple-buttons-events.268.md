Mike | 2017-01-02 00:59:15 UTC | #1

It seems that currently once an UIElement has its Event triggered the other Buttons' Events get silenced.
For example,when pressing in a row 2 buttons subscribed to "Pressed" or "Released" event, only the first one is triggered.
On mobiles it's good to be able to press multiple buttons to achieve combined effects or do multi-selection..., like move + jump when move button and jump button are both pressed.
So I'd like to know how to override the default behavior of UIElement events.

-------------------------

friesencr | 2017-01-02 00:59:15 UTC | #2

The pressed event tracks the last element that was moused down/touched down on.  There is only 1 variable that tracks the element click.  If the element is the same for the down and up events then a 'pressed' event is emitted.  If that variable was refactored to be a vector<uielement> it might work.  It might not be that easy as the drag code my be lumped in there as well as double click.

-------------------------

cadaver | 2017-01-02 00:59:16 UTC | #3

The code is basically written for mouse (one pressed element at a time), and touch is an afterthought, so yes, it would need modifications to work.

-------------------------

