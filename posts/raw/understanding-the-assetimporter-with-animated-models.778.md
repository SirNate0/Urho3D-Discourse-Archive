devrich | 2017-01-02 01:02:49 UTC | #1

Hi,

On the [url]http://urho3d.github.io/documentation/1.32/_tools.html[/url] page i understand that if not importing OGRE models to use AssetImporter.  but i have always had model animations be a part of the 3D model and on that page it says .mdl and .ani ---- if I have a 3D model with several animations ( or even just one animation ) then will the AssetImporter split my 3D model into --> 3Dmodel.mdl 3DmodelAnimation1.ani 3DmodelAnimation2.ani 3DmodelAnimation3.ani etc ?

would the animations be strictly usable only to that specific 3D model or would they work on other 3D models that have the exact same skeleton-rig? ( in my case i'd like to create say 10 characters but all use the same skeleton-rig and all have the same initial t-pose )


Additionally: I have always used 32-bit .png files ( usually with semi-transparent or translucent areas ) in my 3D models but would .dds be better and if so then how to convert my 32-but .png's to the .dds format to keep Urho3D happy with the final .dds file? ( please note I have never worked with .dds files before )


[i][u]Edit[/u][/i]: Also would .dds work on Android or would I need 32-bit .png instead?

[u][i]Edit 2:[/i][/u] before i asked "[u][i]and I export it as .FBX ( is .FBX or .MS3D ok to use? )[/i][/u]" and the answer is here ( i should have looked here first ) [url]http://assimp.sourceforge.net/main_features_formats.html[/url] so currently it doesn't support FBX but does support MS3D which is ok i guess...

-------------------------

jmiller | 2017-01-02 01:02:49 UTC | #2

*edit, others have given better answers*

-------------------------

cadaver | 2017-01-02 01:02:49 UTC | #3

Skinning bone weights are stored in the .mdl. There should not be a problem to use animations in several models that share the same rig, provided that the bone transforms are identical (ie. no repositioning or scaling of bones between models)

-------------------------

codingmonkey | 2017-01-02 01:02:50 UTC | #4

>they work on other 3D models that have the exact same skeleton-rig?
should work yes
Once these different models must be use the same type of rig. 
Binding to the skeleton model is makeing in your favorite 3D editor (Maya, Blender...)

>Also would .dds work on Android or would I need 32-bit .png instead?
i suppose what not, i don't know exactly.
You need to have native texture format for each platform for better perfomance.

*.png I would use only at the stage of development but not at the stage of release. 
He slows down when loading the game, because of the 3D engine is still trying to keep the texture with the native hardware format as I think. 

*.DDS would be preferable to the PC platform. This is a hardware format it is not any additional calculations when loading the game. 
and *.dds also preserve gpu memory bus bandwidth, 'cause it is hardware compression has.

In addition it may contain pre-calculated mipmaps. And If you download the *.png video card again tries to generate them, which takes time.

i'm usually use command line tool - nvdds.exe (from NVDSK TOOLS) + *.bat file for batch convert. 
Aslo you may install plugin for gimp and expors your's textures one by one from gimp )

> is .FBX or .MS3D ok to use?
In your place I would have done so.
save *.fbx -> opened it in the blender -> looked instill is ok with the model? -> And do export through the plug from @reattiva to the project folder

-------------------------

Mike | 2017-01-02 01:02:50 UTC | #5

To supplement previous answers, dds works fine on Android and AssetImporter supports fbx.

-------------------------

devrich | 2017-01-02 01:02:50 UTC | #6

Many thanks for all your help here :smiley:

I am trying to get the AssetImporter compiled on my system right now but it has an ALSA library not found error so as soon as i get that fixed then i'll try to get some of my .fbx models into Urho3D.  Also I think I'll start doing my models using dds.

Thanks again!

-------------------------

devrich | 2017-01-02 01:02:50 UTC | #7

[quote="devrich"]...I am trying to get the AssetImporter compiled on my system right now but it has an ALSA library not found error...[/quote]

Got it!  The answer was to go grab the ALSA 1.0.28 "lib" from their site and then install that to my offline PC.  After that cmake/make worked perfectly to compile Urho3D from source.  Now I got the AssetImporter and everything!!  I imported one of my .FBX models in and it's pretty awesome :smiley:


?? I do have a question about backfaces: how to turn [u][i]OFF[/i][/u] "draw backfaces" on specific .mdl models using Lua Script?

-------------------------

codingmonkey | 2017-01-02 01:02:51 UTC | #8

>I do have a question about backfaces: how to turn OFF "draw backfaces" on specific .mdl models using Lua Script?
You need assign a new material for this part of mesh, and then in Urho3D editor in Material Editor 
[url=http://savepic.su/4724713.htm][img]http://savepic.su/4724713m.png[/img][/url]
choise cull mode, then save material.

-------------------------

devrich | 2017-01-02 01:02:51 UTC | #9

That was just what I needed, thanks codeingmonkey! :slight_smile:

-------------------------

