HappyWeasel | 2021-05-05 16:56:41 UTC | #1

Hi,

I have a simple scene where I "zoom out" (moving camera backwards), and some Staticmodels suddenly dissapear (pop away) after some treshold/distance, while some are visible all the time (until they pass the far clip).

I only change SetModel (.mdl) file for my StaticModel in the sourcecode...  everthing else stays the same...
-> SetModel with   boxes.mdl and mushroom.mdl works, I can zoom out and see them, 
-> but with 80% of my imported fbx files, they dissapear suddenly.. some of those (20%) actually "work" ?  (Similar sized models)

So I guess it is a param for AssetImporter? I checked the fbx files in my 3d modeller and they seem to look fine / similar..

I do 

AssetImporter.exe model myfile.fbx Data\Models\myfile.mdl -nc -nm

Any ideas? (The member variables of the resulting StaticModel all look similar (the Drawable* members))

-------------------------

HappyWeasel | 2021-05-05 17:31:49 UTC | #2

Ok,

It seems that the Materials were  the problem, somehow mine were botched. I upgraded the Urho version to latest a while ago and still had the CoreData from 1.5 I guess. I deleted the shader cache in 
%APPDATA%\urho3d\shadercache (I guess CoreData\Shaders\HLSL\Cache is deprecated?), and now with Materials/DefaultMaterial.xml everything seems to work like I want (at least no more sudden dissapearance). Gonna work my way back from that..

-------------------------

Rook | 2021-05-21 07:47:09 UTC | #3

Interesting, thanks for the reply hopefully it will be a useful tip for anyone with the same issue.

-------------------------

