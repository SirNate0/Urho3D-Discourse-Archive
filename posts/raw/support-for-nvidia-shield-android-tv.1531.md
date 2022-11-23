esak | 2017-01-02 01:08:20 UTC | #1

I have purchased an Nvidia Shield Android TV (based on Android 5.1) and tried to run my game on it.
Generally it seemed to work, but showed some glitches on some textures (which doesn't show up on my Android phone and tablet).
But my main concern is that I can't control the game with the included Shield controller (that basically looks like an Xbox controller).
So what do I need to do to support this controller, any ideas?

-------------------------

esak | 2017-01-02 01:08:20 UTC | #2

I have made some progress with the Shield controller:
I hooked on to the events for JoystickButtonDown, JoystickAxisMove and JoystickHatMove and got some events here.
The controller is though not recognized (in IsController()), but the button-mapping seems to be the same as the defined controller-buttons.
The problem I have now is that these events are not fired when holding down the axis-controller and the hat-buttons (they are just triggered once when pressing down) + I don't know how to correcly interpret the axis-values.
Anyone tried hooking up some other game controller (like Xbox) and have some code to share?

-------------------------

thebluefish | 2017-01-02 01:08:21 UTC | #3

My [url=https://github.com/thebluefish/Urho3D-Misc/tree/master/InputManager]old InputMapper stuff[/url] worked fine with Xbox 360 and PS4 controller (Using DS4Windows), however it was targeting Urho3D version 1.32, so it will need to be updated before it is useful. It is also very limited in use and outdated by a newer version in my private repo, so I cannot provide any support on it.

It is normal behavior for button events to only fire once. That is why they are events. Ideally you would internally track the state of some action, and trigger the action based on input events. Alternatively you can query the Input system yourself to track the input state during each Update.

Axis stuff can get somewhat mucked up across controllers. Some controllers use different axis for different things, including the Xbox 360 controller's famous triggers (which are both implemented as 1 axis when using DirectInput).

IsController() is based on SDL_IsGameController. SDL will mark a joystick as a controller if it has standardized mapped bindings for the controller. These are added via SDL_GameControllerAddMapping, and you can see an example of this in the InputManager example above where I provide bindings for the Xbox 360 controller. If bindings don't exist, SDL will treat the joystick as a simple generic joystick.

-------------------------

esak | 2017-01-02 01:08:22 UTC | #4

@thebluefish: Thanks for the pointer!

I managed to read the current axis and hat values in SceneUpdate-event, using the defined controller-constants. So now that part is working.  :slight_smile: 

Now I'm struggling with rendering glitches, it seems that when I use shadows I get black dithering (really small and many points) on the shadowed nodes.
If I turn all shadows off, everything looks OK.
The strange thing is that it works correctly with shadows on my Android-tablet (Samsung Glaxy Note 8.0).

Another problem is that on my tablet, it reports that there is a joystick (when there isn't) and this is connected to the accelerometer!

Any pointers on my new issues?

-------------------------

