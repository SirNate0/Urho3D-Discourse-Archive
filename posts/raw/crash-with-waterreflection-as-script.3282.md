Cpl.Bator | 2017-06-27 08:36:25 UTC | #1

Hello, i've found a script for waterreflection here : https://discourse.urho3d.io/t/water-reflection-script/62 , is work fine 
with some modification ( like fov ) with the editor. 

But, when i load the scene with native c++, my application crash with any error message , if i comment
the line 35 & 36: "Viewport@ rttViewport = Viewport(renderer.viewports[0].scene, reflectionCamera);" , the program run without any error and i dont see any reflection...

i have created in c++ an empty scene, after i loading scene and i grabing camera from previously loaded scene for create viewport. and i don't known why that dont work.

can anyone help me ?
thanks. and sorry for my bad english.

-------------------------

Alex-Doc | 2017-06-26 12:03:21 UTC | #2

Please make sure you check the pointers, is viewports[0] valid?
Posting the callstack of the crash would help a lot too.

-------------------------

Cpl.Bator | 2017-06-26 12:12:13 UTC | #3

Ok, i'm beginner with AngelScript, how can view the callstack ?
"renderer.viewports[0].scene" is not provided by the current scene and the curent viewport ?

-------------------------

Alex-Doc | 2017-06-26 13:41:45 UTC | #4

I'm not sure about AngelScript, I'd just check its console output.
You said you can reproduce the crash in C++ too, so you can put a breakpoint on the culprit line of code and see what's going wrong.

Without looking at your code it's difficult to tell where the problem is, the only suggestions I can give you with the information I have are these.

You could also try checking the pointer in AngelScript as:
[code]Viewport@ view = renderer.viewports[0]; 
if(view is null)
    Print("Viewport is not there!");[/code]
Note: the above can be used to check any pointer. For example, the renderer or the camera, just use and adapt to the correct data types.

In C++ would be way simpler though.
If you did not already, I strongly suggest you to learn how to use GDB or VisualStudio debugger, as they literally save you a lot of time and troubles.

-------------------------

