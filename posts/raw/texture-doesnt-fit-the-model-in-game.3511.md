crisx | 2017-08-31 02:39:39 UTC | #1

Hi

I've got something weird with one model, in Blender it looks like this:
![house2|373x425](upload://tAgu5hW3izN8cPFCOFCZlHL7pkf.png)

I used the Urho3D-Blender plugin to export the model, I successfully got the model, material and texture files, but when used in, it look like this:

![house|668x500](upload://jF3RvhAKFdoOsoc1DS1Gqyj2tDS.png)

It doesn't match the size of the model, I think the wrong technique is used in the material (Techniques/DiffNormal.xml). I didn't did anything special in the code:

    					StaticModel* Object = tileNode->CreateComponent<StaticModel>();
					Object->SetModel(cache->GetResource<Model>("Models/medium_h_1.mdl"));
					Object->SetCastShadows(true);
					Object->SetMaterial(cache->GetResource<Material>("Materials/Mittel_Haus.xml"));

I put the blend file here: https://ufile.io/8po1d

thxs

-------------------------

Victor | 2017-08-30 14:23:55 UTC | #2

Hmm..., with the exporter, I'd make sure you exported the UV coords. At least, that's what it looks like initially... I could be wrong though. I hope you find a solution to your issue!

-------------------------

codingmonkey | 2017-08-30 21:13:06 UTC | #3

Hi! It seems like your model have two UVs channels (  UVTex and UVMap )
first uv fits unwrapped model right, but last UV seems that not
so you may try to delete broken uv (?)
or try add postfix "__UV1" for proper uv data set "UVTex" +"_UV1"

[https://github.com/reattiva/Urho3D-Blender/blob/master/guide.txt](https://github.com/reattiva/Urho3D-Blender/blob/master/guide.txt)
> Blockquote
=====
 UV
=====
To export UV you need an UV map, you can see the list in the Data page of the current selected object.
The Urho MDL format supports two sets of UV coordinates. You can specify what maps to use by appending "_UV1" or
"_UV2" to the layer name. These suffixes can be used together but also alone, if they are missing the first used
layer will be chosen.
If the exporter reports some "Invalid UV" this means that some triangles of the mesh are mapped in the UV map to
triangles with an area null or too small. You need to increase the area in the UV map, you can set the option
'Select vertices with errors' to find these triangles.

-------------------------

crisx | 2017-09-02 17:02:43 UTC | #4

I tried using AssetImporter with the exported fbx, and parts of the texture were correctly applied on the generated mdl, but the result still looked far from the original. I'm a total newbie with blender, so far the Urho3D-Blender plugin is working great. I think it's just some tweaking matter

Here's the report from the Urho3D-Blender plugin when I check the "Merge Objects" option
![Image2|690x263](upload://bWLShAZ2vjQEI6DBUDvtVxJYiCV.png)

-------------------------

rasteron | 2017-09-04 02:17:22 UTC | #5

Hey there crisx,

The blend file model does not seem to be game ready and so you need to do some fixes. So here you go..

![house|690x367](upload://yqXR7xR5JZMXj0kDgXBB5TSpofH.jpg)


I see you are doing a toon style game there and so the new blend file is setup for diffuse only to keep it simple, but it should not be a problem in case you need to add normals, specular, etc. This is now Urho3D Blender Add-on export ready with the exported sample files.

**medieval_house.zip:** https://ufile.io/paz48

Hope that helps.

-------------------------

crisx | 2017-09-03 10:57:22 UTC | #6

Thanks rasteron,
I'll try what you said on other models I've got problems with,
I'm still learning how to use the Urho3D Editor properly

-------------------------

