George1 | 2017-09-20 13:51:01 UTC | #1

Hi,
I'm trying to look at some models using the editor on a 4k laptop screen. 
I wish I have eagle eye for this.
Do we have a config or any setting file to scale the editor on 4k screen?
Any setting without rebuild the engine?

Thanks

-------------------------

weitjong | 2017-09-21 01:41:18 UTC | #2

I don't think SDL has any support for 4k on Windows platform yet. SDL and hence Urho3D only has support for retina display on Mac at the moment. When on retina display, the editor script will scale up (2x) the UI. You can try to execute the script "ui.scale = 2" via the editor's command console. Never tested yet, so not sure what will be the result.

-------------------------

George1 | 2017-09-20 15:37:09 UTC | #3

Sorry,
I'm noob at this, how do do that?
Do you startup the command line and start up the editor from there?
Or do you do this at command prompt:

Editor.bat ui.scale=2

-------------------------

Modanung | 2017-09-20 15:50:05 UTC | #4

You can open the command console with **F1** and then set it to _Script_ mode (it may be set to _FileSystem_) after which you can type `ui.scale = 2` and hit enter to double the UI's scale.
Static elements don't seem to scale properly though.

-------------------------

George1 | 2017-09-20 15:49:58 UTC | #5


Awesome,
It works, thanks mate.
It was on FileSystem.

-------------------------

George1 | 2017-09-20 16:06:11 UTC | #6

I found a bug after we scale the ui.

After I create a box, if I left click on the position textbox. The ui control on the Attribute inspector is lost.

I can right click or middle click on the Attribute inspector ui control. But not left click. 

I think left click missed the ui control after scaling and it unselect the selected object.

-------------------------

weitjong | 2017-09-21 01:50:55 UTC | #7

I think it could be due to input subsystem not scaling up correctly. On Mac this has been done automatically when the engine detects high DPI mode. I am afraid you have to get your hand dirty this time to modify the engine. It is interesting to learn that RMB and MMB work while only LMB hit by the scaling though.

-------------------------

