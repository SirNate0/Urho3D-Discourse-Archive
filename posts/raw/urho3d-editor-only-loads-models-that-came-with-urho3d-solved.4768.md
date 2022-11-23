GodMan | 2018-12-19 22:27:59 UTC | #1

I'm not sure if I am overlooking something, but I started to mess with the editor to help me make simple scenes. I set the resource path correctly. The models I use work perfectly fine in urho3d, but they do not show up in the options to select a model file. I have tried to set the models as static, and animated to test in the editor, but the only models that show to choose from our the default ones that came with urho3d. The models are in .mdl format.

-------------------------

I3DB | 2018-12-19 21:23:11 UTC | #2

I don't know the answer, but wondering if it is somehow related to a post I just made ...

https://discourse.urho3d.io/t/resourcecache-getmodel-fails-loading-model-files/4767

-------------------------

GodMan | 2018-12-19 21:43:19 UTC | #3

I have not mess with the editor too much. Maybe it's because the models with Urho3d are really simple models? I'm not sure.

-------------------------

GodMan | 2018-12-19 22:28:40 UTC | #4

Okay so I solved my issue. For me since I have more than one copy of the Urho3d1.7 folder on my desktop. The editor kept pointing to an old copy that really had no changes. I deleted the now inactive copies of Urho3d, and now it loads the correct directory with the correct models.

See if this is your issue.

-------------------------

I3DB | 2018-12-20 15:19:09 UTC | #5

Not my issue. I can point the desktop version of Samply game to my other project's Data folder and it works fine.

I suspect it's failing loading something required by the model and there is no inner exception or more detailed info, at least on the C# side.

edit: turns out it was sort of my issue, but in a different way. The .mdl files were not being properly assembled during deployment to the device.

-------------------------

