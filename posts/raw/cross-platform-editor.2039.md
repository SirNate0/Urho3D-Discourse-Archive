enelex | 2017-01-02 01:12:29 UTC | #1

Hi!

Some time I close look at urho. And my like this. Very nice performance. I tested unity, ue4, but urho get best performance.
So we planed foundate us studio game project on this engine.

Ever nice, but I not pro coder, little know java, today write script launcher for urho on my table. And me serious need editor on my android table. For work every time on project. 
Maybe you say for what on android game development tools, editor, its be very hard.
No, its nice, table really big.

About running, every okey except no line/point render work and mouse action. 
Line, point don't need. But with viewport big trouble. Don't turn, don't translate. Touchscreen don't work. N GUI nice work with touch.

Pliss help make editor work with touch.

-Thank

-------------------------

Bananaft | 2017-01-02 01:12:30 UTC | #2

Hello, welcome to the forum.

Have you considered getting a mouse for your tablet? Might be much easier than fixing touch input.

-------------------------

cadaver | 2017-01-02 01:12:30 UTC | #3

It's relatively easy to take the virtual joystick & camera rotation code from e.g. NinjaSnowWar. However I'm fairly certain the user experience will still be lacking, as the editor simply has been programmed for keyboard & mouse, there's no way around it, and I don't think "official" Urho developer time should be spent on this.

-------------------------

enelex | 2017-01-02 01:12:37 UTC | #4

Hi.

Thank for answer. Nice, nice, nice engine. Work very good on table.

I explore editor view code and some other stuff. So I replace mouse button input.touches[0].delta.x != 0 || input.touches[0].delta.x != 0

Its start work, camera success rotate. But in console error null pointer exception at this line. I can't fix. 

And cannot understand how to use input.touchBegin/Move/End - when I try - get crash.

Scripting get very nice performance.

cadaver, thank for engine. 
I explore more that unreal and unity, but first time see this performance. I mean on android table. Desktop its desktop...

-------------------------

cadaver | 2017-01-02 01:12:37 UTC | #5

input.touches[0] is illegal when there are no touches ongoing, and is going to return a null. To be sure, have code like:

[code]
if (input.numTouches > 0 && input.touches[0] !is null)
{
    ...
}
[/code]

-------------------------

enelex | 2017-01-02 01:12:37 UTC | #6

Thank, its work. But I can't detect touch end. else don't work, don't release mouse.

[code]
void AndroidUpdateView (float timeStep) {
	 
	 if (ui.HasModalElement() || ui.focusElement !is null) {
        ReleaseMouseLock();
        return;
    }
	 
	//Rotate camera
	if (input.numTouches > 0 && input.touches[0] !is null) {
		SetMouseLock();		
		activeViewport.cameraYaw += input.touches[0].delta.x * cameraBaseRotationSpeed;
		activeViewport.cameraPitch += input.touches[0].delta.y * cameraBaseRotationSpeed;
    	Quaternion q = Quaternion(activeViewport.cameraPitch, activeViewport.cameraYaw, 0);
    	cameraNode.rotation = q; 		
     }
     
     else {
     	ReleaseMouseLock();
     }
}
[/code]

-------------------------

