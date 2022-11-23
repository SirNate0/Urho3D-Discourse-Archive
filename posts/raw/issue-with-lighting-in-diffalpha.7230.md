emenninga | 2022-04-01 23:36:26 UTC | #1

Using a tree model where each bough is a simple billboard with a png texture of a bough. (DiffAlpha technique)
Specifically this [free model](https://sketchfab.com/3d-models/low-poly-pine-tree-99fb6a37547840e3a295689df032ba28).
The tree looks good from one side, but the other side is glowing. I could post my material, but it is very basic. What should I be looking for?  (metallic = 0, setting cull to none glowed from all sides)
Thanks  
![oktree|164x256](upload://47l1zjpWMw6UKWVHsltyUoyftQS.jpeg)
![glowingtree|158x256](upload://4aDetAX21KsnDVOtlukS7zqAHjl.jpeg)

-------------------------

JSandusky | 2022-04-02 05:03:43 UTC | #2

Link us to a model we can test, not a web reference to something requiring 30 bloody logins.

-------------------------

elix22 | 2022-04-02 07:21:16 UTC | #3

Probably caused by some directional light in your scene.
Decrease the "Brightness Multiplier" of your light to 0.5.

-------------------------

emenninga | 2022-04-02 18:00:14 UTC | #4

Sorry -- I thought the link would allow an easy view of the model.

-------------------------

emenninga | 2022-04-02 18:17:24 UTC | #5

You're right the light is involved, but I started with the Water sample, so the only light is the skybox light. If I reduce the brightness, the whole scene gets dark. I did more investigation. The tree is simple rects with a PNG texture of a bough. If I use Diff.xml technique then the rects are visible too (duh) but if I use DiffAlpha.xml then the texture is fully transparent everywhere.  Is there a way to not add transparency beyond the texture? I'm fairly comfortable with shader code, but just don't know passes, and the pass differences between Diff.xml and DiffAlpha.xml confuse me. Is there documentation about these details?

-------------------------

Nerrik | 2022-04-02 21:47:01 UTC | #6

If you want your branches / leaves texture to be transparent try:

`<shader psdefines="ALPHAMASK" />`

in your material file and use an non alpha technology, in your case Diff . 

It just discard's all textureareas with alphachannel < 0.5 and is usually used for trees and plants

Alternatively you can adjust the 

`<parameter name="MatSpecColor" value="1 1 1 1" />` (For Lightning) at diffalpha tech. the last value is the "reflectstrength / shine"
and
`<parameter name="MatDiffColor" value="1 1 1 1" />` (For Color)

Parameters of your model.

If you use alpha technologies you sometimes have to adjust these values to fit your modellook to the other non alpha models in your Scene

-------------------------

Nerrik | 2022-04-03 00:02:15 UTC | #7

addendum:

"but if I use DiffAlpha.xml then the texture is fully transparent everywhere. "

Alpha technologies in Uhro3D arent there to take one whole model and display one part of it solid and one part transparent (depending on the alphastrength of the Texture).

The "solid" part will always been a little transparent - you have to build your model with multiple materials in your design program if you want to have only parts of it transparent and use different technologies / materials.

So the thing you want to achieve you better make with ALPHAMASK

-------------------------

emenninga | 2022-04-03 00:14:32 UTC | #8

Thanks @Nerrik. That works the way I expected. Would love documentation about the various techniques, passes, materials, parameters, etc.  Hard to find these kinds of details.

-------------------------

Nerrik | 2022-04-03 00:54:51 UTC | #9

no problem, dont forget to set the cull value for leaves / plants to "none" so the plant can be seen from both sides and not only in the normal direction.

`<cull value="none" />`

-------------------------

Nerrik | 2022-04-03 01:14:22 UTC | #10

[https://urho3d.io/documentation/1.7/_materials.html](https://urho3d.io/documentation/1.7/_materials.html)

Some kind of documentation about the materials / passes / parameters, could be more detailed but with a little practice you'll learn it fast ;)

-------------------------

SirNate0 | 2022-04-03 04:35:09 UTC | #11

[quote="Nerrik, post:7, topic:7230"]
The “solid” part will always been a little transparent
[/quote]

As long as you don't have the alpha for the MattDiffColor less than 1 (i.e. you only use the alpha channel of the texture, and transparency doesn't bleed into the opaque regions in generating mipmaps) then where the texture is opaque the model should be opaque. Though there are differences in how the rendering is done (reverted after all of the non alpha materials with CPU side depth sorting of the models, etc.), the results should be the same, just slightly less efficient if the whole model is opaque.

-------------------------

JSandusky | 2022-04-07 07:40:42 UTC | #12

[quote="SirNate0, post:11, topic:7230"]
As long as you don’t have the alpha for the MattDiffColor less than 1 (i.e. you only use the alpha channel of the texture, and transparency doesn’t bleed into the opaque regions in generating mipmaps) then where the texture is opaque the model should be opaque.
[/quote]

Yeah, so long as BLEND_REPLACE is the blend mode. If there's a case where that's not true then it's a bug.

-------------------------

