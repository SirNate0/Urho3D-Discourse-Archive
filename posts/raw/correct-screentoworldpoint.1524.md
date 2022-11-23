freegodsoul | 2017-01-02 01:08:15 UTC | #1

Hi!
[b]Camera::ScreenToWorldPoint()[/b] works as not as expected. Currently, depth of the screen point is used as a distance on normalized ray. It gives a spherical distortion effect to flat geometry on screen (right picture). ?ommon sense prompts me that this method should [b]unproject[/b] point by using camera projection matrix inverse (left picture). Ray-based method should be renamed for example in [b]ScreenToWorldPointPolar[/b] or something else. In some cases this can be useful.

[img]http://gdurl.com/m_0u[/img]

-------------------------

cadaver | 2017-01-02 01:08:16 UTC | #2

Good point, the current implementation is indeed wrong.

You can easily get the current behavior by calling GetScreenRay() and manipulating the returned ray so I don't believe a separate function is needed.

-------------------------

cadaver | 2017-01-02 01:08:16 UTC | #3

Fixed in master branch.

-------------------------

freegodsoul | 2017-01-02 01:08:16 UTC | #4

[quote="cadaver"]Fixed in master branch.[/quote]
Thanks! =)

-------------------------

