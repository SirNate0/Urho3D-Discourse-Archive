Liichi | 2017-04-20 10:50:56 UTC | #1

Hi, I'm trying to delete the scene and load the main menu when I click. The problem is that nothing happens when i click.
PS: I tried to do the same thing from a button on ui and it works.

Code: https://pastebin.com/YGgDPZ9g

Thanks.

-------------------------

1vanK | 2017-04-18 06:04:46 UTC | #2

 http://discourse.urho3d.io/t/how-do-i-set-another-scene/2186/8

-------------------------

Liichi | 2017-04-19 02:34:20 UTC | #3

Still not working :confused: 
This line is not begin executed: 
> `scene_.RemoveAllChildren();`

I also tried:

> File loadFile(fileSystem.programDir + "Data/Scenes/empty.xml", FILE_READ); //clear scene
> scene_.LoadXML(loadFile);

-------------------------

Sinoid | 2017-04-19 03:08:12 UTC | #4

Add more print statements, make every other line a print statement indicating the next call, and with the last one being "Finished GoToMenu." This will make sure you're not crashing the angelscript context somewhere.

If your original "Creating Menu (:" message prints in both cases then something is happening somewhere, and you need to narrow it down.

-------------------------

Liichi | 2017-04-19 23:34:35 UTC | #5

I added a lot of prints :P and I realized that when I call the GoToMenu() function from DelayedExecute the variable **scene_** is null, but when I call it from the ui button no.
> if(scene_!=null){
>     Print("scene != null");
>     scene_.RemoveAllChildren();
> }else Print("null scene");

Output from DelayedExecute: _"null scene"._
Output from ui button: _"scene != null"._

**EDIT: I did some tests and it seems that the script loaded by UrhoPlayer is in another angelscript context that the script that calls the function GoToMenu():/**

**Test i made: https://pastebin.com/4ZTDCT11**

-------------------------

Liichi | 2017-04-20 10:51:00 UTC | #6

Fixed in the worst possible way i think. (:
I added this line to HandleUpdate: 
> if(scene_.GetChild("tomenu")!=null)GoToMenu();

Then when i have to call GoToMenu(); i just do:
> scene.CreateChild("tomenu");

-------------------------

Modanung | 2017-04-20 10:43:35 UTC | #7

Couldn't you store that in a `bool`ean?

-------------------------

Liichi | 2017-04-20 20:27:28 UTC | #8

No, it seems that when I use #include from a scriptinstance it creates a new context or something like that.

-------------------------

Sinoid | 2017-04-21 05:31:52 UTC | #9

This doesn't sound right. The context shouldn't be the problem, script-module might be, but I still wouldn't expect that here.

Is your project small enough to post? If not I have a reasonably small delta for adding asPEEK debugging that might work (you can use the web-based debugger, or I have a full IDE for Angelscript). It was never and probably never will be merged due to instability (it'll time out randomly and can sometimes jam things up while running ... it's better than nothing though).

-------------------------

Liichi | 2017-04-21 22:08:22 UTC | #10

My project has more than 40 script files. I'm going to write a minimal example (only 2 script files).
Tomorrow I upload the files. :)

-------------------------

Liichi | 2017-04-22 22:31:57 UTC | #11

Scripts:
https://pastebin.com/ULcVdfga (Global.as)
https://pastebin.com/ejLLAK2K (Instance.as)

Scene:
https://pastebin.com/Nm4utjWe (scene.xml)

cmd:
Urho3DPlayer.exe Scripts/Global.as

-------------------------

