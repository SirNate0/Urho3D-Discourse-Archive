Mike | 2017-01-02 00:58:47 UTC | #1

Currently I'm using this piece of code (inside a MouseButtonDown Event) to acquire a RigidBody2D (in lua):

[code]
	local touchPos = camera:ScreenToWorldPoint(Vector3(eventData:GetInt("X") / graphics.width, eventData:GetInt("Y") / graphics.height, 0))
	local body = physicsWorld2D:GetRigidBody(touchPos)
[/code]
It works fine, but is there a better/easier way to do this?

-------------------------

aster2013 | 2017-01-02 00:58:47 UTC | #2

Hi, mike

Do you think provide a function
[code]
RigidBody2D* PhysicsWorld2D::GetRigidBody(int mouseX, int mouseY, Camera* camera = 0) const;
[/code] is better?

-------------------------

Mike | 2017-01-02 00:58:47 UTC | #3

Hi aster,

This kind of function would be awesome as it does the math for us and is easy to use (less script is always better).

-------------------------

aster2013 | 2017-01-02 00:58:47 UTC | #4

I have added it for you, but please attention, when your viewport size not equal to graphics size, it will get error result.

-------------------------

Mike | 2017-01-02 00:58:48 UTC | #5

That's very nice, thanks aster.

-------------------------

Mike | 2017-01-02 00:58:48 UTC | #6

Aster, sorry for not having seen this at first, but 'mouseX' and 'mouseY' can in fact be misleading, as the function is intended to work with any kind of input, whether mouse, touch, joystick...
inputX and inputY, or simply x and y as in GetElementAt() could be more explanatory, what do you think?

-------------------------

aster2013 | 2017-01-02 00:58:48 UTC | #7

thanks, i will rename it.

-------------------------

