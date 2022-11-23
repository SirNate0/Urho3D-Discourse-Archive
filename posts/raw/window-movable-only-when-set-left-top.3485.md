Alex-Doc | 2017-08-24 09:31:40 UTC | #1

Hi, I'm trying to make an in-game editor but I'm facing a problem:
The Window elements can only be moved/dragged around with the mouse, when the horizontal and vertical alignment are set respectively to "Left" and to "Top".
Is this a bug or am I doing something wrong?

[Screenshots here](http://imgur.com/a/OuOi1)

-------------------------

cadaver | 2017-08-24 12:00:25 UTC | #2

It is an intentional limitation, because left-top is when the UI element's coordinate system makes directly sense in regard to movement. Possibly it wouldn't be a huge change to the code to support it in any case, but it would involve hackish calculations. Of course you can also simulate any alignment as the start position to the movement, by calculating the coordinates yourself.

-------------------------

