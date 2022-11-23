fnadalt | 2018-08-25 22:34:44 UTC | #1

Hi! I'd like to report en Editor crash. When clicking on an item in the Hierarchy panel, the app crashed, without even showing anything
on the Inspector panel. Latest master branch debug compilation.

Backtrace:
#0  0x0000555555d046de in Urho3D::CScriptArray::Release (this=0x555500005555) at /home/flaco/build/Urho3D/Source/Urho3D/AngelScript/Addons.cpp:1596
#1  0x0000555555d6264f in asCScriptEngine::CallObjectMethod (this=0x5555573215f0, obj=0x555500005555, i=0x555557335c20, s=0x555557335cb0)
    at /home/flaco/build/Urho3D/Source/ThirdParty/AngelScript/source/as_scriptengine.cpp:4020
#2  0x0000555555d62501 in asCScriptEngine::CallObjectMethod (this=0x5555573215f0, obj=0x555500005555, func=25)
    at /home/flaco/build/Urho3D/Source/ThirdParty/AngelScript/source/as_scriptengine.cpp:3987
#3  0x0000555555d8e080 in asCContext::ExecuteNext (this=0x555558025860) at /home/flaco/build/Urho3D/Source/ThirdParty/AngelScript/source/as_context.cpp:2781
#4  0x0000555555d8a6f4 in asCContext::Execute (this=0x555558025860) at /home/flaco/build/Urho3D/Source/ThirdParty/AngelScript/source/as_context.cpp:1318
#5  0x0000555555b3d7af in Urho3D::ScriptFile::Execute (this=0x555557159790, function=0x555557fc91e0, parameters=..., unprepare=true)
    at /home/flaco/build/Urho3D/Source/Urho3D/AngelScript/ScriptFile.cpp:323
#6  0x0000555555b4079a in Urho3D::ScriptEventInvoker::HandleScriptEvent (this=0x555558261b20, eventType=..., eventData=...)
    at /home/flaco/build/Urho3D/Source/Urho3D/AngelScript/ScriptFile.cpp:955
#7  0x0000555555b46797 in Urho3D::EventHandlerImpl<Urho3D::ScriptEventInvoker>::Invoke (this=0x555557f23a80, eventData=...)
    at /home/flaco/build/Urho3D/Source/Urho3D/AngelScript/../AngelScript/../Core/Object.h:315
#8  0x0000555555b269d1 in Urho3D::Object::OnEvent (this=0x555558261b20, sender=0x555557d342c0, eventType=..., eventData=...)
    at /home/flaco/build/Urho3D/Source/Urho3D/Core/Object.cpp:116
#9  0x0000555555b274d6 in Urho3D::Object::SendEvent (this=0x555557d342c0, eventType=..., eventData=...) at /home/flaco/build/Urho3D/Source/Urho3D/Core/Object.cpp:330
#10 0x0000555555b272da in Urho3D::Object::SendEvent (this=0x555557d342c0, eventType=...) at /home/flaco/build/Urho3D/Source/Urho3D/Core/Object.cpp:294
#11 0x0000555555ecf0d9 in Urho3D::ListView::SetSelections (this=0x555557d342c0, indices=...) at /home/flaco/build/Urho3D/Source/Urho3D/UI/ListView.cpp:585
#12 0x0000555555eced47 in Urho3D::ListView::SetSelection (this=0x555557d342c0, index=4) at /home/flaco/build/Urho3D/Source/Urho3D/UI/ListView.cpp:513
#13 0x0000555555ed0eaf in Urho3D::ListView::HandleUIMouseClick (this=0x555557d342c0, eventType=..., eventData=...)
    at /home/flaco/build/Urho3D/Source/Urho3D/UI/ListView.cpp:1046
#14 0x0000555555ed57c9 in Urho3D::EventHandlerImpl<Urho3D::ListView>::Invoke (this=0x555557f19f70, eventData=...)
    at /home/flaco/build/Urho3D/Source/Urho3D/UI/../Core/../Core/Object.h:315
#15 0x0000555555b26a1c in Urho3D::Object::OnEvent (this=0x555557d342c0, sender=0x555556fc39c0, eventType=..., eventData=...)
    at /home/flaco/build/Urho3D/Source/Urho3D/Core/Object.cpp:124
