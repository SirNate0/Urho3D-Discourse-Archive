Lumak | 2017-10-20 16:59:41 UTC | #1

Spherical Images: https://github.com/Lumak/Urho3D-Assets/tree/master/SkyImages
Model: https://github.com/Lumak/Urho3D-Assets/blob/master/Models/SkyDome.mdl

The skydome model is just a half-sphere with UV's intact and maps the sky images correctly.

edit:
If you want to view all the images at once, here's the link to the commit: https://github.com/Lumak/Urho3D-Assets/commit/1224de27dd7647cd9d45eeaf33118f8f1ea37bfe

Memory usage:
* for 2048x1024 images = 8 MB
* for 1024x512 images = 2 MB
compare that with use of current skybox images: 6x1024x1024 = 24 MB

-------------------------

smellymumbler | 2017-10-20 17:38:45 UTC | #2

No special shader is needed for the sky dome?

-------------------------

Lumak | 2017-10-20 17:52:19 UTC | #3


[b]Component:[/b] Skybox
[b]Model:[/b] you can use Models/Sphere.mdl or the one that I linked above - SkyDome.mdl
[b]Material:[/b]
[code]
<material>
	<technique name="Techniques/DiffSkydome.xml" />
	<texture unit="diffuse" name="SkyImages/vp_sky_v3_015_1024.png" />
	<parameter name="MatDiffColor" value="1 1 1 1" />
    <cull value="none" />
</material>
[/code]

-------------------------

