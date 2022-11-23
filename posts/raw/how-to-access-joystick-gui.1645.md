practicing01 | 2017-01-02 01:09:12 UTC | #1

Hello, I've loaded a joystick with the following lua code:
[code]
local layout = cache:GetResource("XMLFile", "UI/DualJoy.xml")
self.joyID_ = input:AddScreenJoystick(layout, cache:GetResource("XMLFile", "UI/DefaultStyle.xml"))
input:SetScreenJoystickVisible(self.joyID_, true)
[/code]

I tried accessing its gui through the following code but it didn't work:
[code]
local joystick = input:GetJoystick(self.joyID_)
local joygui = joystick.screenJoystick
[/code]

I need to be able to resize the gui for when the resolution changes.  On native it does not resize automatically and I don't have a second phone to test mobile.  If it resizes automatically on mobile then I can forget about native.  Thanks for any help.

Side Note:  Diagonal directions for hats don't work, quite annoying on mobile..

-------------------------