#16 0x0000555555b27638 in Urho3D::Object::SendEvent (this=0x555556fc39c0, eventType=..., eventData=...) at /home/flaco/build/Urho3D/Source/Urho3D/Core/Object.cpp:361
#17 0x0000555555e925da in Urho3D::UI::SendClickEvent (this=0x555556fc39c0, eventType=..., beginElement=0x555558dd7d10, endElement=0x555558dd7d10, pos=...,
    button=Urho3D::MOUSEB_LEFT, buttons=..., qualifiers=...) at /home/flaco/build/Urho3D/Source/Urho3D/UI/UI.cpp:1650
#18 0x0000555555e917ba in Urho3D::UI::ProcessClickEnd (this=0x555556fc39c0, windowCursorPos=..., button=Urho3D::MOUSEB_LEFT, buttons=..., qualifiers=..., cursor=
    0x555557d0d310, cursorVisible=true) at /home/flaco/build/Urho3D/Source/Urho3D/UI/UI.cpp:1472
#19 0x0000555555e92a5e in Urho3D::UI::HandleMouseButtonUp (this=0x555556fc39c0, eventType=..., eventData=...)
    at /home/flaco/build/Urho3D/Source/Urho3D/UI/UI.cpp:1720
#20 0x0000555555e9cf33 in Urho3D::EventHandlerImpl<Urho3D::UI>::Invoke (this=0x555556fbfaf0, eventData=...)
    at /home/flaco/build/Urho3D/Source/Urho3D/UI/../Core/../Core/Object.h:315
#21 0x0000555555b26a1c in Urho3D::Object::OnEvent (this=0x555556fc39c0, sender=0x555556f76f70, eventType=..., eventData=...)
    at /home/flaco/build/Urho3D/Source/Urho3D/Core/Object.cpp:124
#22 0x0000555555b27638 in Urho3D::Object::SendEvent (this=0x555556f76f70, eventType=..., eventData=...) at /home/flaco/build/Urho3D/Source/Urho3D/Core/Object.cpp:361
#23 0x0000555555fe71e0 in Urho3D::Input::SetMouseButton (this=0x555556f76f70, button=Urho3D::MOUSEB_LEFT, newState=false)
    at /home/flaco/build/Urho3D/Source/Urho3D/Input/Input.cpp:1768
#24 0x0000555555fe7eeb in Urho3D::Input::HandleSDLEvent (this=0x555556f76f70, sdlEvent=0x7fffffffe3e0) at /home/flaco/build/Urho3D/Source/Urho3D/Input/Input.cpp:1961
#25 0x0000555555fe1ead in Urho3D::Input::Update (this=0x555556f76f70) at /home/flaco/build/Urho3D/Source/Urho3D/Input/Input.cpp:419
#26 0x0000555555fe9ed7 in Urho3D::Input::HandleBeginFrame (this=0x555556f76f70, eventType=..., eventData=...)
    at /home/flaco/build/Urho3D/Source/Urho3D/Input/Input.cpp:2436
#27 0x0000555555ff08ed in Urho3D::EventHandlerImpl<Urho3D::Input>::Invoke (this=0x5555572ee430, eventData=...)
    at /home/flaco/build/Urho3D/Source/Urho3D/Input/../Core/../Core/Object.h:315
#28 0x0000555555b26a1c in Urho3D::Object::OnEvent (this=0x555556f76f70, sender=0x555556f68960, eventType=..., eventData=...)
    at /home/flaco/build/Urho3D/Source/Urho3D/Core/Object.cpp:124
