Kanfor | 2017-01-02 01:10:35 UTC | #1

Hi, urhofans.

This is my code

[code]SubscribeToEvent(Ui_Button[TOUCH_BUTTON_HELP].button_, E_PRESSED, URHO3D_HANDLER(Ui_Class, PressHelpDown));[/code]

It works fine, but if I don't move the cursor mouse and I press <space> the function PressHelpDown is call again. Why?
Is there a solution for this problem?

Thank you!

-------------------------

1vanK | 2017-01-02 01:10:35 UTC | #2

after click on button, it still focused, so bunnon pressed again when you press space. it is tipycal behavior for UI (try same in Windows)
you can use SetFocusMode(FM_NOTFOCUSABLE)

-------------------------

Kanfor | 2017-01-02 01:10:42 UTC | #3

Many thanks again!  :wink:

-------------------------

