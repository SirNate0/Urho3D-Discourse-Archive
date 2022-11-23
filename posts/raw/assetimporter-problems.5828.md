Chimareon | 2020-01-20 22:30:15 UTC | #1

Hi guys, 
I am working on Urho3d App for HoloLens.
I would like to Import .fbx models into my app.
I know there is AssetImporter NuGet Package, which I downloaded into my Visual Project.

I cannot however find any guide on how to use it. 
Would anyone who had succesfully used it care to guide me / Point me in direction of nearest good tutorial?

best regards
Chimareon

-------------------------

Alibaba | 2020-01-20 14:07:32 UTC | #2

Guide for use here: https://urho3d.github.io/documentation/1.4/_tools.html

-------------------------

Chimareon | 2020-01-20 14:18:58 UTC | #3

@Alibaba: I have seen this, but I cannot find the file i am supposed to execute in cmdline (I am on windows 10). I tried just calling AssetImporter as shown on the page You suggested, didn't work. Should I add something to PATH?

-------------------------

Alibaba | 2020-01-20 14:33:46 UTC | #4

Yes, it looks like this: (i rename "AssetImporter" to "as" for convenience)
![image|690x388](upload://ygD99CPh5MpAGKMjItaSGecTmdE.png)

-------------------------

Chimareon | 2020-01-20 15:09:26 UTC | #5

I'll try it tomorrow, when I am back in office.
thanks a lot :slightly_smiling_face:

-------------------------

Valdar | 2020-01-21 08:16:21 UTC | #6

There should be an AssetImporter program in your Urho install (unless you opted out for it when you built Urho). Look in the path ...\BUILDROOT\bin\tool\AssetImporter.exe. Just run it from the command line in that folder/directory without arguments for a help screen. As usual, add the folder to your Windows path to allow it to run anywhere.

-------------------------

Chimareon | 2020-01-21 09:57:12 UTC | #7

thanks a lot to You both, found it, added to PATH and it works.

I am adding .mdl through       var component = Node.CreateComponent<StaticModel>();
                                               component.Model = ResourceCache.GetModel("Models/Model.mdl");
                                               component.Material = Material.FromImage("Textures/texture.jpg");
                                               //or
                                               component.SetMaterial(ResourceCache.GetMaterial("Models/DefaultMaterial.xml"))

And I cannot see the object in game, but do not know if it is due to lack of texture or lack of object.
Game throws no errors and other objects are visible.

HALP?

-------------------------

guk_alex | 2020-01-21 11:31:40 UTC | #8

Try to import it in the Editor, may be the scale of imported model is too big or too small. There you can play with position or scale to quickly find out whats wrong (also, check the log messages).

-------------------------

Modanung | 2020-01-21 13:28:04 UTC | #9

Also see if your game outputs any messages of the "Resource not found" sort. Materials are not required to make a model visible. Lighting *is*, as well as either a `StaticModel` or `AnimatedModel` component.

And welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

