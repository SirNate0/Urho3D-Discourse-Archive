eyyildiz | 2018-06-14 07:39:35 UTC | #1

Greetings, i have recently started learning Urho3D via UrhoSharp for Xamarin. 
I'm new to game development, but i have the programming experience in c#.

Everything was looking good until i wanted to bring my own 3D models into Urho world.
I have downloaded some models for blend from internet, they all seem to work well in blend.

However, i could not import them into Urho's .mdl format.

I have tried different assimport applications as well, but none of them did work, as well as Urho3D editor's import button.

![error_image|272x500](upload://fw02NejAzrNjxEkwcRYDW4LI3jL.jpg)

I really liked the idea behind Urho3D, however, if i can not import models from popular 3DEditors like Blender etc, its of no use to me.

Any idea about what i am doing wrong or how can i solve this ?
Is this an assimport problem?

You can find the blend file i have tried to import here:
https://free3d.com/3d-model/audi-r8-14024.html

Thanks in advance!

-------------------------

Eugene | 2018-06-14 08:59:19 UTC | #2

AFAIK Blender Urho3D export addon is the most stable way of importing.

-------------------------

Miegamicis | 2018-06-14 09:20:57 UTC | #3

I also use the Blender Urho3D  addon to export models and so far haven't got any issues related to that. On more thing to try is to use AssetImporter tool which comes with the engine, tho it requires more manual work.

https://github.com/reattiva/Urho3D-Blender

-------------------------

