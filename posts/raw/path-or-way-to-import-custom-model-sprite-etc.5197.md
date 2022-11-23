codefive | 2019-05-28 22:56:00 UTC | #1

I have tried for days to import a image, also a 3d model, i place them in Urho3D bin/Data/Models or Urho3D bin/Data/Urho2D folder in the case of the image, but no luck, my assets cant be found, i have also tried in my project root. What am i doing wrong besides being a noob here? Thank to everyone !

-------------------------

Leith | 2019-05-29 00:11:50 UTC | #2

Hi codefive and welcome to the forums!

I remember spending a few fruitless days myself, so I understand your frustration!
Are you able to load stock Urho assets? If you can, great, read on..

I keep my imported models (.mdl files) in bin/Data/Models. I put the material (.xml) files in bin/Data/Materials and any textures in bin/Data/Textures.
(Actually, I have subfolders in the Models folder, one for each Character, and one for general scenery)
Now I look carefully at the Material xml file because I almost always need to adjust the texture filepaths (in material .xml file) to refer to the Textures Folder ... eg "MyTexture.png" becomes "Textures/MyTexture.png"
Finally, I may wish to have a MaterialSet (.txt file) which is stored in the same folder as my models, in the case that a model requires more than one material.

-------------------------

codefive | 2019-05-29 01:24:31 UTC | #3

Oh now i understand, one last question, how do i create .mdl files and .xml materials ? Will Blender be ok? For what i understand theres no .fbx or other "support", it really doesnt matter, i just want to know how to create them.

-------------------------

Leith | 2019-05-29 01:30:45 UTC | #4

There's a few options.

Urho3D's scene editor is the absolute easiest way to import models of various formats, including obj and fbx. As soon as you import a model into a dummy scene, the .mdl file, materials and textures are all created for you in the proper folders. The editor is really just executing the AssetImporter commandline tool - if we want more control, we can do that ourselves...

Next option is to export from blender to FBX format, and then use Urho's AssetImporter utility to convert the FBX into model, material and animation files.

Third option is to install (in Blender) the Urho3D export plugin (I don't personally use this one).

-------------------------

codefive | 2019-05-29 01:32:23 UTC | #5

@Leith thank you a lot !! And the scene editor, and etc content i compile it from github ? I totally missed those ones, didnt knew they existed LOL Thank you one more time !!

-------------------------

Leith | 2019-05-29 01:36:42 UTC | #6

After building the Urho3D sourcecode, you'll have a "bin" folder containing the binary executable files for the samples, and there will also be a shell script (aka batch file) to launch the editor (same folder as the samples)
I think AssetImporter is also in this same folder, but I could be wrong about that, I tend to copy the AssetImporter binary all over the place.

-------------------------

codefive | 2019-05-29 01:43:13 UTC | #7

Well i am begining to have the impression i am exceeding your kindness, to many questions from me !! For what i see Urho3D comunity is great ! I dont want to throw dirt here, but i dont feel at home with "popular" 3D Engines, yes you know them, i will rather stay with Urho !! And with such a warm wellcome from all of you to me, i think i will stick arround a lot of time ! Thank you !

-------------------------

Leith | 2019-05-29 01:47:03 UTC | #8

You're very welcome, as are your questions - believe me I hammered this forum with all kinds of "dumb questions" for months, and I'm still really just scratching the surface :)
I tend to feel the same about "those" engines, Urho3D is a great alternative. Though the community may not be huge, it is quite active, and very friendly.

-------------------------

codefive | 2019-05-29 01:46:56 UTC | #9

Yep, so much to learn !! See you arround @Leith !!

-------------------------

Modanung | 2019-05-29 05:46:16 UTC | #10

The add-on for Blender @Leith mentioned can be found here:
https://github.com/reattiva/Urho3D-Blender

I don't think I ever used the AssetImporter during the five years I've been develin' with Urho.

And welcome to the forums, @codefive! :confetti_ball: :slightly_smiling_face:

-------------------------

jmiller | 2019-05-29 14:19:31 UTC | #11

Enter @codefive! Welcome. :confetti_ball: 

Let us know how it goes!

Would you like a brochure? I have brochures: :laughing:

The most current docs, terse but packed with good info:
  https://urho3d.github.io/documentation/HEAD/
The easily-missed `Related pages` : https://urho3d.github.io/documentation/HEAD/pages.html
  https://github.com/urho3d/Urho3D/wiki

The Samples are good study, and like Editor, will output messages to console (F1) and .log files, and accept some options to set Resource paths, etc.
  https://urho3d.github.io/documentation/HEAD/_running.html

Cheers

-------------------------

codefive | 2019-05-29 17:43:56 UTC | #12

@jmiller , @Modanung, Leith ,  yesterday i have created my first app with Urho3D, very simple, but there it is, thank you to all of you and the comunity !!

-------------------------