#29 0x0000555555b27638 in Urho3D::Object::SendEvent (this=0x555556f68960, eventType=..., eventData=...) at /home/flaco/build/Urho3D/Source/Urho3D/Core/Object.cpp:361
#30 0x0000555555b2078e in Urho3D::Time::BeginFrame (this=0x555556f68960, timeStep=0.0187795013) at /home/flaco/build/Urho3D/Source/Urho3D/Core/Timer.cpp:126
#31 0x0000555555b0890a in Urho3D::Engine::RunFrame (this=0x555556f68f40) at /home/flaco/build/Urho3D/Source/Urho3D/Engine/Engine.cpp:497
#32 0x0000555555b1831e in Urho3D::Application::Run (this=0x555556f68e90) at /home/flaco/build/Urho3D/Source/Urho3D/Engine/Application.cpp:86
#33 0x0000555555a94abe in RunApplication () at /home/flaco/build/Urho3D/Source/Tools/Urho3DPlayer/Urho3DPlayer.cpp:42
#34 0x0000555555a94b70 in main (argc=3, argv=0x7fffffffe7d8) at /home/flaco/build/Urho3D/Source/Tools/Urho3DPlayer/Urho3DPlayer.cpp:42

Scene: bin/Data/Scenes/World.xml

“World” project:
https://drive.google.com/open?id=1chko8MpacAUgmSWMnhY0dTEI18wkmxX_

4.17.2-1-ARCH
gcc versión 8.1.1
AMD Athlon(tm) 64 X2 Dual Core Processor 4600+
1995MiB System memory
Cedar [Radeon HD 5000/6000/7350/8350 Series]

-------------------------

weitjong | 2018-08-26 04:17:54 UTC | #2

It is most probably related to AngelScript version upgrade. The latest version of AngelScript has changed how it handles constant strings. On our side that has impacted how we write our StringFactory class. In the master branch we have now a new StringFactory class which is backed by StringMap type (aka `HashMap<StringHash, String>`). In order to make it works, the hash generated by StringHash class should be good and fast enough without the worry of hash collision. To do that, I have changed the hash calculation logic to be case-sensitive (see https://urho3d.github.io/documentation/HEAD/_porting_notes.html "From 1.7 to master"). That change has broken the Editor somewhat and the necessary fixes have been made, but I am not surprised if there are still some being left out.

If you have some saved XML files, you have to make sure all your string constants have the correct letter case. For example: "CheckBox" as a UIElement type is correct, while "Checkbox" is wrong. Depends on where the string constant is being used, the mismatch may cause an AS crashes.

HTH.

-------------------------

fnadalt | 2018-08-29 17:36:56 UTC | #3

I con reproduce the crash simply by:
Open Editor
Add local Node
(Try to) add a Static Model.... Crash.

I reached Scripts/Editor/AttributeEditor.as:1215... attrInfo.type=12
Fails within GetResourcePicker... never returns I think
Called from Scripts/Editor/AttributeEditor.as:366

Help...

-------------------------

weitjong | 2018-08-30 13:37:46 UTC | #4

I am not able to reproduce the crash on my Linux host system. Added the static model component and picked a model  to render successfully.

-------------------------

JTippetts | 2018-08-31 02:54:57 UTC | #5

Make sure your Urho3DPlayer.exe is seeing the absolute latest CoreData and Data folders. The line numbers you list ( [366](https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scripts/Editor/AttributeEditor.as#L366) and  [1215](https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scripts/Editor/AttributeEditor.as#L1215) ) don't really seem to match up well with the current version of AttributeEditor.as, unless I'm mistaken, so you might be trying to run an old version and that's an invitation to Crash City.

-------------------------

MrMilad | 2018-12-09 14:43:58 UTC | #6

I'm having the same issue.
vs 2017 15.9.3
win10 10.0.15063 Build 15063
NVIDIA GeForce GT 640M
8gb ram

-------------------------

Yatsomi | 2019-04-26 20:40:39 UTC | #7

@fnadalt Hi. I had the same problem with editor. Crash after adding components. Using latest commit in windows 10.
My problem fixed using @lezak suggestion in [here](https://github.com/urho3d/Urho3D/issues/2384). Changing line 1203 in AttributeEditor.as 
from
`if (resourcePickers[i].type == resourceType)` 
to 
`if (resourcePickers[i].type.value == resourceType.value)`

-------------------------

Modanung | 2019-02-13 09:20:41 UTC | #8

If you only modified a script (as-file) rebuilding should not be required.

-------------------------

Yatsomi | 2019-02-20 13:39:26 UTC | #9

Yeah you are right, my bad, sorry.

-------------------------

