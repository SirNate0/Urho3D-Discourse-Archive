godan | 2017-01-02 01:14:25 UTC | #1

I've been using the native UI extensively recently, and I think it's great (despite the ongoing debate to replace it with a third party lib :slight_smile:). However, there are some convenience functions that would be handy:

- Button::SetHoverColor(Color color) /Get
- Button::SetPressedColor(Color color) /Get
- Button::SetNormalColor(Color color) /Get

I have found that having to create separate images for the different button states, when all I need is a different color, adds quite a bit of work. And having these color properties wouldn't change the existing flow. 

Then some more data in the UIEvents:

- Add DX,DY to OnResized (i.e. DX, DY is the difference in pixels from the old size to the new size). This will help with responsive layouts, I think.

In general, I think Urho should come with some higher level UI classes. ListView and ScrollView are really great. Along with this, a good Toolbar class would be nice (I need to write this so I will try to contribute this myself). For example, I wrote a PopUp class that has been a huge time saver: [github.com/danhambleton/UrhoPopUp](https://github.com/danhambleton/UrhoPopUp)

[img]https://dl.dropboxusercontent.com/u/69779082/UrhoPopUp.PNG[/img]

-------------------------

cadaver | 2017-01-02 01:14:25 UTC | #2

The colors certainly make sense (though will make Button attribute inspector even more cluttered; the UIElement attributes themselves are already quite horrible considering how many there are), as does the resize delta.

As for the higher level elements, get contributing :wink:

-------------------------

1vanK | 2017-01-02 01:14:26 UTC | #3

[quote="godan"]

- Button::SetHoverColor(Color color) /Get
- Button::SetPressedColor(Color color) /Get
- Button::SetNormalColor(Color color) /Get
[/quote]

I did smooth color transition between button states in my game [github.com/1vanK/Soulmates/blob ... Button.cpp](https://github.com/1vanK/Soulmates/blob/master/GameSrc/MyButton.cpp)
I think it looks nicer than switching

-------------------------

Lumak | 2017-01-02 01:14:26 UTC | #4

In some industries, they add sprites into a Multiple-image Network Graphics (MNG) file and transition between 4 states:
-normal
-pressed
-hover
-disabled

Which really simplifies creating 2D games or UI layouts.

-------------------------

cadaver | 2017-01-02 01:14:27 UTC | #5

Delta parameters added for resize.

-------------------------

