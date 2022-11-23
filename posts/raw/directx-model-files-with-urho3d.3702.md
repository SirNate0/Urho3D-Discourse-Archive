GodMan | 2017-10-31 15:35:18 UTC | #1

Hello Urho3d forum user I've decided to give Urho3d a try as I use to use Irrlicht but most of it's active developers have left. I've compiled Urho3d 1.7 and everything works fine except when I try to use a 3d model I converted from AssetImporter. The model itself seems to load fine but I can never get the diffuse texture to show. I've read the documentation and scoured the forums heres a screenshot. ![screen1|690x291](upload://oCxCpePvjOh0OqHBUyvBZJscQko.jpg)

Also with the animation I ran into 2 problems. One the animation appears to be playing way to fast. Two I believe the AssetImporter removed key frames and ruined the animation. I viewed this topic and commented out the part of code in AssetImporter and when I convert the model I don't get any errors however the animation is still ruined only parts of the model animate correctly. [Topic on differing channel keyrames](https://discourse.urho3d.io/t/cant-get-animations-in-this-model-to-work/2709)

I use 3ds max I know people use blender but I've been using 3ds max since 2008 so I would like to keep using it if possible.
I've used this model and animation in Irrlicht just fine so I know they work correctly.

-------------------------

Dave82 | 2017-10-31 17:46:44 UTC | #2


[quote="GodMan, post:1, topic:3702"]
One the animation appears to be playing way to fast.
[/quote]
Well if you use 3ds max i assume you use Panda exporter so your best bet is to export your models without
animation frames.And export animation into Urho's .ani format.And play those animations separately with playAnimation() where you can set speed , blending , weight etc.

[quote="GodMan, post:1, topic:3702"]
The model itself seems to load fine but I can never get the diffuse texture to show.
[/quote]
I'm not suse but it probably the material isn't automatically applied to your model.
Use yourModel->SetMaterial() to apply the corresponding materials to your model.Also make sure the textures are placed in the data/textures folder (or in a folder registered by the engine)


EDIT : Also here's my biped animation exporter script.(Unfortunately this works only with biped rigs so if you use your own bone structure you need to modify the script)

https://discourse.urho3d.io/t/3ds-max-biped-animation-export-script/1071

-------------------------

Eugene | 2017-10-31 17:59:29 UTC | #3

If you make a portable sample (X with animation and code/guidelines), I could try to debug AssetImporter when I have enough time. If it corrupts animation, it should be fixed.

-------------------------

GodMan | 2017-10-31 22:06:30 UTC | #4

Here's a rar file of the original model file in DirectX format and the items Asset Importer spits out. [https://ufile.io/hl1v0](https://ufile.io/hl1v0)

I'm using the Skeletal Animation sample all I've done is passed my custom model and materials. 
@Dave82 I've used the  modelObject->SetMaterial(cache->GetResource<Material>("Materials/JoinedMaterial_#1.xml")); 
in this example but still no texture displayed. I checked the hierarchy also and even changed the model material to one that was already in the scene and it did not show up on the model as well so I believe AssetImporter messed up something. Perhaps because the model is using a multi sub object material. Also I can't use your maxscript as the character has bones and not max's biped system. Also how can you export the model in DirectX format but not have any animations in the file how would Asset Importer create them then??

-------------------------

GodMan | 2017-10-31 22:26:47 UTC | #5

I'd like to update that I tried using the fbx format instead and ran that through Asset Importer and everything seems to be okay the .ani file was 23kb instead of 2kb from the DirectX conversion and the diffuse texture did show up fine. I do believe the DirectX conversion seem to cause some sort of problem I'm not using panda exporter I use to use it in the past but I upgraded to max 2015 and I believe panda exporter was not available for max 2015 sadly. After checking materials and textures they were working on the DirectX model but some kind of error I suppose destroyed the uvs and animations so that's why they were not working. Is the fbx format okay to use for converting as I used the same animation model and texture and it converted it fine bare in mind I have not tried to use normal mapping or anything that requires tangents and Binormals so fingers crossed.

-------------------------

Dave82 | 2017-10-31 23:39:53 UTC | #6

[quote="GodMan, post:5, topic:3702, full:true"]
I’d like to update that I tried using the fbx format instead and ran that through Asset Importer and everything seems to be okay the .ani file was 23kb instead of 2kb from the DirectX conversion and the diffuse texture did show up fine. I do believe the DirectX conversion seem to cause some sort of problem I’m not using panda exporter I use to use it in the past but I upgraded to max 2015 and I believe panda exporter was not available for max 2015 sadly. After checking materials and textures they were working on the DirectX model but some kind of error I suppose destroyed the uvs and animations so that’s why they were not working. Is the fbx format okay to use for converting as I used the same animation model and texture and it converted it fine bare in mind I have not tried to use normal mapping or anything that requires tangents and Binormals so fingers crossed.
[/quote]


I'm glad you succeeded ! About the tangents AFAIK fbx can export tangents.Max has some really cumbersome way of handling vertices so elements like tangents require some serious hack if you need to calculate them manually.

 I'm a max user as well since 2006-2007 ! Can i ask you what's your experience with max 2015 ? i'm using 2010 and it seems that whenewer Autodesk release a new version it only meke it slower and introduce more bugs along the old bugs which are present from max 7...

-------------------------

GodMan | 2017-11-01 20:33:59 UTC | #7

I chose max 2015 as the newer one seemed strange to me. They had it were anything you select in the viewport had a glow outline around it. Their were some other things to I just can't remember so I settled for 3ds max 2015. I stated out with 3ds max 2008 modding the old halo ce game.

-------------------------

