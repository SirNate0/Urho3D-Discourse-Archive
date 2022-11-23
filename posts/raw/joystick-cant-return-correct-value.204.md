att | 2017-01-02 00:58:51 UTC | #1

hi,
I need to use Gyro accelerometer to control my game object. I found JoystickState can return three axis position.
But the coordinate mapping is different on iOS and android devices? and the value returned from iOS device is too small to use.
I tested the JoystickState on nexus 4 and ipad3.

-------------------------

Mike | 2017-01-02 00:58:52 UTC | #2

On Android Axis #0 is left-right and Axis #1 is front-back (Axis #2 is complimentary to the 2 other ones and is not usefull as is).
The Axis values need to be multiplied to suit your needs and Axis #1 may need to be negatively signed.

-------------------------

