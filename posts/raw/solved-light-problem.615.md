Lichi | 2017-01-02 01:01:40 UTC | #1

Hi, I created a spotlight on the scene attached to the camera, but when the camera moves (and the light), light starts blinking creating horizontal lines. Anyone know how to fix it?
ty.
PS: i take a screenshot to show what happens to me but in the screenshot no errors appear :/

-------------------------

Lichi | 2017-01-02 01:01:43 UTC | #2

I used paint to simulate the error
[img]http://www.subeimagenes.com/img/light-1168503.html[/img]
[url]http://www.subeimagenes.com/img/light-1168503.html[/url]
PS: the error ocurrs when light is moving.

-------------------------

hdunderscore | 2017-01-02 01:01:43 UTC | #3

Seems like tearing? You can try enabling vsync either via [url=http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_audio.html#a47d9e2bbbd31dc8ded6f4e83486cdcb4]SetMode[/url] or the engine 'VSync' initialization parameter.

-------------------------

Lichi | 2017-01-02 01:01:43 UTC | #4

[quote="hd_"]Seems like tearing? You can try enabling vsync either via [url=http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_audio.html#a47d9e2bbbd31dc8ded6f4e83486cdcb4]SetMode[/url] or the engine 'VSync' initialization parameter.[/quote]
thank you very much !! I spent a whole day trying to fix the problem (:

-------------------------

