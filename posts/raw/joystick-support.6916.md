nickwebha | 2021-07-10 11:43:52 UTC | #1

Is there a proper way to access the joystick? I have my:

```
void Level::GamePadConnected( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Connected" << std::endl;
};

void Level::GamePadDisconnected( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Disconnected" << std::endl;
};

void Level::GamePadButtonDown( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Button Down" << std::endl;
};

void Level::GamePadButtonUp( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Button Up" << std::endl;
};

void Level::GamePadAxisMove( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Axis Move" << std::endl;
};

void Level::GamePadHatMove( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Hat Move" << std::endl;
};

SubscribeToEvent( Urho3D::E_KEYDOWN, URHO3D_HANDLER( Level, HandleKeyDown ) );
SubscribeToEvent( Urho3D::E_JOYSTICKCONNECTED, URHO3D_HANDLER( Level, GamePadConnected ) );
SubscribeToEvent( Urho3D::E_JOYSTICKDISCONNECTED, URHO3D_HANDLER( Level, GamePadDisconnected ) );
SubscribeToEvent( Urho3D::E_JOYSTICKBUTTONDOWN, URHO3D_HANDLER( Level, GamePadButtonDown ) );
SubscribeToEvent( Urho3D::E_JOYSTICKBUTTONUP, URHO3D_HANDLER( Level, GamePadButtonUp ) );
SubscribeToEvent( Urho3D::E_JOYSTICKAXISMOVE, URHO3D_HANDLER( Level, GamePadAxisMove ) );
SubscribeToEvent( Urho3D::E_JOYSTICKHATMOVE, URHO3D_HANDLER( Level, GamePadHatMove ) );
```
But can not figure out how to get the values out. Joystick IDs, values for different axis, buttons, etc. I have searched and searched but can not find anything on Google or in the samples.

This is as far as I have gotten. I have four gamepads connected for four players.

-------------------------

SirNate0 | 2021-07-10 16:34:50 UTC | #2

The information you want is stored in the eventData argument. See here for a list of which events have which parameters:
https://urho3d.io/documentation/HEAD/_event_list.html

Also, you can just the Input subsystem directly rather than subscribing to the fairly large number of events. It's up to you and how complicated your actions would be which you want to go with.

-------------------------

nickwebha | 2021-07-10 16:35:35 UTC | #3

I saw this list but there was one thing that confused me about it. Let us say I have the lines:

```
void Level::GamePadButtonDown( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Button Down " << eventData[ Urho3D::XXX ].GetInt() << std::endl;
};
```
in order to get which button was pressed. What should *XXX* be? (Obviously using `cout` is just a test to see it working, the real code will do something with it.)

In other words, the list does not define which constant in the `Urho3D` namespace I must use.

I tried checking out the Urho3D source and found `InputConstants.h` and `InputEvents.h`. Neither of which helped (unless I am missing something, which I am sure I am). I also checked out the samples (grep'ed and everything) but none of them seem to demonstrate the proper usage.

I tried

```
void Level::GamePadButtonDown( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Button Down " << eventData[ Urho3D::JoystickButtonDown::Button ].GetInt() << std::endl;
};
```
but no go.

**Edit 1**
The `GetSubsystem< Urho3D::Input >()` method would probably be preferred.

**Edit 2**

```
void Level::GamePadButtonDown( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Button Down " << eventData[ Urho3D::MouseButtonDown::P_BUTTON ].GetInt() << std::endl;
};

void Level::GamePadButtonUp( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Button Up " << eventData[ Urho3D::MouseButtonUp::P_BUTTON ].GetInt() << std::endl;
};
```

This seems to be working. Is this correct? Are the joysticks emulated as mice? Or just called that?

**Edit 3**

```
void Level::GamePadConnected( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Connected " << eventData[ Urho3D::JoystickConnected::P_JOYSTICKID ].GetInt() << std::endl;
};

void Level::GamePadDisconnected( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Disconnected " << eventData[ Urho3D::JoystickDisconnected::P_JOYSTICKID ].GetInt() << std::endl;
};

void Level::GamePadButtonDown( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Button Down " << eventData[ Urho3D::JoystickButtonDown::P_JOYSTICKID ].GetInt() << " " << eventData[ Urho3D::JoystickButtonUp::P_BUTTON ].GetInt() << std::endl;
};

void Level::GamePadButtonUp( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Button Up " << eventData[ Urho3D::JoystickButtonUp::P_JOYSTICKID ].GetInt() << " " << eventData[ Urho3D::JoystickButtonUp::P_BUTTON ].GetInt() << std::endl;
};

void Level::GamePadAxisMove( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Axis Move " << eventData[ Urho3D::JoystickAxisMove::P_JOYSTICKID ].GetInt() << " " << eventData[ Urho3D::JoystickAxisMove::P_AXIS ].GetInt() << " " << eventData[ Urho3D::JoystickAxisMove::P_POSITION ].GetFloat() << std::endl;
};

void Level::GamePadHatMove( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	std::cout << "GamePad Hat Move " << eventData[ Urho3D::JoystickHatMove::P_JOYSTICKID ].GetInt() << " " << eventData[ Urho3D::JoystickHatMove::P_HAT ].GetInt() << " " << eventData[ Urho3D::JoystickHatMove::P_POSITION ].GetInt() << std::endl;
};
```

I think I got it. Is it supposed to be more like this? They give the same results.

I had to dig into *InputEvents.h* for the values.

-------------------------

