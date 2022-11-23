Liichi | 2017-01-29 00:06:52 UTC | #1

Hi I have a problem with the materials, they look stretched and when I move the camera the texture changes position.

I already try to use all versions of urho (directx and opengl), and all renderpaths.

Images:
http://imgur.com/a/ZBwTK

Thanks.

-------------------------

hdunderscore | 2017-01-29 02:16:55 UTC | #2

Did you export UV's with your model?

-------------------------

Liichi | 2017-01-29 02:47:10 UTC | #3

No, i just exported the model to .dae and set the material using urho's attribute inspector.

-------------------------

hdunderscore | 2017-01-29 20:17:00 UTC | #4

You need UV texture coordinates for the texture to be displayed on the model appropriately. Whether you need to include them when you exported to dae, or whether you need to set an option when importing to Urho, or maybe you just didn't generate UVs on the model to begin with? 

Maybe you can elaborate on your workflow. If you use blender, the simplest path is to use this Urho3D exporter and select UVs as one of the export options: 
https://github.com/reattiva/Urho3D-Blender

-------------------------

Liichi | 2017-01-29 03:56:37 UTC | #5

It works! Thanks! :D
ps: I just had to create the UV and export to .dae.

-------------------------

