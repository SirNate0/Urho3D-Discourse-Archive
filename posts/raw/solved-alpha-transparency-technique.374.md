Bluemoon | 2017-01-02 00:59:57 UTC | #1

The numerous techniques included with urho3D has really saved me a lot of stress and brain overloads  :smiley: . But there seems to be a problem with the Alpha Enabled techniques, like the DiffAlpha DiffNormalAlpha, DiffNormalSpecAlpha and most likely other techniques that have alpha included. The issue is when a material that has any of these technique is applied to an object, the alpha effect affects parts of the object that are not meant to be transparent according to the texture used. This usually happens when the object has surfaces that occlude each other. I made a model to explain this.

[img]http://s25.postimg.org/71addtwml/Screenshot_Mon_Aug_04_03_05_33_2014.png[/img]

The model on the left is a continues mesh model, the head and the veil covering the face are joined together, the material has a technique of DiffAlpha so as to give an alpha effect to the veil while the head remains with its diffuse appearance. Looking at this model one will see the transparency defect at the side of the head due to the occluded sides showing through to the front. The model at the right is an object with two sub entities each having its own material. The material of the head has a plain Diff technique while that of the veil has DiffAlpha. Doing it this way the problem doesn't show up, but I'm a bit concerned that this method would involve unnecessary sub entities if I were to have transparency in some of my models since I would have to separate each transparent part into its own material.

I know this issue can be corrected by writing one or two shaders  :smiley: , but I will like to know if there is already a work-around for it

-------------------------

cadaver | 2017-01-02 00:59:57 UTC | #2

I can't see your image, but I should know the issue.

The basic idea is that transparent materials do not write into the depth buffer, so they're prone to depth glitches. Having completely error-free alpha rendering would at its most extreme make it necessary to sort the object's triangles on the CPU according to the view angle before rendering, which Urho of course doesn't do. What it does is a depth sorting of the submeshes according to their distance from camera, so if you have glitching transparent parts, you can possibly fix them by separating into more submeshes.

A transparent material is always disadvantageous to an opaque material, because in addition to the depth write and ordering issue, it is more costly to render due to blending. Furthermore you don't get the benefit of depth occlusion, as transparencies are rendered last in the scene render, so if a large part of your transparent material is fully opaque, any objects that are behind are rendered first, then overwritten. That in mind, you should certainly separate the fully opaque parts of your model into a separate submesh (material). Also whenever you can, use alpha test (tree leaves, hair in some cases) instead of alpha blend, as these are treated the same as opaques, they just have the additional per-pixel pass/fail test in the pixel shader.

-------------------------

Bluemoon | 2017-01-02 00:59:57 UTC | #3

Sorry for the image (still figuring out how to properly post images :frowning: )

Thanks for the answer, let me try out the alpha test option you mentioned cos I have some trees with leaves that use alpha enabled texture.

-------------------------

