umen | 2017-01-02 00:58:56 UTC | #1

Hello 
this is for the mobile developers , that are using this engine . 
in other engines for example cocose2d-x one can develop in windows desktop his game and when there is need to simulate the Touch and multiTouch feature , its using the mouse .  ( as the mac/ android simulator do)
this very good feature that enable productivity as many are prefer to develop on windows and then to the final touches and compilation on mac or eclipse with real device.

-------------------------

cadaver | 2017-01-02 00:58:56 UTC | #2

This is a good idea. It just has to be hacked deep enough into SDL (add a SDL touch device, emit SDL touch events) so that SDL's gesture recognition can work on the emulated touch.

-------------------------

umen | 2017-01-02 00:58:57 UTC | #3

maybe we can ask the SDL experts in the forums how is the best way to hack this .
i found some links that port the mouse events to SDL touch events like this :
[url]http://www.dinomage.com/2013/05/howto-sdl-on-android-part-2-platform-details/[/url]
[url]http://www.philhassey.com/blog/2010/07/23/android-day-4-video-cleanup-input-handling/[/url]

but not info about mapping mouse events to touch events , maybe it can be custom build in the Urho3D layer , i don't know much of Urho3d how complex can it be .
looking in the Touch.cpp source i see there is mapping from the screen Gyroscope to the SDL joystick . i wander how complex it to do the same mouse -> to -> touch

-------------------------

cadaver | 2017-01-02 00:58:57 UTC | #4

Initial single touch emulation via the left mouse button is in. Something that would be easy to add would be a two-finger pinch via eg. right mouse: the start point of a drag sets a stationary finger, and the second finger moves with the mouse.

-------------------------

umen | 2017-01-02 00:58:57 UTC | #5

Hey you are quick , can you tell me where did you changed the code ? im going to do git pull of the master , 
don't worry about the  two-finger pinch its not even implemented in the other engines as far as i know if you implement it the engine will be  ahead of the others  , left mouse for touch / multi touch  is fine for start .
so how to test it ?
Thanks!

-------------------------

cadaver | 2017-01-02 00:58:57 UTC | #6

The function you're looking for is Input::SetTouchEmulation(), or input.touchEmulation property in script. It is briefly mentioned on the Input doxygen page.

-------------------------

umen | 2017-01-02 00:58:57 UTC | #7

Ok got the code compiles just fine , now looking at the SetTouchEmulation(bool enable) , how does it work ?
in my game in the start i just set it to true , so each time i click with my left mouse , it is like i touched with my finger right ? 
and when testing in iOS i don't do any think , its automatically will support the Touch events with the right positions and all right ? 
Thanks again

-------------------------

cadaver | 2017-01-02 00:58:57 UTC | #8

Yes, when you set it to true on desktop platforms, normal mouse events stop, but you start getting touch events when you hold the left button down. You'll also get stationary touch events from other mouse buttons.

On Android and iOS SetTouchEmulation(true) is disregarded.

Btw. if you grab the very latest master branch revision, you can also use the command line option -touch in Urho3DPlayer to enable the emulation mode.

-------------------------

