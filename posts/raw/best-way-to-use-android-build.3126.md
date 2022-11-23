Jillinger | 2017-05-14 02:57:08 UTC | #1

Hi all
I am working with Visual Studio, and I can work from both code and editor from VS. I am looking to test android, but I am not sure of the way(s) that can really work for me.
I think, if I understand correctly from what was said to me earlier, I cannot build for android with VS.
I tried to use Eclipse, but it doesn't seem to recognize the file for import - which I built from command line. I also don't have cmake_eclipse.bat - only cmake_eclipse.sh, so I  was not able to use that feature.
I did build for android successfully. Only I don't know how to use the files.<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/fbe97921a1ade6095448fc5eaa8625b78e95cc3a.jpg" width="425" height="280">

Can someone help me in this area? Thanks.

-------------------------

weitjong | 2017-05-14 05:41:30 UTC | #2

The best way is don't use VS, but then again someone else may know better with VS.

-------------------------

rasteron | 2017-05-15 20:47:23 UTC | #3

Hi, you need Ant or Gradle, JDK and Android SDK/NDK.

More info here under **Android build process**
https://urho3d.github.io/documentation/1.6/_building.html

That still works for me using command line with Ant, NDK 13 and JDK 8.

-------------------------

Jillinger | 2017-05-15 01:41:48 UTC | #4

[quote="weitjong, post:2, topic:3126, full:true"]
The best way is don't use VS, but then again someone else may know better with VS.
[/quote]

Right. Okay. That one's clear... I think.

-------------------------

Jillinger | 2017-05-15 01:55:30 UTC | #5

[quote="rasteron, post:3, topic:3126"]
you need Ant or Gradle, JDK and Android SDK/NDK.
[/quote]

I think I am with you.
Let me know if I got you right.
I follow the **Android build process** in the manual (which I already did, and I got an .apk from ant debug. I didn't build a release, because I didn't have a keystore file, but I recently created one.:slight_smile:)
So now, what I can do is use the instructions from "**Using Urho3D as external library**" to create my own project, and then use the Android build process to build the android package.
Is that correct?
So in a case like this, I would not be able to work with the editor to create a project for android?

-------------------------

Modanung | 2017-05-15 02:59:51 UTC | #6

[quote="Jillinger, post:5, topic:3126"]
So in a case like this, I would not be able to work with the editor to create a project for android?
[/quote]

Why would this stop you from using the editor?

-------------------------

Jillinger | 2017-05-15 12:01:15 UTC | #7

Well, that's what I am asking. I don't know.
How would I go about using the editor, and create for android?

-------------------------

Modanung | 2017-05-15 18:06:08 UTC | #8

Ah. Well, as of now I _don't_ think the editor does anything platform specific. It is purely for content creation like scenes, materials, particle effects and prefabs; which is platform agnostic. The Urho3DPlayer running the script should be built for the platform you're using the editor on. And things like 3D models and textures should (again, at the moment) all be created with other software.
Also there is no building projects from within the editor (yet) either.

-------------------------

Jillinger | 2017-05-15 18:27:59 UTC | #9

Hmmm.
Now that you mentioned it... I just realized. Why am I using the editor, if I can only save out to an .xml, or .obj. It seems, as you said, "It is purely for content creation". 
Thank for drawing this to my attention. I was here using the editor with the idea that I would be able to make my game from here. I didn't even think about the export format.

So let me see if I understand how I can use the editor then.
Say I create an entire scene like Ninja Snow Wars,and save it out to an .xml. Do I then create a script which uses the .xml, which would then be used in my project?

-------------------------

Modanung | 2017-05-15 19:53:35 UTC | #10

Any node (along with it's children and components) can be saved to XML, JSON or binary format which can later be [instantiated](https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scripts/NinjaSnowWar.as#L758-L762) into your scene. Personally, I rather assemble the objects _in_ code as it gives more control and oversight. For the occasional precise positioning I copy positions from within Blender (sometimes from the 3D cursor). But this might very well change in the future.
That said, writing a (simple) editor made specifically for your project might also be something to consider. This takes away a lot of visual clutter since you can limit it to your needs and greatly improve the workflow for creating levels.

[spoiler]Replicated nodes are for networking, not prefabs/cloning.[/spoiler]

-------------------------

Jillinger | 2017-05-15 20:47:01 UTC | #11

I examined both the .xml and .as file of NinjaSnowWar, and sure enough the method is as I thought.

`gameScene.LoadXML(cache.GetFile("Scenes/NinjaSnowWar.xml"));`

...and they helped me even better. There is also code used if the game specifically targets android.
So thanks for the help you guys provided. I now know exactly what to do to create, test, build, and deploy for android.:relaxed:

-------------------------

