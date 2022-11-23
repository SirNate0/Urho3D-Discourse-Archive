codder | 2017-01-02 01:08:09 UTC | #1

Hello,

How to make an AnimatedSprite2D illuminated by 3D Light? I need to use a custom material? If yes, someone can make a small material example?

Thanks

-------------------------

codder | 2017-01-02 01:08:09 UTC | #2

I have this technique (SpriterTechnique.xml)
[code]
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
        <pass name="alpha" depthwrite="false" blend="alpha" vs="Urho2D" ps="Urho2D" />
</technique>
[/code]

And this material
[code]
<?xml version="1.0"?>
<material>
	<technique name="Techniques/SpriteTechnique.xml" />
	<texture unit="diffuse" name="Urho2D/Box.png" />
</material>

[/code]

I still don't know how to figure the lighting.
What I want to achieve is exactly how the lighting affects a simple Cube or a Sphere in the editor.

-------------------------

codder | 2017-01-02 01:08:09 UTC | #3

Using OpenGL and DiffAlpha.xml technique seems working partially.
[img]http://s3.postimg.org/46i6uwyrn/light.jpg[/img]

Basically the image is darker and probably it doesn't get illuminated because of normal image.

EDIT:
I tried to add
[code]<texture unit="normal" name="Urho2D/Box2.png" />[/code]
And
[img]http://s9.postimg.org/vrkynonq3/Box2.png[/img]

But the same thing...

-------------------------

Bananaft | 2017-01-02 01:08:10 UTC | #4

Can you provide a reference of what effect you trying to achieve?

You can't use normal maps on billboards in Urho right out the box. As tangent and binormal vectors are not generated for billboard mesh.  You can write custom shader, to calculate tangent and binormal vectors in vertex programm.

-------------------------

codder | 2017-01-02 01:08:10 UTC | #5

Solved by using a plane with a material that use DiffLightMapAlpha.xml as technique.

-------------------------

