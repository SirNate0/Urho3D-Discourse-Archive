wqf | 2021-10-20 15:16:14 UTC | #1

I try to use the engine without the player.I’m working with wxWidgets + Urho3D and I  use a  wxPanel as the externalwindow.Below are the parameters of the engine I set.
```c++
engineParameters_["ResourcePaths"] = "Data;CoreData";
	engineParameters_["LogName"] = "wxUrho3D.log";
	engineParameters_["ExternalWindow"] = panel->GetHandle();
	engineParameters_["FullScreen"] = false;
	engineParameters_["WindowResizable"] = true;
	engineParameters_["WindowWidth"] = 1280;
	engineParameters_["WindowHeight"] = 720;
```
It works well in windows,and the player is also hidden.But an error will be reported on the mac.The following is the error message on the mac.
![{CF33DD23-2116-48D6-7A45-473A07A50B76}|690x388](upload://sIWCYQYStm39jbrsS04d8QpNapM.png)
if anyone can give me some suggestions or tell me the correct usage of externalwindow,I will be grateful.

-------------------------

elix22 | 2021-10-21 06:27:48 UTC | #2

Yep , it's a known issue
You will have to do some modifications on the SDL side to make it work.
Look at the link below , it should be a good start 

https://github.com/flowercodec/sdl2

-------------------------

wqf | 2021-10-21 07:07:41 UTC | #3

Thank you very much for your suggestion,I will try it later.

-------------------------

