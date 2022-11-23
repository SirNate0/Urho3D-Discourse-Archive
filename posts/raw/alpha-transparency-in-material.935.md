Vivek | 2017-01-02 01:04:13 UTC | #1

I have a mesh in which I want certain section to be transparent. The area in a png with transparency. I also have seperate alpha map(Grey Scale).
Is there any premade material in urho 3D or do I have to use multiple pass for rendering transparent mesh over inside mesh.
If required please also mention what kind of image format should be used for my requirement.

-------------------------

amit | 2017-01-02 01:04:13 UTC | #2

see [post2783.html?p2783](http://discourse.urho3d.io/t/png-transparent-zones-filled-in-black/503/1)

-------------------------

Vivek | 2017-01-02 01:04:13 UTC | #3

ok, It worked. But there was some problems.
As required the area marked by yellow is transparent.
But the rest of the outter mesh is also semi transparent, more predominantly shown in the area marked by red arrow.
[img]http://img.ctrlv.in/img/15/03/16/5506c6e7d51f2.png[/img]
[code]<material>
    <technique name="Techniques/DiffNormalAlpha.xml" />
    <texture unit="diffuse" name="Textures/ab.png" />
	<texture unit="normal" name="Textures/Heart_Norm.jpg" />
    <parameter name="MatDiffColor" value="1 1 1 1" />
    <depthbias constant="-0.00001" slopescaled="0" />
</material>[/code]
But the overall effect I wanted is not good enough so I will try fresnel in outter layer, the idea is to use same path as [b]Water Material[/b] but use fresnel shader.
Any help in exactly how to do the above would be nice.

-------------------------

Vivek | 2017-01-02 01:04:13 UTC | #4

ok, fresnel is working now.
@amit , Thanks for the link, it help me in the alpha transparency issue but the above issue remains.

-------------------------

